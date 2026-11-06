"""Core data loading and at-risk screening logic for TeacherPlus.

Pure standard library so it can be unit-tested without the MCP SDK.

The screening is deliberately rule-based and transparent: every flag comes
with the plain-language reasons that triggered it, so a teacher can check
the evidence instead of trusting an opaque score. It is a prompt for a
human conversation, never a diagnosis or a label.
"""

from __future__ import annotations

import csv
import os
from dataclasses import dataclass, field, asdict
from datetime import date, timedelta
from pathlib import Path
from statistics import mean
from typing import Iterable

# ---------------------------------------------------------------------------
# Data location
# ---------------------------------------------------------------------------

BUNDLED_SAMPLE = Path(__file__).resolve().parent.parent / "sample-data"


def resolve_data_dir() -> tuple[Path, str]:
    """Return (data_dir, source) where source explains how it was chosen."""
    env = os.environ.get("TEACHERPLUS_DATA_DIR", "").strip()
    if env:
        return Path(env).expanduser(), "TEACHERPLUS_DATA_DIR"
    home = Path.home() / "TeacherPlus" / "data"
    if (home / "students.csv").exists():
        return home, "~/TeacherPlus/data"
    return BUNDLED_SAMPLE, "bundled sample data (fictional students)"


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as f:
        return [
            {(k or "").strip().lower(): (v or "").strip() for k, v in row.items()}
            for row in csv.DictReader(f)
        ]


def _split(value: str) -> list[str]:
    return [p.strip() for p in value.replace(",", ";").split(";") if p.strip()]


def _parse_date(value: str) -> date | None:
    try:
        return date.fromisoformat(value[:10])
    except (ValueError, TypeError):
        return None


@dataclass
class Dataset:
    data_dir: Path
    source: str
    students: dict[str, dict] = field(default_factory=dict)
    classes: dict[str, dict] = field(default_factory=dict)
    grades: list[dict] = field(default_factory=list)
    attendance: list[dict] = field(default_factory=list)
    behavior: list[dict] = field(default_factory=list)
    procedures: str = ""

    def latest_date(self) -> date:
        dates = [
            r["_date"]
            for r in (*self.grades, *self.attendance, *self.behavior)
            if r.get("_date")
        ]
        return max(dates) if dates else date.today()

    def students_in(self, class_id: str | None) -> list[dict]:
        if not class_id:
            return list(self.students.values())
        return [s for s in self.students.values() if class_id in s["class_ids"]]


def load_dataset(data_dir: Path | None = None) -> Dataset:
    if data_dir is None:
        data_dir, source = resolve_data_dir()
    else:
        source = "explicit path"
    if not (data_dir / "students.csv").exists():
        raise FileNotFoundError(
            f"No students.csv found in {data_dir}. See README.md for the expected "
            "files, or unset TEACHERPLUS_DATA_DIR to use the sample data."
        )

    ds = Dataset(data_dir=data_dir, source=source)

    for row in _read_csv(data_dir / "students.csv"):
        sid = row.get("student_id")
        if not sid:
            continue
        row["class_ids"] = _split(row.get("class_ids", ""))
        row["supports"] = _split(row.get("supports", ""))
        row["name"] = f"{row.get('first_name', '')} {row.get('last_name', '')}".strip()
        ds.students[sid] = row

    for row in _read_csv(data_dir / "classes.csv"):
        if row.get("class_id"):
            ds.classes[row["class_id"]] = row

    for row in _read_csv(data_dir / "grades.csv"):
        row["_date"] = _parse_date(row.get("date", ""))
        row["status"] = (row.get("status") or "submitted").lower()
        try:
            score = float(row["score"]) if row.get("score") else None
            max_score = float(row.get("max_score") or 100)
        except ValueError:
            score, max_score = None, 100.0
        row["_score"], row["_max"] = score, max_score
        row["_pct"] = (
            round(100 * score / max_score, 1)
            if score is not None and max_score > 0
            else None
        )
        ds.grades.append(row)

    for row in _read_csv(data_dir / "attendance.csv"):
        row["_date"] = _parse_date(row.get("date", ""))
        row["status"] = (row.get("status") or "present").lower()
        ds.attendance.append(row)

    for row in _read_csv(data_dir / "behavior.csv"):
        row["_date"] = _parse_date(row.get("date", ""))
        row["type"] = (row.get("type") or "concern").lower()
        ds.behavior.append(row)

    proc = data_dir / "procedures.md"
    if proc.exists():
        ds.procedures = proc.read_text(encoding="utf-8")

    return ds


# ---------------------------------------------------------------------------
# Screening
# ---------------------------------------------------------------------------


@dataclass
class Thresholds:
    failing_pct: float = 60.0  # average below this -> high concern
    low_pct: float = 70.0  # average below this -> moderate concern
    trend_drop_pts: float = 10.0  # recent vs earlier average drop
    missing_count: int = 3  # missing assignments in window
    attendance_rate: float = 90.0  # below = chronic absenteeism (US standard)
    tardy_count: int = 5
    behavior_concerns: int = 3
    window_days: int = 30  # look-back window for counts


@dataclass
class Flag:
    category: str  # academics | engagement | attendance | behavior
    severity: int  # points: 3 high, 2 moderate, 1 watch
    reason: str


@dataclass
class StudentScreen:
    student_id: str
    name: str
    tier: str  # High | Moderate | Watch | None
    score: int
    flags: list[Flag]
    metrics: dict
    supports: list[str]
    strengths: list[str]

    def to_dict(self) -> dict:
        d = asdict(self)
        d["flags"] = [asdict(f) for f in self.flags]
        return d


def _tier(score: int) -> str:
    if score >= 5:
        return "High"
    if score >= 2:
        return "Moderate"
    if score >= 1:
        return "Watch"
    return "None"


def _filter_class(rows: Iterable[dict], class_id: str | None) -> list[dict]:
    if not class_id:
        return list(rows)
    # Attendance/behavior rows may omit class_id (daily attendance) - keep those.
    return [r for r in rows if not r.get("class_id") or r["class_id"] == class_id]


def screen_student(
    ds: Dataset,
    student_id: str,
    class_id: str | None = None,
    as_of: date | None = None,
    t: Thresholds | None = None,
) -> StudentScreen:
    t = t or Thresholds()
    as_of = as_of or ds.latest_date()
    window_start = as_of - timedelta(days=t.window_days)
    s = ds.students[student_id]

    def mine(rows):
        return [
            r
            for r in _filter_class(rows, class_id)
            if r.get("student_id") == student_id
            and (r["_date"] is None or r["_date"] <= as_of)
        ]

    grades = mine(ds.grades)
    attendance = mine(ds.attendance)
    behavior = mine(ds.behavior)

    flags: list[Flag] = []
    strengths: list[str] = []
    metrics: dict = {}

    # --- Academics -------------------------------------------------------
    graded = [g for g in grades if g["_pct"] is not None and g["status"] != "excused"]
    # Points-based average; missing work counts as zero, as most gradebooks do.
    missing_all = [g for g in grades if g["status"] == "missing"]
    earned = sum(g["_score"] for g in graded if g["status"] != "missing")
    possible = sum(g["_max"] for g in graded if g["status"] != "missing") + sum(
        g["_max"] for g in missing_all
    )
    avg = round(100 * earned / possible, 1) if possible else None
    metrics["average_pct"] = avg
    if avg is not None:
        if avg < t.failing_pct:
            flags.append(Flag("academics", 3, f"Current average {avg}% is failing (< {t.failing_pct:g}%)."))
        elif avg < t.low_pct:
            flags.append(Flag("academics", 2, f"Current average {avg}% is below {t.low_pct:g}%."))
        elif avg >= 90:
            strengths.append(f"Strong average ({avg}%).")

    dated = sorted(
        [g for g in graded if g["_date"] and g["status"] != "missing"],
        key=lambda g: g["_date"],
    )
    if len(dated) >= 4:
        half = len(dated) // 2
        earlier = mean(g["_pct"] for g in dated[:half])
        recent = mean(g["_pct"] for g in dated[half:])
        metrics["earlier_avg_pct"] = round(earlier, 1)
        metrics["recent_avg_pct"] = round(recent, 1)
        drop = earlier - recent
        if drop >= t.trend_drop_pts:
            flags.append(
                Flag("academics", 2, f"Scores dropped {drop:.0f} points (from {earlier:.0f}% to {recent:.0f}%) on recent work.")
            )
        elif recent - earlier >= t.trend_drop_pts:
            strengths.append(f"Scores are improving ({earlier:.0f}% -> {recent:.0f}%).")

    # --- Engagement (missing work) --------------------------------------
    recent_missing = [
        g for g in missing_all if g["_date"] is None or g["_date"] >= window_start
    ]
    metrics["missing_total"] = len(missing_all)
    metrics["missing_recent"] = len(recent_missing)
    metrics["missing_assignments"] = [g.get("assignment", "") for g in missing_all]
    if len(recent_missing) >= t.missing_count * 2:
        flags.append(Flag("engagement", 3, f"{len(recent_missing)} missing assignments in the last {t.window_days} days."))
    elif len(recent_missing) >= t.missing_count:
        flags.append(Flag("engagement", 2, f"{len(recent_missing)} missing assignments in the last {t.window_days} days."))
    elif grades and not missing_all:
        strengths.append("No missing assignments.")

    # --- Attendance -------------------------------------------------------
    if attendance:
        absent = [a for a in attendance if a["status"] in ("absent", "unexcused")]
        excused = [a for a in attendance if a["status"] == "excused"]
        tardy = [a for a in attendance if a["status"] == "tardy"]
        days = len(attendance)
        # Chronic absenteeism counts excused absences too.
        rate = round(100 * (days - len(absent) - len(excused)) / days, 1)
        metrics.update(
            attendance_rate_pct=rate,
            days_recorded=days,
            absences=len(absent) + len(excused),
            unexcused_absences=len(absent),
            tardies=len(tardy),
        )
        if rate < t.attendance_rate - 10:
            flags.append(Flag("attendance", 3, f"Attendance rate {rate}% (severe chronic absence)."))
        elif rate < t.attendance_rate:
            flags.append(Flag("attendance", 2, f"Attendance rate {rate}% is below {t.attendance_rate:g}% (chronic absence)."))
        elif rate >= 97:
            strengths.append(f"Excellent attendance ({rate}%).")
        recent_tardy = [a for a in tardy if a["_date"] and a["_date"] >= window_start]
        if len(recent_tardy) >= t.tardy_count:
            flags.append(Flag("attendance", 1, f"{len(recent_tardy)} tardies in the last {t.window_days} days."))

    # --- Behavior ---------------------------------------------------------
    concerns = [
        b
        for b in behavior
        if b["type"] != "positive" and b["_date"] and b["_date"] >= window_start
    ]
    positives = [b for b in behavior if b["type"] == "positive"]
    metrics["behavior_concerns_recent"] = len(concerns)
    metrics["positive_notes"] = len(positives)
    if len(concerns) >= t.behavior_concerns:
        flags.append(Flag("behavior", 2, f"{len(concerns)} behavior concerns logged in the last {t.window_days} days."))
    elif len(concerns) >= 1:
        flags.append(Flag("behavior", 1, f"{len(concerns)} behavior concern(s) logged recently."))
    if positives:
        strengths.append(f"{len(positives)} positive behavior note(s) on file.")

    score = sum(f.severity for f in flags)
    return StudentScreen(
        student_id=student_id,
        name=s["name"],
        tier=_tier(score),
        score=score,
        flags=flags,
        metrics=metrics,
        supports=s.get("supports", []),
        strengths=strengths,
    )


TIER_ORDER = {"High": 0, "Moderate": 1, "Watch": 2, "None": 3}


def screen_class(
    ds: Dataset,
    class_id: str | None = None,
    as_of: date | None = None,
    t: Thresholds | None = None,
) -> list[StudentScreen]:
    results = [
        screen_student(ds, s["student_id"], class_id, as_of, t)
        for s in ds.students_in(class_id)
    ]
    return sorted(results, key=lambda r: (TIER_ORDER[r.tier], -r.score, r.name))

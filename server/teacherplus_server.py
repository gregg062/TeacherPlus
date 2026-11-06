# /// script
# requires-python = ">=3.10"
# dependencies = ["mcp>=1.2"]
# ///
"""TeacherPlus MCP server.

Exposes a teacher's local class data (roster, gradebook, attendance,
behavior log, classroom procedures) to Claude, and runs transparent
at-risk screening. Everything is read from local CSV files; nothing is
sent anywhere except to the Claude session the teacher is using.
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import risk  # noqa: E402

try:  # mcp >= 2
    from mcp.server.mcpserver import MCPServer as _Server
except ImportError:  # mcp 1.x
    from mcp.server.fastmcp import FastMCP as _Server

INSTRUCTIONS = """\
TeacherPlus gives you the teacher's class data. Call `data_status` first if \
you are unsure which data is loaded. Student records are confidential \
(FERPA): only use them for the teacher's request, never put them in public \
places, and refer to students by first name in documents meant for others \
(e.g. substitutes). At-risk flags are a screening aid based on simple, \
listed rules - present them as "worth a check-in", with their reasons, \
never as a diagnosis or label."""

mcp = _Server("teacherplus", instructions=INSTRUCTIONS)


def _ds() -> risk.Dataset:
    return risk.load_dataset()


def _as_of(value: str | None) -> date | None:
    return date.fromisoformat(value) if value else None


def _student_public(s: dict) -> dict:
    keys = (
        "student_id", "first_name", "last_name", "grade_level", "class_ids",
        "supports", "accommodations", "notes", "guardian_name",
        "guardian_email", "preferred_language",
    )
    return {k: s.get(k) for k in keys if s.get(k) not in (None, "", [])}


@mcp.tool()
def data_status() -> dict:
    """Show where TeacherPlus is reading data from and what was found."""
    ds = _ds()
    return {
        "data_dir": str(ds.data_dir),
        "source": ds.source,
        "students": len(ds.students),
        "classes": len(ds.classes),
        "grade_records": len(ds.grades),
        "attendance_records": len(ds.attendance),
        "behavior_records": len(ds.behavior),
        "has_procedures": bool(ds.procedures),
        "latest_record_date": ds.latest_date().isoformat(),
        "note": (
            "Using fictional sample data. Set TEACHERPLUS_DATA_DIR or create "
            "~/TeacherPlus/data to use real class data."
            if ds.data_dir == risk.BUNDLED_SAMPLE
            else "Using the teacher's own data."
        ),
    }


@mcp.tool()
def list_classes() -> list[dict]:
    """List the teacher's classes/periods with schedule, room and enrollment."""
    ds = _ds()
    out = []
    for c in ds.classes.values():
        out.append({**c, "enrolled": len(ds.students_in(c["class_id"]))})
    return out


@mcp.tool()
def get_roster(class_id: str | None = None) -> list[dict]:
    """Roster for one class (or all students), including supports such as
    IEP/504/ELL, accommodations and notes. Use for seating charts, sub plans
    and grouping."""
    return [_student_public(s) for s in _ds().students_in(class_id)]


@mcp.tool()
def get_student_profile(student_id: str, class_id: str | None = None) -> dict:
    """Everything on file for one student: info, grades, missing work,
    attendance, behavior notes and a screening summary. Use before writing
    report comments or parent emails."""
    ds = _ds()
    if student_id not in ds.students:
        matches = [
            s["student_id"]
            for s in ds.students.values()
            if student_id.lower() in s["name"].lower()
        ]
        if len(matches) == 1:
            student_id = matches[0]
        else:
            return {"error": f"Student '{student_id}' not found.", "possible_matches": matches}

    def rows(src):
        return [
            {k: v for k, v in r.items() if not k.startswith("_") and k != "student_id"}
            for r in risk._filter_class(src, class_id)
            if r.get("student_id") == student_id
        ]

    return {
        "student": _student_public(ds.students[student_id]),
        "screening": risk.screen_student(ds, student_id, class_id).to_dict(),
        "grades": rows(ds.grades),
        "attendance_exceptions": [
            a for a in rows(ds.attendance) if a.get("status") != "present"
        ],
        "behavior_log": rows(ds.behavior),
    }


@mcp.tool()
def flag_at_risk_students(
    class_id: str | None = None,
    as_of: str | None = None,
    include_watch: bool = True,
    failing_pct: float = 60.0,
    low_pct: float = 70.0,
    missing_count: int = 3,
    attendance_rate: float = 90.0,
    window_days: int = 30,
) -> dict:
    """Screen students for academic, engagement, attendance and behavior
    warning signs. Returns students sorted High -> Moderate -> Watch, each
    with the specific reasons, metrics, strengths and existing supports.

    as_of: ISO date (YYYY-MM-DD); defaults to the latest date in the data.
    Thresholds can be tuned to match school policy."""
    ds = _ds()
    t = risk.Thresholds(
        failing_pct=failing_pct,
        low_pct=low_pct,
        missing_count=missing_count,
        attendance_rate=attendance_rate,
        window_days=window_days,
    )
    results = risk.screen_class(ds, class_id, _as_of(as_of), t)
    keep = {"High", "Moderate"} | ({"Watch"} if include_watch else set())
    flagged = [r.to_dict() for r in results if r.tier in keep]
    counts = {tier: sum(r.tier == tier for r in results) for tier in risk.TIER_ORDER}
    return {
        "as_of": (_as_of(as_of) or ds.latest_date()).isoformat(),
        "class_id": class_id or "all",
        "students_screened": len(results),
        "tier_counts": counts,
        "flagged": flagged,
        "rules": (
            "Points: failing avg 3 / low avg 2; score drop 2; missing work 2-3; "
            "attendance below threshold 2-3, frequent tardies 1; behavior 1-2. "
            "Tier: High = 5+ points; Moderate = 2-4; Watch = 1."
        ),
        "disclaimer": (
            "Screening aid only. Confirm with the student, family and support "
            "staff before acting; flags are not labels."
        ),
    }


@mcp.tool()
def class_summary(class_id: str, as_of: str | None = None) -> dict:
    """Class-level snapshot: average, grade distribution, assignments with
    the most missing work or lowest scores, and at-risk counts. Good for
    progress reports to admin or planning reteaching."""
    ds = _ds()
    if class_id not in ds.classes:
        return {"error": f"Unknown class_id '{class_id}'.", "classes": list(ds.classes)}
    screens = risk.screen_class(ds, class_id, _as_of(as_of))
    avgs = [s.metrics["average_pct"] for s in screens if s.metrics.get("average_pct") is not None]
    bands = {"A (90+)": 0, "B (80-89)": 0, "C (70-79)": 0, "D (60-69)": 0, "F (<60)": 0}
    for a in avgs:
        key = "A (90+)" if a >= 90 else "B (80-89)" if a >= 80 else "C (70-79)" if a >= 70 else "D (60-69)" if a >= 60 else "F (<60)"
        bands[key] += 1

    by_assignment: dict[str, dict] = {}
    for g in ds.grades:
        if g.get("class_id") != class_id:
            continue
        a = by_assignment.setdefault(g.get("assignment", "?"), {"pcts": [], "missing": 0, "date": g.get("date")})
        if g["status"] == "missing":
            a["missing"] += 1
        elif g["_pct"] is not None and g["status"] != "excused":
            a["pcts"].append(g["_pct"])
    assignments = [
        {
            "assignment": name,
            "date": a["date"],
            "average_pct": round(sum(a["pcts"]) / len(a["pcts"]), 1) if a["pcts"] else None,
            "missing": a["missing"],
        }
        for name, a in by_assignment.items()
    ]
    return {
        "class": ds.classes[class_id],
        "enrolled": len(screens),
        "class_average_pct": round(sum(avgs) / len(avgs), 1) if avgs else None,
        "grade_distribution": bands,
        "lowest_scoring_assignments": sorted(
            [a for a in assignments if a["average_pct"] is not None],
            key=lambda a: a["average_pct"],
        )[:3],
        "most_missing_assignments": sorted(assignments, key=lambda a: -a["missing"])[:3],
        "tier_counts": {tier: sum(s.tier == tier for s in screens) for tier in risk.TIER_ORDER},
    }


@mcp.tool()
def get_sub_plan_context(day: str | None = None) -> dict:
    """Everything a substitute needs: schedule/periods and rooms, classroom
    procedures (emergency, attendance, dismissal, helpers), and per-class
    roster notes limited to what a sub needs (first name, supports,
    accommodations, notes). `day` is optional and only echoed back."""
    ds = _ds()
    classes = []
    for c in sorted(ds.classes.values(), key=lambda c: c.get("period", "")):
        students = ds.students_in(c["class_id"])
        classes.append({
            **c,
            "enrolled": len(students),
            "students_needing_attention": [
                {
                    "first_name": s.get("first_name"),
                    "last_initial": (s.get("last_name") or "")[:1],
                    "supports": s.get("supports"),
                    "accommodations": s.get("accommodations"),
                    "notes": s.get("notes"),
                }
                for s in students
                if s.get("supports") or s.get("accommodations") or s.get("notes")
            ],
        })
    return {
        "day": day,
        "classes": classes,
        "procedures": ds.procedures or "(No procedures.md found - ask the teacher for routines, emergency procedures and helpful staff.)",
    }


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()

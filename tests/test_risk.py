import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "server"))
import risk  # noqa: E402


def write(path, header, rows):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def make_ds(tmp_path, grades, attendance=(), behavior=()):
    write(tmp_path / "students.csv", ["student_id", "first_name", "last_name", "class_ids"],
          [["A", "Ann", "Able", "C1"], ["B", "Bo", "Best", "C1"]])
    write(tmp_path / "classes.csv", ["class_id", "name"], [["C1", "Math"]])
    write(tmp_path / "grades.csv",
          ["student_id", "class_id", "assignment", "date", "score", "max_score", "status"], grades)
    write(tmp_path / "attendance.csv", ["student_id", "date", "status"], attendance)
    write(tmp_path / "behavior.csv", ["student_id", "date", "type", "description"], behavior)
    return risk.load_dataset(tmp_path)


def test_clean_student_not_flagged(tmp_path):
    ds = make_ds(tmp_path, [["B", "C1", f"hw{i}", f"2026-10-0{i}", 95, 100, "submitted"] for i in range(1, 5)])
    r = risk.screen_student(ds, "B", "C1")
    assert r.tier == "None" and r.flags == []
    assert any("Strong average" in s for s in r.strengths)


def test_missing_work_counts_as_zero_and_flags(tmp_path):
    grades = [["A", "C1", "hw1", "2026-10-01", 80, 100, "submitted"]] + [
        ["A", "C1", f"m{i}", f"2026-10-0{i+2}", "", 100, "missing"] for i in range(3)
    ]
    r = risk.screen_student(make_ds(tmp_path, grades), "A", "C1")
    assert r.metrics["average_pct"] == 20.0
    cats = {f.category for f in r.flags}
    assert {"academics", "engagement"} <= cats
    assert r.tier == "High"


def test_excused_work_ignored(tmp_path):
    grades = [["A", "C1", "hw1", "2026-10-01", 90, 100, "submitted"],
              ["A", "C1", "hw2", "2026-10-02", "", 100, "excused"]]
    r = risk.screen_student(make_ds(tmp_path, grades), "A", "C1")
    assert r.metrics["average_pct"] == 90.0 and r.tier == "None"


def test_declining_trend(tmp_path):
    scores = [95, 92, 75, 70]
    grades = [["A", "C1", f"q{i}", f"2026-10-1{i}", s, 100, "submitted"] for i, s in enumerate(scores)]
    r = risk.screen_student(make_ds(tmp_path, grades), "A", "C1")
    assert any("dropped" in f.reason for f in r.flags)


def test_chronic_absence(tmp_path):
    att = [["A", f"2026-10-{d:02d}", "absent" if d <= 3 else "present"] for d in range(1, 21)]
    r = risk.screen_student(make_ds(tmp_path, [], att), "A")
    assert r.metrics["attendance_rate_pct"] == 85.0
    assert any(f.category == "attendance" for f in r.flags)


def test_behavior_window(tmp_path):
    beh = [["A", "2026-01-01", "concern", "old"]] * 5 + [["A", "2026-10-20", "concern", "new"]]
    grades = [["A", "C1", "hw", "2026-10-30", 90, 100, "submitted"]]
    r = risk.screen_student(make_ds(tmp_path, grades, behavior=beh), "A")
    assert r.metrics["behavior_concerns_recent"] == 1


def test_sample_data_ranks_expected_students():
    ds = risk.load_dataset(risk.BUNDLED_SAMPLE)
    results = risk.screen_class(ds)
    high = {r.name for r in results if r.tier == "High"}
    assert {"Caleb Ito", "Ethan Green"} <= high
    assert next(r for r in results if r.name == "Sofia Herrera").tier == "None"

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import check_math  # noqa: E402


def ok(item):
    return check_math.check(item)[0]


def test_correct_answers_pass():
    assert ok({"type": "arithmetic", "problem": "3/4 + 1/6", "answer": "11/12"})
    assert ok({"type": "arithmetic", "problem": "1 1/2 × 2/3", "answer": 1})
    assert ok({"type": "equation", "problem": "3(x - 2) + 4 = 19", "answer": {"x": 7}})
    assert ok({"type": "equation", "problem": "5 - 2n = 3n + 20", "answer": {"n": -3}})
    assert ok({"type": "system", "problem": ["2x + y = 7", "x - y = 2"], "answer": "(3, 1)"})
    assert ok({"type": "system", "problem": ["y = 2x + 1", "4x - 2y = 6"], "answer": "none"})
    assert ok({"type": "system", "problem": ["y = 2x + 1", "2y = 4x + 2"], "answer": "infinite"})
    assert ok({"type": "equivalent", "problem": "2(x + 3) - x", "answer": "x + 6"})
    assert ok({"type": "inequality", "problem": "-2x + 5 < 11", "answer": "x > -3"})
    assert ok({"type": "point_check", "problem": "y >= -x + 4", "point": {"x": 2, "y": 2}, "answer": True})
    assert ok({"type": "slope", "problem": [[1, 2], [3, 8]], "answer": "3"})
    assert ok({"type": "line_through", "problem": [[0, -1], [2, 5]], "answer": "y = 3x - 1"})


def test_wrong_answers_fail():
    assert not ok({"type": "inequality", "problem": "-2x + 5 < 11", "answer": "x < -3"})  # forgot to flip
    assert not ok({"type": "inequality", "problem": "x + 1 < 4", "answer": "x <= 3"})  # boundary wrong
    assert not ok({"type": "system", "problem": ["2x + y = 7", "x - y = 2"], "answer": "(1, 3)"})
    assert not ok({"type": "equivalent", "problem": "2(x + 3)", "answer": "2x + 3"})  # partial distribution
    assert not ok({"type": "system", "problem": ["y = 2x + 1", "2y = 4x + 2"], "answer": "none"})
    assert not ok({"type": "arithmetic", "problem": "1/2 + 1/3", "answer": "2/5"})  # add across


def test_cli_exit_code(tmp_path):
    f = tmp_path / "k.json"
    f.write_text(json.dumps([{"id": "a", "type": "arithmetic", "problem": "2+2", "answer": 5}]))
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "check_math.py"), str(f)], capture_output=True, text=True)
    assert r.returncode == 1 and "FAIL" in r.stdout


def test_standards_lookup():
    run = lambda *a: subprocess.run([sys.executable, str(ROOT / "tools" / "standards.py"), *a], capture_output=True, text=True)
    r = run("get", "A-REI.C.6", "MS-LS1-6", "RL.7.2")
    assert r.returncode == 0
    assert "Solve systems of linear equations exactly and approximately" in r.stdout
    assert "photosynthesis" in r.stdout and "theme or central idea" in r.stdout
    r = run("get", "XYZ.9.9")
    assert r.returncode == 1 and "NOT FOUND" in r.stdout
    r = run("search", "add and subtract fractions unlike denominators", "--set", "math", "--grade", "5")
    assert "5.NF.A.1" in r.stdout


def test_algebra_example_builds_and_all_answers_verify():
    r = subprocess.run([sys.executable, str(ROOT / "examples" / "algebra1-long-term-sub" / "build.py")], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "298/298 correct" in r.stdout

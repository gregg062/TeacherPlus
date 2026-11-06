#!/usr/bin/env python3
"""Look up K-12 standards bundled with TeacherPlus (standard library only).

Usage:
  python3 standards.py get HSA-REI.C.6 [MS-LS1-6 ...]
  python3 standards.py search "systems of linear equations" [--set math|ela|ngss] [--grade HS|7|K]
  python3 standards.py list --set math --grade 8 [--domain "Expressions"]

Sets: math = Common Core Mathematics, ela = Common Core ELA/Literacy,
ngss = Next Generation Science Standards (performance expectations).
Prints matching standards with their official text, so codes and wording
are quoted from the source instead of from memory.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

DIR = Path(__file__).resolve().parent.parent / "references" / "standards"
SETS = {"math": "ccss-math.csv", "ela": "ccss-ela.csv", "ngss": "ngss.csv"}


def load(sets: list[str]) -> list[dict]:
    rows = []
    for s in sets:
        with (DIR / SETS[s]).open(encoding="utf-8") as f:
            for r in csv.DictReader(f):
                r["set"] = s
                rows.append(r)
    return rows


def norm_code(c: str) -> str:
    c = c.upper().replace("CCSS.MATH.CONTENT.", "").replace("CCSS.ELA-LITERACY.", "")
    return re.sub(r"[\s_]", "", c)


def code_variants(code: str) -> set[str]:
    """HSA-REI.C.6, A-REI.C.6, A.REI.C.6 and HSA.REI.C.6 should all match."""
    c = norm_code(code)
    out = {c, c.replace(".", "-", 1)}
    if c.startswith("HS") and len(c) > 3 and c[2].isalpha() and not c.startswith("HS-"):
        out |= {c[2:], c[2:].replace("-", ".", 1)}
    else:
        for prefix in ("HS",):
            out.add(prefix + c)
            out.add(prefix + c.replace(".", "-", 1))
    return {norm_code(x) for x in out}


def grade_ok(row: dict, grade: str | None) -> bool:
    if not grade:
        return True
    g = grade.upper().lstrip("0") or "0"
    parts = row["grade"].upper().split(",")
    return g in parts or row["grade"].upper() == g or (g in ("9", "10", "11", "12") and "HS" in parts)


def show(rows: list[dict]) -> None:
    for r in rows:
        print(f"[{r['set']}] {r['code']}  (grade {r['grade']}; {r.get('domain') or r.get('topic', '')})")
        print(f"  {r['statement']}")
        for k in ("clarification", "assessment_boundary"):
            if r.get(k):
                print(f"  {k.replace('_', ' ').title()}: {r[k]}")
        print()


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("get")
    g.add_argument("codes", nargs="+")
    for name in ("search", "list"):
        p = sub.add_parser(name)
        if name == "search":
            p.add_argument("query")
        p.add_argument("--set", choices=list(SETS), action="append")
        p.add_argument("--grade")
        p.add_argument("--domain")
        p.add_argument("--limit", type=int, default=15)
    a = ap.parse_args(argv)

    rows = load(getattr(a, "set", None) or list(SETS))
    if a.cmd == "get":
        found, missing = [], []
        for code in a.codes:
            v = code_variants(code)
            hits = [r for r in rows if norm_code(r["code"]) in v]
            (found.extend(hits) if hits else missing.append(code))
        show(found)
        for m in missing:
            print(f"NOT FOUND: {m} - do not cite this code; search by topic instead.")
        return 1 if missing else 0

    rows = [r for r in rows if grade_ok(r, a.grade)]
    if a.domain:
        rows = [r for r in rows if a.domain.lower() in (r.get("domain") or r.get("topic") or "").lower()]
    if a.cmd == "search":
        terms = [t for t in re.findall(r"[a-z0-9]+", a.query.lower()) if len(t) > 2]
        scored = []
        for r in rows:
            text = " ".join(r.get(k, "") for k in ("statement", "domain", "topic", "clarification", "core_ideas")).lower()
            score = sum(text.count(t) for t in terms) + 3 * (a.query.lower() in text)
            if score:
                scored.append((score, r))
        rows = [r for _, r in sorted(scored, key=lambda x: -x[0])]
    show(rows[: a.limit])
    if not rows:
        print("No matches. Try fewer or different words, or drop --grade.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

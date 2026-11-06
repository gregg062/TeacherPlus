#!/usr/bin/env python3
"""Builds the 4-week Algebra 1 long-term sub example.

Lesson scripts are written by hand below. Problems are defined by their
numbers; worked solutions are generated step by step, and every answer is
then verified independently with tools/check_math.py. The build fails if
any answer is wrong.

Run:  python3 examples/algebra1-long-term-sub/build.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import date
from fractions import Fraction as F
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import check_math  # noqa: E402
import standards as stds  # noqa: E402

MINUS = "−"

# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------


def _is_decimal(x: F) -> bool:
    d = x.denominator
    for p in (2, 5):
        while d % p == 0:
            d //= p
    return d == 1


def n(x, dec: bool = False) -> str:
    x = F(x)
    if x.denominator == 1:
        s = str(abs(x.numerator))
    elif dec and _is_decimal(x):
        s = f"{float(abs(x)):g}"
    else:
        s = f"{abs(x.numerator)}/{x.denominator}"
    return (MINUS if x < 0 else "") + s


def term(c, v: str, first: bool, dec: bool = False) -> str:
    c = F(c)
    if c == 0:
        return ""
    mag = "" if (abs(c) == 1 and v) else n(abs(c), dec)
    if v and c.denominator != 1 and not (dec and _is_decimal(c)):
        mag = f"({mag})"
    body = f"{mag}{v}"
    if first:
        return (MINUS if c < 0 else "") + body
    return f" {MINUS if c < 0 else '+'} {body}"


def lin(cx=0, cy=0, k=0, order=("x", "y"), dec=False) -> str:
    parts, first = [], True
    coeffs = {"x": F(cx), "y": F(cy)}
    for v in order:
        t = term(coeffs[v], v, first, dec)
        if t:
            parts.append(t)
            first = False
    if F(k) != 0 or first:
        parts.append(term(k, "", first, dec) if F(k) != 0 else "0")
    return "".join(parts)


def subst(pairs, const=0) -> str:
    """Show substitution like 2(3) − (1) + 4: pairs of (coefficient, value)."""
    out, first = [], True
    for c, v in pairs:
        c = F(c)
        if c == 0:
            continue
        mag = "" if abs(c) == 1 else n(abs(c))
        body = f"{mag}({n(v)})"
        out.append((MINUS if c < 0 else "") + body if first else f" {MINUS if c < 0 else '+'} {body}")
        first = False
    if F(const) != 0:
        out.append(n(const) if first else f" {MINUS if const < 0 else '+'} {n(abs(F(const)))}")
    return "".join(out) or "0"


def pt(x, y) -> str:
    return f"({n(x)}, {n(y)})"


def slope_form(m, k) -> str:
    return f"y = {lin(m, 0, k)}"


@dataclass
class Eq:
    """a x + b y = c"""
    a: F
    b: F
    c: F
    show_slope: bool = False  # display as y = mx + k
    dec: bool = False  # show terminating fractions as decimals (money, percents)

    def __post_init__(self):
        self.a, self.b, self.c = F(self.a), F(self.b), F(self.c)

    def __str__(self):
        if self.show_slope and self.b == 1:
            return f"y = {lin(-self.a, 0, self.c, dec=self.dec)}"
        return f"{lin(self.a, self.b, dec=self.dec)} = {n(self.c, self.dec)}"

    def check_str(self):
        return f"{lin(self.a, self.b)} = {n(self.c)}"

    def std_str(self):
        return f"{lin(self.a, self.b, dec=self.dec)} = {n(self.c, self.dec)}"


def std(a, b, x, y) -> Eq:
    return Eq(a, b, a * x + b * y)


def slope_eq(m, x, y) -> Eq:
    """y = m x + k through (x, y), stored as -m x + y = k."""
    return Eq(-F(m), 1, F(y) - F(m) * x, show_slope=True)


# ---------------------------------------------------------------------------
# Problems: each returns (prompt, steps, answer_text, checker_items)
# ---------------------------------------------------------------------------


@dataclass
class Problem:
    prompt: str
    steps: list[str]
    answer: str
    checks: list[dict] = field(default_factory=list)


def p_identify(m, k) -> Problem:
    e = slope_form(m, k)
    return Problem(
        f"Identify the slope and y-intercept of {e}.",
        [f"The equation is in the form y = mx + b, so the slope m is the number multiplying x and b is the constant.",
         f"m = {n(m)}, b = {n(k)}, so the line crosses the y-axis at {pt(0, k)}."],
        f"slope {n(m)}, y-intercept {n(k)} (the point {pt(0, k)})",
        [{"type": "line_through", "problem": [[0, str(F(k))], [1, str(F(m) + k)]], "answer": e}],
    )


def p_to_slope(a, b, c) -> Problem:
    e = Eq(a, b, c)
    m, k = -F(a) / b, F(c) / b
    steps = [f"Start: {e}"]
    if a != 0:
        steps.append(f"{'Subtract' if a > 0 else 'Add'} {n(abs(F(a)))}x {'from' if a > 0 else 'to'} both sides: {lin(0, b)} = {lin(-F(a), 0, c)}")
    if b != 1:
        steps.append(f"Divide every term on both sides by {n(b)}: y = {lin(m, 0, k)}")
    pts = [[str(x), str((F(c) - F(a) * x) / b)] for x in (0, 3)]
    return Problem(
        f"Write {e} in slope-intercept form. Then name the slope and y-intercept.",
        steps + [f"Slope {n(m)}, y-intercept {n(k)}."],
        f"{slope_form(m, k)}; slope {n(m)}, y-intercept {n(k)}",
        [{"type": "line_through", "problem": pts, "answer": slope_form(m, k)}],
    )


def p_graph(m, k) -> Problem:
    m = F(m)
    rise, run = m.numerator, m.denominator
    pts = [(0, F(k)), (run, F(k) + rise), (2 * run, F(k) + 2 * rise)]
    return Problem(
        f"Graph {slope_form(m, k)}. List three points on the line.",
        [f"Plot the y-intercept {pt(0, k)}.",
         f"Slope {n(m)} = rise {n(rise)} / run {run}: from {pt(*pts[0])} go {'up' if rise > 0 else 'down'} {abs(rise)} and right {run} to {pt(*pts[1])}.",
         f"Repeat to get {pt(*pts[2])}. Draw a line through the points with arrows on both ends."],
        f"points {pt(*pts[0])}, {pt(*pts[1])}, {pt(*pts[2])}",
        [{"type": "line_through", "problem": [[str(a), str(b)] for a, b in pts], "answer": slope_form(m, k)}],
    )


def p_is_solution(e1: Eq, e2: Eq, x, y) -> Problem:
    steps, ok_all, checks = [], True, []
    for i, e in enumerate((e1, e2), 1):
        val = e.a * x + e.b * y
        ok = val == e.c
        ok_all &= ok
        if e.show_slope:
            rhs = -e.a * x + e.c
            steps.append(f"Equation {i}: {e}. Substitute: {n(y)} = {subst([(-e.a, x)], e.c)} = {n(rhs)}. {'True ✓' if ok else 'False ✗'}")
        else:
            steps.append(f"Equation {i}: {e}. Substitute: {subst([(e.a, x), (e.b, y)])} = {n(val)}. {'Equals ' + n(e.c) + ' ✓' if ok else 'Not ' + n(e.c) + ' ✗'}")
        checks.append({"type": "point_check", "problem": e.check_str(), "point": {"x": str(x), "y": str(y)}, "answer": ok})
    steps.append("It must work in BOTH equations to be a solution." if not ok_all else "It works in both equations, so it is a solution.")
    return Problem(f"Is {pt(x, y)} a solution of the system  {e1}  and  {e2}?", steps,
                   "Yes" if ok_all else "No", checks)


def p_graph_system(m1, m2, x, y) -> Problem:
    e1, e2 = slope_eq(m1, x, y), slope_eq(m2, x, y)
    k1, k2 = e1.c, e2.c
    return Problem(
        f"Solve by graphing:  {e1}  and  {e2}.",
        [f"Graph {e1}: start at {pt(0, k1)}, slope {n(m1)}.",
         f"Graph {e2}: start at {pt(0, k2)}, slope {n(m2)}.",
         f"The lines cross at {pt(x, y)}.",
         f"Check in both: {n(y)} = {subst([(m1, x)], k1)} ✓ and {n(y)} = {subst([(m2, x)], k2)} ✓"],
        pt(x, y),
        [{"type": "system", "problem": [e1.check_str(), e2.check_str()], "answer": {"x": str(x), "y": str(y)}}],
    )


def _sub_steps(iso: Eq, other: Eq, var: str):
    """Substitution: isolate `var` from iso (coefficient ±1), plug into other."""
    steps = []
    if var == "y":
        coef, oc = iso.b, iso.a  # coef*y + oc*x = c  -> y = (c - oc x)/coef
        ex, ek = -oc / coef, iso.c / coef
        expr = lin(ex, 0, ek)
        if not iso.show_slope:
            steps.append(f"Solve the first equation for y: {iso}  →  y = {expr}")
        else:
            steps.append(f"The first equation already says y = {expr}.")
        pre, a_other, b_other = other.b, other.a, other.b
        sub_line = f"{lin(a_other, 0)} {'+' if b_other > 0 else MINUS} {'' if abs(b_other) == 1 else n(abs(b_other))}({expr}) = {n(other.c)}"
        tx = a_other + b_other * ex
        tk = b_other * ek
        dist = f"{lin(a_other, 0)}{term(b_other * ex, 'x', False)}{term(b_other * ek, '', False)} = {n(other.c)}"
        other_var = "x"
    else:
        coef, oc = iso.a, iso.b
        ex, ek = -oc / coef, iso.c / coef  # x = ex*y + ek
        expr = lin(0, ex, ek)
        steps.append(f"Solve the first equation for x: {iso}  →  x = {expr}")
        a_other, b_other = other.a, other.b
        sub_line = f"{'' if abs(a_other) == 1 else n(a_other) if a_other > 0 else MINUS + n(abs(a_other))}{MINUS if a_other == -1 else ''}({expr}){term(b_other, 'y', False)} = {n(other.c)}"
        tx = b_other + a_other * ex
        tk = a_other * ek
        dist = f"{lin(0, a_other * ex, 0)}{term(a_other * ek, '', False)}{term(b_other, 'y', False)} = {n(other.c)}"
        other_var = "y"
    steps.append(f"Substitute ({expr}) for {var} in the second equation, keeping the parentheses: {sub_line}")
    steps.append(f"Distribute: {dist}")
    vx = (lambda c: lin(c, 0)) if other_var == "x" else (lambda c: lin(0, c))
    steps.append(f"Combine like terms: {vx(tx)}{term(tk, '', False)} = {n(other.c)}" if tx != 0 else f"Combine like terms: the {other_var} terms cancel, leaving {n(tk)} = {n(other.c)}")
    return steps, tx, tk, ex, ek, other_var, expr


def p_substitution(iso: Eq, other: Eq, var="y", context: str | None = None) -> Problem:
    steps, tx, tk, ex, ek, ov, expr = _sub_steps(iso, other, var)
    checks_sys = [iso.check_str(), other.check_str()]
    if tx == 0:
        if tk == other.c:
            steps.append(f"{n(tk)} = {n(other.c)} is always true, so every point on the line works: infinitely many solutions (the equations are the same line).")
            return Problem(f"Solve by substitution:  {iso}  and  {other}.", steps, "infinitely many solutions",
                           [{"type": "system", "problem": checks_sys, "answer": "infinite"}])
        steps.append(f"{n(tk)} = {n(other.c)} is never true, so there is no solution (the lines are parallel).")
        return Problem(f"Solve by substitution:  {iso}  and  {other}.", steps, "no solution",
                       [{"type": "system", "problem": checks_sys, "answer": "none"}])
    rhs = other.c - tk
    if tk != 0:
        steps.append(f"{'Subtract' if tk > 0 else 'Add'} {n(abs(tk))} {'from' if tk > 0 else 'to'} both sides: {lin(tx, 0) if ov == 'x' else lin(0, tx)} = {n(rhs)}")
    val = rhs / tx
    if tx != 1:
        steps.append(f"Divide both sides by {n(tx)}: {ov} = {n(val)}")
    back = ex * val + ek
    steps.append(f"Substitute {ov} = {n(val)} into {var} = {expr}: {var} = {subst([(ex, val)], ek)} = {n(back)}")
    sol = (val, back) if ov == "x" else (back, val)
    steps.append(f"Solution {pt(*sol)}. Check in the second equation: {subst([(other.a, sol[0]), (other.b, sol[1])])} = {n(other.a * sol[0] + other.b * sol[1])} ✓")
    return Problem(context or f"Solve by substitution:  {iso}  and  {other}.", steps, pt(*sol),
                   [{"type": "system", "problem": checks_sys, "answer": {"x": str(sol[0]), "y": str(sol[1])}}])


def p_elimination(e1: Eq, e2: Eq, context: str | None = None) -> Problem:
    steps = [f"Line up the equations in standard form:  (1) {e1.std_str()}   (2) {e2.std_str()}" if not (e1.show_slope or e2.show_slope)
             else f"Rewrite in standard form (x and y on the left):  (1) {e1.std_str()}   (2) {e2.std_str()}"]
    originals = (e1, e2)
    fixed = []
    for idx, e in enumerate((e1, e2), 1):
        den = 1
        for v in (e.a, e.b, e.c):
            den = den * v.denominator // gcd(den, v.denominator)
        if den != 1:
            e = Eq(e.a * den, e.b * den, e.c * den)
            steps.append(f"Clear the {'decimals' if all(_is_decimal(v) for v in (originals[idx-1].a, originals[idx-1].b, originals[idx-1].c)) else 'fractions'} in equation ({idx}): multiply every term by {den}: {e.check_str()}")
        fixed.append(e)
    e1, e2 = fixed
    a1, b1, c1, a2, b2, c2 = e1.a, e1.b, e1.c, e2.a, e2.b, e2.c
    # choose multipliers so that y (preferred) or x cancels when ADDED
    def mults(p, q):
        if p == -q:
            return 1, 1
        if p == q:
            return 1, -1
        l = abs(p * q) // gcd(int(abs(p)), int(abs(q)))
        k1, k2 = l / abs(p), l / abs(q)
        return (k1, -k2) if (p > 0) == (q > 0) else (k1, k2)

    options = []
    for var, p, q in (("y", b1, b2), ("x", a1, a2)):
        k1, k2 = mults(p, q)
        # prefer: just add (1, 1) < multiply by -1 < larger multipliers; then y before x
        cost = abs(k1) + abs(k2) + (0.5 if (k1 < 0 or k2 < 0) else 0) + (0.1 if var == "x" else 0)
        options.append((cost, var, k1, k2))
    _, var, k1, k2 = min(options)
    k1, k2 = F(k1), F(k2)
    for k, idx, (a, b, c) in ((k1, 1, (a1, b1, c1)), (k2, 2, (a2, b2, c2))):
        if k != 1:
            steps.append(f"Multiply EVERY term of equation ({idx}) by {n(k)}: {lin(k * a, k * b)} = {n(k * c)}")
    A, B, C = k1 * a1 + k2 * a2, k1 * b1 + k2 * b2, k1 * c1 + k2 * c2
    keep = "x" if var == "y" else "y"
    kc = A if keep == "x" else B
    if kc == 0:
        steps.append(f"Add the equations: both variables cancel, leaving 0 = {n(C)}.")
        ans = "infinite" if C == 0 else "none"
        steps.append("0 = 0 is always true: infinitely many solutions (same line)." if C == 0 else f"0 = {n(C)} is never true: no solution (parallel lines).")
        return Problem(context or f"Solve by elimination:  {e1}  and  {e2}.", steps,
                       "infinitely many solutions" if C == 0 else "no solution",
                       [{"type": "system", "problem": [e1.check_str(), e2.check_str()], "answer": ans}])
    steps.append(f"Add the equations. The {var} terms cancel: {lin(kc, 0) if keep == 'x' else lin(0, kc)} = {n(C)}")
    val = C / kc
    if kc != 1:
        steps.append(f"Divide both sides by {n(kc)}: {keep} = {n(val)}")
    if keep == "x":
        rest = (c1 - a1 * val) / b1
        steps.append(f"Substitute x = {n(val)} into equation (1): {subst([(a1, val)])}{term(b1, 'y', False)} = {n(c1)} → {lin(0, b1)} = {n(c1 - a1 * val)}" + ("" if b1 == 1 else f" → y = {n(rest)}"))
        sol = (val, rest)
    else:
        rest = (c1 - b1 * val) / a1
        steps.append(f"Substitute y = {n(val)} into equation (1): {lin(a1, 0)} {MINUS if b1 < 0 else '+'} {'' if abs(b1) == 1 else n(abs(b1))}({n(val)}) = {n(c1)} → {lin(a1, 0)} = {n(c1 - b1 * val)}" + ("" if a1 == 1 else f" → x = {n(rest)}"))
        sol = (rest, val)
    steps.append(f"Solution {pt(*sol)}. Check in equation (2): {subst([(a2, sol[0]), (b2, sol[1])])} = {n(a2 * sol[0] + b2 * sol[1])} ✓")
    return Problem(context or f"Solve by elimination:  {e1}  and  {e2}.", steps, pt(*sol),
                   [{"type": "system", "problem": [e1.check_str(), e2.check_str()], "answer": {"x": str(sol[0]), "y": str(sol[1])}}])


def p_word(text: str, defs: str, e1: Eq, e2: Eq, method: str, sentence: str) -> Problem:
    e1.dec = e2.dec = True
    base = (p_elimination(e1, e2) if method == "elimination"
            else p_substitution(e1, e2, "y" if e1.b in (1, -1) else "x"))
    x, y = [F(v) for v in (base.checks[0]["answer"]["x"], base.checks[0]["answer"]["y"])]
    steps = [f"Define the variables: {defs}", f"Write the system: {e1}  and  {e2}", *base.steps,
             f"Answer the question in a sentence: {sentence.format(x=n(x), y=n(y))}"]
    return Problem(text, steps, sentence.format(x=n(x), y=n(y)), base.checks)


def p_ineq_graph(m, k, op: str) -> Problem:
    line = "dashed" if op in ("<", ">") else "solid"
    above = op in (">", ">=")
    e = f"y {op.replace('>=', '≥').replace('<=', '≤')} {lin(m, 0, k)}"
    test_true = 0 > -F(k) if above else 0 < -F(k)  # is (0,0) a solution?  0 op m*0 + k
    zero_ok = {">": 0 > k, ">=": 0 >= k, "<": 0 < k, "<=": 0 <= k}[op]
    steps = [f"Graph the boundary line {slope_form(m, k)} (start at {pt(0, k)}, slope {n(m)}).",
             f"The symbol is {e.split()[1]}, so the line is {line} ({'points on the line are not solutions' if line == 'dashed' else 'points on the line are solutions'}).",
             f"Test (0, 0): 0 {e.split()[1]} {n(k)} is {'true' if zero_ok else 'false'}, so shade the side {'with' if zero_ok else 'without'} (0, 0) — {'above' if above else 'below'} the line."]
    if k == 0:
        steps[-1] = f"(0, 0) is on the line, so test (0, 1): 1 {e.split()[1]} 0 is {'true' if above else 'false'}, so shade {'above' if above else 'below'} the line."
    probe = {"x": "0", "y": str(F(k) + 1)}
    return Problem(f"Graph {e}.", steps, f"{line} boundary line {slope_form(m, k)}, shade {'above' if above else 'below'}",
                   [{"type": "point_check", "problem": f"y {op} {lin(m, 0, k)}", "point": probe, "answer": above}])


def p_ineq_system_point(ineqs: list[tuple], x, y) -> Problem:
    steps, ok_all, checks = [], True, []
    for m, k, op in ineqs:
        rhs = F(m) * x + k
        ok = {">": y > rhs, ">=": y >= rhs, "<": y < rhs, "<=": y <= rhs}[op]
        ok_all &= ok
        sym = op.replace('>=', '≥').replace('<=', '≤')
        steps.append(f"y {sym} {lin(m, 0, k)}: is {n(y)} {sym} {subst([(m, x)], k)} = {n(rhs)}? {'Yes ✓' if ok else 'No ✗'}")
        checks.append({"type": "point_check", "problem": f"y {op} {lin(m, 0, k)}", "point": {"x": str(x), "y": str(y)}, "answer": ok})
    steps.append("It satisfies every inequality, so it is in the solution region." if ok_all else "It fails at least one inequality, so it is NOT in the solution region.")
    desc = "  and  ".join(f"y {op.replace('>=', '≥').replace('<=', '≤')} {lin(m, 0, k)}" for m, k, op in ineqs)
    return Problem(f"Is {pt(x, y)} a solution of the system  {desc}?", steps, "Yes" if ok_all else "No", checks)


# ---------------------------------------------------------------------------
# Lessons
# ---------------------------------------------------------------------------


@dataclass
class Lesson:
    day: int
    date: date
    title: str
    target: str
    standards: list[str]
    kind: str  # new | quiz | review | test
    intro: str = ""
    do_now: list[Problem] = field(default_factory=list)
    examples: list[Problem] = field(default_factory=list)
    mistake: tuple | None = None  # (problem text, wrong work lines, what's wrong, fix)
    watch: list[tuple[str, str]] = field(default_factory=list)  # (misconception, what to say)
    guided: list[Problem] = field(default_factory=list)
    independent: list[Problem] = field(default_factory=list)
    exit: list[Problem] = field(default_factory=list)
    quiz: list[Problem] = field(default_factory=list)
    extra: str = ""
    materials: str = "Do Now slide or board, guided notes handout, practice handout, exit ticket slips"


D = date
L: list[Lesson] = []

# ---- Week 1 ---------------------------------------------------------------
L.append(Lesson(1, D(2027, 1, 4), "Slope-intercept form (review)",
    "I can identify the slope and y-intercept of a line and rewrite an equation in slope-intercept form.",
    ["HSF-IF.C.7a", "HSA-CED.A.2"], "new",
    intro=("\"This unit is about systems of equations: two equations at once. To solve them by graphing we need to be fast with lines, "
           "so today we review y = mx + b. m is the slope (how steep, and which way), b is where the line crosses the y-axis.\""),
    do_now=[p_identify(2, 5), p_identify(-3, 1), p_identify(F(1, 2), -4)],
    examples=[p_to_slope(3, 1, 7), p_to_slope(4, 2, 10)],
    mistake=("Write 6x + 3y = 12 in slope-intercept form.",
             ["3y = 6x + 12", "y = 2x + 4"],
             "The student added 6x to the right side instead of subtracting it. To remove +6x from the left we subtract 6x from BOTH sides.",
             "3y = −6x + 12, so y = −2x + 4."),
    watch=[("Slope and intercept swapped (graphing y = 3x + 2 starting at 3).", "\"Which number is alone, without an x? That's where we start on the y-axis.\""),
           ("Dividing only the first term by the coefficient of y (y = −2x + 10).", "\"Divide EVERY term on both sides, not just the first one.\"")],
    guided=[p_to_slope(2, 1, -3), p_to_slope(-5, 1, 2), p_to_slope(6, 3, 9)],
    independent=[p_identify(-1, 6), p_identify(F(2, 3), 0), p_to_slope(4, 1, 8), p_to_slope(-2, 1, -5), p_to_slope(8, 4, 12), p_to_slope(3, -1, 4)],
    exit=[p_to_slope(10, 5, 15), p_identify(F(-3, 4), 2)]))

L.append(Lesson(2, D(2027, 1, 5), "Graphing lines from slope-intercept form",
    "I can graph a line from its equation in slope-intercept form.",
    ["HSF-IF.C.7a", "HSA-REI.D.10"], "new",
    intro=("\"Every point on a line is a solution of its equation. Today we graph lines by starting at the y-intercept and using the slope as rise over run.\""),
    do_now=[p_to_slope(2, 1, 6), p_identify(-4, 3), p_identify(F(1, 3), -2)],
    examples=[p_graph(2, -3), p_graph(F(-2, 3), 4)],
    mistake=("Graph y = −2x + 1.",
             ["Plot (0, 1).", "Slope −2: go up 2, right 1 to (1, 3)."],
             "A negative slope goes DOWN as you move right. The student went up.",
             "From (0, 1) go down 2, right 1 to (1, −1)."),
    watch=[("Going up for a negative slope.", "\"Is this line going uphill or downhill from left to right? So is the slope positive or negative?\""),
           ("Starting at the x-axis instead of the y-axis.", "\"b is where the line crosses the y-axis, the vertical one. x is 0 there.\""),
           ("Treating a fraction slope 2/3 as rise 3, run 2.", "\"Rise over run: top number is up/down, bottom number is right.\"")],
    guided=[p_graph(1, 2), p_graph(-3, 5), p_graph(F(1, 2), -1)],
    independent=[p_graph(3, -4), p_graph(-1, 0), p_graph(F(3, 4), -2), p_graph(F(-1, 2), 3), p_graph(4, 1), p_graph(F(-5, 2), 6)],
    exit=[p_graph(-2, 4), p_graph(F(2, 5), -3)],
    materials="Graph paper handout (4 small grids per page), rulers, Do Now slide, exit ticket slips"))

L.append(Lesson(3, D(2027, 1, 6), "What is a system of equations?",
    "I can decide whether an ordered pair is a solution of a system of equations.",
    ["HSA-REI.C.6", "HSA-REI.D.11"], "new",
    intro=("\"A system is two equations about the same two unknowns. A solution is an ordered pair (x, y) that makes BOTH equations true at the same time. "
           "On a graph, that's where the two lines cross.\""),
    do_now=[p_graph(1, -2), p_to_slope(3, 1, 4), p_identify(-2, 7)],
    examples=[p_is_solution(Eq(1, 1, 5), Eq(2, -1, 1), 2, 3), p_is_solution(slope_eq(2, 1, 3), Eq(1, 1, 6), 1, 3)],
    mistake=("Is (4, 1) a solution of x + y = 5 and x − y = 2?",
             ["4 + 1 = 5 ✓", "So (4, 1) is a solution."],
             "The student only checked the first equation. 4 − 1 = 3, not 2, so it fails the second equation.",
             "No, (4, 1) is not a solution; it must work in both equations."),
    watch=[("Checking only one equation.", "\"A solution has to make BOTH equations true. Check every equation.\""),
           ("Substituting x and y in the wrong order.", "\"Ordered pair means (x, y): x first, always.\"")],
    guided=[p_is_solution(Eq(1, 1, 7), Eq(1, -1, 1), 4, 3), p_is_solution(Eq(2, 1, 8), Eq(1, -1, 4), 3, 2), p_is_solution(slope_eq(-1, 2, 4), slope_eq(3, 2, 4), 2, 4)],
    independent=[p_is_solution(Eq(3, 1, 10), Eq(1, 2, 5), 3, 1), p_is_solution(Eq(1, 1, 0), Eq(2, 1, 3), 3, -3), p_is_solution(Eq(1, -2, 4), Eq(3, 1, 5), 2, -1),
                 p_is_solution(slope_eq(2, 0, -3), Eq(1, 1, 3), 2, 1), p_is_solution(Eq(4, -1, 9), Eq(1, 3, -1), 2, -1), p_is_solution(Eq(5, 2, 1), Eq(1, 1, 2), -1, 3)],
    exit=[p_is_solution(Eq(2, 3, 12), Eq(1, -1, 1), 3, 2), p_is_solution(Eq(1, 4, 9), Eq(2, -1, 0), 1, 2)]))

L.append(Lesson(4, D(2027, 1, 7), "Solving systems by graphing",
    "I can solve a system of linear equations by graphing and check my solution.",
    ["HSA-REI.C.6", "HSA-REI.D.11"], "new",
    intro=("\"Yesterday we checked solutions. Today we FIND them: graph both lines carefully and find where they cross. Then check, because graphs can be a little off.\""),
    do_now=[p_is_solution(Eq(1, 1, 6), Eq(1, -1, 2), 4, 2), p_graph(-1, 3), p_graph(2, -1)],
    examples=[p_graph_system(1, -1, 2, 3), p_graph_system(2, F(-1, 2), 2, 1)],
    mistake=("Solve by graphing: y = x + 1 and y = −x + 5.",
             ["The lines cross at (3, 2)."],
             "The student read the point backwards. The lines cross where x = 2 and y = 3. Check: 3 = 2 + 1 ✓ and 3 = −2 + 5 ✓.",
             "(2, 3)"),
    watch=[("Reading the intersection as (y, x).", "\"Go across first for x, then up or down for y.\""),
           ("Sloppy graphs giving the wrong point.", "\"Use a ruler, and ALWAYS check the point in both equations.\""),
           ("Thinking parallel lines have a solution.", "\"If the lines never cross, there's no point that works in both: no solution.\"")],
    guided=[p_graph_system(1, 2, -1, 1), p_graph_system(-2, 1, 1, 2), p_graph_system(3, -1, 0, -2)],
    independent=[p_graph_system(1, -2, 1, 4), p_graph_system(-1, F(1, 2), 2, 1), p_graph_system(2, -1, -1, -3), p_graph_system(F(1, 3), -1, 3, 2), p_graph_system(-3, 1, 2, -1), p_graph_system(4, 2, 0, 3)],
    exit=[p_graph_system(1, -3, 1, 2), p_graph_system(F(1, 2), -2, -2, 1)],
    materials="Graph paper handout, rulers, colored pencils (two colors), exit ticket slips"))

L.append(Lesson(5, D(2027, 1, 8), "Quiz 1 + flex/reteach",
    "I can show what I know about graphing lines and solving systems by graphing.",
    ["HSF-IF.C.7a", "HSA-REI.C.6", "HSA-REI.D.11"], "quiz",
    intro="\"Today is a short quiz on this week's work, then we'll practice whatever needs more work.\"",
    do_now=[p_identify(3, -2), p_to_slope(2, 1, 5)],
    quiz=[p_to_slope(6, 2, 8), p_identify(-4, 9), p_graph(F(-1, 3), 2), p_is_solution(Eq(1, 2, 7), Eq(3, -1, 7), 3, 2),
          p_is_solution(Eq(2, 1, 5), Eq(1, 1, 4), 2, 1), p_graph_system(2, -1, 1, 1), p_graph_system(F(1, 2), -1, 2, 2), p_to_slope(-3, 1, -6)],
    extra=("**Flex plan (after the quiz, about 20 minutes):** Grade the quiz quickly with the key, or sort by question 6-7 only. "
           "If most students missed the graphing-systems questions, reteach Day 4's worked example on the board and do two more together. "
           "Students who did well: independent practice odd problems from Day 4 they skipped, or the challenge: \"Write a system whose solution is (2, −1).\"")))

# ---- Week 2 ---------------------------------------------------------------
L.append(Lesson(6, D(2027, 1, 11), "Substitution (one equation solved for y)",
    "I can solve a system by substitution when one equation is already solved for a variable.",
    ["HSA-REI.C.6"], "new",
    intro=("\"Graphing works, but it's slow and answers like (2.5, 1.3) are hard to read. Substitution gives exact answers. "
           "If one equation tells us what y equals, we can REPLACE y in the other equation with that expression. "
           "Then we have one equation with one variable, which we already know how to solve.\""),
    do_now=[p_graph_system(1, -1, 1, 2), p_to_slope(3, 1, 2), p_is_solution(Eq(1, 1, 4), Eq(2, -1, 5), 3, 1)],
    examples=[p_substitution(slope_eq(2, 1, 5), Eq(3, 1, 8), "y"), p_substitution(slope_eq(-1, 4, -2), Eq(2, -3, 14), "y")],
    mistake=("Solve: y = −x + 4 and 2x − y = 5.",
             ["2x − x + 4 = 5", "x + 4 = 5", "x = 1"],
             "No parentheses, so the minus sign was only applied to the first term. 2x − (−x + 4) = 5 means 2x + x − 4 = 5.",
             "3x − 4 = 5, x = 3, y = 1. Solution (3, 1)."),
    watch=[("Forgetting parentheses when substituting.", "\"Write the parentheses first, then put the expression inside.\""),
           ("Stopping after finding x.", "\"A solution is an ordered pair. Go back and find y.\""),
           ("Substituting back into the same equation you used.", "\"Use the 'y =' equation to find y; check in the other.\"")],
    guided=[p_substitution(slope_eq(3, 2, 4), Eq(1, 1, 6), "y"), p_substitution(slope_eq(-2, 1, 5), Eq(4, 1, 9), "y"), p_substitution(slope_eq(1, -3, -1), Eq(2, 3, -9), "y")],
    independent=[p_substitution(slope_eq(4, 1, 1), Eq(1, 1, 2), "y"), p_substitution(slope_eq(-1, 5, -2), Eq(3, 2, 11), "y"), p_substitution(slope_eq(2, -2, 0), Eq(5, -1, -10), "y"),
                 p_substitution(slope_eq(-3, 2, -4), Eq(1, 2, -6), "y"), p_substitution(slope_eq(1, 6, 4), Eq(2, -3, 0), "y"), p_substitution(slope_eq(5, 0, 3), Eq(2, 1, 3), "y")],
    exit=[p_substitution(slope_eq(2, 3, 7), Eq(1, 1, 10), "y"), p_substitution(slope_eq(-4, 1, 0), Eq(3, 2, 3), "y")]))

L.append(Lesson(7, D(2027, 1, 12), "Substitution (solve for a variable first)",
    "I can solve a system by substitution by first solving one equation for a variable.",
    ["HSA-REI.C.6"], "new",
    intro=("\"Today neither equation starts as 'y ='. Look for a variable with a coefficient of 1 or −1. Solve for it first, then substitute like yesterday.\""),
    do_now=[p_substitution(slope_eq(2, 1, 3), Eq(1, 1, 4), "y"), p_to_slope(5, 1, 3), p_identify(F(-1, 2), 6)],
    examples=[p_substitution(std(3, 1, 2, 1), std(2, 5, 2, 1), "y"), p_substitution(std(1, -2, 4, 1), std(3, 4, 4, 1), "x")],
    mistake=("Solve: x + 3y = 7 and 2x − y = 0.",
             ["x = 7 + 3y", "2(7 + 3y) − y = 0"],
             "To get x alone the student needed to SUBTRACT 3y from both sides: x = 7 − 3y.",
             "2(7 − 3y) − y = 0 → 14 − 7y = 0 → y = 2, x = 1. Solution (1, 2)."),
    watch=[("Sign error when isolating the variable.", "\"What are you doing to both sides? Say it: 'subtract 3y from both sides'.\""),
           ("Choosing a variable with a big coefficient and getting fractions.", "\"Look for a coefficient of 1 or −1 first.\"")],
    guided=[p_substitution(std(2, 1, 3, -1), std(3, -2, 3, -1), "y"), p_substitution(std(1, 4, 2, 1), std(3, -2, 2, 1), "x"), p_substitution(std(-1, 1, 1, 5), std(4, 3, 1, 5), "y")],
    independent=[p_substitution(std(4, 1, 1, 2), std(3, 2, 1, 2), "y"), p_substitution(std(1, -3, 5, 1), std(2, 1, 5, 1), "x"), p_substitution(std(5, -1, 0, 4), std(2, 3, 0, 4), "y"),
                 p_substitution(std(1, 2, -2, 3), std(4, -3, -2, 3), "x"), p_substitution(std(-3, 1, 2, 7), std(2, -1, 2, 7), "y"), p_substitution(std(1, 5, 4, -1), std(-2, -3, 4, -1), "x")],
    exit=[p_substitution(std(3, 1, 1, 4), std(2, -3, 1, 4), "y"), p_substitution(std(1, -1, 6, 2), std(2, 3, 6, 2), "x")]))

L.append(Lesson(8, D(2027, 1, 13), "No solution and infinitely many solutions",
    "I can recognize systems with no solution or infinitely many solutions, algebraically and on a graph.",
    ["HSA-REI.C.6", "HSA-REI.D.11"], "new",
    intro=("\"Sometimes the variables disappear. If we end with something false like 0 = 5, the lines are parallel and there's no solution. "
           "If we end with something always true like 0 = 0, it's the same line twice: infinitely many solutions.\""),
    do_now=[p_substitution(std(2, 1, 1, 3), std(1, -1, 1, 3), "y"), p_graph(2, 1), p_graph(2, -3)],
    examples=[p_substitution(Eq(-2, 1, 1, show_slope=True), Eq(4, -2, 6), "y"), p_substitution(Eq(-3, 1, -2, show_slope=True), Eq(6, -2, 4), "y"),
              p_substitution(std(1, 2, 3, 1), std(2, 1, 3, -1), "x")],
    mistake=("Solve: y = 3x + 1 and 6x − 2y = 4.",
             ["6x − 2(3x + 1) = 4", "6x − 6x − 2 = 4", "−2 = 4", "x = 0, so the solution is (0, 1)."],
             "−2 = 4 is FALSE and has no x in it. It doesn't mean x = 0. It means no ordered pair works.",
             "No solution (the lines have the same slope, 3, and different intercepts, so they're parallel)."),
    watch=[("Writing x = 0 when the variables cancel.", "\"Is −2 = 4 ever true? Then no point works.\""),
           ("Confusing 'no solution' and 'infinitely many'.", "\"False statement: never works, no solution. True statement: always works, infinitely many.\""),
           ("Not connecting to the graph.", "\"Same slope, different intercept: parallel. Same slope, same intercept: same line.\"")],
    guided=[p_substitution(Eq(-1, 1, 4, show_slope=True), Eq(3, -3, -12), "y"), p_substitution(Eq(-4, 1, 1, show_slope=True), Eq(8, -2, 6), "y"), p_substitution(Eq(-2, 1, 3, show_slope=True), Eq(1, 1, 6), "y")],
    independent=[p_substitution(Eq(-5, 1, 2, show_slope=True), Eq(10, -2, 4), "y"), p_substitution(Eq(-5, 1, 2, show_slope=True), Eq(10, -2, -4), "y"), p_substitution(std(1, 1, 2, 2), std(3, 3, 2, 2), "y"),
                 p_substitution(Eq(1, 1, 5), Eq(2, 2, 7), "y"), p_substitution(std(2, 1, 1, -1), std(1, 3, 1, -1), "y"), p_substitution(Eq(F(-1, 2), 1, 3, show_slope=True), Eq(1, -2, -6), "y")],
    exit=[p_substitution(Eq(-2, 1, 5, show_slope=True), Eq(6, -3, 2), "y"), p_substitution(Eq(-1, 1, -3, show_slope=True), Eq(2, -2, 6), "y")]))

L.append(Lesson(9, D(2027, 1, 14), "Word problems with substitution",
    "I can write and solve a system of equations to model a real situation.",
    ["HSA-CED.A.3", "HSA-REI.C.6"], "new",
    intro=("\"Systems are useful when two facts are true about two unknowns. Step 1 is always: define your variables in words, like 'a = number of adult tickets'. "
           "Then write one equation for each fact.\""),
    do_now=[p_substitution(std(1, 1, 3, 4), std(2, -1, 3, 4), "y"), p_substitution(Eq(-3, 1, 1, show_slope=True), Eq(6, -2, 5), "y")],
    examples=[p_word("A school play sold 200 tickets. Adult tickets cost $8 and student tickets cost $5. The play made $1,240. How many of each ticket were sold?",
                     "x = number of adult tickets, y = number of student tickets", Eq(1, 1, 200), Eq(8, 5, 1240), "substitution",
                     "They sold {x} adult tickets and {y} student tickets."),
              p_word("A gym charges a $20 sign-up fee plus $15 a month. Another gym charges $50 to sign up plus $10 a month. After how many months do they cost the same, and what is the cost?",
                     "x = number of months, y = total cost in dollars", Eq(-15, 1, 20, show_slope=True), Eq(-10, 1, 50, show_slope=True), "substitution",
                     "After {x} months both gyms cost ${y}.")],
    mistake=("There are 30 students; there are 4 more girls than boys. Let g = girls, b = boys.",
             ["g + b = 30", "b = g + 4"],
             "The second equation is backwards. There are MORE girls, so g = b + 4. Test it: if b = 13, g should be 17.",
             "g + b = 30 and g = b + 4 → b = 13, g = 17."),
    watch=[("Not defining variables.", "\"What does x stand for? Write it in words before anything else.\""),
           ("Translating word by word and reversing relationships.", "\"Test your equation with a small made-up number. Does it make sense?\""),
           ("Answering with only numbers.", "\"Answer the question in a full sentence with units.\"")],
    guided=[p_word("The sum of two numbers is 45. Their difference is 9. Find the numbers.", "x = the larger number, y = the smaller number", Eq(1, 1, 45), Eq(1, -1, 9), "substitution", "The numbers are {x} and {y}."),
            p_word("A farm has chickens and cows, 50 animals in all, with 140 legs. How many of each animal are there?", "x = number of chickens, y = number of cows", Eq(1, 1, 50), Eq(2, 4, 140), "substitution", "There are {x} chickens and {y} cows.")],
    independent=[p_word("A coffee shop sold 80 drinks: lattes for $4 and teas for $2, for $250 in total. How many of each were sold?", "x = number of lattes, y = number of teas", Eq(1, 1, 80), Eq(4, 2, 250), "substitution", "They sold {x} lattes and {y} teas."),
                 p_word("Phone plan A costs $30 a month plus $5 per GB. Plan B costs $45 a month plus $2 per GB. For how many GB do they cost the same?", "x = GB used, y = monthly cost in dollars", Eq(-5, 1, 30, show_slope=True), Eq(-2, 1, 45, show_slope=True), "substitution", "At {x} GB both plans cost ${y}."),
                 p_word("Jo has 25 coins, all dimes and quarters, worth $4.00. How many of each?", "x = number of dimes, y = number of quarters (work in cents)", Eq(1, 1, 25), Eq(10, 25, 400), "substitution", "Jo has {x} dimes and {y} quarters."),
                 p_word("A rectangle's length is 3 cm more than twice its width. Its perimeter is 36 cm. Find the length and width.", "x = width in cm, y = length in cm", Eq(-2, 1, 3, show_slope=True), Eq(2, 2, 36), "substitution", "The width is {x} cm and the length is {y} cm.")],
    exit=[p_word("A class trip costs $12 per student and $20 per adult. 35 people went and it cost $500. How many students and adults went?", "x = students, y = adults", Eq(1, 1, 35), Eq(12, 20, 500), "substitution", "{x} students and {y} adults went.")]))

L.append(Lesson(10, D(2027, 1, 15), "Quiz 2 + flex/reteach",
    "I can solve systems by substitution, including special cases and word problems.",
    ["HSA-REI.C.6", "HSA-CED.A.3"], "quiz",
    intro="\"Quiz on substitution today, then practice and catch-up.\"",
    do_now=[p_substitution(Eq(-1, 1, 2, show_slope=True), Eq(1, 1, 6), "y"), p_graph(F(1, 2), 1)],
    quiz=[p_substitution(slope_eq(3, 1, 2), Eq(2, 1, 7), "y"), p_substitution(std(1, 3, 2, 3), std(4, -1, 2, 3), "x"), p_substitution(std(2, -1, -1, 2), std(3, 2, -1, 2), "y"),
          p_substitution(Eq(-2, 1, 4, show_slope=True), Eq(6, -3, 3), "y"), p_substitution(Eq(-1, 1, 3, show_slope=True), Eq(2, -2, -6), "y"),
          p_word("Movie tickets cost $9 for adults and $6 for children. A group of 12 paid $87. How many adults and children were there?", "x = adults, y = children", Eq(1, 1, 12), Eq(9, 6, 87), "substitution", "There were {x} adults and {y} children.")],
    extra=("**Flex plan (about 20 minutes):** Sort the quizzes into 3 piles: question 4-5 wrong (special cases), question 6 wrong (word problem), all good. "
           "Pull the special-cases group for a reteach of Day 8 worked examples; the word problem group redoes the Day 9 guided problems with a partner; "
           "everyone else: \"Create a word problem for the system x + y = 10, 3x + 2y = 24 and solve it.\"")))

# ---- Week 3 (Monday Jan 18: no school, MLK Day) ---------------------------
L.append(Lesson(11, D(2027, 1, 19), "Elimination by adding",
    "I can solve a system by adding the equations to eliminate a variable.",
    ["HSA-REI.C.5", "HSA-REI.C.6"], "new",
    intro=("\"Substitution is great when a variable is easy to isolate. When the equations look like 3x + 2y = 12 and 5x − 2y = 4, there's a faster way. "
           "If we ADD the two equations, +2y and −2y cancel. We're allowed to add equations because we're adding equal things to both sides.\""),
    do_now=[p_substitution(std(1, 1, 2, 5), std(3, -1, 2, 5), "y"), p_substitution(Eq(-3, 1, 1, show_slope=True), Eq(6, -2, -2), "y"), p_identify(-1, 4)],
    examples=[p_elimination(std(3, 2, 2, 3), std(5, -2, 2, 3)), p_elimination(std(1, 4, -1, 2), std(-1, 3, -1, 2))],
    mistake=("Solve: 2x + 3y = 13 and 4x − 3y = −1.",
             ["Add: 6x = 14", "x = 7/3"],
             "The student added the left sides but forgot to add the right sides correctly: 13 + (−1) = 12, not 14.",
             "6x = 12, x = 2, then 2(2) + 3y = 13 → y = 3. Solution (2, 3)."),
    watch=[("Adding the left sides but not the right sides correctly.", "\"Add straight down: x's, y's, AND the numbers.\""),
           ("Adding when the terms have the same sign (they don't cancel).", "\"Opposites cancel. 2y + 2y is 4y, not 0. Next lesson we'll fix that by multiplying.\"")],
    guided=[p_elimination(std(1, 1, 4, 1), std(1, -1, 4, 1)), p_elimination(std(2, 5, 3, -1), std(-2, 3, 3, -1)), p_elimination(std(4, -3, 0, 2), std(1, 3, 0, 2))],
    independent=[p_elimination(std(3, 1, 2, 4), std(2, -1, 2, 4)), p_elimination(std(-5, 2, 1, 3), std(5, 4, 1, 3)), p_elimination(std(1, -6, 3, 1), std(2, 6, 3, 1)),
                 p_elimination(std(7, 3, -1, 4), std(-7, 2, -1, 4)), p_elimination(std(2, -5, 5, 2), std(3, 5, 5, 2)), p_elimination(std(-4, 1, -2, -3), std(4, 3, -2, -3))],
    exit=[p_elimination(std(5, 2, 1, 2), std(3, -2, 1, 2)), p_elimination(std(-3, 4, 2, 2), std(3, 1, 2, 2))]))

L.append(Lesson(12, D(2027, 1, 20), "Elimination by multiplying one equation",
    "I can multiply one equation by a number so that a variable cancels, then solve the system.",
    ["HSA-REI.C.5", "HSA-REI.C.6"], "new",
    intro=("\"What if nothing cancels? In 2x + y = 7 and 3x − 2y = 0, the y's are +y and −2y. If we multiply the whole first equation by 2, we get +2y, which cancels with −2y. "
           "Multiplying both sides of an equation by the same number keeps it true.\""),
    do_now=[p_elimination(std(1, 2, 3, 1), std(1, -2, 3, 1)), p_substitution(std(1, -1, 2, 0), std(2, 3, 2, 0), "x")],
    examples=[p_elimination(std(2, 1, 2, 3), std(3, -2, 2, 3)), p_elimination(std(3, 4, -2, 3), std(1, 2, -2, 3))],
    mistake=("Solve: x + 3y = 5 and 2x + 5y = 9 (multiply the first by −2).",
             ["−2x + 3y = −10", "Add: 8y = −1"],
             "The student only multiplied the x term. EVERY term must be multiplied: −2x − 6y = −10.",
             "Add: −y = −1, y = 1, x = 2. Solution (2, 1)."),
    watch=[("Multiplying only one term.", "\"Put the whole equation in a box. Everything in the box gets multiplied.\""),
           ("Choosing a multiplier that doesn't create opposites.", "\"We want the coefficients to be opposites, like 4 and −4.\"")],
    guided=[p_elimination(std(1, 1, 5, 2), std(3, 2, 5, 2)), p_elimination(std(4, -3, 3, 2), std(2, 1, 3, 2)), p_elimination(std(5, 2, -1, 4), std(1, -1, -1, 4))],
    independent=[p_elimination(std(2, 3, 3, -1), std(1, -1, 3, -1)), p_elimination(std(3, 1, 2, 5), std(5, 2, 2, 5)), p_elimination(std(1, 4, -2, 1), std(3, -2, -2, 1)),
                 p_elimination(std(6, 5, 0, 3), std(3, 2, 0, 3)), p_elimination(std(2, -1, 4, -2), std(5, 3, 4, -2)), p_elimination(std(7, 2, 1, -3), std(1, 1, 1, -3))],
    exit=[p_elimination(std(3, 2, 4, -1), std(1, 1, 4, -1)), p_elimination(std(2, 5, -3, 2), std(4, -1, -3, 2))]))

L.append(Lesson(13, D(2027, 1, 21), "Elimination by multiplying both equations",
    "I can multiply both equations so a variable cancels, then solve the system.",
    ["HSA-REI.C.5", "HSA-REI.C.6"], "new",
    intro=("\"Sometimes no single multiplier works, like 3x + 4y = 10 and 2x + 3y = 7. Find the least common multiple of the coefficients of one variable "
           "and multiply both equations to get opposites, like +6x and −6x.\""),
    do_now=[p_elimination(std(2, 1, 1, 3), std(3, -1, 1, 3)), p_elimination(std(1, 2, 4, -1), std(3, 5, 4, -1))],
    examples=[p_elimination(std(3, 4, 2, 1), std(2, 3, 2, 1)), p_elimination(std(5, 3, -1, 3), std(4, -2, -1, 3))],
    mistake=("Solve: 2x + 3y = 12 and 5x − 2y = 11 (eliminate y).",
             ["Multiply (1) by 2: 4x + 6y = 24", "Multiply (2) by 3: 15x − 6y = 11", "Add: 19x = 35"],
             "The right side of equation (2) wasn't multiplied: 3 × 11 = 33.",
             "19x = 57, x = 3, y = 2. Solution (3, 2)."),
    watch=[("Forgetting to multiply the constant.", "\"Box it, multiply everything in the box.\""),
           ("Sign errors when multiplying by a negative.", "\"Say the sign out loud: negative times negative is positive.\""),
           ("Picking a harder variable.", "\"Look at the coefficients. Which pair has the smaller least common multiple?\"")],
    guided=[p_elimination(std(2, 3, 1, 2), std(3, 5, 1, 2)), p_elimination(std(4, 3, 3, -2), std(3, -2, 3, -2)), p_elimination(std(5, 2, 2, -1), std(3, -5, 2, -1))],
    independent=[p_elimination(std(3, 5, -1, 2), std(2, 3, -1, 2)), p_elimination(std(4, -3, 1, 1), std(6, 5, 1, 1)), p_elimination(std(2, 7, 4, -1), std(3, -4, 4, -1)),
                 p_elimination(std(5, 4, 2, -3), std(3, 6, 2, -3)), p_elimination(std(7, 3, 0, 5), std(5, 2, 0, 5)), p_elimination(std(3, 4, F(1), F(1, 2)), std(5, 6, F(1), F(1, 2)))],
    exit=[p_elimination(std(3, 2, 4, -3), std(2, 5, 4, -3)), p_elimination(std(4, 5, -1, 2), std(6, -7, -1, 2))]))

L.append(Lesson(14, D(2027, 1, 22), "Choosing a method + mini-quiz",
    "I can choose an efficient method (graphing, substitution or elimination) and explain my choice.",
    ["HSA-REI.C.6", "HSA-REI.C.5"], "quiz",
    intro=("\"This week lost a day to the holiday, so today combines practice and a short quiz. All three methods give the same answer; "
           "the skill is choosing the fastest one. A variable already alone or with coefficient 1: substitution. Opposite or matching coefficients: elimination. "
           "Want a quick picture or estimate: graphing.\""),
    do_now=[p_elimination(std(1, 1, 3, 2), std(2, -1, 3, 2)), p_substitution(slope_eq(2, 1, 1), Eq(3, 1, 4), "y")],
    examples=[p_substitution(slope_eq(-1, 3, 2), Eq(2, 3, 12), "y"), p_elimination(std(4, 3, 2, -1), std(2, -3, 2, -1))],
    quiz=[p_elimination(std(3, 2, 1, 4), std(5, -2, 1, 4)), p_elimination(std(2, 3, -1, 3), std(3, 2, -1, 3)), p_substitution(std(1, -4, 2, 0), std(3, 5, 2, 0), "x"),
          p_elimination(Eq(2, -3, 5), Eq(-4, 6, -10)), p_elimination(Eq(3, 1, 4), Eq(6, 2, 5))],
    extra=("**Choosing a method — discuss before the quiz (10 minutes):** show the three systems below and have students vote with fingers (1 = graphing, 2 = substitution, 3 = elimination), "
           "then explain their choice to a partner. There is no single right answer; the explanation matters.\n\n"
           "- y = 4x − 1 and 3x + 2y = 9 (substitution: y is already alone)\n- 5x + 3y = 7 and 2x − 3y = 7 (elimination: +3y and −3y)\n- y = x + 2 and y = −x + 4 (graphing works nicely: simple lines)")))

# ---- Week 4 ---------------------------------------------------------------
L.append(Lesson(15, D(2027, 1, 25), "Applications: choose your method",
    "I can model a situation with a system and solve it using an efficient method.",
    ["HSA-CED.A.3", "HSA-REI.C.6"], "new",
    intro="\"Back to real situations, now with every method available. Define variables, write equations, choose a method, answer in a sentence.\"",
    do_now=[p_elimination(std(2, 3, 3, 1), std(4, -3, 3, 1)), p_substitution(Eq(-3, 1, 2, show_slope=True), Eq(3, -1, -2), "y")],
    examples=[p_word("A chemistry teacher mixes a 10% salt solution with a 40% salt solution to get 30 liters of a 20% solution. How many liters of each?",
                     "x = liters of 10% solution, y = liters of 40% solution", Eq(1, 1, 30), Eq(F(1, 10), F(2, 5), 6), "elimination",
                     "Use {x} liters of the 10% solution and {y} liters of the 40% solution."),
              p_word("A kayak goes 24 miles downstream in 2 hours and returns upstream in 3 hours. Find the kayak's speed in still water and the current's speed.",
                     "x = kayak speed in still water (mph), y = current speed (mph); downstream speed x + y = 12, upstream speed x − y = 8", Eq(1, 1, 12), Eq(1, -1, 8), "elimination",
                     "The kayak goes {x} mph in still water and the current is {y} mph.")],
    watch=[("Mixture problems: adding percentages.", "\"Track the amount of salt: 10% of x liters is 0.1x liters of salt.\""),
           ("Rate problems: forgetting the current helps one way and slows the other.", "\"Downstream: speeds add. Upstream: subtract.\"")],
    guided=[p_word("A bakery sells muffins for $3 and cookies for $1.50. One day it sold 120 items for $270. How many muffins and cookies were sold?", "x = muffins, y = cookies", Eq(1, 1, 120), Eq(3, F(3, 2), 270), "elimination", "They sold {x} muffins and {y} cookies."),
            p_word("A test has 30 questions worth 90 points. Multiple choice questions are worth 2 points and short answers 5 points. How many of each type are there?", "x = multiple choice, y = short answer", Eq(1, 1, 30), Eq(2, 5, 90), "elimination", "There are {x} multiple choice and {y} short answer questions.")],
    independent=[p_word("Two cell plans: $25 a month plus $0.10 per text, or $40 a month with unlimited texts. At how many texts do they cost the same?", "x = number of texts, y = monthly cost", Eq(F(-1, 10), 1, 25, show_slope=True), Eq(0, 1, 40, show_slope=True), "substitution", "At {x} texts both plans cost ${y}."),
                 p_word("A plane flies 1,200 miles with the wind in 3 hours and back against the wind in 4 hours. Find the plane's speed and the wind speed.", "x = plane speed in still air, y = wind speed (mph)", Eq(1, 1, 400), Eq(1, -1, 300), "elimination", "The plane flies {x} mph and the wind is {y} mph."),
                 p_word("Mia invests $5,000, part at 3% and part at 5% interest. She earns $190 in a year. How much did she invest at each rate?", "x = dollars at 3%, y = dollars at 5%", Eq(1, 1, 5000), Eq(F(3, 100), F(5, 100), 190), "elimination", "She invested ${x} at 3% and ${y} at 5%."),
                 p_word("The sum of two angles is 90°. One angle is 15° less than twice the other. Find the angles.", "x = the smaller angle, y = the larger angle", Eq(1, 1, 90), Eq(-2, 1, -15, show_slope=True), "substitution", "The angles are {x}° and {y}°.")],
    exit=[p_word("A school store sold 40 pens and pencils for $26. Pens cost $1 and pencils cost $0.50. How many of each were sold?", "x = pens, y = pencils", Eq(1, 1, 40), Eq(1, F(1, 2), 26), "elimination", "The store sold {x} pens and {y} pencils.")]))

L.append(Lesson(16, D(2027, 1, 26), "Linear inequalities in two variables",
    "I can graph a linear inequality in two variables and decide if a point is a solution.",
    ["HSA-REI.D.12"], "new",
    intro=("\"An inequality like y > 2x + 1 has infinitely many solutions: a whole region of the plane. Graph the boundary line (dashed if the boundary isn't included, "
           "solid if it is), then test a point to decide which side to shade.\""),
    do_now=[p_graph(2, 1), p_elimination(std(1, 1, 1, 4), std(1, -1, 1, 4))],
    examples=[p_ineq_graph(2, 1, ">"), p_ineq_graph(F(-1, 2), 3, "<=")],
    mistake=("Graph y < x + 2.",
             ["Draw a solid line through (0, 2) with slope 1.", "Shade above."],
             "< means the boundary is not included (dashed line). Test (0, 0): 0 < 2 is true, so shade the side with (0, 0), which is below.",
             "Dashed line, shade below."),
    watch=[("Solid vs. dashed lines.", "\"Is the line itself included? Only if there's an 'or equal to' line under the symbol.\""),
           ("Shading the wrong side.", "\"Don't guess: test (0, 0). True: shade that side. False: shade the other side.\""),
           ("Testing a point on the line.", "\"If (0, 0) is on the line, test (0, 1) instead.\"")],
    guided=[p_ineq_graph(1, -2, "<"), p_ineq_graph(-3, 4, ">="), p_ineq_graph(F(1, 3), 0, ">")],
    independent=[p_ineq_graph(-1, 5, "<="), p_ineq_graph(2, -3, ">="), p_ineq_graph(F(-2, 3), 1, "<"), p_ineq_graph(4, 0, "<"),
                 p_ineq_system_point([(2, 1, ">")], 1, 4), p_ineq_system_point([(-1, 3, "<=")], 2, 2)],
    exit=[p_ineq_graph(-2, 3, ">"), p_ineq_system_point([(3, -1, "<")], 1, 2)],
    materials="Graph paper handout, rulers, colored pencils, exit ticket slips"))

L.append(Lesson(17, D(2027, 1, 27), "Systems of linear inequalities",
    "I can graph a system of linear inequalities and identify points in the solution region.",
    ["HSA-REI.D.12", "HSA-CED.A.3"], "new",
    intro=("\"Graph each inequality on the same grid, each with its own shading color. The solution is where the shadings overlap. "
           "A point is a solution only if it makes EVERY inequality true.\""),
    do_now=[p_ineq_graph(1, 2, "<"), p_ineq_system_point([(-2, 4, ">=")], 1, 3)],
    examples=[p_ineq_system_point([(1, 1, ">"), (-1, 4, "<=")], 1, 3), p_ineq_system_point([(2, -1, ">="), (F(-1, 2), 2, "<")], 2, 2)],
    mistake=("Is (3, 1) a solution of y < x and y > −x + 5?",
             ["1 < 3 ✓", "So (3, 1) is a solution."],
             "The second inequality wasn't checked: −3 + 5 = 2, and 1 > 2 is false.",
             "No, (3, 1) is not a solution."),
    watch=[("Shading only one inequality.", "\"Use two colors. The answer is where BOTH colors are.\""),
           ("Calling a point on a dashed line a solution.", "\"Dashed means the line isn't included.\"")],
    guided=[p_ineq_system_point([(1, 0, ">"), (-1, 6, "<")], 2, 3), p_ineq_system_point([(2, 1, "<="), (-1, -2, ">=")], 0, 1), p_ineq_system_point([(F(1, 2), 1, ">"), (-3, 5, ">")], 2, 1)],
    independent=[p_ineq_graph(-1, 4, "<"), p_ineq_graph(1, -2, ">="),
                 p_ineq_system_point([(-1, 4, "<"), (1, -2, ">=")], 2, 1), p_ineq_system_point([(-1, 4, "<"), (1, -2, ">=")], 4, 3),
                 p_ineq_system_point([(3, 0, "<="), (0, 2, ">")], 1, 3), p_ineq_system_point([(-2, 1, ">"), (F(1, 2), -1, "<")], 3, 0)],
    exit=[p_ineq_system_point([(2, -3, ">"), (-1, 5, "<=")], 1, 2), p_ineq_system_point([(2, -3, ">"), (-1, 5, "<=")], 3, 4)],
    extra=("**Real-world extension (early finishers):** \"A student can work at most 20 hours a week and needs to earn at least $240. Tutoring pays $15/hour and "
           "lifeguarding pays $12/hour. Write a system of inequalities (t = tutoring hours, g = lifeguarding hours) and name two possible schedules.\" "
           "Answer: t + g ≤ 20, 15t + 12g ≥ 240, t ≥ 0, g ≥ 0; e.g. t = 16, g = 0 or t = 8, g = 10."),
    materials="Graph paper handout, rulers, colored pencils (two colors), exit ticket slips"))

L.append(Lesson(18, D(2027, 1, 28), "Unit review (stations)",
    "I can solve systems of equations and inequalities using all of the methods in this unit.",
    ["HSA-REI.C.5", "HSA-REI.C.6", "HSA-REI.D.11", "HSA-REI.D.12", "HSA-CED.A.3"], "review",
    intro=("\"Tomorrow is the unit test. Today you'll rotate through 4 stations (about 9 minutes each). Each station has an answer key face down: "
           "do the problems, then check, then fix anything you missed before moving on.\""),
    do_now=[p_identify(F(3, 2), -1), p_is_solution(Eq(1, 1, 3), Eq(2, -1, 0), 1, 2)],
    guided=[p_graph_system(1, -1, 2, 1), p_graph_system(-2, F(1, 2), 0, 2), p_substitution(slope_eq(3, 1, 1), Eq(2, 1, 6), "y"), p_substitution(std(1, 2, -1, 3), std(3, -1, -1, 3), "x")],
    independent=[p_elimination(std(2, 3, 3, -1), std(4, -3, 3, -1)), p_elimination(std(3, 4, 2, -1), std(5, 6, 2, -1)), p_elimination(Eq(2, 4, 6), Eq(3, 6, 9)),
                 p_word("Tickets to a concert cost $25 on the floor and $15 in the balcony. 300 tickets were sold for $5,900. How many of each?", "x = floor tickets, y = balcony tickets", Eq(1, 1, 300), Eq(25, 15, 5900), "elimination", "They sold {x} floor tickets and {y} balcony tickets."),
                 p_ineq_graph(F(-1, 2), 2, ">="), p_ineq_system_point([(1, -1, ">"), (-2, 6, "<")], 1, 2)],
    extra=("**Stations** (print each set on its own page with the key folded behind it): Station A = guided problems 1-2 (graphing); Station B = guided problems 3-4 (substitution); "
           "Station C = independent problems 1-3 (elimination and special cases); Station D = independent problems 4-6 (word problem and inequalities). "
           "Circulate and send students who are confident on to the challenge: \"Write a system with no solution where one equation is 2x + 5y = 10.\"")))

L.append(Lesson(19, D(2027, 1, 29), "Unit test",
    "I can show what I know about systems of linear equations and inequalities.",
    ["HSA-REI.C.5", "HSA-REI.C.6", "HSA-REI.D.11", "HSA-REI.D.12", "HSA-CED.A.3"], "test",
    intro=("\"Today is the unit test. Read each question carefully, show your work, and check your answers by substituting. "
           "When you finish, check every answer, then turn it in and read silently.\""),
    quiz=[p_to_slope(3, 1, 5), p_is_solution(Eq(2, 1, 8), Eq(1, -1, 1), 3, 2), p_graph_system(2, -1, 1, 3),
          p_substitution(slope_eq(-2, 2, 1), Eq(3, 2, 8), "y"), p_substitution(std(1, -3, 4, 1), std(2, 5, 4, 1), "x"),
          p_elimination(std(4, 3, 1, 2), std(2, -3, 1, 2)), p_elimination(std(5, 2, 3, -4), std(3, 4, 3, -4)), p_elimination(std(3, 2, -2, 5), std(2, 5, -2, 5)),
          p_substitution(Eq(-4, 1, 3, show_slope=True), Eq(8, -2, 4), "y"), p_elimination(Eq(1, -2, 4), Eq(-3, 6, -12)),
          p_word("A theater sold 150 tickets: adults $12, children $7, for a total of $1,425. How many of each?", "x = adult tickets, y = child tickets", Eq(1, 1, 150), Eq(12, 7, 1425), "elimination", "They sold {x} adult and {y} child tickets."),
          p_word("Plan A: $40 plus $8 per class. Plan B: $64 plus $5 per class. After how many classes do they cost the same?", "x = classes, y = total cost", Eq(-8, 1, 40, show_slope=True), Eq(-5, 1, 64, show_slope=True), "substitution", "After {x} classes both cost ${y}."),
          p_ineq_graph(F(2, 3), -1, "<"), p_ineq_system_point([(1, 2, "<="), (-2, -1, ">")], 1, 2), p_ineq_system_point([(1, 2, "<="), (-2, -1, ">")], -1, 3)],
    extra=("**Test administration:** students with extended time finish in [location, e.g. the resource room with Mrs. Owens] or during [time]. "
           "Read-aloud accommodation: read questions aloud on request without explaining math vocabulary. Collect all tests and calculators. "
           "**Scoring:** 15 questions, 4 points each, 60 total, using the partial-credit rules in the grading guide. "
           "Leave any test you're unsure about for the teacher with a sticky note.")))


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def numbered(problems: list[Problem], start=1) -> str:
    return "\n".join(f"{i}. {p.prompt}" for i, p in enumerate(problems, start))


def key(problems: list[Problem], label: str, start=1) -> str:
    out = []
    for i, p in enumerate(problems, start):
        out.append(f"**{label} {i}.** {p.prompt}  \n**Answer: {p.answer}**")
        out.extend(f"   - {s}" for s in p.steps)
        out.append("")
    return "\n".join(out)


def example_script(p: Problem, i: int) -> str:
    lines = [f"**Worked example {i}:** {p.prompt}", "",
             "Write each step on the board and say what you're doing and why. Ask the question in italics before writing the step and give 3-5 seconds of think time.", ""]
    for j, s in enumerate(p.steps, 1):
        lines.append(f"{j}. {s}")
    said = p.answer if p.answer.endswith(".") else f"So the answer is {p.answer}."
    lines += ["", f"Say: *\"{said} How do we know it's right?\"* (We checked it in the original equations.)", ""]
    return "\n".join(lines)


def run_of_show(ls: Lesson) -> str:
    if ls.kind == "new":
        rows = [("0:00-0:07", "Do Now (silent, independent)", "Problems on the board; answers in the key. Go over 1-2 quickly."),
                ("0:07-0:20", "Mini-lesson: worked examples + find the mistake", "Script below. Students copy the examples into their notes."),
                ("0:20-0:30", "Guided practice (we do)", "Do problem 1 together; students do 2-3 with a partner, then check on whiteboards or by showing work."),
                ("0:30-0:45", "Independent practice (you do)", "Circulate. See students on the support list first. Early finishers: challenge or next problems."),
                ("0:45-0:50", "Exit ticket", "Silent. Collect at the door and sort into got it / nearly / not yet.")]
    elif ls.kind == "quiz":
        rows = [("0:00-0:05", "Do Now", "Quick warm-up; go over answers."),
                ("0:05-0:10", "Mini-lesson / discussion", "See notes below."),
                ("0:10-0:30", "Quiz", "Silent, individual. Extended time per IEP/504 plans."),
                ("0:30-0:50", "Flex / reteach", "See the flex plan below.")]
    elif ls.kind == "review":
        rows = [("0:00-0:06", "Do Now", "Retrieval warm-up."), ("0:06-0:10", "Explain stations", "Groups of 3-4."),
                ("0:10-0:46", "Stations (4 × 9 min)", "Rotate on your signal."), ("0:46-0:50", "Exit: one thing to study tonight", "Students write it on a sticky note.")]
    else:
        rows = [("0:00-0:05", "Settle, materials out, directions", "Calculators allowed [teacher: confirm]. Graph paper provided."),
                ("0:05-0:50", "Unit test", "Silent, individual. Collect all tests.")]
    out = ["| Time | Segment | Notes |", "|---|---|---|"] + [f"| {a} | {b} | {c} |" for a, b, c in rows]
    return "\n".join(out)


def render_lesson(ls: Lesson) -> str:
    o = [f"## Day {ls.day}: {ls.date.strftime('%A, %B %-d')}: {ls.title}", "",
         f"**Learning target:** {ls.target}  ",
         f"**Standards:** {', '.join(ls.standards)} (full text in the calendar)  ",
         f"**Materials:** {ls.materials}", "", "### Run of show (50 minutes)", "", run_of_show(ls), ""]
    if ls.intro:
        o += ["### Opening (say this)", "", ls.intro, ""]
    if ls.do_now:
        o += ["### Do Now", "", numbered(ls.do_now), ""]
    if ls.examples:
        o += ["### Mini-lesson: worked examples (script)", ""]
        for i, p in enumerate(ls.examples, 1):
            o.append(example_script(p, i))
    if ls.mistake:
        prob, wrong, why, fix = ls.mistake
        o += ["**Find the mistake** (project or write this; ask students to find and explain the error with a partner for 2 minutes):", "",
              f"> {prob}  ", *[f"> {w}  " for w in wrong], "",
              f"*What's wrong:* {why}  ", f"*Correct:* {fix}", ""]
    if ls.watch:
        o += ["### Watch for (common mistakes and what to say)", ""]
        o += [f"- **{m}** Say: {s}" for m, s in ls.watch]
        o.append("")
    if ls.guided:
        o += ["### Guided practice" if ls.kind != "review" else "### Stations A-B", "", numbered(ls.guided), ""]
    if ls.independent:
        o += ["### Independent practice" if ls.kind != "review" else "### Stations C-D", "", numbered(ls.independent), ""]
    if ls.exit:
        o += ["### Exit ticket", "", numbered(ls.exit), "",
              "**Sorting:** all correct = *got it* (start tomorrow's Do Now normally); one error = *nearly* (hand back with a hint tomorrow); "
              "both wrong or blank = *not yet* (sit with these students during tomorrow's guided practice). Record counts in the handoff log.", ""]
    if ls.quiz:
        o += [f"### {'Unit test' if ls.kind == 'test' else 'Quiz'} (print separately)", "", numbered(ls.quiz), ""]
    if ls.extra:
        o += [ls.extra, ""]
    o += ["### Answer key (fully worked)", ""]
    for label, ps in (("Do Now", ls.do_now), ("Example", ls.examples), ("Guided", ls.guided), ("Practice", ls.independent),
                      ("Exit", ls.exit), ("Test" if ls.kind == "test" else "Quiz", ls.quiz)):
        if ps:
            o.append(key(ps, label))
    o.append("---\n")
    return "\n".join(o)


def all_problems(ls: Lesson):
    for name in ("do_now", "examples", "guided", "independent", "exit", "quiz"):
        for i, p in enumerate(getattr(ls, name), 1):
            yield f"day{ls.day}-{name}-{i}", p


def main() -> int:
    # 1. Verify every answer independently with tools/check_math.py
    items = []
    for ls in L:
        for pid, p in all_problems(ls):
            assert p.checks, f"{pid} has no verification"
            for j, c in enumerate(p.checks, 1):
                items.append({"id": f"{pid}.{j}", **c})
    keys_path = HERE / "answer-keys.json"
    keys_path.write_text(json.dumps(items, indent=1, ensure_ascii=False), encoding="utf-8")
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "check_math.py"), str(keys_path)], capture_output=True, text=True)
    summary = r.stdout.strip().splitlines()[-1]
    if r.returncode != 0:
        print(r.stdout)
        print("Answer verification FAILED; not writing lesson files.")
        return 1
    print(f"Verified answers: {summary}")

    # 2. Standards text, looked up from the bundled standards
    all_codes = sorted({c for ls in L for c in ls.standards})
    rows = stds.load(["math"])
    stext = {}
    for c in all_codes:
        hit = [r for r in rows if stds.norm_code(r["code"]) in stds.code_variants(c)]
        assert hit, f"standard {c} not found"
        stext[c] = hit[0]["statement"]

    # 3. Write files
    weeks = {1: (1, 5), 2: (6, 10), 3: (11, 14), 4: (15, 19)}
    titles = {1: "Week 1: Lines and solving systems by graphing", 2: "Week 2: Substitution",
              3: "Week 3: Elimination (4 days: Monday is MLK Day)", 4: "Week 4: Applications, inequalities, review and test"}
    for w, (a, b) in weeks.items():
        body = [f"# {titles[w]}", "", "Algebra 1 · Unit: Systems of linear equations and inequalities · Long-term sub package (EXAMPLE)", "",
                f"*Every answer in this file was computer-checked with `tools/check_math.py` ({summary}).*", ""]
        body += [render_lesson(ls) for ls in L if a <= ls.day <= b]
        (HERE / f"week-{w}.md").write_text("\n".join(body), encoding="utf-8")

    cal = ["| Day | Date | Lesson | Learning target | Type | Standards |", "|---|---|---|---|---|---|"]
    for ls in L:
        cal.append(f"| {ls.day} | {ls.date.strftime('%a %b %-d')} | {ls.title} | {ls.target} | {ls.kind} | {', '.join(ls.standards)} |")
        if ls.day == 10:
            cal.append("| — | Mon Jan 18 | **No school: Martin Luther King Jr. Day** | | | |")
    std_table = "\n".join(f"- **{c}**: {stext[c]}" for c in all_codes)
    (HERE / "01-calendar.md").write_text(
        "# Pacing calendar\n\nAlgebra 1, Unit: Systems of linear equations and inequalities. January 4-29, 2027 (19 school days).\n\n"
        + "\n".join(cal) + "\n\n## Standards (official text, looked up with `tools/standards.py`)\n\n" + std_table +
        "\n\n© Copyright 2010. National Governors Association Center for Best Practices and Council of Chief State School Officers. All rights reserved.\n",
        encoding="utf-8")
    print("Wrote 01-calendar.md and week-1..4.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())

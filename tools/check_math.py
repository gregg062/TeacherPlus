#!/usr/bin/env python3
"""Verify math answer keys with exact arithmetic (standard library only).

Claude writes the answer key as JSON, runs this, and fixes anything that
fails BEFORE showing the key to the teacher.

Usage:
  python3 check_math.py key.json        (or pipe JSON on stdin)

Input: a JSON list of items, each with an "id", a "type", a "problem" and
the claimed "answer":

  {"id": "1", "type": "arithmetic",   "problem": "3/4 + 1/6",         "answer": "11/12"}
  {"id": "2", "type": "equation",     "problem": "3(x - 2) + 4 = 19", "answer": {"x": 7}}
  {"id": "3", "type": "system",       "problem": ["2x + y = 7", "x - y = 2"], "answer": {"x": 3, "y": 1}}
  {"id": "4", "type": "system",       "problem": ["y = 2x + 1", "4x - 2y = 6"], "answer": "none"}   # or "infinite"
  {"id": "5", "type": "equivalent",   "problem": "2(x + 3) - x",      "answer": "x + 6"}
  {"id": "6", "type": "inequality",   "problem": "-2x + 5 < 11",      "answer": "x > -3"}
  {"id": "7", "type": "point_check",  "problem": "y > 2x + 1", "point": {"x": 0, "y": 3}, "answer": true}
  {"id": "8", "type": "slope",        "problem": [[1, 2], [3, 8]],    "answer": "3"}
  {"id": "9", "type": "line_through", "problem": [[1, 2], [3, 8]],    "answer": "y = 3x - 1"}

Supports +, -, *, /, ^ (integer powers), parentheses, implicit
multiplication (2x, 3(x+1), xy) and single-letter variables. Answers may be
numbers, fractions ("-3/4"), decimals or mixed numbers ("1 1/2").
"""

from __future__ import annotations

import ast
import json
import re
import sys
from fractions import Fraction
from itertools import product

# --------------------------------------------------------------------------
# Safe exact parser
# --------------------------------------------------------------------------


def _prep(expr: str) -> str:
    s = str(expr).strip()
    for a, b in {"−": "-", "–": "-", "×": "*", "·": "*", "÷": "/", "^": "**", "≤": "<=", "≥": ">="}.items():
        s = s.replace(a, b)
    s = re.sub(r"(\d+)\s+(\d+)/(\d+)", r"(\1+\2/\3)", s)  # mixed numbers 1 1/2
    s = re.sub(r"(?<=[0-9a-zA-Z)])\s*(?=[a-zA-Z(])", "*", s)  # 2x, 3(x), x(y), )(
    s = re.sub(r"(?<=[a-zA-Z])(?=[a-zA-Z])", "*", s)
    s = re.sub(r"\*\*\*", "**", s)
    return s


def _num(v) -> Fraction:
    if isinstance(v, bool):
        raise ValueError("boolean is not a number")
    if isinstance(v, (int, float)):
        return Fraction(str(v))
    return evaluate(str(v), {})


def evaluate(expr: str, env: dict[str, Fraction]) -> Fraction:
    tree = ast.parse(_prep(expr), mode="eval")

    def ev(n):
        if isinstance(n, ast.Expression):
            return ev(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool):
            return Fraction(str(n.value))
        if isinstance(n, ast.Name):
            if n.id not in env:
                raise ValueError(f"no value for variable '{n.id}'")
            return env[n.id]
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, (ast.USub, ast.UAdd)):
            v = ev(n.operand)
            return -v if isinstance(n.op, ast.USub) else v
        if isinstance(n, ast.BinOp):
            a, b = ev(n.left), ev(n.right)
            if isinstance(n.op, ast.Add):
                return a + b
            if isinstance(n.op, ast.Sub):
                return a - b
            if isinstance(n.op, ast.Mult):
                return a * b
            if isinstance(n.op, ast.Div):
                if b == 0:
                    raise ZeroDivisionError("division by zero")
                return a / b
            if isinstance(n.op, ast.Pow):
                if b.denominator != 1 or abs(b) > 12:
                    raise ValueError("only small integer exponents are supported")
                return a ** int(b)
        raise ValueError(f"unsupported syntax in '{expr}'")

    return ev(tree)


def variables(expr: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z]", _prep(expr)))


def split_relation(s: str) -> tuple[str, str, str]:
    m = re.search(r"(<=|>=|!=|=|<|>)", _prep(s).replace("==", "="))
    if not m:
        raise ValueError(f"no =, < or > in '{s}'")
    p = _prep(s).replace("==", "=")
    return p[: m.start()], m.group(1), p[m.end():]


def fmt(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


# --------------------------------------------------------------------------
# Linear algebra helpers
# --------------------------------------------------------------------------

SAMPLES = [Fraction(v) for v in (0, 1, -2, 3, Fraction(1, 2), -5, 7, Fraction(-7, 3))]


def affine(f: str, vs: list[str]):
    """Return (coeffs, constant) if expression f is affine in vs, else None."""
    zero = {v: Fraction(0) for v in vs}
    c0 = evaluate(f, zero)
    coeffs = {v: evaluate(f, {**zero, v: Fraction(1)}) - c0 for v in vs}
    for vals in list(product(SAMPLES[:4], repeat=len(vs)))[:20]:
        env = dict(zip(vs, vals))
        if evaluate(f, env) != c0 + sum(coeffs[v] * env[v] for v in vs):
            return None
    return coeffs, c0


def solve_linear_system(eqs: list[str]):
    vs = sorted(set().union(*(variables(e) for e in eqs)))
    rows = []
    for e in eqs:
        l, op, r = split_relation(e)
        if op != "=":
            raise ValueError("systems must be equations")
        a = affine(f"({l})-({r})", vs)
        if a is None:
            return vs, "nonlinear"
        coeffs, c = a
        rows.append([coeffs[v] for v in vs] + [-c])
    n, m = len(vs), len(rows)
    piv_cols, r = [], 0
    for col in range(n):
        p = next((i for i in range(r, m) if rows[i][col] != 0), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        rows[r] = [x / rows[r][col] for x in rows[r]]
        for i in range(m):
            if i != r and rows[i][col] != 0:
                k = rows[i][col]
                rows[i] = [a - k * b for a, b in zip(rows[i], rows[r])]
        piv_cols.append(col)
        r += 1
    if any(all(x == 0 for x in row[:-1]) and row[-1] != 0 for row in rows):
        return vs, "none"
    if len(piv_cols) < n:
        return vs, "infinite"
    return vs, {vs[c]: rows[i][-1] for i, c in enumerate(piv_cols)}


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------


def as_solution(ans) -> dict[str, Fraction] | str:
    if isinstance(ans, str) and ans.strip().lower() in ("none", "no solution", "infinite", "infinitely many"):
        return "none" if ans.strip().lower().startswith("no") else "infinite"
    if isinstance(ans, list):  # [x, y]
        return {"x": _num(ans[0]), "y": _num(ans[1])}
    if isinstance(ans, str):  # "(3, 1)" or "x = 3, y = 1"
        pairs = re.findall(r"([a-zA-Z])\s*=\s*([-\d./ ]+)", ans)
        if pairs:
            return {v: _num(x.strip()) for v, x in pairs}
        nums = re.findall(r"-?\d+(?:\.\d+)?(?:/\d+)?", ans)
        if len(nums) == 2:
            return {"x": _num(nums[0]), "y": _num(nums[1])}
    if isinstance(ans, dict):
        return {k: _num(v) for k, v in ans.items()}
    if isinstance(ans, (int, float)):
        return {"x": _num(ans)}
    raise ValueError(f"can't read answer {ans!r}")


def check(item: dict) -> tuple[bool, str]:
    t, prob, ans = item.get("type"), item.get("problem"), item.get("answer")

    if t == "arithmetic":
        val = evaluate(prob, {})
        return val == _num(ans), f"computed {fmt(val)}"

    if t == "equivalent":
        vs = sorted(variables(prob) | variables(str(ans)))
        for vals in list(product(SAMPLES, repeat=len(vs)))[:60]:
            env = dict(zip(vs, vals))
            try:
                a, b = evaluate(prob, env), evaluate(str(ans), env)
            except ZeroDivisionError:
                continue
            if a != b:
                return False, f"differs at {', '.join(f'{k}={fmt(v)}' for k, v in env.items())}: {fmt(a)} vs {fmt(b)}"
        return True, "equivalent at all test values"

    if t == "equation":
        return check_system([prob], ans)

    if t == "system":
        return check_system(list(prob), ans)

    if t == "point_check":
        l, op, r = split_relation(prob)
        env = {k: _num(v) for k, v in item["point"].items()}
        a, b = evaluate(l, env), evaluate(r, env)
        truth = {"<": a < b, ">": a > b, "<=": a <= b, ">=": a >= b, "=": a == b, "!=": a != b}[op]
        return truth == bool(ans), f"point {'satisfies' if truth else 'does not satisfy'} it ({fmt(a)} {op} {fmt(b)})"

    if t == "inequality":
        return check_inequality(prob, ans)

    if t == "slope":
        (x1, y1), (x2, y2) = [[_num(v) for v in p] for p in prob]
        if x1 == x2:
            return str(ans).lower() in ("undefined", "none"), "slope is undefined (vertical line)"
        m = (y2 - y1) / (x2 - x1)
        return m == _num(ans), f"computed slope {fmt(m)}"

    if t == "line_through":
        bad = []
        for p in prob:
            x, y = (_num(v) for v in p)
            l, op, r = split_relation(ans)
            if evaluate(l, {"x": x, "y": y}) != evaluate(r, {"x": x, "y": y}):
                bad.append(f"({fmt(x)}, {fmt(y)})")
        return not bad, "passes through all points" if not bad else f"does not pass through {', '.join(bad)}"

    raise ValueError(f"unknown type '{t}'")


def check_system(eqs: list[str], ans) -> tuple[bool, str]:
    claimed = as_solution(ans)
    vs, actual = solve_linear_system(eqs)
    if actual == "nonlinear":
        if not isinstance(claimed, dict):
            return False, "nonlinear: can only verify specific solutions"
        ok = all(
            evaluate(l, claimed) == evaluate(r, claimed)
            for l, _, r in (split_relation(e) for e in eqs)
        )
        return ok, ("claimed solution satisfies every equation (nonlinear: other solutions not ruled out)"
                    if ok else "claimed solution does NOT satisfy the equation(s)")
    if isinstance(actual, str):
        return claimed == actual, f"system has {'no solution' if actual == 'none' else 'infinitely many solutions'}"
    shown = ", ".join(f"{v} = {fmt(actual[v])}" for v in vs)
    if not isinstance(claimed, dict):
        return False, f"actual solution: {shown}"
    if set(claimed) != set(actual) and len(claimed) == len(actual) == 1:
        claimed = {next(iter(actual)): next(iter(claimed.values()))}
    return claimed == actual, f"computed {shown}"


def check_inequality(prob: str, ans: str) -> tuple[bool, str]:
    l, op, r = split_relation(prob)
    vs = sorted(variables(prob))
    if len(vs) != 1:
        raise ValueError("inequality checks need exactly one variable")
    v = vs[0]
    al, aop, ar = split_relation(ans)
    a = affine(f"({l})-({r})", vs)
    if a is None:
        raise ValueError("only linear inequalities are supported")
    coeffs, c = a
    boundary = -c / coeffs[v] if coeffs[v] else None
    tests = list(SAMPLES) + ([boundary, boundary + Fraction(1, 7), boundary - Fraction(1, 7)] if boundary is not None else [])

    def truth(lhs, o, rhs, env):
        x, y = evaluate(lhs, env), evaluate(rhs, env)
        return {"<": x < y, ">": x > y, "<=": x <= y, ">=": x >= y, "=": x == y}[o]

    for tv in tests:
        env = {v: tv}
        if truth(l, op, r, env) != truth(al, aop, ar, env):
            return False, f"disagrees at {v} = {fmt(tv)} (boundary is {fmt(boundary) if boundary is not None else 'none'})"
    return True, f"same solution set (boundary {v} = {fmt(boundary) if boundary is not None else 'none'})"


def main() -> int:
    raw = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    items = json.loads(raw)
    if isinstance(items, dict):
        items = items.get("items", [items])
    failures = 0
    for i, item in enumerate(items, 1):
        label = item.get("id", i)
        try:
            ok, detail = check(item)
        except Exception as e:  # report and continue
            ok, detail = False, f"ERROR: {e}"
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {label}: {detail}")
    print(f"\n{len(items) - failures}/{len(items)} correct")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

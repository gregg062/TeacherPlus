# Example: 4-week Algebra 1 long-term sub package

A complete example of what the `long-term-sub-plans` skill produces. It's also the reference the skill reads to match structure and level of detail.

- 19 school days (January 4-29, 2027, with MLK Day off), unit: systems of linear equations and inequalities.
- Every lesson: run of show, opening script, worked examples written step by step, a "find the mistake" task, common mistakes with what to say, guided and independent practice, exit ticket with a sorting rule, and a fully worked answer key.
- **Every answer (298 checks) is verified** by `tools/check_math.py`. `answer-keys.json` holds all the checks.
- Standards text is quoted from the bundled Common Core file via `tools/standards.py`.

## Files

`00-overview.md` · `01-calendar.md` · `week-1.md` to `week-4.md` · `02-grading-guide.md` · `03-family-letters.md` · `04-handoff-log.md`

## How it was made

`build.py` contains the hand-written parts (scripts, misconceptions, word problems, flex plans) and the numbers for each problem. It generates the step-by-step solutions, checks every answer, and writes the week files. The build stops if any answer is wrong. Rebuild after edits:

```
python3 examples/algebra1-long-term-sub/build.py
```

Status: DRAFT, awaiting educator review. Reviewer: please check the lesson sequence, pacing, scripts and misconception notes as you would a real sub plan.

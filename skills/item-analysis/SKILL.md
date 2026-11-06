---
name: item-analysis
description: Analyze class results on a quiz or test from item-level or skill-level scores (names removed) to find which questions and skills students missed, common wrong answers, and what to reteach, plus a grouping plan. Use when a teacher pastes or uploads test scores, item results, exit ticket tallies, or asks "what should I reteach" or "how did my class do on this test".
---

# Item analysis

## Privacy first

This skill works with **de-identified** data. Ask the teacher to remove names (use numbers or initials) before pasting or uploading. If names are present, don't repeat them; refer to "Student 1, 2..." and suggest removing them next time. If the TeacherPlus connector is loaded, `class_summary` gives assignment-level results without names.

## Accepted input

Any of: a table of students × items (1/0 or points), responses per item (A/B/C/D), per-standard scores, or tallies ("18 of 26 got Q4 right").

## Analysis

1. **Overall**: class average, spread (how many students in each band), and how it compares to the teacher's mastery target (default 80%).
2. **Item difficulty**: percent correct per item. Flag items below 60% (needs reteaching) and any item where most students chose the *same* wrong answer — that's a shared misconception (or a flawed item; check the key and wording).
3. **By skill/standard**: group items by objective; rank skills from weakest to strongest.
4. **Suspicious items**: items high-scoring students missed but low scorers got right usually have a key error or ambiguous wording — recommend reviewing them.

## Action plan

- **Whole-class reteach** for skills below the target: the likely misconception and a different way to teach it (see `adjust-on-the-fly`, `lesson-delivery`).
- **Small groups**: a grouping by skill (using numbers/initials) with a task for each group, including an extension group.
- **Re-assessment** idea: 2-3 new items per reteached skill.
- **Next time**: changes to instruction or to the test items.

Show percent-correct results as a simple table or chart sorted weakest first.

## Accuracy tools

`<plugin-root>` is the folder two levels above this skill's base directory (the one containing `tools/` and `references/`).

- **Misconceptions:** read `<plugin-root>/references/misconceptions/<subject>.md` (algebra-1, fractions, middle-school-science, ela) when it matches the topic, and use it for misconception notes and distractors. For other subjects, draw on known research and say the notes are general.

## Evidence base

Formative use of assessment data (Black & Wiliam; Wiliam). Full citations and strength of evidence: `<plugin-root>/references/research.md`.

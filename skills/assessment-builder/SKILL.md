---
name: assessment-builder
description: Create quizzes, unit tests, common assessments and performance tasks with answer keys, point values, a test blueprint, and a mix of question types and difficulty. Use when a teacher asks for a quiz, test, exam, assessment, question bank, review game questions, or practice test.
---

# Assessment builder

## Ask once (only what's missing)

Grade, subject, topic or standards/objectives covered, length (number of questions or minutes), question types wanted, and whether students have accommodations that need an alternate version.

## 1. Blueprint first

A short table: **Objective/standard | # items | Question types | Cognitive level (recall / apply / analyze-explain) | Points**. Weight by importance and instructional time — not equal by default. Aim for roughly a third of points beyond recall unless the teacher says otherwise. Show it before (or with) the test.

## 2. The assessment

- Clear student directions and point values on every section.
- Order easy → harder within each section so students build confidence.
- Mix of types that suit the objective: multiple choice, short constructed response, problems, a performance/application task, an explanation question.
- Include space guidance for written answers.

## 3. Answer key and scoring

- Correct answer for every item, and for multiple choice the misconception each distractor targets.
- Scoring guide for constructed responses: full / partial / no credit with examples of each.
- Objective tag on every item, so results can be analyzed by skill (see `item-analysis`).

## 4. Versions (if asked)

- **Alternate form** (Form B) with parallel items for retakes or absent students.
- **Accommodated version**: same objectives; fewer items per objective, simplified language (not simplified content), more white space, word bank where appropriate, read-aloud friendly.

## Item writing rules

- One clear problem per item; no trick questions, no double negatives, no "all/none of the above".
- Distractors plausible and similar in length; correct answers spread across positions.
- Reading level at or below grade unless reading is what's assessed.
- Avoid culturally narrow contexts or names/stereotypes; use inclusive, varied contexts.
- Run the `assessment-review` checklist before presenting.

## Accuracy tools

`<plugin-root>` is the folder two levels above this skill's base directory (the one containing `tools/` and `references/`).

- **Math accuracy:** for any math answer key, write each problem and its claimed answer as JSON and run `python3 <plugin-root>/tools/check_math.py keys.json` (usage is in the file's header). Fix every FAIL and re-run until all pass. If you can't run code, mark the key "not machine-checked, please verify".
- **Standards:** look up codes and wording with `python3 <plugin-root>/tools/standards.py get <code>` or `search "<topic>" --set math|ela|ngss --grade <g>`. Quote the official text. Never cite a code the tool can't find. For state-specific standards, ask the teacher to paste them.
- **Misconceptions:** read `<plugin-root>/references/misconceptions/<subject>.md` (algebra-1, fractions, middle-school-science, ela) when it matches the topic, and use it for misconception notes and distractors. For other subjects, draw on known research and say the notes are general.

## Evidence base

Item-writing guidelines (Haladyna, Downing & Rodriguez); Depth of Knowledge (Webb; Hess); alignment of objectives and assessment (Wiggins & McTighe). Full citations and strength of evidence: `<plugin-root>/references/research.md`.

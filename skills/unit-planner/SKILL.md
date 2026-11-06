---
name: unit-planner
description: Plan a full unit of instruction using backward design - goals and standards, big ideas, essential questions, the summative assessment first, then a lesson-by-lesson sequence with formative checks and a pacing calendar. Use when a teacher asks to plan a unit, module, topic over several weeks, or a project-based unit.
---

# Unit planner (backward design)

Plan from the end: decide what students must understand and be able to do, decide how they'll show it, then plan the learning.

## Ask once (only what's missing)

Grade, subject, topic, standards (or "find them"), number of days and period length, what students already know, and any required texts, materials or common assessments.

## Stage 1 — Desired results

- **Standards** addressed (code + short text). If the teacher hasn't given them, propose the likely standards for their state/framework and mark them *"verify against your state standards"*.
- **Big ideas / enduring understandings** (2-3): transferable ideas, phrased "Students will understand that...".
- **Essential questions** (2-4): open, arguable, revisited throughout the unit.
- **Knowledge and skills**: "Students will know..." / "Students will be able to..." — specific and measurable.
- **Key vocabulary** (tiered: topic-specific and general academic words).

## Stage 2 — Evidence

- **Summative assessment** (performance task and/or test): what students do, the real-world context if one fits, and a rubric or blueprint (use `rubric-builder` / `assessment-builder`). Each Stage 1 goal must be assessed.
- **Formative checkpoints** at key points in the unit (exit tickets, quizzes, drafts) with what the teacher will do with the results.
- **Pre-assessment** on day 1 to find what students already know.

## Stage 3 — Learning plan

A calendar table: **Day | Learning target ("I can...") | Key activities | Formative check | Homework/notes**. Build in:
- a hook/launch lesson that raises the essential questions;
- spaced retrieval of earlier content;
- at least one flex/reteach day after the main formative checkpoint;
- review before the summative, and a reflection after.

## Check before finishing

Run an alignment check and show it as a small table: every goal → where it is taught → where it is assessed. Flag gaps or activities that don't serve a goal. Note differentiation (support and extension) for the main tasks.

## Accuracy tools

`<plugin-root>` is the folder two levels above this skill's base directory (the one containing `tools/` and `references/`).

- **Standards:** look up codes and wording with `python3 <plugin-root>/tools/standards.py get <code>` or `search "<topic>" --set math|ela|ngss --grade <g>`. Quote the official text. Never cite a code the tool can't find. For state-specific standards, ask the teacher to paste them.
- **Misconceptions:** read `<plugin-root>/references/misconceptions/<subject>.md` (algebra-1, fractions, middle-school-science, ela) when it matches the topic, and use it for misconception notes and distractors. For other subjects, draw on known research and say the notes are general.

## Evidence base

Backward design (Wiggins & McTighe); spaced retrieval (Cepeda et al.; Dunlosky et al.); formative assessment (Wiliam). Full citations and strength of evidence: `<plugin-root>/references/research.md`.

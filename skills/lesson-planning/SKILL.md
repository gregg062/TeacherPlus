---
name: lesson-planning
description: Create lesson plans, unit outlines, differentiated activities, exit tickets, quizzes and rubrics. Use when a teacher asks for a lesson plan, activity, worksheet, assessment, rubric, reteach plan, or ways to differentiate for students.
---

# Lesson planning

1. Confirm the essentials (ask once, only what's missing): grade/subject, topic or standard, lesson length, and what students already know. Use `list_classes` for period length when relevant.
2. If the teacher wants it tailored to their class, call `class_summary` (to see which assignments need reteaching) and `get_roster` (for supports like IEP/504/ELL). Plan for needs, but don't name students in the lesson plan itself unless asked — use groups ("students needing read-aloud").
3. Lesson plan format:
   - Objective (student-friendly "I can..." statement) and standard if known.
   - Materials.
   - Timed sequence: hook / direct instruction / guided practice / independent or group work / closure, adding up to the period length.
   - Checks for understanding during the lesson and an exit ticket (with answer key).
   - Differentiation: support (sentence frames, worked examples, reduced load, read-aloud), ELL (vocabulary, visuals), extension.
   - Accommodations that apply from the roster, as actions.
4. For quizzes and worksheets, include an answer key and point values. For rubrics, use a table with 3–4 levels and observable descriptors.
5. For a reteach plan, start from the assignment with the lowest average or most missing work in `class_summary` and target the likely misconception.

## Related skills

- Multi-week planning → `unit-planner`; standards and rigor → `standards-alignment`.
- Turning the plan into a minute-by-minute run of show, script and slides → `lesson-delivery`.
- Exit tickets and hinge questions → `checks-for-understanding`; tiered tasks and scaffolds → `differentiation`.

The TeacherPlus connector is optional here: if it isn't available, plan from what the teacher tells you.

## Accuracy tools

`<plugin-root>` is the folder two levels above this skill's base directory (the one containing `tools/` and `references/`).

- **Math accuracy:** for any math answer key, write each problem and its claimed answer as JSON and run `python3 <plugin-root>/tools/check_math.py keys.json` (usage is in the file's header). Fix every FAIL and re-run until all pass. If you can't run code, mark the key "not machine-checked, please verify".
- **Standards:** look up codes and wording with `python3 <plugin-root>/tools/standards.py get <code>` or `search "<topic>" --set math|ela|ngss --grade <g>`. Quote the official text. Never cite a code the tool can't find. For state-specific standards, ask the teacher to paste them.
- **Misconceptions:** read `<plugin-root>/references/misconceptions/<subject>.md` (algebra-1, fractions, middle-school-science, ela) when it matches the topic, and use it for misconception notes and distractors. For other subjects, draw on known research and say the notes are general.

## Evidence base

Rosenshine's principles; backward design (Wiggins & McTighe); formative assessment (Wiliam). Full citations and strength of evidence: `<plugin-root>/references/research.md`.

---
name: checks-for-understanding
description: Create checks for understanding and formative assessment for use during a lesson - hinge questions, exit tickets, mini-whiteboard prompts, quick polls, do-now and retrieval practice, with what each wrong answer reveals. Use when a teacher asks for exit tickets, bell ringers, do nows, warm-ups, hinge questions, formative checks, retrieval practice, or "how do I know if they got it".
---

# Checks for understanding

The goal is evidence from **every** student, fast, that tells the teacher what to do next.

## What to produce

For the topic/objective given:

1. **Hinge question(s)** — multiple choice, answerable in under a minute, where every wrong option is a *specific, common misconception*. For each option give: what choosing it reveals, and what to do next. Specify the response method (fingers 1-4, letter cards, mini-whiteboards, poll) so all students answer at once.
2. **Mini-whiteboard prompts** — 3-5 short problems/questions of increasing difficulty the teacher can fire in a row.
3. **Exit ticket** — 2-3 items: one core-skill item, one that requires explaining or applying, optionally one self-rating. Include an answer key and a sorting rule: *got it / nearly / not yet*, with the plan for each group tomorrow.
4. **Do Now / retrieval practice** — 3-5 questions mixing yesterday's content with something from 2-4 weeks ago (spaced retrieval), answerable independently in 5 minutes without notes.

Only produce the types asked for; if not specified, give a hinge question and an exit ticket.

## Quality rules

- Each item checks the objective, not reading ability or trivia. Keep language at or below grade level.
- Distractors must be plausible; no "all of the above", no joke options, no clues in option length or grammar.
- Prefer questions that reveal *thinking* ("Which step is wrong?", "Explain why...") over pure recall when the objective is conceptual.
- Include decision rules: e.g. "If 80%+ are correct, move on; if not, reteach using..."
- Accessible formats: can be read aloud, works on paper and screen.

## Accuracy tools

`<plugin-root>` is the folder two levels above this skill's base directory (the one containing `tools/` and `references/`).

- **Math accuracy:** for any math answer key, write each problem and its claimed answer as JSON and run `python3 <plugin-root>/tools/check_math.py keys.json` (usage is in the file's header). Fix every FAIL and re-run until all pass. If you can't run code, mark the key "not machine-checked, please verify".
- **Misconceptions:** read `<plugin-root>/references/misconceptions/<subject>.md` (algebra-1, fractions, middle-school-science, ela) when it matches the topic, and use it for misconception notes and distractors. For other subjects, draw on known research and say the notes are general.

## Evidence base

Formative assessment and hinge questions (Black & Wiliam; Wiliam); retrieval and spaced practice (Roediger & Karpicke; Dunlosky et al.); item-writing guidelines (Haladyna et al.). Full citations and strength of evidence: `<plugin-root>/references/research.md`.

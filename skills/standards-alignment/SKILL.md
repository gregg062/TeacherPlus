---
name: standards-alignment
description: Check how well a lesson, unit, assignment or assessment aligns to standards and to its own objective - which standards it meets, how deeply (cognitive demand / depth of knowledge), gaps, and how to raise rigor. Use when a teacher asks to align to standards, unpack a standard, check rigor, map DOK or Bloom's levels, or "what standard does this hit".
---

# Standards alignment & rigor

## Unpacking a standard

When given a standard, break it into:
- **Skills (verbs)** and **concepts (nouns)** — e.g. "*Analyze* (skill) *how an author develops point of view* (concept)".
- The **level of thinking** the standard demands (Depth of Knowledge 1-4: recall → skill/concept → strategic thinking → extended thinking).
- **Learning targets** in student language, sequenced from simpler to the full standard.
- What **proficient evidence** would look like, plus a sample task at the right level.

## Checking a lesson or task

1. List the standards it plausibly addresses. Mark which are *fully*, *partially*, or *only loosely* met. Never claim alignment without pointing to the specific part of the task.
2. For each task/question, identify the DOK level and compare it with the standard's level. Lessons commonly *under-reach* (recall-only tasks for an "analyze" standard) — call that out.
3. Check internal alignment: objective ↔ activities ↔ assessment. Does the assessment measure the objective? Do the activities prepare students for it?
4. Recommend 2-3 specific revisions that raise rigor or close gaps, e.g. turning a recall question into an explanation/justification question, adding a transfer task, or removing busywork.

## Rules

- If the teacher's state or framework is unknown, ask or note your assumption (e.g. Common Core, NGSS, a state's own standards). Quote standard codes only when confident and tell the teacher to verify them.
- Higher DOK means more complex thinking, not more work or harder vocabulary.

## Accuracy tools

`<plugin-root>` is the folder two levels above this skill's base directory (the one containing `tools/` and `references/`).

- **Standards:** look up codes and wording with `python3 <plugin-root>/tools/standards.py get <code>` or `search "<topic>" --set math|ela|ngss --grade <g>`. Quote the official text. Never cite a code the tool can't find. For state-specific standards, ask the teacher to paste them.

## Evidence base

Depth of Knowledge (Webb; Hess et al.); revised Bloom's taxonomy (Anderson & Krathwohl). Full citations and strength of evidence: `<plugin-root>/references/research.md`.

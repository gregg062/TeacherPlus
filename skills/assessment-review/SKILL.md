---
name: assessment-review
description: Review a teacher's existing quiz, test, worksheet or assignment for quality - ambiguous or flawed questions, answer giveaways, misalignment with objectives, rigor, bias, accessibility and length - and propose fixed versions. Use when a teacher asks to check, review, improve, critique or proofread a test, quiz, worksheet or assignment.
---

# Assessment review

Review like an experienced head of department doing a supportive pre-check: be specific and fix things, not just list problems.

## Checklist

1. **Alignment** — Does every item measure a stated objective? Are important objectives missing or underweighted? Is the cognitive level right for the standard?
2. **Clarity** — ambiguous wording, more than one defensible answer, double negatives, unclear directions, missing units or info.
3. **Giveaways & flaws** — longest option is correct, grammatical clues ("an" before the answer), one item answers another, implausible distractors, "all/none of the above", answer patterns.
4. **Answer key** — check every answer is correct; solve problems independently.
5. **Rigor** — share of recall vs. apply/explain items; any trick questions.
6. **Bias and accessibility** — culturally narrow contexts, stereotypes, unnecessary reading load, font/layout issues, images without description, enough working space.
7. **Length and timing** — realistic for the period (estimate minutes per item type) and for students with extended time.
8. **Scoring** — points match importance; constructed responses have clear criteria.

## Output

1. A two-line overall verdict (strengths first).
2. A table: **Item | Issue | Why it matters | Fixed version**. Prioritize: errors in the key and unfair items first, then alignment, then polish.
3. A summary of alignment (objective → items) and estimated completion time.
4. Offer the fully revised assessment.

## Accuracy tools

`<plugin-root>` is the folder two levels above this skill's base directory (the one containing `tools/` and `references/`).

- **Math accuracy:** for any math answer key, write each problem and its claimed answer as JSON and run `python3 <plugin-root>/tools/check_math.py keys.json` (usage is in the file's header). Fix every FAIL and re-run until all pass. If you can't run code, mark the key "not machine-checked, please verify".
- **Standards:** look up codes and wording with `python3 <plugin-root>/tools/standards.py get <code>` or `search "<topic>" --set math|ela|ngss --grade <g>`. Quote the official text. Never cite a code the tool can't find. For state-specific standards, ask the teacher to paste them.

## Evidence base

Item-writing guidelines (Haladyna, Downing & Rodriguez); Depth of Knowledge (Webb). Full citations and strength of evidence: `<plugin-root>/references/research.md`.

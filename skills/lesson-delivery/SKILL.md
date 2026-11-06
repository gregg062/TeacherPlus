---
name: lesson-delivery
description: Turn a lesson plan into what the teacher actually says and does in the room - a minute-by-minute run of show, teacher script, think-alouds, questions to ask, anticipated misconceptions, transitions, and slides. Use when a teacher asks how to teach, deliver, present, model or script a lesson, wants a "run of show", talking points, a slide deck, or says "I'm teaching this tomorrow".
---

# Lesson delivery

A plan says *what* students will learn; delivery is *how the 50 minutes actually go*. Produce something the teacher can glance at mid-lesson.

## 1. Inputs

Use the teacher's lesson plan if they have one (or build a quick one with `lesson-planning`). Ask only if missing: grade, period length, what students did last lesson, and whether they have a projector / mini-whiteboards / devices.

## 2. Run of show (one page, glanceable)

A table: **Clock time | Segment | Teacher does / says | Students do | Materials | Check**. Use real clock times if the period start is known (`list_classes`), otherwise 0:00-based. Segments normally follow gradual release:

1. **Do Now (3-5 min)** — independent retrieval of prior learning, posted before students arrive.
2. **Hook (2-4 min)** — a question, image, demo or short story that creates a need to know.
3. **I do — model (5-10 min)** — teacher thinks aloud through one example.
4. **We do — guided practice (8-12 min)** — students do the next steps with prompts; teacher checks every student.
5. **You do — independent / group practice (10-15 min)** — teacher circulates with a plan (who to see first).
6. **Closure + exit ticket (5 min)** — students state the learning and show it.

Every segment ends with a quick check, and every transition has a cue ("Pens down, eyes up in 3, 2, 1").

## 3. Teacher script (for the parts that matter most)

- **Opening words** — the learning target in student language and why it matters.
- **Think-aloud** for the model example, written in first person, including the teacher noticing and fixing a likely mistake.
- **Key questions**, labelled by purpose: *recall*, *check*, *push thinking*. Include planned wait time and who answers (cold call, all-write, turn-and-talk) — never "Any questions?".
- **Clear directions** for each activity in the format *what, how long, what done looks like, what to do if stuck*. Keep each set under 30 seconds to say.

## 4. Anticipated misconceptions

For the 2-3 most likely errors: what it looks like in student work, why students think it, and a 1-minute response (a counterexample, a question, a quick visual) — not just re-explaining louder.

## 5. Contingencies

- **Running behind:** what to cut (never cut the check for understanding or closure).
- **Ahead / early finishers:** an extension that deepens rather than adds more of the same.
- **Most students stuck at the check:** a reteach move (see `adjust-on-the-fly`).

## 6. Slides (if wanted)

One idea per slide: Do Now, learning target, hook, model example (build step by step), guided practice, directions slide with timer for each activity, exit ticket. Large text, minimal words, directions stay on screen during the activity. Use the session's slide/presentation tooling if available; otherwise give slide-by-slide content and speaker notes.

## Rules

- Times must add up exactly to the period length.
- Teacher talk in any single stretch should rarely exceed 10 minutes; students should be doing something every few minutes.
- Write in plain, natural teacher voice suitable for the grade level — no scripted-sounding jargon.

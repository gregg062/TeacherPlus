---
name: sub-plans
description: Write a complete, ready-to-print substitute teacher plan. Use when a teacher says they will be absent, out sick, at a training or field trip, or asks for "sub plans", "emergency sub plans", or "plans for a substitute".
---

# Substitute plans

Produce a plan a substitute who has never been in the building can follow without asking anyone.

## 1. Gather context

1. Call `get_sub_plan_context` (TeacherPlus connector). It returns the schedule, rooms, classroom procedures and, per class, only the students who need attention (first name + last initial, supports, accommodations, notes).
2. Ask the teacher only for what is still missing, in a single message:
   - date(s) of the absence;
   - what each class should do (topic, pages, handouts, links) — or offer to design a no-tech, sub-friendly activity that reviews the current unit;
   - where materials are.
   If the teacher says "emergency" or "just make something", don't ask: build generic review activities from the class names and note where the teacher should fill in details.

## 2. Write the plan

Use this structure, one page per section where possible:

1. **Welcome & essentials** — teacher name, room, date, key contacts (from procedures), where the attendance login/paper roster is, bathroom & phone rules.
2. **Daily schedule** — a table: period, time, room, class, enrolled, activity summary.
3. **Emergency procedures** — copied from procedures, short and bold.
4. **Lesson plans, one per class/period**
   - Objective in one sentence.
   - Timed agenda (e.g. *0–5 min bell-ringer, 5–30 min ..., last 5 min exit ticket*), adding up to the period length.
   - Exact instructions to read aloud to students.
   - Materials and where they are.
   - What to collect and where to leave it.
   - Early-finisher activity.
5. **Students to know** — per class, from the connector: supports/accommodations translated into concrete actions the sub can take ("Jordan B.: may take extra time — let him finish during the early-finisher time"). Include safety/medical/custody notes. Never include grades, at-risk flags, diagnoses or disciplinary history.
6. **Helpers** — neighbor teacher and reliable student helpers.
7. **End-of-day notes** — a short form for the sub: who was absent, who was helpful, any problems, what was not finished.

## Rules

- Activities must work without the teacher's login, without labs/chemicals/sharp tools, and with a sub who doesn't know the subject.
- Use first name + last initial only. Keep it to what the sub needs (FERPA minimum necessary).
- Default output: a printable document (DOCX or PDF if the teacher's environment supports it, otherwise well-formatted Markdown). Offer a one-page "emergency sub plan" version that can stay in the sub folder all year.

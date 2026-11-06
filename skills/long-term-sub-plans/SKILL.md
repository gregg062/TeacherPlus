---
name: long-term-sub-plans
description: Build a complete long-term substitute package for a planned absence of one week or more (parental leave, surgery, medical or family leave) - unit pacing calendar, a consistent daily routine, scripted daily lessons with worked examples, fully worked and verified answer keys, a grading guide, family letters, and a handoff log. Use when a teacher will be out for more than a few days, mentions maternity/paternity leave, a long-term sub, or asks for weeks of sub plans.
---

# Long-term substitute plans

A long-term sub package is a curriculum handed to someone who may **not** be a specialist in the subject. Everything must be followable by a capable adult who doesn't know the content, the students or the school, without calling the teacher.

`<plugin-root>` is the folder two levels above this skill's base directory (the one containing `tools/` and `references/`). Shared resources:
- `<plugin-root>/tools/check_math.py` — verifies math answer keys (see step 5).
- `<plugin-root>/tools/standards.py` — looks up standards text by code or topic.
- `<plugin-root>/references/misconceptions/` — common misconceptions by subject.
- `<plugin-root>/examples/algebra1-long-term-sub/` — a complete 4-week Algebra 1 example. Read its `00-overview.md` and one week file before writing a package, and match its structure and level of detail.

## 1. Gather (ask once, in one message, only what's missing)

- Dates of the leave (and return), courses/periods, period length, and the school calendar (holidays, testing, early release days).
- Where the class is now: the last thing taught and how it went. If the TeacherPlus connector is available, call `class_summary` for each class.
- What must be covered: units/standards, required curriculum materials, common assessments with dates.
- Who the sub is, if known (certified in the subject? same sub the whole time?), and the teacher's preference for what the sub grades.
- School systems: gradebook/LMS access for the sub, copy procedures, the department contact.

If the teacher can't answer some questions, make reasonable assumptions, state them at the top of the package, and leave [bracketed blanks] for school-specific facts. Never invent school policies or student details.

## 2. Package structure (one folder or document set)

1. **Overview for the sub** (2 pages max): welcome, how the package is organized, the daily routine, who to contact for what, what to do if a lesson doesn't fit the time.
2. **Pacing calendar**: a table of every school day: **Date | Day # | Learning target ("I can...") | Standard | Lesson type (new / practice / quiz / review / flex) | Materials**. Include:
   - a quiz roughly weekly and any unit test;
   - **flex/reteach days**: at least one per week (snow days, assemblies and re-teaching will happen);
   - spaced review of earlier units.
   Look up standard codes with `python3 <plugin-root>/tools/standards.py` and quote their wording; don't cite codes from memory.
3. **Daily routine** — the same every day so students and sub settle in quickly. Default for a 45-60 minute class:
   Do Now (5-8 min retrieval) → mini-lesson with worked examples (10-15) → guided practice "we do" (10) → independent practice (10-15) → exit ticket (5).
4. **Daily lesson plans** (one page each, plus handouts), each with:
   - learning target in student language and the standard;
   - the Do Now (mixing yesterday's skill with older ones) with answers;
   - **scripted worked examples**: exact steps and the words to say, so a non-specialist can teach it. Include one "find the mistake" example where suitable (error analysis is research-supported for algebra);
   - the 2-3 likely misconceptions for the lesson (from `<plugin-root>/references/misconceptions/`), what they look like and what to say;
   - guided and independent practice problems, easier to harder;
   - exit ticket with the sorting rule (got it / nearly / not yet) and what to do tomorrow for each group;
   - an optional video idea (the teacher records the mini-lesson before leaving, or a vetted free video) for subs who are not comfortable teaching the content;
   - early-finisher work and what to collect.
5. **Answer keys — fully worked, verified**: show every step, not just the final answer, so the sub can help a student mid-problem and grade partial work.
   - **For math:** write every problem with its claimed answer as a JSON list, run `python3 <plugin-root>/tools/check_math.py keys.json`, fix every FAIL, and run it again until all pass. Say in the package that answer keys were computer-checked. If you can't run code, write "answer keys not machine-checked, please verify" at the top of the keys.
   - **For other subjects:** model answers plus scoring guides with sample responses at each score.
6. **Grading guide**: what the sub grades (with keys/rubrics) and what to save for the teacher; points for each assignment; how to enter grades; the late work and retake policy; what counts as complete for practice work.
7. **Students**: accommodations translated into actions; a small-group plan for students who were already struggling; students with medical/safety notes. A long-term sub generally counts as school staff with a legitimate educational interest under FERPA, so they can receive more than a one-day sub, but the teacher should follow school policy and share only what the sub needs (use the connector's `get_roster` if available). Never include at-risk tiers or disciplinary histories in the package.
8. **Communication**: a letter to families introducing the sub and how learning will continue, a weekly update template the sub can send, and the contact plan (department head for curriculum questions, office for attendance, case manager for IEPs).
9. **Handoff log**: a daily log table for the sub: **Date | What was taught | What wasn't finished | Exit ticket results (counts) | Concerns / notes**. Plus a return-week plan so the teacher knows exactly where to restart.
10. **Contingencies**: what moves on a lost day (use flex days), what to do if most of the class fails a quiz (reteach on the next flex day using the misconception notes), emergency/technology-free backup lessons.

## 3. Quality checks before handing over

- Every day in the date range has a plan, and the calendar matches real dates and days of the week.
- Each lesson's timings add up to the period length.
- Every standard in the calendar was looked up, and every learning target matches its standard.
- Every problem has a worked solution; math keys passed `check_math.py`.
- The package never assumes the sub knows the subject, the students, or school systems.
- Instruction follows the evidence base: consistent routine, explicit instruction with worked examples, daily retrieval, checks for understanding, spaced review (see `<plugin-root>/references/research.md`).

## Output

Produce the package as separate, printable documents (overview, calendar, one file per week of lessons with keys, grading guide, family letter, handoff log). For large packages, start with the overview and calendar for the teacher's approval, then write the weeks.

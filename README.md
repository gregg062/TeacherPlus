# TeacherPlus

A Claude plugin that helps teachers plan, deliver and assess lessons, differentiate, coach colleagues and lead a department, and handle the everyday writing: substitute plans, report card comments and parent emails. It also includes an early-warning screen for students who may need support.

It has two parts:

- **Skills** — instructions that tell Claude how to do each task well (structure, tone, privacy rules).
- **A local connector (MCP server)** — reads the teacher's roster, gradebook, attendance and behavior log from CSV files on their own computer, and runs the at-risk screening. Student data isn't uploaded anywhere except to the Claude conversation the teacher is using.

## What it can do

TeacherPlus covers the whole teaching cycle: plan → differentiate → deliver → assess → reflect, plus coaching, department leadership and the writing teachers do every week. `report-comments` and `at-risk-review` are built around the class-data connector; `sub-plans`, `long-term-sub-plans`, `parent-communication` and `lesson-planning` can use it when it's available. Everything else works with no connector and no student records.

| Area | Skills |
|---|---|
| Deliver the lesson | `lesson-delivery`, `checks-for-understanding`, `discussion-and-engagement`, `adjust-on-the-fly`, `classroom-management`, `lesson-reflection` |
| Plan & curriculum | `lesson-planning`, `unit-planner`, `standards-alignment`, `curriculum-map` |
| Differentiate | `differentiation`, `leveled-texts` |
| Assess | `assessment-builder`, `rubric-builder`, `assessment-review`, `item-analysis` |
| Coach & lead | `lesson-review`, `observation-feedback`, `coaching-cycle`, `department-leadership`, `new-teacher-mentoring` |
| Communicate & grow | `class-communications`, `parent-communication`, `professional-growth` |
| Substitutes | `sub-plans` (a day or two), `long-term-sub-plans` (a week or more) |
| Uses class data (connector) | `report-comments`, `at-risk-review` |

Teachers just ask in plain language, for example:

- "I'm teaching area of triangles tomorrow, give me a run of show and what to say" → `lesson-delivery`
- "Half the class got the whiteboard check wrong, 25 minutes left" → `adjust-on-the-fly`
- "Make a hinge question on comparing fractions" → `checks-for-understanding`
- "Give me feedback on my lesson plan" → `lesson-review`
- "Write up my walkthrough notes for this teacher" → `observation-feedback`
- "I'm out Friday, make sub plans" → `sub-plans`
- "Who in period 3 is struggling?" → `at-risk-review`

Skills can also be run directly, e.g. `/teacherplus:lesson-delivery`.

## Educator-reviewed

Every skill is reviewed, edited and tested by an experienced educator (25 years in the classroom, master's in curriculum, instructional coach and head of department) before it is marked approved. Review status for each skill is tracked in [REVIEW.md](REVIEW.md), and skills have test cases in `evals/` graded against her criteria.

## How TeacherPlus avoids wrong answers

- **Research-based methods.** Skills follow well-evidenced teaching practice (explicit instruction, worked examples, retrieval practice, formative assessment, backward design and more). Every skill names its sources; full citations and the strength of the evidence are in [references/research.md](references/research.md).
- **Verified math.** Math answer keys are checked by `tools/check_math.py`, which recomputes every answer with exact arithmetic (equations, systems, inequalities, fractions, slopes). Claude fixes anything that fails before showing the key.
- **Real standards text.** Common Core math and ELA and NGSS are bundled in `references/standards/`, and `tools/standards.py` looks codes up so they are quoted, not remembered. Unknown codes are refused.
- **Subject knowledge.** `references/misconceptions/` lists the errors students commonly make in Algebra 1, fractions, middle school science and ELA, with teaching responses.
- **Worked examples.** `examples/algebra1-long-term-sub/` is a complete 4-week Algebra 1 long-term sub package (19 lessons, 298 computer-checked answers) that skills use as their quality benchmark.
- **Educator review and tests.** See below.

## At-risk screening: how students get flagged

Rule-based and transparent, so every flag lists the reasons behind it. Defaults follow common early-warning indicators and can be changed per request ("use 65% as failing").

| Area | Rule (default) | Points |
|---|---|---|
| Academics | Average below 60% / below 70% | 3 / 2 |
| Academics | Recent scores ≥10 points below earlier scores | 2 |
| Engagement | ≥6 / ≥3 missing assignments in last 30 days | 3 / 2 |
| Attendance | Attendance rate below 80% / below 90% (chronic absence) | 3 / 2 |
| Attendance | ≥5 tardies in last 30 days | 1 |
| Behavior | ≥3 / 1–2 concerns logged in last 30 days | 2 / 1 |

**Tiers:** High = 5+ points · Moderate = 2–4 · Watch = 1. Averages are points-based, missing work counts as zero, and excused work is ignored. Strengths (high averages, improvement, good attendance, positive notes) are reported too.

The screen is meant to start a conversation. It doesn't diagnose anything, and the skills tell Claude never to show flags to substitutes or families.

## Install

Requirements: [uv](https://docs.astral.sh/uv/) (it installs the Python MCP SDK automatically on first run).

**Claude Code:**

```
/plugin marketplace add gregg062/teacherplus
/plugin install teacherplus@teacherplus
```

**Claude desktop / Cowork:** add the plugin from this repository through the plugin settings, or zip the repository and upload it as a custom plugin.

No `uv`? If Python has the MCP SDK installed (`pip install mcp`), change `.mcp.json` to use `"command": "python3", "args": ["${CLAUDE_PLUGIN_ROOT}/server/teacherplus_server.py"]`.

Ask Claude "what TeacherPlus data is loaded?" to check the setup. Out of the box it uses the fictional students in `sample-data/`.

## Using your own data

Put your files in `~/TeacherPlus/data/` (or any folder, and set the `TEACHERPLUS_DATA_DIR` environment variable to that path). Export them from your gradebook/SIS as CSV; column names are case-insensitive and only `students.csv` is required. See `sample-data/` for complete examples.

**students.csv** — `student_id, first_name, last_name, grade_level, class_ids, supports, accommodations, notes, guardian_name, guardian_email, preferred_language`
- `class_ids` and `supports` can hold several values separated by `;` (e.g. `SCI7-P1;ADV`, `IEP;ELL`).

**classes.csv** — `class_id, name, period, start_time, end_time, room`

**grades.csv** — `student_id, class_id, assignment, category, date, score, max_score, status`
- `status`: `submitted` (default), `late`, `missing`, `excused`. Dates are `YYYY-MM-DD`.

**attendance.csv** — `student_id, date, status` (optional `class_id`)
- `status`: `present`, `absent`, `excused`, `tardy`.

**behavior.csv** — `student_id, class_id, date, type, description`
- `type`: `concern` or `positive`.

**procedures.md** — free text for subs: emergency procedures, routines, helpful staff, student helpers.

## Privacy

Student records are protected (FERPA in the US). TeacherPlus:

- reads data only from the folder you choose, on your computer;
- gives substitutes only first name + last initial, supports and safety notes, never grades or flags;
- drafts parent messages but never sends them;
- `.gitignore` excludes `data/` so real student files don't get committed by accident.

Check your district's policy on using AI tools with student data before connecting real records.

## Development

```
uv run --with pytest pytest -q tests      # unit tests for the screening logic
claude plugin eval .                      # run the skill test cases (evals/)
python3 examples/algebra1-long-term-sub/build.py   # rebuild + re-verify the example
python3 server/teacherplus_server.py      # run the MCP server over stdio
```

Layout:

```
.claude-plugin/plugin.json        plugin manifest
.claude-plugin/marketplace.json   lets this repo be added as a plugin marketplace
.mcp.json                         registers the connector
server/risk.py                    data loading + screening (standard library only)
server/teacherplus_server.py      MCP tools
skills/*/SKILL.md                 task instructions (28 skills)
evals/                            test cases + grading criteria per skill
REVIEW.md                         educator review tracker
sample-data/                      fictional class for demos
tests/                            pytest suite
tools/                            check_math.py (answer checker), standards.py (standards lookup)
references/                       research.md, standards/, misconceptions/
examples/                         complete worked examples (4-week Algebra 1 sub package)
```

## Ideas for next versions

- Direct connectors for Google Classroom, Canvas, PowerSchool or a Google Sheets gradebook instead of CSV export.
- Tracking interventions and check-ins over time, so the screen can show whether support is working.
- IEP progress-monitoring notes and accommodation checklists.
- Connector mocks so the data-driven skills have automated tests too.

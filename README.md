# TeacherPlus

A Claude plugin that helps teachers with the everyday work around teaching: substitute plans, report card comments, parent emails, lesson plans, and an early-warning screen for students who may need support.

It has two parts:

- **Skills** — instructions that tell Claude how to do each task well (structure, tone, privacy rules).
- **A local connector (MCP server)** — reads the teacher's roster, gradebook, attendance and behavior log from CSV files on their own computer, and runs the at-risk screening. Student data isn't uploaded anywhere except to the Claude conversation the teacher is using.

## What it can do

| Ask Claude... | Skill | Connector tools used |
|---|---|---|
| "I'm out Friday, make sub plans" | `sub-plans` | `get_sub_plan_context` |
| "Who in period 3 is struggling?" | `at-risk-review` | `flag_at_risk_students`, `get_student_profile` |
| "Write report card comments for period 1" | `report-comments` | `get_student_profile`, `class_summary` |
| "Email Liam's dad about his missing work" | `parent-communication` | `get_student_profile` |
| "Plan a reteach lesson on cells" | `lesson-planning` | `class_summary`, `get_roster` |

You can also run a skill directly, e.g. `/teacherplus:sub-plans`.

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
python3 server/teacherplus_server.py      # run the MCP server over stdio
```

Layout:

```
.claude-plugin/plugin.json        plugin manifest
.claude-plugin/marketplace.json   lets this repo be added as a plugin marketplace
.mcp.json                         registers the connector
server/risk.py                    data loading + screening (standard library only)
server/teacherplus_server.py      MCP tools
skills/*/SKILL.md                 task instructions
sample-data/                      fictional class for demos
tests/                            pytest suite
```

## Ideas for next versions

- Direct connectors for Google Classroom, Canvas, PowerSchool or a Google Sheets gradebook instead of CSV export.
- Tracking interventions and check-ins over time, so the screen can show whether support is working.
- IEP progress-monitoring notes and accommodation checklists.

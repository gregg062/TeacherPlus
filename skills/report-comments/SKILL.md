---
name: report-comments
description: Write report card comments, progress report narratives, or end-of-term student summaries from the teacher's gradebook data. Use when a teacher asks for report card comments, progress reports, narrative grades, interim reports, or a summary of how a student or class is doing.
---

# Report card & progress comments

## Individual student comments

1. Ask (once, only if not given): which class, which students (default: everyone in the class), length (default 3–4 sentences / ~60–90 words), tone or school template, and any required elements (e.g. standards, a next step).
2. For each student call `get_student_profile` with the `class_id`. Use the screening's metrics, strengths and flags plus the grades and behavior notes.
3. Write each comment with:
   - a specific strength backed by evidence (an assignment, an improvement, a positive note);
   - one area for growth, phrased as a skill to build, backed by evidence;
   - one concrete next step for the student and, if helpful, for home;
   - for flagged students, an honest but kind statement (e.g. "has 3 missing assignments that are affecting the grade").
4. Vary sentence openings and vocabulary across students — no copy-paste feel. Use the student's first name and correct grade-level reading for families. Mention neither IEP/504/ELL status nor at-risk tiers in the comment.

Output a table (Student | Comment | Word count) that can be pasted into the SIS, and flag any student where data was too thin to write a fair comment.

## Class progress report (for admin, department or PLC)

Call `class_summary` and `flag_at_risk_students`. Report: class average and distribution, assignments that need reteaching (lowest scoring / most missing), number of students by tier (no names unless the teacher asks), and planned interventions. Keep it to one page.

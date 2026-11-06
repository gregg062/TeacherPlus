---
name: at-risk-review
description: Identify and review students who may need extra support, using grades, missing work, attendance and behavior data. Use when a teacher asks who is struggling, who is at risk or failing, who to check in with, for an MTSS/RTI/SST referral list, or for an early-warning or progress-monitoring report.
---

# At-risk review

## 1. Screen

1. Call `flag_at_risk_students` (TeacherPlus connector) for the class the teacher means, or with no `class_id` for all classes. If the teacher mentions school policy thresholds (e.g. "failing is below 65", "chronic absence is 10%"), pass them through as parameters.
2. If `data_status` says sample data is loaded, tell the teacher once that these are fictional students and how to connect their own data (see README).

## 2. Present

Lead with a short summary ("3 students High, 3 Moderate, 1 Watch out of 14"). Then a table sorted by tier:

| Student | Tier | Why flagged | Strengths | Existing supports | Suggested next step |

- **Why flagged** — the reasons from the tool, verbatim or tightened; never invent reasons.
- **Strengths** — always include them; they make the follow-up conversation better.
- **Suggested next step** — concrete and proportionate, e.g.:
  - missing work → 1:1 check-in, missing-work list, set a make-up plan, family contact;
  - failing/declining grades → reteach/small group, check prerequisite skills, offer retake;
  - attendance → contact family to ask what's getting in the way, loop in counselor/attendance office;
  - behavior → private conversation, look for patterns (time, task, peers), counselor;
  - multiple areas or IEP/504/ELL support → bring to the student support team / case manager.
- A sudden drop with "seems withdrawn/tired" style notes may be a wellbeing issue: recommend a check-in with the counselor, not just an academic intervention.

Offer follow-ups: draft parent emails (`parent-communication` skill), a check-in plan, or a referral summary for the student support team (use `get_student_profile` for detail).

## Rules

- These flags are a screening aid built from simple, listed rules. Say "may need support" / "worth a check-in", never "at-risk kid" or labels. Note that the data can be incomplete (e.g. ungraded work, attendance entered late).
- Don't speculate about causes (home life, disability, etc.).
- Keep results with the teacher. Don't put them in documents for substitutes, students or other families.

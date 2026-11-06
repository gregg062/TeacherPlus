---
name: parent-communication
description: Draft emails, letters or call notes to parents and guardians - concerns about grades, missing work, attendance or behavior, positive news, conference invitations, class newsletters. Use when a teacher wants to contact, email, call or write to a family or guardian.
---

# Parent & guardian communication

1. For an individual student, call `get_student_profile` to get the guardian name, email, preferred language and the facts. For a whole-class message, call `list_classes`/`get_roster` only if needed.
2. Structure for concern messages:
   - warm opening and something genuinely positive about the student;
   - the concern, stated with specific facts (dates, assignment names, number of absences) — no judgments or labels;
   - what the teacher is already doing;
   - one or two concrete asks or options (a call time, a missing-work list attached, a make-up deadline);
   - an invitation to share anything that would help, and contact details.
3. Keep it under ~200 words, plain language (around a 6th–8th grade reading level), no jargon or acronyms (spell out "IEP" only if the family already uses it).
4. If `preferred_language` isn't English, offer a translated version alongside the English one and note that a school interpreter should review it for anything sensitive.
5. Positive-news messages should be short and specific — teachers are encouraged to send these too, especially to families of flagged students.

## Rules

- Draft only. Never send. If a mail connector (e.g. Gmail) is available, offer to save the drafts there; the teacher sends them.
- Only mention the one student the message is about. Never mention other students, at-risk tiers, or screening scores.
- Respect notes like custody restrictions in the student record: only address the listed guardian.

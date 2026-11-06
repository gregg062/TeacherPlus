# Educator review tracker

Every skill in TeacherPlus is reviewed and tested by an experienced educator before release. This file tracks that review.

**How to review a skill**

1. Read `skills/<name>/SKILL.md`. Edit it directly, or mark it up in a copy and send it back. Change anything: wording, steps, rules, examples.
2. Add exemplars: excellent real (anonymized) examples of the output can go in `skills/<name>/examples/` and the skill will point to them.
3. Edit the test checklist in `evals/<name>/graders/criteria.md`: what a response *must* do to pass. Add more test cases by copying a folder in `evals/`.
4. Run the tests: `claude plugin eval . --case <name>` (or all: `claude plugin eval .`). Read the outputs in the HTML report and judge them yourself as well.
5. Update the row below: status, reviewer, date.

**Status:** Draft → In review → Approved (✅ = shipped as educator-approved)

## Deliver the lesson

| Skill | Status | Test case | Reviewer | Date | Notes |
|---|---|---|---|---|---|
| `lesson-delivery` | Draft | yes | | | |
| `checks-for-understanding` | Draft | yes | | | |
| `discussion-and-engagement` | Draft | yes | | | |
| `adjust-on-the-fly` | Draft | yes | | | |
| `classroom-management` | Draft | yes | | | |
| `lesson-reflection` | Draft | yes | | | |

## Plan & curriculum

| Skill | Status | Test case | Reviewer | Date | Notes |
|---|---|---|---|---|---|
| `lesson-planning` | Draft | — | | | |
| `unit-planner` | Draft | yes | | | |
| `standards-alignment` | Draft | yes | | | |
| `curriculum-map` | Draft | yes | | | |

## Differentiate

| Skill | Status | Test case | Reviewer | Date | Notes |
|---|---|---|---|---|---|
| `differentiation` | Draft | yes | | | |
| `leveled-texts` | Draft | yes | | | |

## Assess

| Skill | Status | Test case | Reviewer | Date | Notes |
|---|---|---|---|---|---|
| `assessment-builder` | Draft | yes (+ `math-answer-key`) | | | |
| `rubric-builder` | Draft | yes | | | |
| `assessment-review` | Draft | yes | | | |
| `item-analysis` | Draft | yes | | | |

## Coach & lead

| Skill | Status | Test case | Reviewer | Date | Notes |
|---|---|---|---|---|---|
| `lesson-review` | Draft | yes | | | |
| `observation-feedback` | Draft | yes | | | |
| `coaching-cycle` | Draft | yes | | | |
| `department-leadership` | Draft | yes | | | |
| `new-teacher-mentoring` | Draft | yes | | | |

## Communicate & grow

| Skill | Status | Test case | Reviewer | Date | Notes |
|---|---|---|---|---|---|
| `class-communications` | Draft | yes | | | |
| `parent-communication` | Draft | yes | | | |
| `professional-growth` | Draft | yes | | | |

## Uses class data (connector)

| Skill | Status | Test case | Reviewer | Date | Notes |
|---|---|---|---|---|---|
| `sub-plans` | Draft | yes | | | |
| `long-term-sub-plans` | Draft | yes | | | |
| `report-comments` | Draft | — | | | |
| `at-risk-review` | Draft | — | | | |

Skills marked — under *Test case* rely on the class-data connector; tests for them need connector mocks (planned).

## Reference material

| Item | Status | Reviewer | Date | Notes |
|---|---|---|---|---|
| `references/research.md` (evidence base and citations) | Draft | | | Check each summary against the source |
| `references/misconceptions/algebra-1.md` | Draft | | | |
| `references/misconceptions/fractions.md` | Draft | | | |
| `references/misconceptions/middle-school-science.md` | Draft | | | |
| `references/misconceptions/ela.md` | Draft | | | |
| `examples/algebra1-long-term-sub/` (4-week example) | Draft | | | Review as a real sub plan: sequence, pacing, scripts |
| `references/standards/` (bundled standards) | Spot-checked | | | Licensing to confirm before selling; NGSS incomplete |


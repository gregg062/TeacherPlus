# Bundled standards

| File | Standards | Rows | Notes |
|---|---|---|---|
| `ccss-math.csv` | Common Core State Standards for Mathematics, K-12 | 517 | Includes lettered sub-standards (e.g. 8.EE.C.8b) |
| `ccss-ela.csv` | Common Core State Standards for English Language Arts & Literacy | 989 | Includes literacy in history/social studies, science and technical subjects |
| `ngss.csv` | Next Generation Science Standards, performance expectations | 188 | **Incomplete:** the official NGSS has about 208 performance expectations. Some are missing from this source. Treat "not found" as "check nextgenscience.org", not "doesn't exist". |

Look up with `tools/standards.py` (see its header for usage).

## Source

Converted from the compilation at github.com/galacticpolymath/standardX (file `allStandards.csv`), which was built from the official Common Core download (corestandards.org) and the Achievement Standards Network's NGSS data. Spot-checked against the official wording for HSA-REI.C.5, HSA-REI.C.6, HSA-REI.D.12, 8.EE.C.8b, 5.NF.A.1, RL.7.2 and MS-LS1-6.

## Licensing: check before selling the plugin

- **Common Core:** © Copyright 2010. National Governors Association Center for Best Practices and Council of Chief State School Officers. All rights reserved. The Common Core public license allows copying and distributing the standards with this notice; review its terms (corestandards.org/public-license) before commercial distribution.
- **NGSS:** NGSS is a registered trademark, and the standards require a specific attribution and non-endorsement notice. Copy the current wording and use terms from nextgenscience.org (the trademark holder has changed over time, so don't rely on an old notice) before distributing.
- The standardX compilation repository is GPL-3.0 licensed. The standards text belongs to the organizations above, but confirm the compilation's license doesn't affect how you distribute this data. An alternative is to rebuild these files directly from the official downloads.

## State standards

Many states use their own standards, often adapted from these. When a teacher's state differs, skills ask the teacher to paste the relevant standards rather than guessing.

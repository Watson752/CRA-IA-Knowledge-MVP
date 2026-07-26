---
title: Public Audit Case Library
aliases:
  - Audit case index
  - IA case library
note_type: navigation
primary_domain: navigation
domains:
  - governance
  - case
  - audit
domain: internal-audit
status: active
classification: public
content_origin: derived-analysis
authoritative: false
official_source: Internal Audit and Program Evaluation
publisher: Canada Revenue Agency
publication_date: 2026-07-23
as_of_date: 2026-07-23
last_verified: 2026-07-23
source_url: "https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/internal-audit-program-evaluation.html"
source_status: current
owner: MVP-Author
review_status: analytical-draft
approved_for_ai_retrieval: true
related_sources:
  - "[[99-Sources/CRA-Public-Source-Register]]"
  - "[[99-Sources/source-notes/SRC-CRA-IA-PE-Landing]]"
related_cases:
  - "[[08-Cases/Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]]"
  - "[[08-Cases/Internal Audit - Specific Cyber Security Controls]]"
  - "[[08-Cases/Internal Audit - Charities Audit Process]]"
  - "[[08-Cases/Internal Audit - Accounts Receivable National Inventory]]"
  - "[[08-Cases/Internal Audit - Enterprise Fraud Management System]]"
  - "[[08-Cases/Evaluation - Audit Yield]]"
related_processes: []
related_organizations:
  - "[[Audit, Evaluation, and Risk Branch]]"
related_systems: []
related_datasets: []
related_risks: []
related_controls: []
related_procedures: []
related_methods: []
tags:
  - internal-audit
  - case-studies
  - index
---

# Public Audit Case Library

Index of **published CRA internal audit and evaluation reports** selected for this MVP baseline. Each case note is Class **A** at the fact layer, with report URL, date, scope, and findings paraphrased from official HTML/PDF only.

**Reminder:** Reports reflect their **audit or evaluation period**. See [[Public-Sources-Only-Notice]].

Official listing: [Internal Audit and Program Evaluation](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/internal-audit-program-evaluation.html) ([[99-Sources/source-notes/SRC-CRA-IA-PE-Landing]]).

Branch×case matrix (official relationships only): [[Public-Audit-Case-Map]]. Ownership vocabulary: [[Ownership and Assurance Roles]].

## Case studies (MVP baseline)

| Topic | Report date (published) | Case note |
|-------|-------------------------|-----------|
| Oversight, use, and continuous improvement of business intelligence | 2024-06-18 | [[08-Cases/Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] |
| Specific cyber security controls | 2023-03 | [[08-Cases/Internal Audit - Specific Cyber Security Controls]] |
| Charities audit process | 2025-01-14 | [[08-Cases/Internal Audit - Charities Audit Process]] |
| Accounts receivable national inventory (ARNI) | 2026-05-14 | [[08-Cases/Internal Audit - Accounts Receivable National Inventory]] |
| Enterprise fraud management system (EFMS) | 2026-01-23 | [[08-Cases/Internal Audit - Enterprise Fraud Management System]] |
| Evaluation – Audit yield (performance / cash recovery) | 2020-01 | [[08-Cases/Evaluation - Audit Yield]] |

Full case index and journey text: [[08-Cases/README]].

## Demo journeys (study sequences)

Three curated paths for workshops and self-study. Each starts from concept notes named in the case, then reads the case note, then optional related case.

### Demo 1 — Business intelligence governance

**Goal:** Understand BI oversight, horizontal reuse, and continuous improvement from a published IA report.

**Sequence:** [[Business Intelligence]] → [[Business Intelligence Governance]] → [[Data Governance]] → [[Horizontal Collaboration]] → [[Continuous Improvement]] → **[[08-Cases/Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]]** → [[13-Bridge-Notes/How the CRA Business Intelligence Audit Supports the Knowledge-Vault Concept]] (derived).

**Pair with learning path:** [[12-Learning-Paths/Learning Path - Software Professional]] or [[12-Learning-Paths/Learning Path - Data and Statistics Professional]].

### Demo 2 — Cyber and fraud technology controls

**Goal:** Read subset-of-controls cyber assurance and employee-fraud monitoring technology in public reports (including protected-content limits).

**Sequence:** [[Cyber and Data Security]] → [[Cybersecurity]] → [[Defence in Depth]] → **[[08-Cases/Internal Audit - Specific Cyber Security Controls]]** → **[[08-Cases/Internal Audit - Enterprise Fraud Management System]]**.

**Pair with learning path:** [[12-Learning-Paths/Learning Path - Software Professional]].

### Demo 3 — Reporting, statistics, and outcomes

**Goal:** Compare fiscal impact, cash recovery, and operational metrics; understand matching and snapshot limitations.

**Sequence:** [[Performance Reporting]] → [[Evidence Reliability]] → [[Population Completeness]] → [[Missing Data]] → **[[08-Cases/Evaluation - Audit Yield]]** → **[[08-Cases/Internal Audit - Accounts Receivable National Inventory]]** → [[How Statistical Limitations Affect Audit Conclusions]] → [[How Missing Data Limits Audit Assurance]].

**Note:** The prioritized IA report *Internal Audit – Tax and Benefits Operations Results Information* was referenced as underway in **2018** public material but **no final published report was located on Canada.ca** during vault research (**2026-07-23**). Journey 3 uses **Evaluation – Audit Yield** as the public reporting/results-information demonstration case.

**Pair with learning path:** [[12-Learning-Paths/Learning Path - Data and Statistics Professional]] or [[12-Learning-Paths/Learning Path - Auditor]].

## Thematic grouping (quick reference)

- **Data and analytics governance:** BI case  
- **Security and IT controls:** Cyber case; EFMS case  
- **Compliance process:** Charities audit process  
- **Financial operations / inventory:** ARNI case  
- **Integrated compliance outcomes:** Evaluation – Audit Yield  
- **Missing / incomplete data and assurance limits:** Charities, ARNI, EFMS, Audit Yield, BI (see [[Missing Data]], [[How Missing Data Limits Audit Assurance]])  

Deeper technology context: [[CRA-Technology-and-Risk-Map]]. Aggregate statistics context: [[CRA-Data-and-Statistics-Map]].

## Synthetic demo (non-CRA scenario)

[[14-Synthetic-Demos/Synthetic Digital Decision Controls Review]] — Class D exercise; not grounded in a published CRA audit report.

## Adding cases

When adding a new published report:

1. Add a row to [[99-Sources/CRA-Public-Source-Register]] and create `99-Sources/source-notes/SRC-….md`  
2. Create `08-Cases/<Note-Name>.md` with Class A frontmatter  
3. Link here, in [[08-Cases/README]], and from domain maps as appropriate  
4. Log discovery in [[RESEARCH_LOG]]  

Return to [[Home]].

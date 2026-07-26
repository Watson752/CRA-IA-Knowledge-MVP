---
title: "Test-02: Multi-System Management Reporting (Post-Fix)"
note_type: testing
primary_domain: testing
domains:
  - testing
  - organization
  - audit
  - software
  - data
classification: public
content_origin: derived-analysis
authoritative: false
official_source: false
as_of_date: 2026-07-26
last_verified: 2026-07-26
source_status: diagnostic
review_status: analytical-draft
approved_for_ai_retrieval: false
tags:
  - testing
  - post-fix
  - integrated
  - data-pipeline
---

# Test-02: Multi-System Management Reporting (Post-Fix)

## Question

A management report is assembled from several source systems using APIs, batch processes and transformations. How should Internal Audit determine whether management can rely on the report?

## Post-fix answer (vault-supported)

[[Management Review]] is first-class. [[Data Pipeline and Reporting Map]] starts at [[Business Process Owner]] and includes presentation → Management Review → Evidence Reliability → Audit Conclusion. [[How Data Pipelines Affect Evidence Reliability]] and [[How Data Quality Affects Management Reporting]] connect pipeline quality to reliance. Ownership reporting chain documented in [[Ownership and Assurance Roles]]. Totals ≠ accuracy and SGE ≠ reliable remain explicit. Audit Yield / ARNI / EFMS / BI remain bounded precedents.

## Diagnostic checks

| Check | Post-fix finding |
|---|---|
| Start only at final report? | **No** — source-to-report path with BPO start |
| Transformations, rejects, exclusions? | **Yes** |
| Business vs technical ownership separated? | **Yes** — reporting chain + BI case pattern |
| Reproducibility ≠ validity? | **Yes** |
| Historical cases interpreted appropriately? | **Yes** |
| Management Review path complete? | **Yes** — dedicated note + map |

## Score

| Criterion | Baseline | Post-fix | Rationale |
|---|---:|---:|---|
| Governance and ownership integration | 1 | **2** | Management Review + BPO reporting chain + pipeline map ownership start |
| End-to-end technical reasoning | 2 | **2** | Prior pipeline stage notes retained |
| Control and audit-procedure coverage | 2 | **2** | Management Review OE language; recon/rejects retained |
| Statistical and evidence reasoning | 2 | **2** | Completeness≠accuracy; reproducibility≠validity; DQ bridges |
| Public-case grounding | 2 | **2** | Bounded case use retained |
| **Total** | **9** | **10** | |

## Remaining issue

Deep reject-aging / mapping-reperformance workbooks remain teaching-level stubs.

## Test metadata

- Test ID: Test-02-Multi-System-Management-Reporting
- Suite: Integrated Post-Fix regression
- Output path: `16-Testing/Integrated/Post-Fix/Test-02-Multi-System-Management-Reporting.md`
- Vault substantive notes modified during this test: **none**
- Baseline reference: `16-Testing/Integrated/Baseline/Test-02-Multi-System-Management-Reporting.md`

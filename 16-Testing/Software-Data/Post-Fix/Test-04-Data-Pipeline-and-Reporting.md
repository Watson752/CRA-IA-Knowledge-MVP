---
title: "Test-04: Data Pipeline and Management Reporting Reliability (Post-Fix)"
note_type: testing
primary_domain: software-data
domains:
  - software
  - data
  - audit
  - testing
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
  - software-data
  - data-pipeline
---

# Test-04: Data Pipeline and Management Reporting Reliability (Post-Fix)

## Question

A management report is generated from several source systems through a data pipeline. How should an auditor assess whether the report can be relied upon?

## Post-fix answer (vault-supported)

[[Data Pipeline]] and [[Data Pipeline and Reporting Map]] teach source → extract ([[API Integration]] / [[Batch Processing]]) → [[Data Transformation]] / [[Field Mapping]] → [[Rejected Records]] → [[Data Reconciliation]] → [[Management Reporting]] → reliance. [[Data Lineage]], [[Reference Data]], and [[Assessment Cut-Off Date]] are first-class. [[Data Accuracy]], [[Population Completeness]], [[Record Uniqueness]], and [[Data Timeliness]] remain distinct. Totals reconciliation ≠ field accuracy ([[Data Reconciliation]], [[System-Generated Evidence]]).

**Audit Yield** remains the primary multi-source reliance case; ARNI/EFMS/Charities remain secondary completeness examples.

## Diagnostic checks

| Check | Post-fix finding |
|---|---|
| Focus only on final report? | **No** |
| Transformations and failed records? | **Yes** — transformation + Rejected Records |
| Accuracy ≠ completeness? | **Yes** — dedicated dimension notes |
| Change management ↔ pipeline? | **Yes** — Change Management linked on pipeline/SGE |
| Report-period cut-offs? | **Yes** — Assessment Cut-Off Date |

## Score

| Criterion | Baseline | Post-fix | Rationale |
|---|---:|---:|---|
| End-to-end data-flow understanding | 1 | **2** | First-class pipeline stage notes + map |
| Data-quality and completeness analysis | 2 | **2** | Dimensions split out; totals≠accuracy restated |
| Control and procedure coverage | 1 | **2** | Reconciliation, rejects, mapping, lineage notes |
| Evidence-reliance reasoning | 2 | **2** | SGE + Management Reporting + lineage |
| Public-case application | 2 | **2** | Audit Yield still primary bounded case |
| **Total** | **8** | **10** | |

## Remaining issue

Stage notes are Class C stubs—not CRA ETL runbooks or tool inventories. Full procedure workbooks (reject aging, mapping reperformance) remain teaching-level.

## Test metadata

- Output: `16-Testing/Software-Data/Post-Fix/Test-04-Data-Pipeline-and-Reporting.md`
- Vault notes modified during this test: **none**

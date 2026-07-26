---
title: "Data Pipeline and Reporting Map"
aliases:
  - "Pipeline Map"
  - "Reporting Reliance Map"
note_type: navigation
primary_domain: navigation
domains:
  - software
  - data
  - audit
  - control
  - navigation
classification: public
content_origin: derived-analysis
authoritative: false
official_source: false
as_of_date: 2026-07-26
last_verified: 2026-07-26
source_status: current
review_status: analytical-draft
approved_for_ai_retrieval: false
tags:
  - MOC
  - software-data
  - onboarding
---

# Data Pipeline and Reporting Map

Derived map for multi-source report reliance.

## Path

```text
[[Business Process Owner]] / report owner
→ [[Source System Data]]
→ [[Data Pipeline]] ([[API Integration]] / [[Batch Processing]])
→ [[Data Transformation]] / [[Field Mapping]]
→ [[Rejected Records]] / [[Record Uniqueness]] checks
→ [[Data Reconciliation]]
→ Reporting dataset / presentation
→ [[Management Reporting]] / report logic
→ [[Management Review]]
→ [[Evidence Reliability]]
→ [[Audit Conclusion]]
```

Related: [[Statistics and Evidence Map]] · [[Reproducible Analytics Map]] · [[Population Completeness]] · [[Selection Bias]] · [[How Data Pipelines Affect Evidence Reliability]] · [[How Data Quality Affects Management Reporting]]

## Quality dimensions (keep distinct)

[[Data Accuracy]] · [[Population Completeness]] · [[Record Uniqueness]] · [[Data Timeliness]] · [[Data Quality]]

**Totals reconciliation ≠ field accuracy** ([[Data Reconciliation]]).

## Cut-off / lineage

[[Assessment Cut-Off Date]] · [[Data Lineage]] · [[Reference Data]] · [[Change Management]]

## Cases (bounded)

- [[Evaluation - Audit Yield]] — multi-system matching / measure reliance
- [[Internal Audit - Accounts Receivable National Inventory]] — metric completeness/attribution
- [[Internal Audit - Enterprise Fraud Management System]] — load/re-ingestion completeness

## Related

- [[CRA-Data-and-Statistics-Map]] · [[Evidence and Conclusion Map]] · [[Software and Controls Map]] · [[Data-Quality Engagement Path]] · [[Integrated Knowledge Map]]

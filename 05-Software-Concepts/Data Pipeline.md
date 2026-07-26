---
title: "Data Pipeline"
aliases:
  - "ETL Pipeline"
  - "ELT Pipeline"
  - "Data Integration Pipeline"
note_type: software-concept
primary_domain: software-data
domains:
  - software
  - data
  - audit
classification: public
content_origin: general-professional-knowledge
authoritative: false
official_source: false
as_of_date: 2026-07-26
last_verified: 2026-07-26
source_status: current
review_status: analytical-draft
approved_for_ai_retrieval: false
related_cases: []
tags:
  - pipeline
  - onboarding
---

A **data pipeline** moves and transforms data from [[Source System Data|source systems]] through extraction, transformation, integration, and load into reporting datasets. Teaching model:

```text
Source systems → extraction → transformation → integration → reconciliation
→ reporting dataset → report logic → management review → audit reliance
```

Balanced stage totals do **not** prove every record/field is accurate ([[Data Quality]], [[Data Reconciliation]]). Subject to [[Change Management]] and access control on jobs/datasets.

## Related notes

- [[Source System Data]]
- [[API Integration]]
- [[Batch Processing]]
- [[Data Transformation]]
- [[Field Mapping]]
- [[Rejected Records]]
- [[Data Lineage]]
- [[Data Reconciliation]]
- [[Management Reporting]]
- [[Assessment Cut-Off Date]]
- [[System-Generated Evidence]]
- [[Evaluation - Audit Yield]]

## Sources

General professional knowledge.

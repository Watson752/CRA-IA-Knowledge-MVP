---
title: "Data Quality and Bias Map"
aliases: []
note_type: navigation
primary_domain: navigation
domains:
  - statistics
  - data
  - audit
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
  - statistics-analytics
  - onboarding
---

# Data Quality and Bias Map

## Quality dimensions

[[Data Quality]] · [[Data Accuracy]] · [[Population Completeness]] · [[Record Uniqueness]] · [[Data Timeliness]] · [[Missing Data]]

## Missingness forms

[[Missing Records]] · [[Missing Values]] · [[Systematic Exclusion]] · [[Non-Response or Unavailable Evidence]] · [[Data Suppression]]

**Not all missing data creates bias** — assess random vs systematic ([[Missing Data]]).

## Bias

```text
[[Data Pipeline]] filters / rejects
→ [[Missing Data]] / [[Systematic Exclusion]]
→ [[Selection Bias]] or [[Survivorship Bias]]
→ weaker [[Evidence Reliability]]
→ narrower [[Audit Conclusion]]
```

Mitigations: [[Data Reconciliation]] · [[Sensitivity Analysis]] · document exclusions · alternative evidence

Bridges: [[How Missing Data Limits Audit Assurance]] · [[How Statistical Bias Can Mislead an Audit]] · [[How Data Quality Affects Management Reporting]]

Path: [[Data-Quality Engagement Path]] · [[Integrated Knowledge Map]]

[[Statistics and Evidence Map]] · [[Data and Statistics Onboarding Path]]

---
title: "Reproducibility"
aliases: 
  - "Analytical Reproducibility"
  - "Repeatability"
note_type: statistical-method
primary_domain: statistics-analytics
domains:
  - statistics
  - audit
  - data
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
  - analytics
  - onboarding
---

**Reproducibility** means another analyst can obtain the **same result** from the **same inputs and method**. Necessary for defensible analytics—not sufficient for correctness ([[Analytical Validity]]).

Document for audit analytics workpapers:

- analytical objective (tied to [[Audit Objective]] / [[Criteria]]);
- source data ([[Source System Data]], [[Data Lineage]]);
- extraction date / [[Assessment Cut-Off Date]];
- query or code (version-controlled where possible);
- parameters;
- transformation steps ([[Data Transformation]]);
- [[Inclusion and Exclusion Rules]];
- software/package versions where relevant;
- data dictionary / field definitions;
- exception handling ([[Rejected Records]]);
- retained outputs;
- review or independent [[Reperformance]].

A reproducible query on an incomplete [[Retrieved Population]] or with wrong join logic is still **invalid** for the engagement question.

## Related notes

- [[Analytical Validity]]
- [[Analytics]]
- [[Methodology]]
- [[Evidence Reliability]]
- [[Data Lineage]]
- [[Full-Population Analysis]]
- [[Reperformance]]
- [[Outdated Analytics]]
- [[Reproducible Analytics Map]]

## Sources

General professional knowledge; audit analytics documentation practice.

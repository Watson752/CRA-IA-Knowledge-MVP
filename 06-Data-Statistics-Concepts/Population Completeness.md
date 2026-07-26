---
title: Population Completeness
aliases: []
note_type: statistical-method
primary_domain: statistics-analytics
domains:
  - statistics
  - data
  - audit
  - risk
domain: data-statistics
status: active
classification: public
content_origin: general-professional-knowledge
authoritative: false
official_source: null
publisher: null
publication_date: null
as_of_date: 2026-07-23
last_verified: 2026-07-23
source_url: null
source_status: unknown
owner: MVP-Author
review_status: unreviewed
approved_for_ai_retrieval: false
related_sources: []
related_cases: []
related_processes: []
related_organizations: []
related_systems: []
related_datasets: []
related_risks: []
related_controls: []
related_procedures: []
related_methods: []
tags: []
---

**Population completeness** means the audited or analyzed population includes all records that should be in scope— no systematic omissions, truncation, or filter errors. Incomplete populations inflate [[Sampling Risk]] and can invalidate extrapolations from samples to totals.

[[Missing Data]] often produces those gaps: omitted segments, truncated extracts, missing time periods, or entire records never loaded. Completeness checks compare source counts, control totals, hash totals, or independent registers. Cut-off errors at an [[Assessment Cut-Off Date]] are a frequent cause of gaps between financial and operational data.

**Access and pipeline examples:** [[User Access Dataset]] extracts must include nested groups, [[Service Accounts]], and [[Dormant Accounts]] still enabled; [[Data Pipeline]] filters/rejects can silently drop segments. Completeness is distinct from [[Data Accuracy]].

In statistical agencies and large programs, completeness interacts with coverage studies and late-reported transactions. Auditors state when conclusions apply only to retrieved subsets. Link to [[Data Quality]] and [[Evidence Reliability]] when audit procedures depend on full population analytics.

## Related notes

- [[Missing Data]]
- [[Data Quality]]
- [[Data Accuracy]]
- [[Sampling Risk]]
- [[Assessment Cut-Off Date]]
- [[Evidence Reliability]]
- [[Structured Data]]
- [[Analytics]]
- [[User Access Dataset]]
- [[Access Review Testing]]
- [[Data Pipeline]]
- [[Rejected Records]]
- [[Data Reconciliation]]

## Sources

General professional knowledge; audit and statistical sampling literature. See source register when linked.

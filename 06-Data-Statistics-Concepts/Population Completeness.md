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

**Population completeness** means the [[Retrieved Population]] includes all items that belong in the [[Intended Population]] for the [[Audit Objective]], [[Scope]], and [[Audit Period]]—no systematic omissions, truncation, or filter errors ([[Inclusion and Exclusion Rules]]). Incomplete populations inflate [[Sampling Risk]] and can invalidate [[Statistical Extrapolation]].

[[Missing Data]] often produces those gaps: [[Missing Records]], omitted segments ([[Systematic Exclusion]]), truncated extracts, missing time periods, or entire records never loaded. Completeness checks compare source counts, control totals, hash totals, or independent registers ([[Data Reconciliation]]). Cut-off errors at an [[Assessment Cut-Off Date]] are a frequent cause of gaps between financial and operational data.

**Access and pipeline examples:** [[User Access Dataset]] extracts must include nested groups, [[Service Accounts]], and [[Dormant Accounts]] still enabled; analysing only active/successful items can create [[Survivorship Bias]]. [[Data Pipeline]] filters/rejects can silently drop segments. Completeness is distinct from [[Data Accuracy]].

In statistical agencies and large programs, completeness interacts with coverage studies and late-reported transactions. Auditors state when conclusions apply only to retrieved subsets—never treat the extract as the intended universe without testing. Incomplete populations weaken [[Evidence Reliability]] and force narrower [[Audit Conclusion]]s. Validate the [[Sampling Frame]] before [[Sample Selection]].

## Related notes

- [[Audit Population]]
- [[Intended Population]]
- [[Retrieved Population]]
- [[Sampling Frame]]
- [[Audit Objective]]
- [[Scope]]
- [[Sample Selection]]
- [[Missing Data]]
- [[Missing Records]]
- [[Data Quality]]
- [[Data Accuracy]]
- [[Sampling Risk]]
- [[Assessment Cut-Off Date]]
- [[Evidence Reliability]]
- [[Survivorship Bias]]
- [[Selection Bias]]
- [[Structured Data]]
- [[Analytics]]
- [[User Access Dataset]]
- [[Access Review Testing]]
- [[Data Pipeline]]
- [[Rejected Records]]
- [[Data Reconciliation]]
- [[Audit Conclusion]]
- [[Population and Sampling Map]]

## Sources

General professional knowledge; audit and statistical sampling literature. See source register when linked.

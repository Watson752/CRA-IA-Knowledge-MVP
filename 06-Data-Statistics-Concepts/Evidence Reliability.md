---
title: Evidence Reliability
aliases: []
note_type: data-concept
primary_domain: software-data
domains:
  - software
  - data
  - audit
  - statistics
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

**Evidence reliability** is the extent to which information supports audit conclusions without material misstatement or ambiguity. Reliability increases with independent sources, system integrity, documented lineage, and corroboration; it decreases with manual manipulation, weak access controls, or unknown extraction logic.

For digital [[Evidence]], auditors consider who can alter data, whether logs are protected, and whether analytics scripts are version-controlled ([[Reproducibility]]). [[Data Quality]] and [[Population Completeness]] directly affect reliability; [[Missing Data]] (absent records, fields, periods, or supporting workpapers) is a common reason reliability falls short of the conclusion being drawn. [[Selection Bias]] and incomplete extracts can make results look precise yet unreliable for the [[Intended Population]].

Reliability is judged relative to the [[Audit Objective]] and [[Criteria]]— not absolute truth. A reproducible analysis can still be invalid ([[Analytical Validity]]). [[How Statistical Limitations Affect Audit Conclusions]] extends reliability to published statistics and estimates and to [[Audit Conclusion]] strength.

Distinguish reliability from relevance: reliable but off-scope data still fails appropriateness tests.

## Related notes

- [[Evidence]]
- [[Data Quality]]
- [[Population Completeness]]
- [[Missing Data]]
- [[Structured Data]]
- [[IT Controls]]
- [[How Statistical Limitations Affect Audit Conclusions]]
- [[System-Generated Evidence]]
- [[Evidence Hierarchy]]
- [[Audit Logging]]
- [[Evidence and Conclusion Map]]
- [[Outlier Analysis]]
- [[Full-Population Analysis]]
- [[Statistics and Evidence Map]]

## Sources

General professional knowledge; IIA evidence standards; ISACA audit data analytics guidance. See source register when linked.

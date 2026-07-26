---
title: Data Suppression
aliases:
  - Statistical Disclosure Control - Suppression
note_type: statistical-method
primary_domain: statistics-analytics
domains:
  - statistics
  - data
  - audit
  - control
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

**Data suppression** withholds or masks cell values in published tables to reduce re-identification risk or protect confidential business information. Suppression rules often trigger when counts are below thresholds or when dominant contributors could be inferred. It is a standard statistical disclosure control technique alongside [[Rounding]] and aggregation.

Suppression affects [[Comparability Across Editions]] and may limit [[Small-Cell Analysis]]. Users cannot assume missing cells equal zero. Auditors working with public statistics must read methodological notes and not reconstruct suppressed values from other sources inappropriately.

Internal audit datasets may also redact fields for privacy; suppression differs from [[Data Quality]] errors but similarly constrains analysis. Treat suppressed or redacted cells as a distinct form of [[Missing Data]]—intentional and disclosed—not as accidental incompleteness.

Understanding suppression is essential for [[How Statistical Limitations Affect Audit Conclusions]] when audits reference public aggregate data.

## Related notes

- [[Rounding]]
- [[Small-Cell Analysis]]
- [[Comparability Across Editions]]
- [[How Statistical Limitations Affect Audit Conclusions]]
- [[Data Quality]]
- [[Missing Data]]

## Sources

General professional knowledge; statistical disclosure control handbooks (national statistics offices). See source register when linked.

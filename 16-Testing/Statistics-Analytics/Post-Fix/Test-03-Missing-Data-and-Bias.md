---
title: "Test-03: Missing Data and Bias (Post-Fix)"
note_type: testing
primary_domain: statistics-analytics
domains:
  - statistics
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
  - statistics-analytics
  - missing-data
  - bias
---
# Test-03: Missing Data and Bias (Post-Fix)

## Question

How can missing data, selection bias and survivorship bias distort an audit analysis?

## Post-fix answer (vault-supported)

[[Missing Data]] taxonomy remains strong; [[Missing Records]], [[Missing Values]], [[Systematic Exclusion]], and [[Non-Response or Unavailable Evidence]] are first-class. [[Selection Bias]] is distinct from sampling variability ([[Sampling Risk]]). [[Survivorship Bias]] covers completed/active/successful-only views. Not all missingness creates bias. Mitigations include [[Data Reconciliation]] and [[Sensitivity Analysis]]. Path: incomplete extract → non-representative set → biased rate → weaker [[Evidence Reliability]] / [[Audit Conclusion]]. Cases still label official vs derived interpretation; bias titles not retrofitted onto Class A findings.

## Diagnostic checks

| Check | Post-fix finding |
|---|---|
| Assume all missingness random? | **No** |
| Confuse selection bias with sampling variability? | **No** — separated in Sampling Risk + Selection Bias |
| Recognise excluded failed/closed cases? | **Yes** — Survivorship Bias + dormant/rejects links |
| Direction of distortion? | **Improved** — bias notes + sensitivity analysis |
| Derived interpretations labelled? | **Yes** — case practice unchanged |

## Score

| Criterion | Baseline | Post-fix | Rationale |
|---|---:|---:|---|
| Missingness distinction | 2 | **2** | Retained; first-class record/value notes |
| Selection-bias clarity | 1 | **2** | Dedicated note + sampling-risk split |
| Survivorship-bias clarity | 0 | **2** | Dedicated Survivorship Bias note |
| Audit-conclusion connection | 2 | **2** | Retained + Audit Conclusion |
| Source and case accuracy | 2 | **2** | No unsupported causal retrofit on cases |
| **Total** | **7** | **10** | |

## Remaining issue

Case notes intentionally not titled as “selection/survivorship bias” findings (SA-D5). Directional up/down rate bias examples remain light outside Sensitivity Analysis.

## Test metadata

- Output: `16-Testing/Statistics-Analytics/Post-Fix/Test-03-Missing-Data-and-Bias.md`
- Vault notes modified during this test: **none**

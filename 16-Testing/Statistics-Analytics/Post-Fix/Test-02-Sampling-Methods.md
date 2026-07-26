---
title: "Test-02: Sampling Methods (Post-Fix)"
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
  - sampling
---
# Test-02: Sampling Methods (Post-Fix)

## Question

What is the difference between random sampling, stratified sampling and judgmental sampling, and when might each be appropriate in an audit?

## Post-fix answer (vault-supported)

[[Random Sampling]], [[Stratified Sampling]], and [[Judgmental Sampling]] are distinct. [[Sample Selection]] compares selection basis, [[Representativeness]], and whether [[Statistical Extrapolation]] is supported. Stratification samples **within** strata (not merely picking high-risk items). Judgmental/risk-based picks normally **do not** support population-wide extrapolation ([[Sampling Risk]]). No universal sample-size rule; [[Materiality]] / [[Risk Assessment]] guide focus. [[Evaluation - Audit Yield]] remains the stratified public example (**95%** segment-bound).

## Diagnostic checks

| Check | Post-fix finding |
|---|---|
| Stratification = only high-risk picks? | **No** — within-stratum sampling stated |
| Judgmental presented as statistically representative? | **No** — explicit non-extrapolation |
| Random valid without complete population? | **No** — frame completeness required |
| Materiality and risk linked? | **Yes** — Materiality + Risk-Based Selection |
| Unsupported sample-size claims? | **Avoided** |

## Score

| Criterion | Baseline | Post-fix | Rationale |
|---|---:|---:|---|
| Method distinction | 1 | **2** | Three method notes + comparison table |
| Representativeness and extrapolation accuracy | 1 | **2** | Extrapolation note; judgmental limit explicit |
| Audit-use explanation | 1 | **2** | Sample Selection when-to-use / extrapolation column |
| Sampling-risk coverage | 1 | **2** | Variability vs selection bias separated |
| Source and case grounding | 1 | **1** | Still primarily Audit Yield for stratified; no dedicated public random/judgmental cases |
| **Total** | **5** | **9** | |

## Remaining issue

No public CRA case that teaches pure random-only or judgmental sampling as methods. Notes remain thin Class C stubs. No [[Substantive Testing]] note (SA-D3).

## Test metadata

- Output: `16-Testing/Statistics-Analytics/Post-Fix/Test-02-Sampling-Methods.md`
- Vault notes modified during this test: **none**

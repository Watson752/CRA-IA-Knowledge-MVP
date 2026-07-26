---
title: "Test-05: Statistical vs Operational Significance (Post-Fix)"
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
  - significance
---
# Test-05: Statistical vs Operational Significance (Post-Fix)

## Question

What is the difference between statistical significance and operational significance, and why does the distinction matter in Internal Audit?

## Post-fix answer (vault-supported)

[[Statistical Significance]] (detectability under a model) is distinct from [[Operational Significance]] (practical importance to outcomes, compliance, exposure, etc.). [[Materiality]], [[Effect Size]], [[Confidence Interval]], and [[Rare High-Impact Events]] support triage. No universal significance level. Large-N tiny effects may be detectable yet immaterial; non-significance ≠ no risk. [[Evidence Evaluation]] / [[Finding]] clarify report “significance” ≠ statistical test result. [[Professional Judgment]] + [[Criteria]] govern elevation. [[Statistical Interpretation Map]] navigates the cluster.

## Diagnostic checks

| Check | Post-fix finding |
|---|---|
| Statistical significance = proof of importance? | **No** — explicitly separated |
| Non-significance = proof of no issue? | **No** — explicitly forbidden |
| Rare high-impact recognised? | **Yes** — Rare High-Impact Events |
| Criteria and professional judgment connected? | **Yes** |
| Synthetic examples labelled? | **N/A in concept notes**; baseline synthetics remain labelled |

## Score

| Criterion | Baseline | Post-fix | Rationale |
|---|---:|---:|---|
| Conceptual distinction | 0 | **2** | Both notes + interpretation map |
| Materiality and risk connection | 1 | **2** | Materiality + Operational Significance + Risk Assessment links |
| Confidence and uncertainty discussion | 1 | **2** | Confidence Interval + effect size + prior limitation notes |
| Misuse prevention | 1 | **2** | Explicit sig≠important / non-sig≠safe / no universal α |
| Audit applicability | 1 | **2** | Finding / Evidence Evaluation / Professional Judgment wired |
| **Total** | **4** | **10** | |

## Remaining issue

No numeric worked examples inside concept notes (intentionally—no invented CRA thresholds). CI note is conceptual, not a calculation workbook.

## Test metadata

- Output: `16-Testing/Statistics-Analytics/Post-Fix/Test-05-Statistical-vs-Operational-Significance.md`
- Vault notes modified during this test: **none**

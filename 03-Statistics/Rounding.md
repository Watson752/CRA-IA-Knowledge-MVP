---
title: Rounding
aliases:
  - CRA statistical rounding
  - Rounding in T1 statistics
note_type: statistical-method
primary_domain: statistics-analytics
domains:
  - statistics
  - data
  - audit
  - control
  - business
domain: statistics
status: active
classification: public
content_origin: official-public-source
authoritative: true
official_source: Canada Revenue Agency
publisher: Government of Canada
publication_date: 2025
as_of_date: 2026-07-23
last_verified: 2026-07-23
source_url: "https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/income-statistics-gst-hst-statistics/t1-final-statistics/2023-tax-year.html"
source_status: current
owner: MVP-Author
review_status: source-verified
approved_for_ai_retrieval: true
related_sources:
  - "[[99-Sources/source-notes/SRC-CRA-T1-Stats-2023]]"
related_cases: []
related_processes: []
related_organizations:
  - "[[Canada Revenue Agency]]"
related_systems: []
related_datasets: []
related_risks: []
related_controls: []
related_procedures: []
related_methods: []
tags:
  - rounding
  - statistics
  - data-quality
---

# Rounding

CRA applies explicit **rounding rules** in **Individual Income Tax Return Statistics** as part of [[Public Data Confidentiality Procedures]].

## Rules (2023 tax year edition)

Official explanatory notes specify:

| Measure | Rounding rule |
|---------|----------------|
| **Counts** | Nearest multiple of **10** (example: 104 → 100; 105 → 110) |
| **Dollar amounts** (Tables 1–5) | Nearest **thousand** |

**Totals may not add** due to rounding or [[Data Suppression]].

## Audit and analytics implications

- Reconciliation of published totals to micro-level calculations will show **immaterial differences** even without suppression.
- Rate calculations (for example dollars per return) inherit rounding error; small denominators amplify apparent variance ([[Small-Cell Analysis]]).
- Rounding is distinct from [[Assessment Cut-Off Date]] effects but combines with them when comparing editions ([[Comparability Across Editions]]).

## Sources

- [Individual Income Tax Return Statistics (2023 tax year) — Confidentiality procedures](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/income-statistics-gst-hst-statistics/t1-final-statistics/2023-tax-year.html)
- [[Individual Income Tax Return Statistics]]

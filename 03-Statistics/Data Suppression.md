---
title: Data Suppression
aliases:
  - Statistical suppression CRA T1
  - Confidentiality suppression
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
  - suppression
  - confidentiality
  - statistics
---

# Data Suppression

In CRA **Individual Income Tax Return Statistics**, **data are suppressed where warranted** to protect tax filer information under [[Public Data Confidentiality Procedures]].

## How suppression appears in tables

- A **zero [0]** in a cell means the value is **suppressed for confidentiality**, not necessarily a true zero count or amount.
- Suppressed information **includes valid zeroes** (a filer count or dollar amount that is genuinely zero may still be withheld when disclosure rules require).
- **Totals may not equal** the sum of displayed detail because of suppression (and [[Rounding]]).

## Implications for analysis

Suppression creates **structural missingness** in public tables. Analysts cannot recover suppressed cells from published CSV/PDF outputs. Joins to audit samples by fine-grained dimensions (small provinces, rare income ranges, intersection of age and source of income) often align with suppressed cells—see [[Small-Cell Analysis]].

For a general profession-wide treatment of suppression and disclosure control, see also references in [[06-Data-Statistics-Concepts/Analytics]] when a dedicated concept note is added under `06-Data-Statistics-Concepts/`.

## Linkage in the vault

[[Individual Income Tax Return Statistics]] → constrained by [[Data Suppression]] (with [[Rounding]], [[Assessment Cut-Off Date]], [[Comparability Across Editions]]) → affects [[Small-Cell Analysis]] → relevant to [[How Statistical Limitations Affect Audit Conclusions]].

## Sources

- [Individual Income Tax Return Statistics (2023 tax year) — Confidentiality procedures](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/income-statistics-gst-hst-statistics/t1-final-statistics/2023-tax-year.html)
- [[Public Data Confidentiality Procedures]]

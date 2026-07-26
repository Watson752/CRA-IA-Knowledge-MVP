---
title: Comparability Across Editions
aliases:
  - Edition comparability T1 stats
  - Extraction timeframe comparison
note_type: statistical-method
primary_domain: statistics-analytics
domains:
  - statistics
  - data
  - audit
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
  - comparability
  - time-series
  - statistics
---

# Comparability Across Editions

**Individual Income Tax Return Statistics** are published as **editions** (publication year) tied to a **tax year**. Trend analysis requires aligning tax year, cut-off date, classifications, and table geography rules.

## Extraction time frame changes

Starting with the **2025 edition (2023 tax year)**, CRA adopted an **earlier extraction cut-off** (**November 30, 2024** versus **June 30, 2025** referenced for the prior approach) to improve **timeliness**. Official guidance: when comparing this edition with **previous editions**, **differences in extraction time frames** should be taken into consideration.

Effects include:

- Lower counts or amounts versus a later cut-off for the **same tax year** when reassessments and late processing continue after November 30.
- Breaks in time series if earlier editions used a longer post-tax-year processing window.

## Other comparability factors

| Factor | Consideration |
|--------|----------------|
| Tax year vs edition year | Landing page lists edition year and tax year (for example 2026 edition for 2024 tax year) |
| Geography | Taxation (Table 1) vs residence (Tables 2–5) — [[Tax Statistics by Area]] |
| Income grouping | Range boundaries and line item definitions — [[Tax Statistics by Tax Bracket]] |
| Disclosure | [[Data Suppression]] and [[Rounding]] rules may be stable but still distort level changes in small cells |
| Revision | [[Statistical Revision]] may update an edition |

## Distinction from departmental operational metrics

Fiscal-year **actual** highlights (for example [[Electronic Filing Statistics]] for **2024–25**) are not directly comparable to tax-year assessment tables without explicit mapping.

## Sources

- [Individual Income Tax Return Statistics (2023 tax year)](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/income-statistics-gst-hst-statistics/t1-final-statistics/2023-tax-year.html)
- [Individual Income Tax Return Statistics (landing)](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/income-statistics-gst-hst-statistics/t1-final-statistics.html)
- [[Individual Income Tax Return Statistics]]

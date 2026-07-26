---
title: Tax Statistics by Tax Bracket
aliases:
  - Income range statistics
  - T1 income ranges
note_type: dataset
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
  - income-ranges
  - t1
  - statistics
---

# Tax Statistics by Tax Bracket

In CRA’s **Individual Income Tax Return Statistics**, distributional tables group filers by **income ranges** based on **total income assessed** (T1 line 15000), not by statutory **marginal tax rate brackets**. This note uses the vault title “tax bracket” as a colloquial entry point; the official classification is **income ranges**.

## Table 2 — Tax return line items by income ranges

**Table 2** presents tax return line items cross-tabulated by income ranges. The table begins with total returns, then ranges from **$4,999 and under** through **$250,000 and over**. National and provincial/territorial tables use **province or territory of residence** ([[Tax Statistics by Area]]).

Income ranges are based on **total income assessed**, which includes employment, pension, investment, self-employment, other sources, and non-taxable income components as defined in the publication. Total income assessed may differ from economic income in other publications because certain non-taxable amounts are excluded while some grossed-up amounts (for example eligible dividends) may be included.

## Taxable vs non-taxable (related classification)

The publication also classifies returns as **taxable** or **non-taxable** using a rule based on the sum of net federal tax, net provincial tax, CPP/EI on self-employment, and social benefit repayments (taxable if that sum is at least **$2**). High total-income filers may still be non-taxable after deductions and credits.

## Limitations

Range-level counts and dollars are rounded and may be suppressed ([[Rounding]], [[Data Suppression]]). Sparse ranges exacerbate [[Small-Cell Analysis]] issues when linking to audit samples.

## Sources

- [Individual Income Tax Return Statistics (2023 tax year) — Income ranges classification; Table 2 description](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/income-statistics-gst-hst-statistics/t1-final-statistics/2023-tax-year.html)
- [[Individual Income Tax Return Statistics]]

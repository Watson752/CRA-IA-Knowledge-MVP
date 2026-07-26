---
title: Initial Assessment Data
aliases:
  - First assessment statistics
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
  - assessment
  - t1
  - statistics
---

# Initial Assessment Data

In **Individual Income Tax Return Statistics**, each return contributes the values from its **most recent assessment** available as of the [[Assessment Cut-Off Date]]. For returns never reassessed by that date, the published figures reflect the **initial assessment** (first assessment recorded in the extraction window).

## Official compilation rule

CRA states that the **most recent assessment** is used to compile the statistics. Returns **not yet reassessed** by the cut-off therefore appear with **initial assessment** line values.

## Contrast with reassessed returns

When CRA completes a **reassessment** on or before the cut-off, tables use **reassessed values** instead of the original assessment ([[Reassessment Data]]). The publication does not separately flag which cells are initial versus reassessed at the aggregate level.

## Revision over time

Later editions or [[Statistical Revision]] can replace initial-assessment-based figures when reassessments post-date an earlier cut-off.

## Sources

- [Individual Income Tax Return Statistics (2023 tax year) — Explanatory notes](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/income-statistics-gst-hst-statistics/t1-final-statistics/2023-tax-year.html)
- [[Individual Income Tax Return Statistics]]

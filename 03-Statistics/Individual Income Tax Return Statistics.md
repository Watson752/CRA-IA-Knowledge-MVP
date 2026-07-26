---
title: Individual Income Tax Return Statistics
aliases:
  - T1 Final Statistics
  - T1 return statistics
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
related_datasets:
  - Open Government dataset 5954b30b-9179-4f4c-adca-445372df4c60
related_risks: []
related_controls: []
related_procedures: []
related_methods: []
tags:
  - t1
  - income-tax
  - statistics
---

# Individual Income Tax Return Statistics

**Individual Income Tax Return Statistics** presents data from individual income tax and benefit returns processed for a stated **tax year**. The series was formerly known as **T1 Final Statistics**. Each **edition** (publication year) corresponds to a tax year and includes explanatory notes, PDF/CSV tables, and (for recent editions) an Open Government dataset.

## 2025 edition — 2023 tax year (verified 2026-07-23)

Authoritative scope for the edition documented in this vault:

- Data are from returns **processed for the 2023 tax year**.
- Statistics include the most recent **2023 tax year assessments or reassessments** up to the cut-off date **November 30, 2024**.
- Starting with this edition, CRA uses an **earlier extraction cut-off** (November 30, 2024 versus June 30, 2025 in prior practice) to increase timeliness; when comparing editions, **extraction time frames** must be taken into account ([[Comparability Across Editions]], [[Assessment Cut-Off Date]]).
- The **most recent assessment** is used; for reassessed returns, the **most current reassessed values** are used ([[Reassessment Data]]).
- **All statistics in the publication are subject to revision** ([[Statistical Revision]]).

Landing page for all editions: [Individual Income Tax Return Statistics (formerly T1 Final Statistics)](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/income-statistics-gst-hst-statistics/t1-final-statistics.html) (lists editions through **2026** for the **2024 tax year**).

Open data: [Individual Income Tax Return Statistics (2023 tax year)](https://open.canada.ca/data/en/dataset/5954b30b-9179-4f4c-adca-445372df4c60).

## Table structure (2023 tax year edition)

| Table | Geography / dimension | Notes |
|-------|------------------------|-------|
| **Table 1** | Province or territory of **taxation** | Only table using **taxation** jurisdiction (not residence); includes **outside Canada** ([[Tax Statistics by Area]]) |
| **Table 2** | Income ranges; provincial/territorial residence where split | Line items by [[Tax Statistics by Tax Bracket]] (income ranges on total income assessed) |
| **Table 3** | Source of income by province/territory of **residence** | Nine source-of-income groups |
| **Table 4** | Age and gender | Residence-based provincial tables |
| **Table 5** | Province or territory of **residence** | Line items by jurisdiction of residence |

Tables 2, 4, and 5 present statistics for tax line items grouped under income ranges, age, gender, and province or territory of residence, as described on the official page. Dollar amounts and counts in tables are subject to [[Public Data Confidentiality Procedures]], [[Data Suppression]], and [[Rounding]]; totals may not add due to suppression or rounding.

## Statistical limitations chain

[[Individual Income Tax Return Statistics]] → constrained by [[Data Suppression]], [[Rounding]], [[Assessment Cut-Off Date]], [[Comparability Across Editions]] → affects [[Small-Cell Analysis]] → relevant to [[How Statistical Limitations Affect Audit Conclusions]].

## Related notes

- [[CRA Public Statistical Data]]
- [[Initial Assessment Data]]
- [[Reassessment Data]]

## Sources

- [Individual Income Tax Return Statistics (2023 tax year)](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/income-statistics-gst-hst-statistics/t1-final-statistics/2023-tax-year.html)
- [[99-Sources/source-notes/SRC-CRA-T1-Stats-2023]]

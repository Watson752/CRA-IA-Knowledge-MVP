---
title: Tax Statistics by Area
aliases:
  - Provincial territorial tax statistics
  - Taxation vs residence geography
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
  - geography
  - t1
  - statistics
---

# Tax Statistics by Area

In [[Individual Income Tax Return Statistics]], geographic breakdowns use two different concepts. Mixing them without relabelling invalidates comparisons.

## Province or territory of taxation (Table 1)

**Table 1 – General statement by province and territory of taxation** is the **only** table in the 2023 tax year edition that uses **province or territory of taxation** rather than residence.

Official definition: province or territory of taxation is the jurisdiction in which **provincial or territorial tax is payable**.

Table 1 presents key statistics by taxation jurisdiction for all returns (non-taxable and taxable) and includes returns from **outside Canada**.

## Province or territory of residence (Tables 2–5)

For **Tables 2, 4, and 5**, provincial and territorial subtables use **province or territory of residence**: the jurisdiction where the tax filer **resided on December 31** of the tax year, as reported on the return.

**Table 3** shows returns by **source of income** and province or territory of **residence**.

**Table 5** classifies returns according to residence listed on the return.

## Audit and analytics caution

Joining external datasets to CRA area statistics requires matching the same geography field (taxation vs residence). Small populations in a province or territory may trigger [[Data Suppression]] and affect [[Small-Cell Analysis]].

## Sources

- [Individual Income Tax Return Statistics (2023 tax year) — Provincial or territorial classification; Description of tables](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/income-statistics-gst-hst-statistics/t1-final-statistics/2023-tax-year.html)
- [[Individual Income Tax Return Statistics]]

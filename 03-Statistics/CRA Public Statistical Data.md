---
title: CRA Public Statistical Data
aliases:
  - CRA aggregate statistics
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
publication_date: null
as_of_date: 2026-07-23
last_verified: 2026-07-23
source_url: "https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/income-statistics-gst-hst-statistics/t1-final-statistics.html"
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
  - statistics
  - cra
  - open-data
---

# CRA Public Statistical Data

The Canada Revenue Agency publishes **aggregate** statistical products derived from processed tax and benefit returns and related administrative data. These publications support public transparency and research; they do **not** contain taxpayer-identifiable records.

## Primary product family in this vault

- [[Individual Income Tax Return Statistics]] — formerly **T1 Final Statistics**; landing page lists editions by publication year and tax year (for example, 2026 edition for the 2024 tax year, 2025 edition for the 2023 tax year).
- Open Government Portal datasets mirror selected editions (see [[99-Sources/source-notes/SRC-CRA-T1-Stats-2023]]).

## Relationship to performance reporting

Operational highlights such as return volumes and digital filing rates appear in departmental planning and results documents (for example [[Electronic Filing Statistics]] sourced from the 2026–27 Departmental Plan **actual** 2024–25 “CRA by the numbers” section). Those figures are **not** the same series as T1 assessment-based tables and must be labelled by fiscal year and source.

## Limitations common to CRA public statistics

Published CRA aggregate tables are constrained by [[Public Data Confidentiality Procedures]], [[Data Suppression]], and [[Rounding]], and by [[Assessment Cut-Off Date]] choices that affect [[Initial Assessment Data]] versus [[Reassessment Data]]. When comparing editions, apply [[Comparability Across Editions]] and expect [[Statistical Revision]].

## Audit and analytics relevance

Analytical work that joins CRA public statistics to audit populations should document these limitations and their effect on [[Small-Cell Analysis]] and [[How Statistical Limitations Affect Audit Conclusions]].

## Sources

- [Individual Income Tax Return Statistics (landing)](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/income-statistics-gst-hst-statistics/t1-final-statistics.html)
- [[99-Sources/CRA-Public-Source-Register]]

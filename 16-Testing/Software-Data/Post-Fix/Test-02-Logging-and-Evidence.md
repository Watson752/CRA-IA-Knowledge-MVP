---
title: "Test-02: Logging, Evidence, Accountability and Investigation (Post-Fix)"
note_type: testing
primary_domain: software-data
domains:
  - software
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
  - software-data
  - logging
---

# Test-02: Logging, Evidence, Accountability and Investigation (Post-Fix)

## Question

How can weak application logging affect audit evidence, accountability and the ability to investigate exceptions?

## Post-fix answer (vault-supported)

[[Application Logging]], [[Security Logging]], and [[Audit Logging]] are distinguished; “System Logs” alias removed from Audit Logging. Generation ≠ [[Log Review]] ≠ [[Monitoring and Alerting]] ≠ [[Exception Report Review]] ([[Logging and Monitoring Map]]). Reliability conditions include tamper protection, [[Data Retention]], [[Time Synchronization]], [[Identity Attribution]], and [[Incomplete Audit Logging]]. [[System-Generated Evidence]] still states logs/reports are **not** automatically reliable.

Relationship model is navigable end-to-end. **EFMS** supports trail → load → alert teaching; investigation remains outside that report’s published scope.

## Diagnostic checks

| Check | Post-fix finding |
|---|---|
| Logs treated as automatically complete? | **No** |
| Logging and monitoring conflated? | **No** — separate notes + map |
| Retention / log-access considerations? | **Yes** — Data Retention + Audit Logging |
| Log review separated from generation? | **Yes** — Log Review |
| Unsupported case detail? | **Avoided** |

## Score

| Criterion | Baseline | Post-fix | Rationale |
|---|---:|---:|---|
| Logging-concept clarity | 1 | **2** | App / security / audit / alert / review distinguished |
| Evidence-reliability analysis | 2 | **2** | Stronger with time sync + identity attribution notes |
| Control design | 1 | **2** | Log Review, retention, incomplete logging, dataset notes |
| Investigation and monitoring connection | 1 | **2** | Exception Handling + alerting path; EFMS bounds remain |
| Source-grounded application | 2 | **2** | EFMS still carefully used |
| **Total** | **7** | **10** | |

## Remaining issue

Deep forensic investigation playbooks and CRA-specific log schemas are intentionally absent (public-source limits). Stubs remain thin Class C.

## Test metadata

- Output: `16-Testing/Software-Data/Post-Fix/Test-02-Logging-and-Evidence.md`
- Vault notes modified during this test: **none**

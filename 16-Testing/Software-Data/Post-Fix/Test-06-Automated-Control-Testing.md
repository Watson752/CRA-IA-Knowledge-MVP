---
title: "Test-06: Automated Business Rule Design, Implementation and OE Testing (Post-Fix)"
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
  - automated-controls
---

# Test-06: Automated Business Rule Design, Implementation and OE Testing (Post-Fix)

## Question

What evidence and audit procedures could be used to determine whether an automated business rule is correctly designed, implemented and operating throughout the audit period?

## Post-fix answer (vault-supported)

Design / implementation / OE remain first-class. [[Automated Business Rules]], [[System Configuration]], [[Configuration Review]], [[Code Review]], and [[Deployment Approval]] fill technical-evidence gaps. [[Control Implementation]] states pre-production tests ≠ period OE; [[Operating Effectiveness]] covers mid-period changes, exceptions/overrides, and [[False Positives]] / [[False Negatives]]. Procedures include [[Document Review]], [[Walkthrough]], [[Inspection]], [[Reperformance]], [[Sample Selection]], [[Full-Population Analysis]], [[Exception Testing]] ([[Automated Controls Map]], [[Control Testing]]).

**EFMS** sole public case: documentation-review methodology, rule-change history, false positives—configuration still redacted; not treated as a full OE reperformance program.

## Diagnostic checks

| Check | Post-fix finding |
|---|---|
| Requirements confused with implementation? | **No** |
| Pre-production testing as production OE? | **No** — explicit UAT/SIT warning |
| Changes during audit period? | **Yes** |
| Exception paths assessed? | **Yes** — overrides + Exception Testing |
| Outcome errors considered? | **Yes** — FP/FN notes |

## Score

| Criterion | Baseline | Post-fix | Rationale |
|---|---:|---:|---|
| Design/implementation/operation distinction | 2 | **2** | Prior strength + Automated Business Rules path |
| Technical evidence coverage | 1 | **2** | Config, code review, deployment approval notes |
| Audit-procedure appropriateness | 2 | **2** | Expanded Control Testing procedure set |
| Statistics and outcome analysis | 1 | **2** | False Positives / False Negatives + sampling notes |
| Source-grounded application | 2 | **1** | EFMS still not a step-by-step OE tutorial (documentation review only) |
| **Total** | **8** | **9** | |

## Remaining issue

Public cases still do not supply full automated-control OE workpapers (and must not invent protected configuration). Procedure notes remain Class C stubs.

## Test metadata

- Output: `16-Testing/Software-Data/Post-Fix/Test-06-Automated-Control-Testing.md`
- Vault notes modified during this test: **none**

---
title: "Test-01: Objective, Scope, and Criteria (Post-Fix)"
note_type: testing
primary_domain: audit
domains:
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
  - baseline
  - audit
  - objective
  - scope
  - criteria
  - post-fix
---

# Test-01: Objective, Scope, and Criteria (Post-Fix)

## Question

What is the difference between an audit objective, audit scope and audit criteria, and how do they work together?

## Post-fix answer (vault-supported)

[[Audit Objective]], [[Scope]] (alias **Audit Scope**), and [[Criteria]] (alias **Audit Criteria**) remain distinct. [[Audit Planning]] and [[Risk Assessment]] now make planning/risk focus discoverable; [[Audit Period]] names the coverage window. [[Audit Methodology Map]] and [[Audit Lifecycle Map]] concentrate the relationship model for beginners. [[Evidence]] states assessment against criteria within scope.

Primary worked case unchanged in substance: [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]].

```text
Audit objective → what the engagement seeks to determine
Audit scope → boundaries, period, organizations, systems, exclusions
Audit criteria → standards for assessing evidence
Evidence → supports conclusions against criteria within scope
```

## Diagnostic checks

| Check | Post-fix finding |
|---|---|
| Objective/scope conflated? | **No** |
| Criteria described as evidence? | **No** |
| Exclusions explained? | **Yes** (Scope + cases) |
| Trace into public case? | **Yes** (concept backlinks + maps + BI case) |
| Unsupported CRA-specific templates? | **None** in Class C notes |

## Score

| Criterion | Baseline | Post-fix | Rationale |
|---|---:|---:|---|
| Conceptual distinction | 2 | **2** | Still clear; aliases improve discovery |
| Relationship clarity | 1 | **2** | Maps + Audit Planning assemble the chain |
| Public-case application | 2 | **2** | BI + linked exclusion cases |
| Source and content-class accuracy | 2 | **2** | Class C vs Class A preserved |
| Beginner usability | 1 | **2** | Aliases, planning/risk stubs, onboarding path |
| **Total** | **8** | **10** | |

## Remaining issue

Planning/risk stubs are thin Class C notes—not CRA engagement manuals. Do not treat them as Agency-mandated templates.

## Test metadata

- Suite: Post-Fix regression
- Output: `16-Testing/Audit/Post-Fix/Test-01-Objective-Scope-Criteria.md`
- Vault notes modified during this test: **none**

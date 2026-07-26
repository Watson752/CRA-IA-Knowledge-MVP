---
title: "Test-02: Risk, Control, Finding Lifecycle (Post-Fix)"
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
  - audit
  - risk
  - control
  - finding
  - post-fix
---

# Test-02: Risk, Control, Finding Lifecycle (Post-Fix)

## Question

What is the difference between a risk, a control, a control deficiency, an observation, an audit finding and a recommendation?

## Post-fix answer (vault-supported)

Canonical notes now exist for [[Control Deficiency]], [[Audit Observation]], [[Root Cause Analysis]], and [[Consequence or Impact]], alongside [[Risk]], [[Control]], [[Finding]], [[Recommendation]], [[Management Response]], [[Management Action Plan]], and [[Follow-up]]. [[Observation (Procedure)]] disambiguates the testing method from pre-finding observations. [[Risk and Control Map]] / [[Findings and Recommendations Map]] / [[Audit Lifecycle Map]] show the lifecycle.

Not every deficiency/observation becomes a finding ([[Finding]], [[Risk]]). Recommendations remain advisory; management owns MAPs ([[Internal Audit Independence]]).

Primary case: [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]].

## Diagnostic checks

| Check | Post-fix finding |
|---|---|
| Risk equated with finding? | **No** |
| Recommendation as IA-operated control? | **No** |
| Evidence vs conclusions? | **Yes** |
| Response vs recommendation? | **Yes** |
| Root cause & consequence represented? | **Yes** (dedicated notes) |
| Observation → finding gate? | **Yes** ([[Audit Observation]]) |

## Score

| Criterion | Baseline | Post-fix | Rationale |
|---|---:|---:|---|
| Terminology accuracy | 1 | **2** | Missing lifecycle terms now canonical |
| Lifecycle coherence | 2 | **2** | Maps reinforce end-to-end chain |
| Finding-versus-observation distinction | 1 | **2** | Dedicated observation note + procedure disambiguation |
| Public-case grounding | 2 | **2** | BI path still strongest |
| Source and content-class accuracy | 2 | **2** | Class labels preserved |
| **Total** | **8** | **10** | |

## Remaining issue

Public reports often omit explicit “root cause” labels; learners must still avoid inventing causes ([[Root Cause Analysis]] discipline). Stubs are concise.

## Test metadata

- Output: `16-Testing/Audit/Post-Fix/Test-02-Risk-Control-Finding-Lifecycle.md`
- Vault notes modified during this test: **none**

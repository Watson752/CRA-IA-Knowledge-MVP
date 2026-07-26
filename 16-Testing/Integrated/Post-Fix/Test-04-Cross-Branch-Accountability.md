---
title: "Test-04: Cross-Branch Accountability (Post-Fix)"
note_type: testing
primary_domain: testing
domains:
  - testing
  - organization
  - audit
  - software
  - data
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
  - integrated
  - ownership
---

# Test-04: Cross-Branch Accountability (Post-Fix)

## Question

How can unclear accountability between a program branch, ITB, data owners and control owners contribute to control failures?

## Post-fix answer (vault-supported)

Baseline strength retained. Post-fix adds [[How Organizational Ownership Affects System Accountability]]; [[Unclear Accountability]] links ITB/SIIB/Security Branch/AERB as **illustration targets** (not reporting lines) and names incident handoff / MAP-orphan failure modes; [[Ownership and Assurance Roles]] includes ARNI/CVB vignette and a derived reporting accountability chain. ITB≠program owner and AERB≠MAP executor preserved.

## Diagnostic checks

| Check | Post-fix finding |
|---|---|
| Unsupported ownership assigned? | **No** |
| ITB owns program outcomes? | **No** |
| IA independence preserved? | **Yes** |
| Control vs data ownership separated? | **Yes** |
| Branch mandates cited? | **Yes** |
| Branch illustration links labelled? | **Yes** — not reporting lines |

## Score

| Criterion | Baseline | Post-fix | Rationale |
|---|---:|---:|---|
| Organizational accuracy | 2 | **2** | Prior strength retained |
| Role separation | 2 | **2** | ARNI vignette + reporting chain reinforce separation |
| Technical and control-failure reasoning | 2 | **2** | Unclear Accountability failure modes expanded |
| Official-versus-derived labelling | 2 | **2** | Ownership bridge + branch link labels |
| Onboarding usefulness | 2 | **2** | Ownership bridge + Integrated paths |
| **Total** | **10** | **10** | |

## Remaining issue

No dedicated incident-accountability RACI note beyond Unclear Accountability prose; change-approver roles remain general-professional (not CRA CAB).

## Test metadata

- Test ID: Test-04-Cross-Branch-Accountability
- Suite: Integrated Post-Fix regression
- Output path: `16-Testing/Integrated/Post-Fix/Test-04-Cross-Branch-Accountability.md`
- Vault substantive notes modified during this test: **none**
- Baseline reference: `16-Testing/Integrated/Baseline/Test-04-Cross-Branch-Accountability.md`

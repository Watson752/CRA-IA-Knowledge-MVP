---
title: "Software-Data Test Summary"
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
  - summary
  - software-data
---

# Software-Data Test Summary

Regression of baseline Tests 01–06 after software-data repairs. Same questions and scoring criteria as `16-Testing/Software-Data/Baseline/`. Substantive vault notes were **not** modified during this regression. Post-Fix reports: `16-Testing/Software-Data/Post-Fix/`.

## Score table

| Test | Baseline score | Post-fix score | Change | Remaining issue |
|---|---:|---:|---:|---|
| Test-01 Privileged Access | 5 | 10 | +5 | Thin Class C stubs; no dedicated JML note |
| Test-02 Logging and Evidence | 7 | 10 | +3 | No CRA log schemas; investigation depth limited by public sources |
| Test-03 Automated Rules and Overrides | 5 | 9 | +4 | Override frequency/concentration analytics playbook still thin |
| Test-04 Data Pipeline and Reporting | 8 | 10 | +2 | Stage notes are stubs, not CRA ETL runbooks |
| Test-05 Ownership and Change Management | 8 | 10 | +2 | Change roles are general/derived—not official CRA CAB titles |
| Test-06 Automated Control Testing | 8 | 9 | +1 | Public cases still not full OE workpapers; stubs thin |
| **Total** | **41 / 60** | **58 / 60** | **+17** | |

## Totals

- **Baseline:** 41 / 60  
- **Post-fix:** 58 / 60  
- **Net change:** +17  

## Improvement by theme

| Theme | Baseline | Post-fix | Delta | Notes |
|---|---:|---:|---:|---|
| Privileged-access | 5 | 10 | +5 | Full IAM/approval/review/dataset path |
| Logging-and-evidence | 7 | 10 | +3 | App/security/audit vs monitoring/review; reliability conditions |
| Automated-rule and override | 5 | 9 | +4 | Legitimacy taught; FP/FN present; analytics playbook gap |
| Data-pipeline | 8 | 10 | +2 | Stage model + dimension notes + reconciliation caution |
| Ownership and change-management | 8 | 10 | +2 | Requester/approver/deployment authority chain |
| Automated-control testing | 8 | 9 | +1 | Config/code/deploy/FP-FN/procedures; case depth limit |

## Unresolved critical or high-severity issues

From [[Software-Data-Repair-Register]] deferred items and post-fix remainings:

| Severity | Issue | Status |
|---|---|---|
| critical | None open from repair register | — |
| high | None open from repair register (SD-01–SD-14 marked pass) | — |
| medium | Baseline diagnostics had been deferred during repair; now completed here | closed by this summary |
| medium / residual | Class C stubs are not CRA procedure manuals | accepted limitation |
| medium / residual | Override-population analytics playbook thin (Test-03) | open, non-blocking for MVP demo |
| low | No dedicated Joiner–Mover–Leaver note | open |
| low | No Post-Fix suite beyond these regression reports | optional |

No unresolved **critical** issues. No unresolved **high** repair-register items. Remaining gaps are intentional thinness and public-source limits.

## MVP demonstration readiness

**Yes — ready for an MVP demonstration** of the software-and-data onboarding layer, with clear caveats:

1. Use [[Software and Data Onboarding Path]] and the six MOCs as the demo spine.  
2. Emphasize content classes: general-professional vs official case vs derived maps.  
3. Show EFMS / Audit Yield as **bounded** public cases—not as proof of current CRA control weakness or full OE programs.  
4. Do not present Class C stubs as official CRA audit manuals.  
5. System-generated evidence remains “not automatically reliable” in the demo narrative.

## Related

- Baseline: `16-Testing/Software-Data/Baseline/`
- Post-Fix: `16-Testing/Software-Data/Post-Fix/`
- [[Software-Data-Repair-Register]]
- [[POST_FIX_VALIDATION]] (`16-Testing/Software-Data/POST_FIX_VALIDATION.md`)

---
title: "Test-03: Privileged Access and Incomplete Reviews (Post-Fix)"
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
  - privileged-access
---

# Test-03: Privileged Access and Incomplete Reviews (Post-Fix)

## Question

How should Internal Audit examine a system where users may have excessive privileges and periodic access reviews are incomplete?

## Post-fix answer (vault-supported)

[[Identity and Access Map]] now starts at [[Business Process Owner]] / [[Control Ownership]] and ends at [[Evidence]]. [[Joiner-Mover-Leaver]] covers access removal/lifecycle. [[Periodic Access Review]] / [[Access Review Testing]] state documented sign-off ≠ meaningful OE without entitlement examination and executed removals. [[How Access Control Relates to Segregation of Duties]] bridges RBAC/SoD. Excessive ≠ unauthorized retained. EFMS remains monitoring precedent only.

## Diagnostic checks

| Check | Post-fix finding |
|---|---|
| Excessive ≠ unauthorized? | **Yes** |
| User population validated? | **Yes** — User Access Dataset + completeness |
| Documentation ≠ actual review? | **Yes** — explicit OE sentences |
| Service and dormant accounts? | **Yes** |
| BPO → access ownership? | **Yes** — map + BPO Related links |
| Unsupported CRA claims avoided? | **Yes** |

## Score

| Criterion | Baseline | Post-fix | Rationale |
|---|---:|---:|---|
| Role and accountability clarity | 1 | **2** | BPO/control ownership linked; JML; Identity map chain |
| Access-control accuracy | 2 | **2** | Prior distinctions retained |
| Audit-testing methodology | 2 | **2** | Sign-off ≠ OE made explicit |
| Population and sampling integration | 2 | **2** | Prior strength; strata workbook still general |
| Public-case and source accuracy | 2 | **2** | EFMS/cyber bounds preserved |
| **Total** | **9** | **10** | |

## Remaining issue

No dedicated break-glass procedure note; privileged-role strata design remains a general sampling method, not an access-specific workbook.

## Test metadata

- Test ID: Test-03-Privileged-Access-and-Incomplete-Reviews
- Suite: Integrated Post-Fix regression
- Output path: `16-Testing/Integrated/Post-Fix/Test-03-Privileged-Access-and-Incomplete-Reviews.md`
- Vault substantive notes modified during this test: **none**
- Baseline reference: `16-Testing/Integrated/Baseline/Test-03-Privileged-Access-and-Incomplete-Reviews.md`

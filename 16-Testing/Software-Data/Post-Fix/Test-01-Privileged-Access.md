---
title: "Test-01: Privileged Access Risks and Controls (Post-Fix)"
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
  - privileged-access
---

# Test-01: Privileged Access Risks and Controls (Post-Fix)

## Question

How can privileged access create operational, security and compliance risks, and how could an auditor assess whether it is appropriately controlled?

## Post-fix answer (vault-supported)

[[Privileged Access]] is first-class and distinct from ordinary access. [[Excessive Privileges]] vs [[Unauthorized Access]] are defined. Path is traversable: Privileged Access → SoD risk → [[Access Approval]] → [[Periodic Access Review]] → [[Privileged Access Monitoring]] → [[Access Review Testing]] → [[Evidence]], with [[User Access Dataset]], [[Service Accounts]], and [[Dormant Accounts]] for population completeness. [[Identity and Access Map]] navigates the cluster.

**EFMS** remains a bounded detective-monitoring case for unauthorized employee access—not an entitlement-provisioning finding. No claim that a CRA system currently has weak privileged-access controls.

## Diagnostic checks

| Check | Post-fix finding |
|---|---|
| Privileged confused with ordinary access? | **No** — dedicated Privileged Access note |
| Access approval ≠ periodic review? | **Yes** — explicit contrast |
| Access population completeness explained? | **Yes** — User Access Dataset + Population Completeness |
| Service / admin / dormant accounts? | **Yes** — Service Accounts, Dormant Accounts (not “dormant controls”) |
| Unsupported CRA-specific claims? | **Avoided** — case bounds preserved |

## Score

| Criterion | Baseline | Post-fix | Rationale |
|---|---:|---:|---|
| Technical accuracy | 1 | **2** | Privileged / excessive / unauthorized / IAM / RBAC / SoD defined |
| Business-risk connection | 1 | **2** | Risk path + Unauthorized Access + EFMS monitoring context |
| Control and procedure coverage | 0 | **2** | Approval, review, monitoring, Access Review Testing present |
| Evidence and data integration | 1 | **2** | User Access Dataset + completeness/sampling links |
| Public-case and source accuracy | 2 | **2** | EFMS/Cyber still carefully bounded |
| **Total** | **5** | **10** | |

## Remaining issue

Notes are thin Class C stubs—not CRA access-administration manuals. No dedicated joiner–mover–leaver note (covered inside IAM / testing notes).

## Test metadata

- Output: `16-Testing/Software-Data/Post-Fix/Test-01-Privileged-Access.md`
- Vault notes modified during this test: **none**

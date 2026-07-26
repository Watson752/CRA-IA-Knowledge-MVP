---
title: "Change Management Map"
aliases:
  - "Change and Deployment Map"
note_type: navigation
primary_domain: navigation
domains:
  - software
  - data
  - audit
  - control
  - navigation
classification: public
content_origin: derived-analysis
authoritative: false
official_source: false
as_of_date: 2026-07-26
last_verified: 2026-07-26
source_status: current
review_status: analytical-draft
approved_for_ai_retrieval: false
tags:
  - MOC
  - software-data
  - onboarding
---

# Change Management Map

Derived ownership + change lifecycle map. Do not invent CRA CAB org charts.

## Roles

| Role | Note |
|---|---|
| Business / program owner | [[Business Process Owner]] · [[Program Owner]] |
| System owner | [[System Owner]] |
| Technical support | [[Technical Support]] / ITB mandate |
| Data owner | [[Data Owner]] |
| Control owner | [[Control Ownership]] |
| Change requester | [[Change Requester]] |
| Change approver | [[Change Approval]] |
| Deployment authority | [[Deployment Approval]] |
| Internal audit | [[Internal Audit Independence]] / AERB |

## Lifecycle

```text
Change Requester
→ Change Approval (authorize intent)
→ Code Review / build
→ Deployment Approval (go-live)
→ Post-implementation monitoring
→ Unauthorized System Changes (failure mode)
```

Distinct from transactional [[Manual Overrides]]. Ambiguity risk: [[Unclear Accountability]].

## Hub

[[Ownership and Assurance Roles]] · [[Change Management]] · [[Tool Deployment]] · [[IT Controls]]

## Cases (bounded)

- BI audit — SIIB ownership vs ITB service delivery
- EFMS — Security MAP owner; ITB co-named; rule-change governance theme

---
title: Ownership and Assurance Roles
aliases:
  - Ownership & Assurance Roles
  - Ownership and Assurance
note_type: organization
primary_domain: organization-business
domains:
  - organization
  - audit
  - risk
  - control
  - governance
  - data
classification: public
content_origin: derived-analysis
authoritative: false
official_source: false
as_of_date: 2026-07-25
last_verified: 2026-07-25
source_status: current
review_status: analytical-draft
approved_for_ai_retrieval: false
related_sources:
  - "[[99-Sources/source-notes/SRC-CRA-Org-2025]]"
  - "[[99-Sources/source-notes/SRC-TBS-Policy-Internal-Audit]]"
related_cases:
  - "[[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]]"
  - "[[Internal Audit - Enterprise Fraud Management System]]"
tags:
  - ownership
  - assurance
  - onboarding
---

# Ownership and Assurance Roles

Derived onboarding note: it **composes** how different accountability roles fit together in CRA public-audit practice. It does **not** add official CRA org-chart reporting lines or titles beyond what public sources and case notes already state.

## What the CRA Organization page does and does not define

**Official public CRA facts** on [[CRA-Organizational-Overview]] and branch mandate notes include program vs corporate branches, [[Information Technology Branch|ITB]]’s IT mandate, [[Service, Innovation, and Integration Branch|SIIB]]’s data and service roles (including [[Chief Data Officer]] placement where sourced), and [[Audit, Evaluation, and Risk Branch|AERB]]’s independent assurance mandate ([[99-Sources/source-notes/SRC-CRA-Org-2025]]).

The public Organization page **does not** formally define every ownership term used in this vault—business-process owner, program owner, system owner, data owner, control owner, or audit client. Those labels come from **general professional concepts** (linked below), **case-specific** OPI/MAP language in published reports, and this **derived** relationship model.

## Relationship model

```text
Business / program branch (or named program area)
→ owns business outcome / process accountability
→ often appears as OPI and/or MAP owner in public audits

ITB or technical function
→ supports technology (build, run, evolve systems and services)
→ may be named co-responsible for technical MAP actions
→ does NOT automatically own the business process

Data owner / data-accountable role (e.g., CDO mandate; stewards per Data Governance)
→ governs data responsibility (definitions, quality, permitted use)
→ distinct from IT operations and from AERB assurance

Control owner (first line; sometimes split with technical custodians)
→ designs, operates, monitors, and remediates a specific control

Change requester → Change approver → Deployment authority
→ (derived teaching chain) initiate / authorize intent / authorize go-live
→ see [[Change Requester]], [[Change Approval]], [[Deployment Approval]]
→ technical implementers are not automatically approvers

AERB (third line / IA & PE)
→ independently audits or evaluates
→ may judge whether MAPs are reasonable
→ does NOT own the business process, system, data, or corrective execution
```

Management (not AERB) owns [[Management Response]] and [[Management Action Plan]] corrective action after [[Recommendation]]s. Ambiguous ownership is a control risk—see [[Unclear Accountability]].

## Content-class labels

| Class | Meaning in this note |
|---|---|
| **Official public CRA facts** | Branch mandates, ITB/SIIB/AERB roles as on Canada.ca org baseline |
| **Official case-specific facts** | Named OPI, MAP owner, or co-responsible parties in a published audit report |
| **Derived onboarding interpretation** | The composed diagram above; teaching use of “audit client” |
| **General professional concepts** | Linked concept notes (`content_origin: general-professional-knowledge`) |

## Worked example — Business Intelligence audit

Primary illustration: [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]].

| Role in the model | Who in this case (vault-supported) | Class |
|---|---|---|
| Business / program ownership of BI activities | [[Service, Innovation, and Integration Branch]] (SIIB) — BI responsibility since 2011; MAP lead | Official case-specific |
| Program users (not MAP lead) | Selected [[Compliance Programs Branch]] (CPB) and [[Collections and Verification Branch]] (CVB) teams (examined/interviewed) | Official case-specific |
| Technical support | [[Information Technology Branch]] (ITB) — BI service delivery; BIDGSC co-chair; collaboration in action plans | Official case-specific |
| Data leadership signal | [[Chief Data Officer]] = SIIB Assistant Commissioner | Official org + case-specific |
| Independent assurance | [[Audit, Evaluation, and Risk Branch]] (AERB) — publishing branch; judged MAPs reasonable | Official case-specific |
| Corrective action | SIIB agrees to strengthen BI governance (ITB/stakeholders named in plans) | Official case-specific |

This case shows why “BI involves technology” must not collapse into “ITB owns BI.”

Secondary illustration (split maintenance vs MAP lead): [[Internal Audit - Enterprise Fraud Management System]] — [[Security Branch]] MAP owner; [[Information Technology Branch|ITB]] co-named for selected actions; AERB publishes assurance.

## Concept notes (ownership taxonomy)

### Risk and control roles

- [[Business Process Owner]]
- [[Program Owner]]
- [[System Owner]]
- [[Technical Support]]
- [[Data Owner]]
- [[Control Ownership]]
- [[Change Requester]]
- [[Change Approval]] (change approver)
- [[Deployment Approval]] (deployment authority)
- [[Unclear Accountability]]

### Audit and assurance roles

- [[Audit Client]]
- [[Internal Audit Independence]]
- [[Management Action Plan Owner]]

### Frameworks and related concepts

- [[Three Lines Model]]
- [[Change Management]]
- [[Management Action Plan]]
- [[Management Response]]
- [[Data Governance]]
- [[Scope]]
- [[Change Management Map]]
- [[Software and Data Onboarding Path]]

## Related organization navigation

- [[CRA-Program-Branches]]
- [[CRA-Corporate-Branches]]
- [[CRA-Acronym-Dictionary]] (OPI)
- [[Organizational-Onboarding-Path]]
- [[16-Testing/Baseline/Test-05-Ownership-and-Assurance]]

## Sources

Derived from vault org baseline, case org sections, and general professional concept notes. See [[99-Sources/source-notes/SRC-CRA-Org-2025]] and [[99-Sources/source-notes/SRC-TBS-Policy-Internal-Audit]] for official CRA and TBS IA policy anchors.

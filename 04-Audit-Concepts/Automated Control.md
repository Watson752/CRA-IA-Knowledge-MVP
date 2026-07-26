---
title: "Automated Control"
aliases:
  - Automated Controls
  - Application Control (automated)
note_type: audit-concept
primary_domain: audit
domains:
  - audit
  - control
  - risk
classification: public
content_origin: general-professional-knowledge
authoritative: false
official_source: false
as_of_date: 2026-07-26
last_verified: 2026-07-26
source_status: current
review_status: analytical-draft
approved_for_ai_retrieval: false
related_cases: []
tags:
  - audit-methodology
  - onboarding
---

An **automated control** is performed by a system (validations, detection rules, automated workflows)—often expressed as [[Automated Business Rules]].

**Design** tests examine whether logic/configuration is capable of meeting the [[Control Objective]] ([[Design Effectiveness]]). **Implementation** asks whether the approved rule was actually deployed/configured ([[Control Implementation]], [[System Configuration]], [[Deployment Approval]]). **Operating effectiveness** asks whether the rule remained enabled and operated over the [[Audit Period]]—including mid-period changes ([[Change Management]], [[Operating Effectiveness]]).

**Bypass path:** [[Manual Overrides]] can defeat an otherwise effective automated control if approval, logging, and [[Exception Report Review]] are weak. Overrides may be legitimate; test the governance path, not only the happy path.

**Reliance rules:** ITGCs—access and change management—usually required ([[IT Controls]], [[Tool Deployment]], [[System-Generated Evidence]]). Source-code or config inspection alone does not prove period OE. Pre-production testing does not prove production OE for the whole period. Assess outcomes via [[False Positives]] / [[False Negatives]] where relevant.

## Related notes

- [[Automated Business Rules]]
- [[Manual Control]]
- [[Manual Overrides]]
- [[IT Controls]]
- [[Design Effectiveness]]
- [[Control Implementation]]
- [[Operating Effectiveness]]
- [[System Configuration]]
- [[Configuration Review]]
- [[Change Management]]
- [[Audit Logging]]
- [[False Positives]]
- [[False Negatives]]
- [[Internal Audit - Enterprise Fraud Management System]]
- [[Automated Controls Map]]

## Sources

General professional knowledge; ISACA / IT audit practice.

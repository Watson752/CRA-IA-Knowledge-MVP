---
title: "Segregation of Duties"
aliases:
  - "Separation of Duties"
  - "SoD"
note_type: software-concept
primary_domain: software-data
domains:
  - software
  - control
  - risk
  - audit
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
  - access
  - onboarding
---

**Segregation of duties (SoD)** separates incompatible responsibilities so one person cannot initiate, authorize, and conceal a harmful action. For access and change: requestor ≠ approver ≠ implementer; developers ≠ sole production operators; privileged users should not solely control the logs that detect their actions ([[Audit Logging]]).

Failure mode: [[Inadequate Segregation of Duties]]. Related ITGC theme in [[IT Controls]] and CI/CD SoD in [[Tool Deployment]].

## Related notes

- [[Inadequate Segregation of Duties]]
- [[Privileged Access]]
- [[Access Approval]]
- [[Change Approval]]
- [[IT Controls]]
- [[Role-Based Access Control]]

## Sources

General professional knowledge; COSO / IT audit SoD practice.

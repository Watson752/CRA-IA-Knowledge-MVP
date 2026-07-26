---
title: "Identity and Access Map"
aliases:
  - "Access Control Map"
  - "IAM Map"
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

# Identity and Access Map

Derived access-control onboarding map. General professional concepts unless a case is cited.

## Concepts

- [[Identity and Access Management]] · [[Role-Based Access Control]]
- [[Privileged Access]] · [[Excessive Privileges]] · [[Unauthorized Access]]
- [[Segregation of Duties]] · [[Inadequate Segregation of Duties]]
- [[Access Approval]] · [[Periodic Access Review]] (distinct: preventive vs detective)
- [[Privileged Access Monitoring]] · [[Access Review Testing]]
- [[User Access Dataset]] · [[Service Accounts]] · [[Dormant Accounts]]

## Path

```text
[[Business Process Owner]] / [[Control Ownership]]
→ [[Role-Based Access Control]]
→ [[Privileged Access]]
→ [[Excessive Privileges]] / [[Unauthorized Access]] (keep distinct)
→ [[Inadequate Segregation of Duties]] (risk)
→ [[Access Approval]] / [[Joiner-Mover-Leaver]]
→ [[Periodic Access Review]]
→ [[Privileged Access Monitoring]]
→ [[User Access Dataset]] + [[Population Completeness]]
→ [[Access Review Testing]]
→ [[Evidence]]
```

## Bridge

- [[How Access Control Relates to Segregation of Duties]]

## Case (bounded)

- [[Internal Audit - Enterprise Fraud Management System]] — unauthorized employee access **monitoring** / audit trails (not a public privileged-access provisioning audit)

## Related

- [[Software and Controls Map]] · [[Logging and Monitoring Map]] · [[IT Controls]] · [[Access-Control Audit Path]] · [[Integrated Knowledge Map]]

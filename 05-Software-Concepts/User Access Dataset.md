---
title: "User Access Dataset"
aliases:
  - "Access Listing"
  - "Entitlement Extract"
  - "Privileged Account Inventory"
note_type: software-concept
primary_domain: software-data
domains:
  - software
  - data
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

A **user access dataset** is the structured extract of identities and entitlements used for access analytics and [[Access Review Testing]]. Expected elements typically include identity ID, account type (human/[[Service Accounts]]/shared), roles/groups, privileges, owner, last use, status, and source system.

**Completeness:** reconcile to directory/PAM/application admin stores; include nested group memberships, admin, break-glass, [[Dormant Accounts]], and service accounts. Incomplete frames inflate [[Sampling Risk]] ([[Population Completeness]], [[Missing Data]]).

A listing shows entitlement, not appropriate use—pair with [[Audit Logging]] / [[Privileged Access Monitoring]].

## Related notes

- [[Privileged Access]]
- [[Access Review Testing]]
- [[Population Completeness]]
- [[Structured Data]]
- [[Analytics]]
- [[Role-Based Access Control]]
- [[Service Accounts]]
- [[Dormant Accounts]]

## Sources

General professional knowledge.

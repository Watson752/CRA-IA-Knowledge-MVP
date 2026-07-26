---
title: "How Access Control Relates to Segregation of Duties"
aliases:
  - "Access and SoD Bridge"
note_type: bridge-note
primary_domain: bridge
domains:
  - software
  - control
  - audit
  - bridge
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
  - bridge
  - derived-analysis
  - integrated
---

# How Access Control Relates to Segregation of Duties

> **Derived bridge.** Definitions: [[Role-Based Access Control]], [[Segregation of Duties]], [[Privileged Access]].

## Content classes

| Class | Use in this note |
|---|---|
| **Official public facts** | Only where a linked case or org note states them |
| **General professional knowledge** | Linked concept definitions |
| **Derived interpretation** | This bridge’s cross-domain synthesis |
| **Synthetic examples** | Teaching scenarios—not CRA operational claims |


## Connection

RBAC encodes duties into roles. [[Segregation of Duties]] forbids toxic combinations (requestor ≠ approver ≠ implementer; privileged user ≠ sole log custodian). [[Excessive Privileges]] can create SoD conflicts even when access was “authorized.” [[Unauthorized Access]] is a different failure (no valid authorization).

## Audit inquiry path

```text
[[Business Process Owner]] (who may approve access need)
→ [[Access Approval]] / [[Periodic Access Review]]
→ [[User Access Dataset]] + [[Population Completeness]]
→ SoD conflict / dormant / service-account analysis
→ [[Access Review Testing]] → [[Evidence]]
```

Signed reviews ≠ meaningful examination without keep/remove decisions and executed removals ([[Access Review Testing]], [[Operating Effectiveness]]).

## Cases (bounded)

- [[Internal Audit - Enterprise Fraud Management System]] — unauthorized-access **monitoring** theme, not a provisioning/SoD OE audit.

## Related

- [[Identity and Access Map]] · [[How Logging Supports Audit Evidence]]

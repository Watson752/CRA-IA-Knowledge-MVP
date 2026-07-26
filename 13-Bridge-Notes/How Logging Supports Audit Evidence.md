---
title: "How Logging Supports Audit Evidence"
aliases:
  - "Logs as Audit Evidence"
note_type: bridge-note
primary_domain: bridge
domains:
  - software
  - audit
  - data
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

# How Logging Supports Audit Evidence

> **Derived bridge.** Logs are not inherently reliable ([[System-Generated Evidence]]).

## Content classes

| Class | Use in this note |
|---|---|
| **Official public facts** | Only where a linked case or org note states them |
| **General professional knowledge** | Linked concept definitions |
| **Derived interpretation** | This bridge’s cross-domain synthesis |
| **Synthetic examples** | Teaching scenarios—not CRA operational claims |


## Distinctions

| Log type | Note |
|---|---|
| Application / business events | [[Application Logging]] |
| Security / control-relevant trails | [[Audit Logging]] |
| Generation vs review | Logging ≠ [[Log Review]] / [[Monitoring and Alerting]] |

## Reliability conditions

Completeness, retention, tamper resistance, time consistency ([[Time Synchronization]]), identity attribution ([[Identity Attribution]]), and population validation ([[Population Completeness]], [[Incomplete Audit Logging]]).

## Path

```text
Event → Application / Audit Logging → Monitoring / Exception Report Review
→ Evidence Reliability → Audit Conclusion strength
```

## Cases (bounded)

- EFMS: audit trails and alerting; alert counts alone insufficient.

## Related

- [[Logging and Monitoring Map]] · [[Evidence and Conclusion Map]]

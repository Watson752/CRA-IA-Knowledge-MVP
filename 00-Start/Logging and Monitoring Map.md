---
title: "Logging and Monitoring Map"
aliases:
  - "Logs and Monitoring Map"
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

# Logging and Monitoring Map

Derived map. **System-generated logs are not assumed complete or reliable** ([[System-Generated Evidence]]).

## Distinguish

| Concept | Note |
|---|---|
| Application logs | [[Application Logging]] |
| Security logs | [[Security Logging]] |
| Audit trails | [[Audit Logging]] |
| Monitoring / alerts | [[Monitoring and Alerting]] · [[Monitoring and Reporting]] |
| Exception reports | [[Exception Report Review]] |
| Log review | [[Log Review]] |
| Retention / access / tamper | [[Data Retention]] · [[Audit Logging]] |
| Time / identity | [[Time Synchronization]] · [[Identity Attribution]] |
| Reliability | [[Evidence Reliability]] · [[Incomplete Audit Logging]] |

## Path

```text
System activity
→ log generation ([[Application Logging]] / [[Audit Logging]])
→ protected storage ([[Data Retention]], tamper protection)
→ monitoring or review ([[Monitoring and Alerting]] / [[Log Review]])
→ exception investigation
→ audit evidence
→ conclusion
```

## Case (bounded)

- [[Internal Audit - Enterprise Fraud Management System]] — audit-trail capture, loading completeness/timeliness, alerting (investigation out of published scope)

## Related

- [[Evidence and Conclusion Map]] · [[Software and Controls Map]]

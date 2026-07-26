---
title: "Audit Logging"
aliases:
  - Audit Trail
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

**Audit logging** records security- or control-relevant events (access, changes, privileged activity, control-relevant alerts) into an **audit trail**. Distinct from [[Application Logging]] (business/transaction events) and from [[Security Logging]] when the latter is used only for tool telemetry—though they overlap in practice.

Logs can be strong [[System-Generated Evidence]] only when protected from tampering, retained appropriately ([[Data Retention]]), complete enough for the assertion, time-consistent ([[Time Synchronization]]), and attributable ([[Identity Attribution]]). Gaps, weak access to logs, or unknown retention reduce [[Evidence Reliability]]. **Do not** treat system-generated logs as complete without validation ([[Incomplete Audit Logging]], [[Population Completeness]]).

**Generation ≠ review:** configuring logging is not the same control as [[Log Review]] or [[Monitoring and Alerting]]. Related broader concept: [[Monitoring and Reporting]].

## Related notes

- [[Application Logging]]
- [[Security Logging]]
- [[Incomplete Audit Logging]]
- [[Audit Log Dataset]]
- [[Log Review]]
- [[Data Retention]]
- [[Time Synchronization]]
- [[Identity Attribution]]
- [[Monitoring and Alerting]]
- [[System-Generated Evidence]]
- [[Evidence Reliability]]
- [[Privileged Access]]
- [[IT Controls]]
- [[Security Controls]]
- [[Cybersecurity]]
- [[Monitoring and Reporting]]
- [[Internal Audit - Enterprise Fraud Management System]]
- [[Logging and Monitoring Map]]

## Sources

General professional knowledge; security logging practice.

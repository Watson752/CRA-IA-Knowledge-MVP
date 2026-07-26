---
title: "Internal Audit – Enterprise Fraud Management System"
aliases:
  - Internal Audit - Enterprise Fraud Management System
note_type: case
primary_domain: case
domains:
  - case
  - audit
  - business
  - risk
  - control
  - software
  - data
classification: public
content_origin: official-public-source
authoritative: true
publisher: "Audit, Evaluation, and Risk Branch"
publication_date: 2026-01-23
report_date: 2026-01-23
as_of_date: 2026-07-25
last_verified: 2026-07-25
access_date: 2026-07-23
source_url: "https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/internal-audit-program-evaluation/internal-audit-program-evaluation-reports-2026/internal-audit-enterprise-fraud-management-system.html"
official_url: "https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/internal-audit-program-evaluation/internal-audit-program-evaluation-reports-2026/internal-audit-enterprise-fraud-management-system.html"
source_status: current
review_status: source-verified
approved_for_ai_retrieval: false
related_sources:
  - "[[99-Sources/source-notes/SRC-CRA-IA-EFMS-2026]]"
related_organizations:
  - "[[Audit, Evaluation, and Risk Branch]]"
  - "[[Security Branch]]"
  - "[[Information Technology Branch]]"
related_cases: []
tags:
  - case-study
  - fraud
  - public-audit
---

This note summarizes a publicly released CRA report. It is not an internal working paper, does not contain non-public evidence, and should be read with the original official report.

# Internal Audit – Enterprise Fraud Management System

> **Historical context:** Findings describe conditions for the audit period **April 1, 2021 to March 31, 2024** (with pertinent activities since 2017; examination July to December 2024; report dated January 23, 2026). Do not assume the same conditions remain unresolved today unless a current official source says so. Do not reconstruct protected/redacted detail. Separate **what the published report states** from any cross-domain interpretation below.


## What the published report states

**Context.** CRA implemented the Enterprise Fraud Management System (EFMS) in 2017 to reduce risks of unauthorized employee access to taxpayer information. The system records employee transactions and uses business rules to identify questionable activity in real time. The Security Branch’s Internal Fraud Management Solutions (IFMS) Section maintains/enhances EFMS and supports system developers; Internal Affairs reviews alerts. ITB’s Enterprise Fraud Management Services Section maintains EFMS. The report states that EFMS generated more than 17,000 alerts since implementation, including 2,334 in 2022–23 and 1,850 in 2023–24.

**Objective and scope.** The audit sought assurance that EFMS was working as intended by recording, managing, monitoring, and reporting user activities in accordance with CRA policy instruments. It covered capture of audit-trail records through receipt of alerts, not processes after Internal Affairs screening, including investigations and discipline. The period was April 1, 2021 to March 31, 2024, with pertinent activities since 2017; examination was July to December 2024.

**Criteria and methodology.** Criteria concerned application onboarding, review/modification of detection models (business rules), timely alert receipt, and accurate/relevant performance information. The published methodology says it reviewed documentation from Security Branch and ITB to verify policies, procedures, and practices.

**Findings.** The audit concluded EFMS was working as intended, with improvement opportunities. Application onboarding had procedures but lacked a formal risk-assessment framework and formal time-estimation procedures. Business-rule changes were ad hoc across owners; oversight was inconsistent, detailed change history was not centrally maintained, and some rules had not been reviewed or modified even when they generated many false-positive alerts. Record loading had a process and expected-record matching, but was not always timely and controlled. A quarterly dashboard reported six indicators, but the audit identified additional indicators—such as alert resolution by rule and timing from incident to incident/alert creation—that could better inform management.

**Recommendations and MAPs.** Security Branch agreed to document formal onboarding risk assessments with effort considerations; monitor and track business-rule changes; formalize record re-ingestion with expected timeframes and user communications, jointly with ITB; and develop KPIs for efficiency/effectiveness. Action plans included a standardized rule-note field, review of high false-positive rules, centralized re-ingestion material, and improved alert-resolution definitions/data. Targets were May 2026.

**Conclusion.** The public conclusion is positive on the system working as intended while specifically identifying governance, timeliness/control, and performance-measure improvements.

**Limitations.** The report excludes the investigation and discipline stages and contains security-related redactions. It does not disclose system configuration, protected rule details, or a complete assessment of internal-fraud risk.

> Public source limitation: Certain information was not disclosed in the published report. This vault does not attempt to reconstruct it.

## Cross-domain interpretation

This vault interprets the case as a [[Cybersecurity]] monitoring and [[Data Governance]] case. An alerting system’s technical operation, its rule-change governance, data timeliness, and decision-useful metrics each form separate control objectives. A low-level rule change may affect alert volume, false positives, workload, detection coverage, and reporting; centralized, traceable change evidence supports [[Evidence Reliability]] without exposing protected rule logic.

This vault interprets the loading/re-ingestion finding through [[Defence in Depth]]: detection depends on data reaching the monitoring layer in a controlled and timely way, while response depends on the downstream process that was outside scope. This does not imply that the report found a particular exposure or failure. Completeness of transfers into the monitoring layer is also a [[Missing Data]] and [[Data Quality]] concern for evidence of timely detection; see [[How Missing Data Limits Audit Assurance]]. Historical findings and public redactions are not a current-state fraud-risk assessment.

## Questions this case helps a learner explore

- What risk factors and effort estimates should an application-onboarding framework record?
- What minimum evidence should accompany a detection-rule change?
- Which KPIs distinguish alert volume from detection quality, timeliness, and operational effectiveness?
- How can a re-ingestion process validate completeness and communicate its potential impact?
- Where should a system audit’s boundary be drawn between monitoring, investigation, and discipline?

## Reusable concepts and connections

- [[Cybersecurity]] and [[Defence in Depth]] — audit trails, detection, and timely monitoring.
- [[Unauthorized Access]] · [[Audit Logging]] · [[Monitoring and Alerting]] — detective monitoring themes (not an entitlement-provisioning audit).
- [[Automated Business Rules]] · [[Change Management]] · [[False Positives]] — rule governance and outcome quality.
- [[Data Governance]] — ownership, formal changes, and standardized definitions.
- [[Evidence Reliability]], [[Data Quality]], [[Missing Data]], [[Rejected Records]] — record completeness, timeliness, and traceable rule history.
- [[System-Generated Evidence]] — alert counts/dashboards alone may be insufficient.
- [[Performance Reporting]] — indicators must support decisions, not merely describe volume.
- [[Three Lines Model]] — a general framework for separating system operation, oversight, and assurance.
- Maps: [[Logging and Monitoring Map]] · [[Automated Controls Map]]

## Software, statistics, and organizational connections

**Software:** EFMS combines audit-trail ingestion, rule-based alerting, and re-ingestion processes; protected configuration details are not summarized. **Statistics:** alert counts, timing intervals, and false-positive patterns are candidate operational measures, not sufficient evidence by themselves.

## Organizational relationships (labeled)

### Official case-specific relationship

- **Publishing assurance branch:** [[Audit, Evaluation, and Risk Branch|AERB]]
- **Primary management respondent / MAP owner:** [[Security Branch]] (IFMS Section maintains/enhances EFMS; agreed to action plans)
- **Named co-responsible for selected actions:** [[Information Technology Branch|ITB]] (Enterprise Fraud Management Services Section maintains EFMS; jointly named for re-ingestion formalization)
- **Other named operational role in report:** Internal Affairs reviews alerts (unit named in report; not expanded into an unsupported branch ownership claim here)

### Official organizational relationship

- Security Branch and ITB are headquarters **corporate branches** ([[CRA-Corporate-Branches]])

### Derived onboarding interpretation

- Shared EFMS maintenance is a case-stated collaboration; it does **not** by itself prove a reporting line between Security Branch and ITB

### Historical relationship

- EFMS implemented 2017; audit period April 2021–March 2024 (with pertinent activities since 2017)

## Follow-up evidence in vault

**Current remediation / follow-up status:** unknown in this vault.

This note records the **published** report’s findings, recommendations, and any management action-plan **commitments** (target dates). It does **not** contain a later public follow-up report confirming completion or ongoing operating effectiveness. Do not treat MAP dates as proof of current remediation. See [[Interpreting Historical Public Audit Findings]] and [[Follow-up]].

## Sources

- [Internal Audit – Enterprise Fraud Management System (official CRA report)](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/internal-audit-program-evaluation/internal-audit-program-evaluation-reports-2026/internal-audit-enterprise-fraud-management-system.html) — accessed 2026-07-23.

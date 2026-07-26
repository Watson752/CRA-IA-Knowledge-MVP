---
title: "Software-Data Repair Register"
note_type: testing
primary_domain: software-data
domains:
  - software
  - data
  - audit
  - testing
classification: public
content_origin: derived-analysis
authoritative: false
official_source: false
as_of_date: 2026-07-26
last_verified: 2026-07-26
source_status: diagnostic
review_status: analytical-draft
approved_for_ai_retrieval: false
tags:
  - testing
  - repair-register
  - software-data
---

# Software-Data Repair Register

Register of software-and-data layer repairs driven by `16-Testing/Software-Data/Baseline/Test-01` through `Test-06`. Official public finding/recommendation/date/MAP text was **not** rewritten except for adding teaching concept links in case reusable-concept sections (EFMS; Audit Yield interpretation paragraph already carried teaching links).

Severity priority applied: unsupported CRA tech claims → system evidence assumed reliable → unclear ownership → design/OE conflation → missing access/logging/change controls → incomplete pipeline reasoning → missing audit procedures → weak software–statistics links → weak navigation.

| ID | Test | Affected files | Severity | Problem | Proposed correction | Content class | Source required | Action taken | Validation result |
|---|---|---|---|---|---|---|---|---|---|
| SD-01 | Test-01 | new IAM/RBAC/Privileged Access/Excessive/Unauthorized/SoD/Inadequate SoD | high | Privileged vs ordinary access undefined; SoD/IAM missing | Create Class C access concept notes | general-professional | none (EFMS link for unauthorized-access monitoring theme only) | Created 7 notes | pass |
| SD-02 | Test-01 | new Access Approval, Periodic Access Review, Privileged Access Monitoring, Access Review Testing | high | Approval conflated with periodic review; no testing playbook | Create distinct preventive/detective/testing notes | general-professional | none | Created 4 notes; linked Manual Control / Recommendation | pass |
| SD-03 | Test-01 | new User Access Dataset, Dormant Accounts, Service Accounts | high | Access populations incomplete; dormant *controls* ≠ dormant *accounts* | Create dataset + account-type notes; wire Population Completeness | general-professional | none | Created 3 notes; Population Completeness updated | pass |
| SD-04 | Test-02 | new Application Logging, Security Logging; patch Audit Logging | high | App/security/audit trails conflated; “System Logs” alias | Create notes; remove System Logs alias; distinguish generation vs review | general-professional | none | Created + Audit Logging patched | pass |
| SD-05 | Test-02 | new Incomplete Audit Logging, Audit Log Dataset, Log Review, Data Retention, Monitoring and Alerting, Time Synchronization, Identity Attribution | high | Retention/review/time/identity under-specified; logging≠monitoring | Create Class C notes; link System-Generated Evidence | general-professional | none | Created 7 notes; hubs updated | pass |
| SD-06 | Test-02 / Test-03 | new Exception Handling, Exception Report Review | medium | Exception paths thin | Create notes; link overrides and rejects | general-professional | none | Created | pass |
| SD-07 | Test-03 | new Automated Business Rules, Input/Eligibility Validation, Incorrect Automated Decisions | high | No business-rule concept path | Create notes; link Automated Control | general-professional | EFMS/ARNI themes (existing) | Created | pass |
| SD-08 | Test-03 | new Manual Overrides, Unmonitored Manual Overrides, Manual Override Approval | critical | Overrides untaught; legitimacy unclear | Create notes stating overrides may be legitimate | general-professional | none (explicit non-EFMS-override caution) | Created; Automated Control patched | pass |
| SD-09 | Test-03 / Test-06 | new False Positives, False Negatives | high | Outcome analysis missing | Create stats notes; link EFMS FP theme | general-professional + case theme | EFMS public FP text | Created; EFMS reusable links | pass |
| SD-10 | Test-05 / Test-06 | new Change Management, Change Requester, Change Approval, Code Review, Deployment Approval, Unauthorized System Changes, System Configuration, Configuration Review | high | Change lifecycle / approver roles missing | Create notes; extend Ownership and Assurance Roles | general-professional / derived (role model) | none | Created; ownership hub updated | pass |
| SD-11 | Test-05 | new Unclear Accountability | medium | Failure-mode note missing | Create note; link ownership taxonomy | general-professional | none | Created | pass |
| SD-12 | Test-04 | new Source System Data, Data Pipeline, API Integration, Batch Processing, Data Transformation, Field Mapping, Rejected Records, Reference Data, Data Lineage, Data Reconciliation, Transactional Dataset, Management Reporting | high | Pipeline stages not first-class | Create stage notes; accuracy≠completeness reiterated | general-professional | Audit Yield teaching links | Created; Structured Data / Data Quality / SGE updated | pass |
| SD-13 | Test-04 | new Data Accuracy, Data Timeliness, Record Uniqueness | medium | Quality dimensions only inside Data Quality | Thin dimension notes pointing to Data Quality | general-professional | none | Created | pass |
| SD-14 | Test-06 | new Document Review, Sample Selection, Full-Population Analysis, Exception Testing, Stratified Sampling; patch Control Testing / OE / Implementation | high | Procedure gaps; UAT≠OE unstated | Create procedure notes; explicit UAT≠OE / one-instance rules | general-professional | none | Created + patched | pass |
| SD-15 | Test-01–06 | new maps + Software and Data Onboarding Path; Home; Learning Path; Technology map | medium | Weak navigation across software-data layer | Create MOCs and wire Home/paths | derived | none | Created 7 nav notes; hubs updated | pass |
| SD-16 | All | IT Controls, Tool Deployment, Monitoring and Reporting, Manual Control, System-Generated Evidence, Analytics, Evidence map, bridge Missing Data | medium | Hub notes not linked to new concepts | Bidirectional related-notes patches | general-professional / derived | none | Patched | pass |
| SD-17 | Test-01–03 | EFMS case reusable concepts | low | Case not wired to new teaching notes | Add concept links only; no finding text changes | official case + teaching links | existing case | Reusable section updated | pass |
| SD-18 | Test-02 | System-Generated Evidence / Audit Logging | critical | Risk of treating logs as inherently reliable | Restate validation requirements; incomplete-logging note | general-professional | none | Strengthened wording | pass |

## Issues deferred (unresolved)

| ID | Severity | Problem | Why deferred |
|---|---|---|---|
| SD-D1 | low | Notes are thin Class C stubs, not CRA procedure manuals | Intentional; avoid inventing non-public CRA detail |
| SD-D2 | low | No Joiner–Mover–Leaver dedicated note | Covered inside IAM / Access Review Testing; can split later |
| SD-D3 | medium | Baseline diagnostics not re-run | Per instructions: do not rerun tests during repairs |
| SD-D4 | low | Post-Fix suite not created | Optional next step after validation |
| SD-D5 | low | Inadequate Segregation of Duties path node beyond SoD | Created; deeper SoD analytics playbook still thin |

## Notes on content classes

- New software/data/procedure stubs: **general-professional-knowledge** unless navigation/maps (**derived-analysis**).
- Ownership change-approver chain in [[Ownership and Assurance Roles]]: **derived** teaching extension; not an official CRA org-chart.
- Public case updates: **teaching links only** in reusable/interpretation sections. Published findings/recommendations/dates/MAP commitments were not altered.
- No synthetic demo content used as public CRA evidence.
- No CRA-specific IAM product names, log schemas, or current control-weakness claims added.

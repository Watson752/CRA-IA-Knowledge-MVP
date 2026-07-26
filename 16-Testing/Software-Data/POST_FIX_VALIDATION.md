---
title: "Software-Data Post-Fix Validation"
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
  - validation
  - software-data
---

# Software-Data Post-Fix Validation

Validation after implementing repairs from `Software-Data-Repair-Register.md` (baseline Tests 01–06). **Baseline diagnostics were not re-run** (per instructions).

## Summary

Targeted Class C concept notes, hub patches, and navigation maps were added to close demonstrated software-data onboarding gaps. Official public report findings were not rewritten. System-generated evidence continues to require validation. Access approval is distinct from periodic review; logging is distinct from monitoring; overrides may be legitimate but require governance.

## Files created

### Access / identity (14)

`05-Software-Concepts/`: Identity and Access Management; Role-Based Access Control; Privileged Access; Excessive Privileges; Unauthorized Access; Segregation of Duties; Inadequate Segregation of Duties; Access Approval; Periodic Access Review; Privileged Access Monitoring; Access Review Testing; User Access Dataset; Dormant Accounts; Service Accounts

### Logging / monitoring / exceptions (11)

Application Logging; Security Logging; Incomplete Audit Logging; Audit Log Dataset; Log Review; Data Retention; Monitoring and Alerting; Time Synchronization; Identity Attribution; Exception Handling; Exception Report Review

### Automated rules / overrides / outcomes (10)

Automated Business Rules; Automated Input Validation; Automated Eligibility Validation; Incorrect Automated Decisions; Manual Overrides; Unmonitored Manual Overrides; Manual Override Approval; System Configuration; `06-Data-Statistics-Concepts/False Positives.md`; `False Negatives.md`

### Change / accountability (7)

Change Management; Code Review; Deployment Approval; Unauthorized System Changes; `07-Risk-Controls/Change Requester.md`; `Change Approval.md`; `Unclear Accountability.md`

### Pipeline / reporting / quality dimensions (15)

Source System Data; Data Pipeline; API Integration; Batch Processing; Data Transformation; Field Mapping; Rejected Records; Reference Data; Data Lineage; Data Reconciliation; Transactional Dataset; Management Reporting; Data Accuracy; Data Timeliness; Record Uniqueness

### Procedures / sampling (6)

Document Review; Configuration Review; Sample Selection; Full-Population Analysis; Exception Testing; Stratified Sampling

### Navigation (7)

Software and Controls Map; Identity and Access Map; Logging and Monitoring Map; Automated Controls Map; Data Pipeline and Reporting Map; Change Management Map; Software and Data Onboarding Path

### Testing artefacts (2)

`16-Testing/Software-Data/Software-Data-Repair-Register.md`; this `POST_FIX_VALIDATION.md`

## Files modified

| File | Change |
|---|---|
| `04-Audit-Concepts/Audit Logging.md` | Distinctions; removed System Logs alias; reliability conditions; links |
| `04-Audit-Concepts/Automated Control.md` | Design/implementation/OE; overrides; UAT/code≠OE; links |
| `04-Audit-Concepts/Control Implementation.md` | UAT/SIT ≠ period OE |
| `04-Audit-Concepts/Operating Effectiveness.md` | Period/change/exception/FP-FN procedures |
| `04-Audit-Concepts/Control Testing.md` | Expanded procedure list |
| `04-Audit-Concepts/Manual Control.md` | Access approval vs review; log/exception reviews |
| `04-Audit-Concepts/Methodology.md` | Configuration Review / Document Review links |
| `04-Audit-Concepts/Recommendation.md` | Periodic Access Review link |
| `04-Audit-Concepts/System-Generated Evidence.md` | Lineage/time/identity; totals≠accuracy |
| `05-Software-Concepts/IT Controls.md` | IAM/SoD/change/rules/pipeline links |
| `05-Software-Concepts/Tool Deployment.md` | Change/deployment/SoD/excessive privileges |
| `05-Software-Concepts/Monitoring and Reporting.md` | Logging≠alerting≠review |
| `05-Software-Concepts/Structured Data.md` | Pipeline/lineage/reporting links |
| `06-Data-Statistics-Concepts/Data Quality.md` | Dimension notes + pipeline |
| `06-Data-Statistics-Concepts/Population Completeness.md` | Access/pipeline completeness examples |
| `06-Data-Statistics-Concepts/Analytics.md` | FP/FN/full-pop/dataset links |
| `02-Organization/Ownership-and-Assurance-Roles.md` | Change approver chain; unclear accountability |
| `00-Start/Home.md` | New MOC table rows |
| `00-Start/CRA-Technology-and-Risk-Map.md` | Software-data MOC section |
| `00-Start/Evidence-and-Conclusion-Map.md` | Logging/pipeline reliability links |
| `12-Learning-Paths/Learning Path - Internal Audit Software and Data.md` | Maps + discipline reminders |
| `13-Bridge-Notes/How Missing Data Limits Audit Assurance.md` | Reconciliation gap status |
| `08-Cases/Internal Audit - Enterprise Fraud Management System.md` | Reusable concept links only |
| `08-Cases/Evaluation - Audit Yield.md` | Teaching links in interpretation (lineage/pipeline) |

## Issues resolved

- Missing canonical access, logging, override, pipeline, change, and automated-rule notes (SD-01–SD-14)
- Access approval vs periodic review distinction
- Logging vs monitoring vs alerting vs log review distinction
- Overrides may be legitimate; unmonitored overrides as risk state
- System evidence not treated as inherently reliable (restated)
- Design vs implementation vs OE for automated controls; UAT≠period OE
- Accuracy vs completeness vs uniqueness vs timeliness as linked dimensions
- Change requester / approver / deployment authority roles
- Navigation MOCs and software-data onboarding path
- Bidirectional hub and case teaching links

## Issues unresolved

- Baseline Tests 01–06 not re-scored (deferred SD-D3)
- Class C stubs are thin—not full CRA audit programs (intentional SD-D1)
- No dedicated Joiner–Mover–Leaver note (SD-D2)
- No Post-Fix diagnostic suite yet (SD-D4)
- Deep SoD conflict-analytics playbook still light (SD-D5)

## Canonical notes added

**63** new substantive/procedure/dimension concept notes + **7** navigation notes (see Files created). Existing ownership notes (BPO, System Owner, Technical Support, Data Owner, Control Ownership, Internal Audit Independence) were **not** duplicated.

## Broken links

Automated wikilink check across `00-Start`, `04-Audit-Concepts`, `05-Software-Concepts`, `06-Data-Statistics-Concepts`, `07-Risk-Controls`, `12-Learning-Paths`: **0 broken targets** detected.

## Unsupported claims removed / avoided

- Removed misleading `System Logs` alias from [[Audit Logging]] (was blurring application vs audit trails)
- No CRA IAM product names, log schemas, retention periods, or current privileged-access weakness claims introduced
- EFMS explicitly framed as unauthorized-access **monitoring**, not entitlement provisioning or transactional overrides
- Cyber protected findings not reconstructed
- Change-approver chain labelled derived—not an official CRA org chart

## Bidirectional links added

Hubs patched to point to new notes; new notes point back to hubs/cases/maps. Case reusable sections updated for EFMS (and Audit Yield teaching links). Maps provide end-to-end paths:

```text
Privileged Access → Risk → Control → Dataset → Procedure → Evidence → Finding
Source System → Data Pipeline → Reconciliation → Reporting → Evidence Reliability → Audit Conclusion
```

## Public cases updated

| Case | Update type |
|---|---|
| EFMS | Reusable concept wikilinks only |
| Audit Yield | Teaching links in existing derived interpretation paragraph |
| Findings / recommendations / dates / MAPs | **Unchanged** |

## Validation checklist

| Check | Result |
|---|---|
| No broken Wikilinks (sampled folders) | **Pass** |
| No duplicate canonical concepts for required titles | **Pass** |
| CRA technical claims have official public support or are avoided | **Pass** |
| Derived analysis labelled (maps, ownership change chain) | **Pass** |
| System evidence not assumed reliable | **Pass** |
| Access approval ≠ periodic review | **Pass** |
| Logging ≠ monitoring | **Pass** |
| Automated controls ↔ overrides correctly related | **Pass** |
| Data-pipeline stages represented | **Pass** |
| Ownership roles distinct; IA independence preserved | **Pass** |
| Software concepts connect to audit + statistics | **Pass** |
| Synthetic content not used as public evidence | **Pass** |

## Remaining limitations

1. Stubs teach vocabulary and relationships; they are not substitute audit programs.
2. Public cases still do not disclose protected configurations—learners must not invent them.
3. Full vault-wide link crawl outside listed folders was not exhaustive.
4. Re-run of baseline diagnostics recommended as a separate step to produce Post-Fix scores.

## Related

- [[Software-Data-Repair-Register]]
- [[Software and Data Onboarding Path]]
- Baseline folder: `16-Testing/Software-Data/Baseline/`

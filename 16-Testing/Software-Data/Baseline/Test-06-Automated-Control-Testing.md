---
title: "Test-06: Automated Business Rule Design, Implementation and OE Testing"
note_type: testing
primary_domain: software-data
domains:
  - software
  - data
  - audit
  - risk
  - control
  - case
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
  - baseline
  - software-data
  - onboarding
  - automated-controls
  - control-testing
---

# Test-06: Automated Business Rule Design, Implementation and OE Testing

## Question

What evidence and audit procedures could be used to determine whether an automated business rule is correctly designed, implemented and operating throughout the audit period?

## Answer

| Class | Use in this answer |
|---|---|
| **Official public-source** | [[Internal Audit - Enterprise Fraud Management System]] only—business rules / detection models, change history, false-positive alerts, documentation-review methodology, redactions |
| **General professional** | [[Design Effectiveness]], [[Control Implementation]], [[Operating Effectiveness]], [[Control Testing]], [[Automated Control]], [[Walkthrough]], [[Inquiry]], [[Inspection]], [[Reperformance]], [[Observation (Procedure)]], [[Audit Logging]], [[IT Controls]], [[Tool Deployment]], [[System-Generated Evidence]], [[Analytics]], [[Sampling Risk]], [[Population Completeness]], [[Control Frequency]], [[Evidence]], [[Criteria]], [[Control Objective]] |
| **Vault-derived** | Assembled evidence checklists for design / implementation / OE below; several rule-specific notes are **absent** |

**Hard rules (vault-supported):**

1. Do **not** assume source-code or configuration inspection alone proves [[Operating Effectiveness]] for the period—OE requires evidence the control actually performed across the [[Audit Period]] ([[Operating Effectiveness]], [[Automated Control]]).
2. Do **not** assume one successful test proves performance throughout the period ([[Operating Effectiveness]], [[Control Frequency]], [[Sampling Risk]]).
3. [[Walkthrough]] ≠ period OE; [[Inquiry]] alone ≠ OE; documentation ≠ operation ([[Control]], [[Design Effectiveness]]).
4. Do **not** reconstruct protected EFMS rule logic or treat the public EFMS methodology as a full OE reperformance program (published methods emphasize documentation review).

---

### Distinctions the vault does / does not make

| Layer | Meaning for an automated rule | Vault status |
|---|---|---|
| **Business-rule definition** | Approved requirement, policy/criteria, expected I/O, exceptions, risk intent | [[Criteria]], [[Control Objective]], [[Design Effectiveness]]; **no** [[Automated Business Rules]] note |
| **Technical implementation** | Code, decision tables, config objects that encode the rule | [[Control Implementation]], [[Automated Control]]; thin on code/decision-table evidence types |
| **Configuration** | Enabled flags, parameters, thresholds in the target environment | Mentioned across notes; **no** [[System Configuration]] / [[Configuration Review]] note |
| **Deployment** | Release into production | [[Tool Deployment]]; **no** [[Deployment Approval]] / [[Code Review]] notes |
| **Operation** | Rule fires correctly over the period | [[Operating Effectiveness]], [[Control Frequency]] |
| **Exception handling** | Overrides, bypasses, alert dispositions | Largely absent (see Test-03); [[Monitoring and Reporting]] exception reports only |
| **Monitoring** | Ongoing detection that the rule still works | [[Monitoring and Reporting]]; EFMS KPI/alert themes |

The vault **does** clearly separate design vs implementation vs operating effectiveness at the control-methodology layer. It **does not** fully separate rule definition → code → config → deploy → operate → exceptions → monitoring as a single automated-rule path.

---

### Business-rule design — evidence and procedures

**Question ([[Design Effectiveness]]):** If performed as intended, is the rule **capable** of addressing the [[Risk]] / [[Control Objective]]?

| Design element | Evidence to request | Procedures |
|---|---|---|
| **Approved requirement** | Requirement / change request; business owner approval | [[Inspection]]; inquiry of [[Business Process Owner]] / [[System Owner]] (corroborate) |
| **Policy or criteria** | Policy excerpts, [[Criteria]] mapping, eligibility/detection standards | Inspection vs rule specification |
| **Expected inputs and outputs** | I/O matrix, decision table, sample scenarios | Walkthrough; design reperformance of logic on paper/test cases |
| **Exception conditions** | Documented exception/override paths | Design walkthrough of alternate paths (vault thin on overrides) |
| **Intended risk mitigation** | Risk statement linked to control objective | Compare design to [[Control Objective]] / risk register |

**Typical design procedures:** understand risk → inspect policies/configs → [[Walkthrough]] → assess logic of automated rules ([[Design Effectiveness]], [[Automated Control]]). A walkthrough that confirms understanding is **not** period OE.

---

### Technical implementation — evidence and procedures

**Question ([[Control Implementation]]):** Has the designed rule been **put in place** (deployed/configured), distinct from whether it operated all period?

| Implementation element | Evidence | Procedures | Vault status |
|---|---|---|---|
| **Source code or configuration** | Code, rules engine objects, parameter screens | [[Inspection]]; configuration review (phrase in [[Methodology]]) | No dedicated System Configuration / Configuration Review note |
| **Decision tables** | Tabular rule specs synced to prod objects | Inspect mapping requirement → table → config | Not a vault note |
| **Version history** | Repo tags, rule-version IDs, change tickets | Trace versions across [[Audit Period]] | EFMS official: detailed change history not centrally maintained |
| **Test evidence** | Unit/UAT/SIT results | Inspect test packs—**not** alone OE for production period | Implied via [[Tool Deployment]] testing; not explicit “UAT ≠ OE” sentence |
| **Peer review** | Code/rule review sign-off | Inspect review records | **No** [[Code Review]] note |
| **Deployment records** | Release tickets, CAB/go-live approval, pipeline logs | Inspect [[Tool Deployment]] artifacts | **No** [[Deployment Approval]] note |

Implementation sits **between** design and OE: a well-designed rule never deployed cannot operate; a deployed rule may still fail OE ([[Control Implementation]]).

---

### Operating effectiveness — evidence and procedures

**Question ([[Operating Effectiveness]]):** Did the rule actually perform as required—by the system, at the required frequency, during the [[Audit Period]], with sufficient evidence, consistently enough?

| OE element | Evidence | Procedures |
|---|---|---|
| **Production configuration** | Prod extract of rule enablement/parameters at points in the period | Configuration inspection over time; compare to approved versions |
| **Change history** | All changes affecting the rule in-period | Inspect tickets/versions; assess unauthorized or untested changes ([[IT Controls]] change management) |
| **System logs** | Fire/no-fire events, decisions, user/system IDs, timestamps | [[Audit Logging]]; [[Inspection]] of logs; reliability caveats in [[System-Generated Evidence]] |
| **Transactions processed** | Population of items the rule should evaluate | [[Analytics]] / [[Population Completeness]]; sample or full population |
| **Exceptions and overrides** | Bypass/override/alert-close events | Sample high-risk exceptions (vault thin—see Test-03) |
| **Incidents** | Failures, outages, misconfiguration incidents | Inspect incident tickets affecting the rule |
| **Monitoring** | Alerts, dashboards, rule-performance reviews | [[Monitoring and Reporting]]; EFMS alert/KPI themes |
| **Reperformance** | Selected or synthetic inputs with known expected outcomes | [[Reperformance]] in controlled conditions; corroborate with prod evidence |
| **False positives / false negatives** | Wrong fires vs missed fires | Outcome analysis ([[Analytics]]); EFMS official false-positive alert theme; **no** False Positives/Negatives notes |

**ITGC dependency:** Reliance on automated application controls typically requires confidence in access and change management ([[Automated Control]], [[IT Controls]], [[Tool Deployment]]).

---

### Possible reliance on procedures

| Procedure | Design | Implementation | OE / period | Vault caveat |
|---|---|---|---|---|
| **Inspection** | Policies, specs, configs | Code/config, deploy tickets | Logs, tickets, prod configs across period | [[Inspection]] |
| **Walkthrough** | Primary | Understanding deploy path | **Not** period OE substitute | [[Walkthrough]] |
| **Configuration review** | Logic/parameters capable? | Deployed as designed? | Still enabled/unchanged inappropriately? | Named in [[Methodology]]; no titled note |
| **Reperformance** | Logic check on scenarios | Sometimes | Strong OE when data reliable | [[Reperformance]], [[Evidence Hierarchy]] |
| **Data analysis** | Scenario coverage gaps | N/A | Full/large population exception tests | [[Analytics]] |
| **Sampling** | Rare for design | Sample release packs | Sample periods/transactions/changes | [[Sampling Risk]], [[Control Frequency]] |
| **Full-population testing** | N/A | N/A | When extracts complete | [[Sampling Risk]], [[Population Completeness]] |
| **Corroborating evidence** | Always | Always | Always—inquiry/docs alone insufficient | [[Evidence]], [[Inquiry]] |

---

### One public case (supported)

**[[Internal Audit - Enterprise Fraud Management System]]** only.

**Official facts usable for this question:**

- EFMS uses **business rules** to identify questionable activity in real time.
- Criteria included review/modification of detection models (business rules), timely alert receipt, and performance information.
- Published methodology: reviewed documentation from Security Branch and ITB (policies, procedures, practices).
- Findings relevant to automated-rule assurance: ad hoc business-rule changes; inconsistent oversight; detailed change history not centrally maintained; some rules not reviewed/modified despite many **false-positive** alerts; record loading not always timely/controlled.
- Conclusion: working as intended, with governance/timeliness/performance-measure improvements.
- Limitations: investigation out of scope; security redactions; **system configuration and protected rule details not disclosed**.

**Bounded teaching use:** EFMS supports teaching that automated-rule assurance needs **design/governance of rules**, **change history**, **monitoring/false-positive outcomes**, and **feed completeness**—and that documentation review is not the same as disclosing production configuration or performing full OE reperformance. Do **not** invent EFMS rule logic, claim source-code inspection occurred, or treat alert counts as sufficient OE evidence ([[System-Generated Evidence]]).

---

## Test model

```text
Risk / Control Objective / Criteria
→ Business-rule definition (approved requirement, I/O, exceptions)
→ Design effectiveness test (capable if operated as intended)
→ Technical implementation (code/config, review, deploy)
→ Control implementation confirmation (rule actually put in place)
→ ITGC reliance (access + change management)
→ Operating effectiveness over Audit Period
   (prod config + change history + logs + transactions
    + exceptions + monitoring + reperformance / analytics)
→ False positive / false negative outcome analysis
→ Corroborated conclusion (strength matched to evidence)
```

| Stage | Pass condition (teaching) | Fail / limit examples |
|---|---|---|
| Design | Rule capable vs risk if followed | Spec missing exceptions; criteria mismatch |
| Implementation | Approved version deployed to prod | Never released; wrong environment |
| OE | Operated correctly across period | Disabled mid-period; untracked changes; incomplete logs; one clean test only |
| Outcomes | Error profile understood | High false positives ignored; false negatives unmeasured |

---

## Notes and cases used

### Notes present

- [[Automated Control]] · [[Manual Control]] · [[Control]] · [[Control Testing]]
- [[Design Effectiveness]] · [[Control Implementation]] · [[Operating Effectiveness]]
- [[Control Objective]] · [[Control Frequency]] · [[Control Ownership]]
- [[Walkthrough]] · [[Inquiry]] · [[Inspection]] · [[Reperformance]] · [[Observation (Procedure)]]
- [[Audit Logging]] · [[System-Generated Evidence]] · [[Evidence]] · [[Evidence Hierarchy]] · [[Evidence Reliability]]
- [[IT Controls]] · [[Tool Deployment]] · [[Monitoring and Reporting]] · [[Methodology]]
- [[Analytics]] · [[Sampling Risk]] · [[Population Completeness]] · [[Missing Data]] · [[Structured Data]]
- [[Criteria]] · [[Audit Period]] · [[Scope]]

### Case / source

- [[Internal Audit - Enterprise Fraud Management System]] (sole public case for this test)

### Searched; dedicated-note results

| Sought term | Result |
|---|---|
| Automated Business Rules | Not found |
| Automated Input Validation | Not found |
| Automated Eligibility Validation | Not found |
| Control Design | **Present** as alias of [[Design Effectiveness]] |
| Operating Effectiveness | **Present** |
| System Configuration | Not found |
| Change Management | Embedded only |
| Code Review | Not found |
| Deployment Approval | Not found |
| Audit Logging | **Present** |
| Reperformance | **Present** |
| Configuration Review | Phrase in [[Methodology]] only |
| Data Analysis | Nearest: [[Analytics]] |
| Sample Selection | Not found (covered under [[Sampling Risk]] / [[Control Frequency]]) |
| False Positives | Not found (EFMS case text) |
| False Negatives | Not found |

---

## Diagnostic evaluation

| Check | Finding |
|---|---|
| Does the vault confuse requirements with implementation? | **No** at methodology layer—[[Design Effectiveness]] vs [[Control Implementation]] are distinct. Rule-requirement artifacts still lack a dedicated Automated Business Rules note. |
| Does it treat pre-production testing as proof of production operation? | **Not explicitly endorsed.** Implementation ≠ OE is stated; an explicit “UAT/SIT ≠ period OE” line is still missing. |
| Does it include changes during the audit period? | **Yes** for automated controls—OE/ITGC change management; EFMS change-history finding reinforces the point. |
| Does it assess exception paths? | **Weak.** Overrides/exception handling not first-class; monitoring/exception reports only briefly. |
| Does it consider outcome errors? | **Partially.** EFMS false-positive alerts; no False Negatives concept note or FP/FN testing playbook. |

### Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Design/implementation/operation distinction | **2** | Dedicated [[Design Effectiveness]], [[Control Implementation]], [[Operating Effectiveness]] plus Automated Control linkage; walkthrough/inquiry/one-instance caveats explicit. |
| Technical evidence coverage | **1** | Config/logs/deploy/change themes exist, but Code Review, Deployment Approval, System Configuration, decision tables, and version-history playbooks are missing or case-redacted. |
| Audit-procedure appropriateness | **2** | Strong procedure catalog with correct design-vs-OE and corroboration rules; suits automated-rule testing when assembled. |
| Statistics and outcome analysis | **1** | [[Analytics]] / sampling / population completeness available; FP/FN and exception-outcome analysis underdeveloped as vault concepts. |
| Source-grounded application | **2** | EFMS supports rule governance, change history, false positives, and methodology limits without inventing configuration or OE reperformance detail. |
| **Total** | **8 / 10** | |

---

## Missing evidence types

- Approved automated-business-rule requirement / eligibility specification objects
- Decision-table artifacts linked to production rule IDs
- Peer **code/rule review** records
- **Deployment approval** / go-live authorization distinct from developer action
- Production **configuration baselines** and period snapshots (often redacted in public cases)
- Complete **rule version history** / central change register
- Override / exception-path logs with reasons and approvals
- Synthetic/reperformance test packs retained as evidence
- False-negative evaluation evidence (missed events), not only false-positive volume
- Incident tickets tied to rule misconfiguration or disablement

---

## Methodological errors

Risks if a learner misreads the vault or stops at thin stubs:

1. Treating requirement documents or walkthroughs as period OE.
2. Treating source-code inspection or a single reperformance as full-period OE without change history and production enablement evidence.
3. Treating pre-production test results as proof the rule operated in production throughout the [[Audit Period]].
4. Ignoring mid-period rule changes (EFMS theme mitigates if read).
5. Equating alert volume or “working as intended” case language with tested OE of every rule.
6. Ignoring exception/override paths that bypass the automated rule.
7. Analyzing false positives only and never asking about false negatives / detection gaps.
8. Reconstructing protected EFMS configuration or assuming the public methodology included code review/reperformance (it states documentation review).

---

## Missing statistical links

- No [[False Positives]] / [[False Negatives]] concept notes linked to [[Operating Effectiveness]] or [[Analytics]]
- No sample-selection note tailored to automated controls (stratify by rule version, period slice, high-risk transaction types)
- Weak link from override/exception rates → rule quality (see Test-03)
- No playbook for estimating miss rates when only alerted populations are visible (selection bias)
- Limited guidance on interpreting FP rates as management metrics vs audit OE evidence ([[System-Generated Evidence]] helps)

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Create **Automated Business Rules** (and thin Input/Eligibility Validation notes) linking requirement → design → implementation → OE.
2. Add **System Configuration**, **Configuration Review**, **Code Review**, and **Deployment Approval** evidence notes; wire to [[Control Implementation]] and [[Tool Deployment]].
3. Add an explicit sentence on [[Control Implementation]] or [[Operating Effectiveness]]: pre-production testing does not demonstrate production OE for the audit period.
4. Create **False Positives** and **False Negatives** notes with OE/analytics procedures; cross-link EFMS false-positive findings as a bounded example.
5. Extend [[Automated Control]] with a period-change testing checklist (enablement snapshots, version diffs, access to change the rule).
6. Add exception/override OE procedures (or link to Manual Overrides notes when created).
7. Keep EFMS as the single worked case: documentation review + change history + FP monitoring—not a fictional source-code OE program.
8. Add aliases for “control design,” “configuration review,” and “sample selection” to the correct methodology notes.

---

## Test metadata

- Test ID: Test-06-Automated-Control-Testing
- Suite: Software-Data Baseline onboarding diagnostics
- Output path: `16-Testing/Software-Data/Baseline/Test-06-Automated-Control-Testing.md`
- Vault notes modified by this test: **none** (output file created only)
- Process followed: searched automated-rule/design/OE/procedure/false-positive terms and EFMS; assessed definition→monitoring distinctions; did not treat code inspection or one success as period OE; used one public case only; did not implement recommendations

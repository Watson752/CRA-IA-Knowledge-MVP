---
title: "Test-02: Logging, Evidence, Accountability and Investigation"
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
  - logging
  - evidence
  - monitoring
---

# Test-02: Logging, Evidence, Accountability and Investigation

## Question

How can weak application logging affect audit evidence, accountability and the ability to investigate exceptions?

## Answer

| Class | Use in this answer |
|---|---|
| **Official public-source** | Published CRA case facts only—mainly EFMS (audit-trail capture, loading/timeliness, alerting, KPIs); Cyber Security Controls only for governance caution / protected-content limits |
| **General professional** | Concepts from [[Audit Logging]], [[System-Generated Evidence]], [[Evidence Reliability]], [[Evidence Hierarchy]], [[Evidence]], [[Monitoring and Reporting]], [[Missing Data]], [[Population Completeness]], [[IT Controls]], [[Tool Deployment]], [[Automated Control]], [[Design Effectiveness]], [[Operating Effectiveness]], [[Control Testing]] |
| **Vault-derived** | Distinctions among log types, investigation steps for overrides/access changes/failed transactions, and the relationship model below—several sought notes are **absent** |

**Rule for this answer:** Do **not** treat a log as reliable merely because a system generated it ([[System-Generated Evidence]]). Do **not** invent CRA log-configuration weaknesses beyond what public case notes state.

---

### What application and audit logs record

| Log type | Typical content | Vault status |
|---|---|---|
| **Application logging** | Application events: transactions, validations, errors, workflow steps, business-rule outcomes | **No** dedicated [[Application Logging]] note |
| **Audit logging / audit trails** | Security- or control-relevant events: access, changes, alerts (and, in teaching use, who did what, when) | Present as [[Audit Logging]] (aliases: Audit Trail, System Logs) |
| **Operational / security monitoring use of logs** | Aggregated signals for availability, performance, threats; SIEM correlation | [[Monitoring and Reporting]] separates operational vs security monitoring |
| **Evidence derived from logs** | Selected, protected, complete-enough log extracts used as [[Evidence]] | [[System-Generated Evidence]], [[Evidence Hierarchy]], [[Evidence Reliability]] |

[[Audit Logging]] states that audit logging records security- or control-relevant events (access, changes, alerts). [[Monitoring and Reporting]] describes security monitoring (log aggregation, SIEM) and operational monitoring (performance, availability, capacity).

**Vault distinction check (required process):**

| Concept | Distinguished? | Notes |
|---|---|---|
| Operational logs | Partially | Operational *monitoring* named; not a dedicated operational-log concept |
| Security logs | Partially | Security monitoring / privileged activity; not a titled security-log note |
| Audit trails | Yes (thin) | [[Audit Logging]] alias Audit Trail |
| Monitoring alerts | Partially | Alerts/triage in [[Monitoring and Reporting]]; EFMS official alert pipeline |
| Evidence derived from logs | Yes | [[System-Generated Evidence]] + [[Evidence Hierarchy]] (logs/trails must be protected and complete) |

**Gap:** aliases “System Logs” on [[Audit Logging]] and adjacency to [[Monitoring and Reporting]] can blur application logs vs audit trails vs monitoring alerts. There is no [[Incomplete Audit Logging]], [[Audit Log Dataset]], or [[Log Review]] note.

---

### Why missing events or incomplete fields weaken traceability

Traceability needs a reconstructable chain: *who / what / when / where / outcome*. Weaknesses:

| Weakness | Effect on evidence & accountability | Vault anchors |
|---|---|---|
| **Missing events** (never logged, filtered out, failed load) | Cannot prove or disprove that an action occurred; population of activity is incomplete | [[Missing Data]], [[Population Completeness]], [[Audit Logging]] (“complete enough,” gaps reduce reliability) |
| **Incomplete fields** (no user ID, object, before/after, reason code) | Event exists but cannot attribute responsibility or reconstruct the change | [[Missing Data]] (absent fields); identity attribution not a dedicated note |
| **Unknown retention / purged period** | Gaps across the [[Audit Period]]; OE cannot be evidenced | [[Audit Logging]] (unknown retention); retention also mentioned in [[Monitoring and Reporting]] |
| **Weak log access / tampering risk** | Logs may be altered by the same privileged actors they should evidence | [[Audit Logging]], [[Evidence Reliability]] (who can alter data; logs protected) |

EFMS (**official**): record loading had a process and expected-record matching but was **not always timely and controlled**—a public illustration that detection/monitoring evidence depends on complete, timely transfer of audit-trail records into the monitoring layer ([[Missing Data]], [[Data Quality]] interpretation in the case note). That supports *feed completeness*, not a claim that CRA application logging is generally incomplete.

---

### How weak logging affects investigation of overrides, access changes and failed transactions

| Scenario | If logging is weak… | Vault support |
|---|---|---|
| **Manual overrides** | Cannot show who overrode a control, why, or whether approval existed; investigation stalls at “something happened” | **No** [[Manual Overrides]] note; general professional packaging |
| **Access changes** | Cannot reconstruct grants/revokes/privilege elevation timing or actor | [[Audit Logging]] lists “access” among logged event types; [[Privileged Access]] note **missing** (see Test-01) |
| **Failed transactions / exceptions** | Cannot distinguish user error, system reject, timeout, or silent drop; exception handling lacks an audit trail | [[Monitoring and Reporting]] mentions exception reports; **no** [[Exception Handling]] note |
| **Alert → investigation handoff** | Alerts without reliable underlying events produce noise or false comfort | EFMS official scope: capture of audit-trail records through alert receipt; investigation/discipline **out of scope** |

**Accountability impact (vault-derived):** Without attributable, time-ordered, protected events, management and auditors cannot demonstrate control operation or assign responsibility—[[Evidence]] sufficiency/appropriateness fails even if inquiry asserts that “logging exists.”

---

### Controls over log generation, access, retention, review and alerting

| Control area | Design intent (general professional / vault-derived) | Nearest vault anchors |
|---|---|---|
| **Log generation** | Required events and fields configured; logging enabled in production; changes to logging config controlled | [[IT Controls]], [[Tool Deployment]] (missing logging as deployment risk), [[Automated Control]] |
| **Log access** | Least privilege; separation so subjects of monitoring cannot unilaterally alter trails | [[Audit Logging]] (weak access reduces reliability), [[Evidence Reliability]], [[Security Controls]] |
| **Retention** | Retain long enough for policy, investigation, and audit period; document disposal | [[Audit Logging]] (retained appropriately / unknown retention); [[Monitoring and Reporting]] (retention aligned with criteria)—**no** [[Data Retention]] note |
| **Log review** | Periodic or risk-based human review of log extracts / exceptions, distinct from mere generation | Theme only; **no** [[Log Review]] note; [[Manual Control]] covers reviews generally |
| **Monitoring / alerting** | Rules, thresholds, escalation, timely triage—uses logs but is not the same as logging | [[Monitoring and Reporting]]; EFMS alerting / Internal Affairs review of alerts (official) |

**Design vs operating effectiveness evidence (vault-derived packaging of [[Design Effectiveness]] / [[Operating Effectiveness]] / [[Control Testing]]):**

| Question | Evidence examples |
|---|---|
| **Design** | Logging policy/standards; event/field matrix; retention schedule; SIEM/alert design; who may access/alter logs; walkthrough of generation → storage → alert → review |
| **Operating effectiveness** | Period extracts showing required events present; samples of alerts triaged timely; access reviews of log stores; retention job evidence; reconciliation of expected vs loaded records; change tickets for logging/alert-rule changes |

Inquiry that “we log everything” is not OE proof ([[Evidence]], [[Evidence Hierarchy]]).

---

### Why auditors may need to reconcile logs with independent records

Logs are one source. Reconciliation detects silent omissions and filter errors:

- Application transaction counts vs audit-trail event counts
- Access-change tickets vs access events in logs
- Source-system record totals vs monitoring-layer loads (EFMS official theme: expected-record matching / re-ingestion)
- Independent control totals, job schedules, or [[Structured Data]] extracts ([[Population Completeness]], [[Analytics]])

Without reconciliation, a tidy log sample can still miss whole event classes ([[Missing Data]], [[System-Generated Evidence]]).

---

### How time synchronization and user identity affect reliability

| Factor | Why it matters | Vault status |
|---|---|---|
| **Timestamps / time sync** | Skewed clocks break sequencing of overrides, access changes, and failures across systems; false “before/after” conclusions | **Not** in substantive notes; only mentioned in prior diagnostic Test-04 teaching table (“clock/sync”) |
| **User identity attribution** | Shared IDs, missing user fields, or service accounts without owner mapping destroy accountability | Implied by “access” events and privileged-activity monitoring; **not** explicit identity-attribution teaching |
| **Integrity / tamper resistance** | Writable logs undermine all above | Covered in [[Audit Logging]] / [[Evidence Reliability]] |

---

### Relevant public CRA cases (explicitly supported)

#### Primary: [[Internal Audit - Enterprise Fraud Management System]]

**Official public-source facts used here:**

- EFMS records employee transactions and uses business rules to identify questionable activity in real time (audit-trail / detection purpose tied to unauthorized employee access risk).
- Audit scope: capture of audit-trail records through receipt of alerts—not investigation/discipline after Internal Affairs screening.
- Record loading: process and expected-record matching existed, but loading was not always timely and controlled.
- Alert/performance information: quarterly dashboard existed; audit identified additional indicators (e.g., alert resolution by rule; timing from incident to incident/alert creation).
- Conclusion: working as intended, with governance, timeliness/control, and performance-measure improvements.
- Limitations: investigation stage out of scope; security-related redactions; no disclosure of protected configuration/rule detail.

**Teaching use (vault-derived, bounded):** EFMS supports the chain *activity → audit-trail capture → loading → alerting → (investigation beyond published scope)*. It shows that weak or untimely **transfer/completeness** into the monitoring layer weakens detection evidence—and that alert counts/dashboards alone are insufficient ([[System-Generated Evidence]]). It does **not** authorize claims about CRA application-log field schemas, retention periods, or that logging is currently unreliable.

#### Adjacent: [[Internal Audit - Specific Cyber Security Controls]]

Useful for second-line monitoring / three-lines governance questions. Protected findings mean this test **does not** attribute specific logging deficiencies to that case.

---

## Relationship model

Required model:

```text
System activity
→ log generation
→ protected log storage
→ monitoring or review
→ exception investigation
→ audit evidence
→ conclusion
```

| Stage | Meaning | Vault support |
|---|---|---|
| System activity | Transactions, access, changes, failures, overrides | Implied; EFMS “records employee transactions” |
| Log generation | Events written with required fields | [[Audit Logging]]; [[Tool Deployment]] warns missing logging |
| Protected log storage | Access control, tamper resistance, retention | [[Audit Logging]], [[Evidence Reliability]] |
| Monitoring or review | SIEM/alerts and/or human log review | [[Monitoring and Reporting]]; review vs generation **not** sharply separated |
| Exception investigation | Follow-up on alerts/overrides/failures | EFMS: investigation **out of published scope**; no Exception Handling note |
| Audit evidence | Sufficient, appropriate log-derived evidence | [[Evidence]], [[System-Generated Evidence]], [[Evidence Hierarchy]] |
| Conclusion | Strength matched to evidence/limitations | [[Evidence Evaluation]], [[How Statistical Limitations Affect Audit Conclusions]] |

**Nearest existing fragment path:**

```text
[[IT Controls]] / [[Tool Deployment]]
→ [[Audit Logging]]
→ [[Evidence Reliability]] + [[System-Generated Evidence]]
→ [[Monitoring and Reporting]]
→ [[Internal Audit - Enterprise Fraud Management System]] (trail → load → alert)
→ [[Evidence]] / [[Evidence Evaluation]]
→ conclusion strength ([[Missing Data]], [[Population Completeness]])
```

---

## Notes and cases used

### Notes present

- [[Audit Logging]] · [[System-Generated Evidence]] · [[Evidence Reliability]] · [[Evidence Hierarchy]] · [[Evidence]] · [[Evidence Evaluation]]
- [[Monitoring and Reporting]] · [[Missing Data]] · [[Population Completeness]] · [[Data Quality]]
- [[IT Controls]] · [[Security Controls]] · [[Cybersecurity]] · [[Tool Deployment]] · [[Defence in Depth]]
- [[Automated Control]] · [[Manual Control]] · [[Control Testing]] · [[Design Effectiveness]] · [[Operating Effectiveness]]
- [[Analytics]] · [[Structured Data]] · [[Evidence and Conclusion Map]]

### Cases / sources

- [[Internal Audit - Enterprise Fraud Management System]] — primary ([[99-Sources/source-notes/SRC-CRA-IA-EFMS-2026]])
- [[Internal Audit - Specific Cyber Security Controls]] — adjacent only; no protected logging findings reconstructed

### Searched; not found as dedicated notes

| Sought term | Result |
|---|---|
| Application Logging | Not found |
| Audit Logging | **Present** |
| Monitoring and Alerting | Not found (nearest: [[Monitoring and Reporting]]) |
| Incomplete Audit Logging | Not found |
| Audit Log Dataset | Not found |
| Log Review | Not found |
| Privileged Access | Not found (see Test-01) |
| Manual Overrides | Not found |
| Exception Handling | Not found (phrase “exception reports” / case uses of “exception handling” elsewhere are not a logging note) |
| Evidence Reliability | **Present** |
| Data Retention | Not found (retention clauses inside Audit Logging / Monitoring and Reporting only) |

---

## Diagnostic evaluation

| Check | Finding |
|---|---|
| Are logs treated as automatically complete? | **No.** [[System-Generated Evidence]] explicitly rejects automatic reliability; [[Audit Logging]] requires completeness; [[Missing Data]] / [[Population Completeness]] reinforce gaps. |
| Are logging and monitoring conflated? | **Partially.** Separate notes exist, and Audit Logging points to Monitoring as “related,” but aliases (“System Logs”) and SIEM-as-log-aggregation blur generation vs monitoring vs alerting. No “Monitoring and Alerting” note. |
| Are missing retention or access-control considerations identified? | **Yes, briefly** in [[Audit Logging]] (weak access, unknown retention). No dedicated [[Data Retention]] or log-access control note. |
| Is log review separated from log generation? | **No.** Generation conditions are in Audit Logging; review/triage lives mainly under Monitoring and Reporting / general Manual Control—no [[Log Review]] control note. |
| Are unsupported details attributed to public cases? | **Avoidable with care.** EFMS case note bounds scope and redactions; this test must not invent log schemas, retention periods, or investigation outcomes. |

### Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Logging-concept clarity | **1** | [[Audit Logging]] exists and names access/changes/alerts, but Application Logging is absent; operational vs security vs audit trail vs alert vs evidence-from-logs is only partly distinguished. |
| Evidence-reliability analysis | **2** | Strong cluster: not-automatically-reliable system evidence, protection/completeness/retention, Missing Data / Population Completeness, Evidence Hierarchy. Timestamps and identity attribution remain under-specified in substantive notes. |
| Control design | **1** | Generation, access, retention, and monitoring appear as short clauses; no structured control set for Log Review, Data Retention, Incomplete Audit Logging, or Audit Log Dataset; design/OE packaging must be assembled. |
| Investigation and monitoring connection | **1** | EFMS + Monitoring and Reporting connect trails → load → alerts/triage well; investigation of overrides/access changes/failed transactions and Exception Handling are thin or out of case scope. |
| Source-grounded application | **2** | EFMS public facts map cleanly to audit-trail capture, completeness/timeliness of loading, and alert/KPI limits without over-claiming protected detail. |
| **Total** | **7 / 10** | |

---

## Missing logging concepts

- Application Logging (distinct from audit trails / security monitoring)
- Incomplete Audit Logging (failure modes: missing events, fields, periods)
- Audit Log Dataset (schema, keys, reconciliation expectations)
- Log Review (detective control separate from generation)
- Monitoring and Alerting (or clearer split inside Monitoring and Reporting)
- Data Retention (policy/control note beyond one-line mentions)
- Manual Overrides (logging requirements for override paths)
- Exception Handling (logging and escalation of failed transactions)
- Privileged Access (actors who can disable or alter logs—see Test-01)
- Time synchronization / clock integrity (for cross-system sequencing)
- Identity attribution on log events (user, service account, shared ID risks)

---

## Evidence weaknesses

If a learner relies only on the current vault:

1. May equate “logging exists” with reliable [[Evidence]] despite [[System-Generated Evidence]] (mitigated if that note is read).
2. May conflate log generation, SIEM monitoring, and alert triage as one control.
3. May miss that **log review** is a separate operating-effectiveness test from configuration of logging.
4. May not demand reconciliation of logs to independent transaction/access records.
5. May ignore timestamp sync and identity attribution because they are not first-class notes.
6. May over-extend EFMS: treat “working as intended” as proof of strong application logging everywhere, or invent investigation findings outside published scope.
7. Retention and log-access controls are named as risk factors but not taught as testable control objectives with evidence examples.

---

## Unsupported claims

Do **not** claim from the vault:

- CRA application-log field lists, retention periods, SIEM rules, or current logging effectiveness
- That EFMS found application logging incomplete across CRA (published finding is about loading/timeliness/control of records into EFMS and related governance/KPI themes)
- Investigation or discipline outcomes (explicitly out of EFMS scope)
- Protected cyber-control logging deficiencies from the Cyber Security Controls report
- That operational logs, security logs, and audit trails are fully defined as separate vault concepts
- That time synchronization or user-identity attribution controls are documented in substantive notes

Relationship-model steps and override/failed-transaction investigation language in this file are **vault-derived teaching**, not official CRA procedures.

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Create **Application Logging** and tighten [[Audit Logging]] (drop or clarify the “System Logs” alias; point to Application Logging for non-security/debug events).
2. Add **Incomplete Audit Logging**, **Audit Log Dataset**, **Log Review**, and **Data Retention** notes; link to [[Missing Data]], [[Population Completeness]], and [[Evidence Reliability]].
3. Explicitly separate **log generation → protected storage → monitoring/alerting → log review → investigation** in [[Evidence and Conclusion Map]] or a thin logging map.
4. Teach timestamp synchronization and identity attribution as reliability conditions on [[Audit Logging]] or System-Generated Evidence.
5. Add **Manual Overrides** and **Exception Handling** with required log fields and sample OE tests.
6. Cross-link EFMS as the worked example for trail completeness, load reconciliation, and alert insufficiency—without expanding into investigation findings.
7. Add design/OE evidence checklists for logging controls under [[Control Testing]] or Audit Logging.
8. Link Privileged Access (when created) to log-integrity risk (who can disable or alter trails).

---

## Test metadata

- Test ID: Test-02-Logging-and-Evidence
- Suite: Software-Data Baseline onboarding diagnostics
- Output path: `16-Testing/Software-Data/Baseline/Test-02-Logging-and-Evidence.md`
- Vault notes modified by this test: **none** (output file created only)
- Process followed: searched logging/monitoring/override/retention/evidence terms and public CRA cases; checked distinctions among log/monitoring/evidence concepts; verified completeness/retention/tamper themes; did not treat system-generated logs as automatically reliable; did not implement recommendations

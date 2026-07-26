---
title: "Test-01: Privileged Access Risks and Controls"
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
  - privileged-access
  - access-management
---

# Test-01: Privileged Access Risks and Controls

## Question

How can privileged access create operational, security and compliance risks, and how could an auditor assess whether it is appropriately controlled?

## Answer

| Class | Use in this answer |
|---|---|
| **Official public-source** | Published CRA case facts only (mainly EFMS context on unauthorized employee access / audit trails; Cyber Security Controls for governance caution) |
| **General professional** | Definitions and control/testing patterns from [[IT Controls]], [[Defence in Depth]], [[Security Controls]], [[Monitoring and Reporting]], [[Audit Logging]], [[Evidence]], [[Population Completeness]], [[Sampling Risk]], [[Manual Control]], [[Control Ownership]], [[Recommendation]], [[Roles and Responsibilities]], [[Tool Deployment]], [[Risk Algorithms]] |
| **Vault-derived** | Assembled relationship path and testing steps below—the vault does **not** contain dedicated notes for most nodes in the required path |

**Do not** imply that a named CRA production system currently has weak privileged-access controls. Public reports either protect technical finding detail ([[Internal Audit - Specific Cyber Security Controls]]) or address a different control objective ([[Internal Audit - Enterprise Fraud Management System]]—detection of questionable employee activity, not an access-entitlement audit).

---

### What privileged access means

**Privileged access** (general professional / vault-derived packaging) is elevated technical or administrative capability beyond ordinary end-user permissions—for example administrator, root, domain-admin, database DBA, security-admin, break-glass, privileged cloud roles, or highly elevated application roles that can change configurations, override controls, or reach broad data stores.

Vault grounding is thin: [[Defence in Depth]] names **identity and access management** and **least privilege** as complementary ideas; [[IT Controls]] names **access management** as a common ITGC; [[Monitoring and Reporting]] expects monitoring of **privileged activity**. There is **no** dedicated [[Privileged Access]] note distinguishing privileged from ordinary user access.

Ordinary access typically supports a defined business task with limited write/config rights. Privileged access can alter systems, identities, logs, or large data populations—so the same identity failure has wider operational, security, and compliance consequence.

---

### Why it is more sensitive than ordinary access

| Sensitivity driver | Why it matters | Vault status |
|---|---|---|
| Scope of change | Privileged users can alter configurations, roles, jobs, or production data | Implied via [[IT Controls]] change/access themes; not taught as privileged-access risk |
| Bypass potential | Elevated rights can weaken or disable other controls | [[Defence in Depth]] warns shared dependencies can collapse “depth” |
| Data exposure | Broad read/export rights increase confidentiality impact | EFMS official context: unauthorized employee access to taxpayer information is a stated risk the monitoring system addresses |
| Accountability | Shared/admin/service IDs blur who performed an action | [[Audit Logging]] / [[Evidence Reliability]] stress protected, complete logs—not privileged-account accountability specifically |
| Compliance / trust | Misuse or unchecked privilege can breach policy, privacy, and control criteria | General professional; not a dedicated vault note |

---

### Risks: unauthorized changes, data exposure, inappropriate transactions, weak accountability

| Risk theme | Explanation | Content class |
|---|---|---|
| **Unauthorized / uncontrolled changes** | Privileged users can modify code, configs, detection rules, or access rights without adequate approval or trail | General professional; [[IT Controls]] change management; EFMS official theme that business-rule changes were ad hoc / history incomplete (rule governance—not a claim that CRA access provisioning is weak) |
| **Data exposure** | Elevated read or extract rights can expose sensitive taxpayer or employee information | Official EFMS risk context (unauthorized employee access to taxpayer information); general professional for privileged stores |
| **Inappropriate transactions** | Elevated application or process rights can enable improper adjustments, approvals, or overrides | General professional; application-control language in [[IT Controls]] |
| **Weak accountability** | Missing/tampered logs, shared admin IDs, or unmonitored privilege reduce attribution | [[Audit Logging]], [[System-Generated Evidence]], [[Monitoring and Reporting]] (privileged activity) |
| **Operational disruption** | Misconfiguration or accidental privileged action can impair availability | General professional; [[Cybersecurity]] CIA framing |
| **Compliance / control-criteria failure** | Access not aligned to roles, approvals, or reviews fails security criteria | [[Security Controls]], [[Criteria]]; [[Roles and Responsibilities]] mentions testing who approves access |

**Technical permissions ↔ business responsibilities:** Auditors should connect entitlements to job duties and risk (least privilege). Vault support is partial: [[Roles and Responsibilities]] / [[Control Ownership]] cover accountability; [[IT Controls]] names access management and segregation of duties in administrative functions; there is **no** note that maps role definitions → technical permission sets (RBAC) or a [[User Access Dataset]] model.

---

### Excessive privileges vs unauthorized access

| Concept | Meaning | Vault status |
|---|---|---|
| **Excessive privileges** | Access was granted (or left after role change) beyond what the duty requires—authorized in a weak sense, but inappropriate | Phrase appears in [[Tool Deployment]] (“excessive privileges”); **no** dedicated note |
| **Unauthorized access** | Access or use without valid authorization (never approved, revoked but still active, credential misuse, or policy-prohibited use) | Phrase in [[Cybersecurity]]; EFMS official purpose includes reducing unauthorized employee access risk |

These are related but not identical: excessive privilege can *enable* unauthorized or inappropriate use, yet a user can hold excessive rights while every login is still “authorized.” Conversely, unauthorized access can occur with ordinary rights (stolen credentials) or with privilege. The vault does **not** teach this distinction explicitly.

---

### How segregation of duties relates to privileged access

**Segregation of duties (SoD)** separates incompatible responsibilities so one person cannot initiate, authorize, and conceal a harmful action. For privileged access, SoD typically means:

- requestor ≠ approver ≠ implementer of elevated access;
- developers ≠ production operators for privileged changes (echoed for models in [[Risk Algorithms]]);
- privileged users should not solely control the logs that would detect their actions ([[Audit Logging]] reliability);
- CI/CD / admin functions should not concentrate unchecked power ([[Tool Deployment]], [[IT Controls]]).

Vault status: SoD is mentioned inside [[IT Controls]], [[Tool Deployment]], and [[Risk Algorithms]], but there is **no** [[Segregation of Duties]] or [[Inadequate Segregation of Duties]] note, and no link from SoD conflicts → privileged role design.

---

### Preventive and detective controls

| Type | Control examples (general professional / vault-derived) | Nearest vault anchors |
|---|---|---|
| **Preventive** | Least privilege / RBAC; access approval before grant; SoD constraints; MFA for privileged paths; just-in-time / time-bound elevation; secure deployment (no default/admin sprawl) | [[Defence in Depth]] least privilege; [[IT Controls]] access management; [[Tool Deployment]]; [[Roles and Responsibilities]] (who approves access); [[Manual Control]] (approvals) |
| **Detective** | Privileged-activity monitoring; audit logging; periodic access review / certification; SIEM alerts; exception reporting | [[Monitoring and Reporting]]; [[Audit Logging]]; [[Recommendation]] example of quarterly access reviews for privileged accounts; [[Control Ownership]] (reviews lapse without ownership); [[Manual Control]] (access certifications) |

**Access approval vs periodic access review (critical distinction—under-taught):**

| Control | Timing | Purpose |
|---|---|---|
| **Access approval** | Before (or at) grant / change of privilege | Prevent inappropriate entitlement from being issued |
| **Periodic access review** | Recurring after grant | Detect privilege creep, role-change leftovers, dormant/orphan accounts |

The vault mentions approvals and access reviews in separate places but **does not** define or contrast [[Access Approval]] and [[Periodic Access Review]] as first-class notes.

---

### Evidence an auditor could request

| Evidence | Why | Vault linkage |
|---|---|---|
| Privileged-account policy / procedure | Design criteria | [[Criteria]], [[Security Controls]], [[IT Controls]] |
| Access request / approval tickets | Preventive control operation | [[Manual Control]], [[Roles and Responsibilities]] |
| Role–permission matrices / RBAC definitions | Business duty ↔ technical rights | Missing as dedicated note; general professional |
| Complete privileged-user population extract | Frame for testing | [[Population Completeness]], [[Structured Data]], [[Analytics]]—not an access-specific dataset note |
| Joiner/mover/leaver evidence | Timely revoke / adjust | General professional; ownership themes in [[Control Ownership]] |
| Periodic review packages (sign-offs, removals) | Detective control OE | [[Recommendation]] example; [[Manual Control]]; Test-03 teaching illustration |
| Privileged-activity logs / SIEM alerts / triage evidence | Monitoring operation | [[Audit Logging]], [[Monitoring and Reporting]], [[System-Generated Evidence]] |
| SoD conflict reports | Incompatible privilege combinations | Mentioned only as ITGC theme |
| Change tickets for privileged config | Unauthorized change risk | [[IT Controls]], EFMS change-history theme (detection rules) |

---

### How access populations and samples may be tested

1. **Define the complete population** of privileged identities in scope (human admins, security roles, DBAs, cloud privileged roles, **service/system accounts**, break-glass, and **dormant** accounts still enabled)—then reconcile the extract to independent sources (directory OUs, PAM inventory, application admin tables). Incomplete frames inflate [[Sampling Risk]] ([[Population Completeness]], [[Missing Data]]).
2. **Stratify** where risk differs (e.g., domain admin vs app role; interactive vs service accounts).
3. **Test design:** inspect approval/SoD/review procedures; walkthrough grant and review cycles ([[Control Testing]], [[Design Effectiveness]]).
4. **Test operating effectiveness:** sample grants across the period for documented approval; sample review cycles for completeness of population reviewed, reviewer authority (not self-review), timely completion, and follow-up removals ([[Operating Effectiveness]], [[Manual Control]]).
5. **Full-population analytics** when extracts allow: orphan accounts, unused privileged IDs, SoD conflicts, privileges without owner ([[Analytics]] on [[Structured Data]]).
6. **Corroborate** listings with logs and tickets; do not treat the listing alone as proof of control ([[Evidence]], [[System-Generated Evidence]]).

Vault status: general sampling/completeness/evidence notes are strong; **no** [[Access Review Testing]] or [[User Access Dataset]] playbook.

---

### Limitations of relying only on an access listing

An access listing is necessary but not sufficient:

- May be **incomplete** (filters omit service, shared, or nested group memberships) → [[Population Completeness]].
- Shows **entitlement**, not whether use was appropriate or monitored → need [[Audit Logging]] / [[Monitoring and Reporting]].
- Does not prove **approval** or **periodic review** occurred → need tickets and certification evidence.
- Stale extracts miss movers/leavers; quality issues reduce [[Evidence Reliability]] / [[Data Quality]].
- Does not demonstrate **business need** without role/responsibility mapping.
- Privileged users who can alter logs undermine listing + log reliance unless log integrity is controlled ([[Audit Logging]], [[System-Generated Evidence]]).

---

### Public CRA case used (supported)

**[[Internal Audit - Enterprise Fraud Management System]]** (official public source): CRA implemented EFMS to reduce risks of **unauthorized employee access to taxpayer information**; the system records employee transactions and uses business rules to identify questionable activity in real time; the audit covered capture of audit-trail records through alert receipt and found the system working as intended with governance/timeliness/performance-measure improvements.

**How it supports this question (vault-derived teaching use, carefully bounded):**

- Shows a **detective / monitoring** response to unauthorized-access risk (audit trails + alerting), aligned with [[Audit Logging]] and [[Monitoring and Reporting]].
- Illustrates that **system-generated alert counts alone are not enough** without reliable loading, change governance, and decision-useful metrics ([[System-Generated Evidence]], [[Evidence Reliability]]).
- Does **not** constitute a finding that CRA privileged-access provisioning, SoD, or periodic access reviews are weak—those topics are outside the published EFMS objective/scope as summarized in the vault.

**[[Internal Audit - Specific Cyber Security Controls]]** is a relevant adjacent case for cyber governance / three-lines monitoring, but protected finding detail means it **cannot** be used to claim specific privileged-access control weaknesses.

---

## Relationship path

Required teaching path (nodes mostly **absent** as dedicated notes; assembled for this diagnostic):

```text
[[Privileged Access]]
→ [[Excessive Privileges]]
→ [[Inadequate Segregation of Duties]]
→ [[Access Approval]]
→ [[Periodic Access Review]]
→ [[Privileged Access Monitoring]]
→ [[Access Review Testing]]
→ [[Audit Evidence]]
```

| Step | Intended teaching link | Vault reality |
|---|---|---|
| Privileged Access | Elevated rights vs ordinary access | **Missing** dedicated note |
| Excessive Privileges | Privilege beyond duty | Phrase only in [[Tool Deployment]] |
| Inadequate Segregation of Duties | Incompatible privileged powers | SoD mentions only; **no** inadequacy note |
| Access Approval | Preventive grant control | “Who approves access” in [[Roles and Responsibilities]]; **no** note |
| Periodic Access Review | Detective certification | Example wording in [[Recommendation]] / [[Control Ownership]]; **no** note distinguishing from approval |
| Privileged Access Monitoring | Detective monitoring of use | Theme in [[Monitoring and Reporting]]; **no** titled note |
| Access Review Testing | How auditors test reviews/populations | **Missing**; general [[Control Testing]] / [[Sampling Risk]] / [[Population Completeness]] only |
| Audit Evidence | Sufficiency/appropriateness of evidence | Present as [[Evidence]] (alias Audit Evidence) |

**Nearest existing fragment path (what a learner can actually traverse today):**

```text
[[IT Controls]] (access management, SoD)
→ [[Defence in Depth]] (IAM, least privilege)
→ [[Tool Deployment]] (excessive privileges)
→ [[Roles and Responsibilities]] / [[Manual Control]] (approvals, certifications)
→ [[Recommendation]] / [[Control Ownership]] (periodic privileged access reviews)
→ [[Monitoring and Reporting]] + [[Audit Logging]] (privileged activity / logs)
→ [[Population Completeness]] + [[Sampling Risk]] + [[Evidence]]
→ [[Internal Audit - Enterprise Fraud Management System]] (unauthorized access monitoring case)
```

---

## Notes and cases used

### Notes present (supporting fragments)

- [[IT Controls]] · [[Security Controls]] · [[Cybersecurity]] · [[Defence in Depth]]
- [[Tool Deployment]] · [[Monitoring and Reporting]] · [[Audit Logging]] · [[System-Generated Evidence]]
- [[Control]] · [[Control Ownership]] · [[Control Testing]] · [[Manual Control]] · [[Automated Control]]
- [[Design Effectiveness]] · [[Operating Effectiveness]]
- [[Evidence]] · [[Evidence Reliability]] · [[Evidence Hierarchy]]
- [[Population Completeness]] · [[Missing Data]] · [[Data Quality]] · [[Sampling Risk]] · [[Analytics]] · [[Structured Data]]
- [[Roles and Responsibilities]] · [[Recommendation]] · [[Criteria]] · [[Risk]]
- [[Risk Algorithms]] (developer/operator segregation mention)

### Cases / sources

- [[Internal Audit - Enterprise Fraud Management System]] — official unauthorized-employee-access risk context; audit-trail / alerting case ([[99-Sources/source-notes/SRC-CRA-IA-EFMS-2026]])
- [[Internal Audit - Specific Cyber Security Controls]] — cyber governance; protected findings; **not** used to allege privileged-access weakness ([[99-Sources/source-notes/SRC-CRA-IA-Cyber-2023]])

### Searched; not found as dedicated notes

| Sought term | Result |
|---|---|
| Privileged Access | Not found |
| Identity and Access Management | Phrase in [[Defence in Depth]] / [[Cybersecurity]] only |
| Role-Based Access Control | Not found |
| Excessive Privileges | Phrase in [[Tool Deployment]] only |
| Unauthorized Access | Phrase in [[Cybersecurity]]; EFMS case context |
| Segregation of Duties | Mentions in [[IT Controls]], [[Tool Deployment]], [[Risk Algorithms]] only |
| Inadequate Segregation of Duties | Not found |
| Access Approval | Not found (approval mentioned in [[Roles and Responsibilities]] / [[Manual Control]]) |
| Periodic Access Review | Example in [[Recommendation]]; lapse theme in [[Control Ownership]]; no note |
| Privileged Access Monitoring | Theme in [[Monitoring and Reporting]] only |
| User Access Dataset | Not found |
| Access Review Testing | Not found |
| Audit Logging | **Present** as [[Audit Logging]] |

---

## Diagnostic evaluation

| Check | Finding |
|---|---|
| Is privileged access confused with ordinary user access? | **Risk of confusion — yes.** No dedicated definition; learner must infer from “access management,” “least privilege,” and “privileged activity/accounts” fragments. |
| Does the vault distinguish access approval from periodic review? | **No.** Approvals and reviews appear in separate notes without a contrast or linked pair. |
| Does it explain why the access population must be complete? | **Partially, at general level.** [[Population Completeness]] / [[Sampling Risk]] are strong, but not applied to privileged-access extracts, nested groups, or service accounts. |
| Does it account for service, administrator and dormant accounts? | **No for accounts.** [[Security Controls]] mentions “dormant controls” (unused controls), not dormant accounts. Administrator/service/break-glass populations are not taught. |
| Does it avoid unsupported CRA-specific claims? | **Yes in case notes.** EFMS and Cyber cases separate official facts, redactions, and interpretation; this test must not invent CRA privileged-access weaknesses. |

### Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Technical accuracy | **1** | Fragments (ITGC access, least privilege, privileged activity, logging) are directionally correct, but privileged vs ordinary access and excessive vs unauthorized are not defined as first-class concepts. |
| Business-risk connection | **1** | EFMS supplies official unauthorized-access / taxpayer-information risk context; Tool Deployment links excessive privileges to risk. Full operational/security/compliance typology for privileged access is not connected. |
| Control and procedure coverage | **0** | Required path notes (Privileged Access → … → Access Review Testing) are almost entirely missing; access approval vs periodic review is not taught; SoD/RBAC/IAM lack dedicated notes. |
| Evidence and data integration | **1** | Strong general evidence, logging, population-completeness, and sampling notes exist, but no [[User Access Dataset]] or [[Access Review Testing]] bridge; listing limitations for access are under-specified. |
| Public-case and source accuracy | **2** | EFMS and Cyber notes carefully bound official facts vs interpretation and avoid reconstructing protected content; usable without unsupported CRA access-control claims. |
| **Total** | **5 / 10** | |

---

## Missing controls

Dedicated (or clearly titled) control/concept notes absent or insufficient for onboarding:

- Privileged Access (definition vs ordinary access)
- Identity and Access Management
- Role-Based Access Control / least-privilege entitlement model
- Excessive Privileges
- Unauthorized Access (as access-risk concept distinct from EFMS monitoring)
- Segregation of Duties / Inadequate Segregation of Duties
- Access Approval (preventive)
- Periodic Access Review (detective; contrasted with approval)
- Privileged Access Monitoring
- Joiner–mover–leaver / timely revocation (related)
- Service, shared, administrator, break-glass, and dormant account controls

---

## Missing datasets

- User Access Dataset (fields, sources, reconciliation expectations)
- Privileged-account inventory / PAM extract model
- Role–permission matrix dataset
- Access request / approval ticket population
- Access certification / review results dataset
- Privileged-activity log schema expectations (event types, retention, integrity)
- SoD conflict report dataset

---

## Weak links

1. No traversable wikilink path for the required Privileged Access → … → Audit Evidence chain.
2. [[Recommendation]]’s “quarterly access reviews for privileged accounts” example is not backed by a Periodic Access Review concept note.
3. [[Population Completeness]] is not linked to access-population completeness (nested groups, service accounts, omitted OU filters).
4. [[Monitoring and Reporting]] “privileged activity” is not linked to Access Approval / Periodic Access Review / Access Review Testing.
5. [[Manual Control]] mentions access certifications but does not connect to testing steps or population completeness.
6. [[IT Controls]] names access management and SoD without teaching excessive vs unauthorized privilege.
7. EFMS case is easy to over-read as an access-provisioning audit; onboarding must keep scope boundaries explicit.
8. Technical permissions are only weakly tied to business responsibilities ([[Roles and Responsibilities]] mentions who approves access, but no RBAC / duty-mapping note).

---

## Unsupported claims

Do **not** claim from the vault:

- That any specific CRA system has weak privileged-access, SoD, or access-review controls (not stated in public case summaries; Cyber findings protected).
- That EFMS is an access-approval or periodic-access-review control (it is an unauthorized-activity detection / audit-trail system per the published summary).
- That CRA currently fails least privilege, RBAC, or privileged-account monitoring.
- That “dormant controls” in [[Security Controls]] means dormant user accounts.
- That the vault already contains Privileged Access, IAM, RBAC, Access Approval, Periodic Access Review, User Access Dataset, or Access Review Testing as dedicated notes.
- Detailed CRA internal access-administration procedures or datasets (out of public scope).

Worked testing steps and the required relationship path in this file are **vault-derived teaching**, not official CRA audit manuals.

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Create Class C concept notes for the required path: **Privileged Access**, **Excessive Privileges**, **Unauthorized Access**, **Segregation of Duties**, **Inadequate Segregation of Duties**, **Access Approval**, **Periodic Access Review**, **Privileged Access Monitoring**, **Access Review Testing**, plus **Identity and Access Management** and **Role-Based Access Control**.
2. Explicitly contrast **Access Approval** (preventive, at grant) vs **Periodic Access Review** (detective, recurring) and link both to [[Manual Control]], [[Control Ownership]], and [[Recommendation]].
3. Add a thin **User Access Dataset** note: expected fields, reconciliation to directory/PAM/app stores, inclusion of admin/service/dormant/break-glass accounts, and [[Population Completeness]] checks.
4. Wire [[Population Completeness]] / [[Sampling Risk]] / [[Analytics]] examples to privileged-access populations and Access Review Testing procedures.
5. Extend [[IT Controls]] or Privileged Access with the excessive-vs-unauthorized distinction and business-duty ↔ permission mapping.
6. Cross-link [[Internal Audit - Enterprise Fraud Management System]] as a **detective monitoring** case for unauthorized employee access risk—without implying entitlement-control findings.
7. Add account-type coverage (administrator, service, shared, dormant) under Privileged Access or User Access Dataset; do not reuse “dormant controls” language for dormant accounts.
8. Add aliases so common search terms (IAM, RBAC, SoD, privileged accounts, access certification) resolve to the new notes.

---

## Test metadata

- Test ID: Test-01-Privileged-Access
- Suite: Software-Data Baseline onboarding diagnostics
- Output path: `16-Testing/Software-Data/Baseline/Test-01-Privileged-Access.md`
- Vault notes modified by this test: **none** (output file created only)
- Process followed: searched complete vault for required access/IAM/SoD/review/logging terms and public CRA cases; assessed technical–business risk connection; labeled official vs general vs derived content; avoided unsupported CRA access-control claims; did not implement recommendations

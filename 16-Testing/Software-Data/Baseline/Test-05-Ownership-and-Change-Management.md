---
title: "Test-05: Ownership Roles and Change Management Accountability"
note_type: testing
primary_domain: software-data
domains:
  - software
  - data
  - audit
  - risk
  - control
  - organization
  - governance
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
  - ownership
  - change-management
---

# Test-05: Ownership Roles and Change Management Accountability

## Question

What is the difference between business-process ownership, system ownership, technical support and change approval, and how can unclear accountability lead to control failures?

## Answer

| Class | Use in this answer |
|---|---|
| **Official public CRA facts** | Branch mandates (ITB, SIIB, AERB, program/corporate split) from org baseline |
| **Official case-specific** | Named OPI/MAP/co-responsible parties in BI, EFMS, ARNI, charities, cyber cases |
| **General professional** | [[Business Process Owner]], [[System Owner]], [[Technical Support]], [[Data Owner]], [[Control Ownership]], [[Program Owner]], [[IT Controls]], [[Tool Deployment]], [[Three Lines Model]], [[Internal Audit Independence]] |
| **Derived onboarding** | Composed responsibility model and change-lifecycle stages; [[Ownership and Assurance Roles]] synthesis |

**Rule:** Do **not** infer actual CRA ownership for a system unless a public source or case note supports it. Do **not** claim [[Information Technology Branch|ITB]] owns all business processes—the vault explicitly rejects that collapse.

---

### Role explanations

#### Business-process ownership

A [[Business Process Owner]] is accountable for a defined end-to-end **process and its business outcomes**—setting requirements, accepting residual risk within policy, ensuring process-level controls fit, and responding to gaps. This is **not** the same as building every supporting system ([[Technical Support]]).

**Content class:** general professional concept. The public Organization page does not use “business-process owner” as a formal org-chart title; in vault practice accountability often appears as a named program area, OPI, or MAP owner in a published audit.

#### Accountability for program outcomes

[[Program Owner]] language covers program objectives, performance, and sustained policy alignment—often a headquarters [[CRA-Program-Branches|program branch]] in CRA public-audit practice. Related to but not identical to business-process ownership: a program may span several processes; a process may cut across programs.

**Official case-specific examples (not universal rules):**

| Subject | Named accountability pattern | Case |
|---|---|---|
| BI activities | [[Service, Innovation, and Integration Branch|SIIB]] responsibility / MAP lead | BI audit |
| Collections inventory (ARNI) | [[Collections and Verification Branch|CVB]] OPI/MAP pattern | ARNI |
| Charities audit process | Program branch as MAP owner (LPRAB) | Charities |
| EFMS remediation | [[Security Branch]] MAP owner; ITB jointly named for selected items | EFMS |

#### System ownership

A [[System Owner]] is accountable for a named system’s fitness for purpose (onboarding, rule/configuration governance, performance information, policy alignment)—distinct from every user and from generic infrastructure operations. Ownership often **splits** between a business/security custodian and a technical maintainer.

**EFMS (official case-specific, carefully bounded):** Security Branch IFMS maintains/enhances EFMS; ITB Enterprise Fraud Management Services also maintains EFMS; Security Branch is MAP owner with ITB jointly named for selected remediation. The vault does **not** invent a single enterprise “system owner” title or reporting line between those branches.

#### Technical development or support

[[Technical Support]] means building, operating, evolving, and securing technology that enables processes. **Official public CRA fact:** [[Information Technology Branch|ITB]] develops, operates, maintains, and evolves CRA IT. Enabling a capability does **not** automatically make IT accountable for the business outcome or every MAP lead role.

**BI case (official case-specific):** ITB provides BI **service delivery** while SIIB holds BI **responsibility**—the teaching example that “BI involves technology” must not become “ITB owns BI.”

#### Data ownership

A [[Data Owner]] is accountable for defined information assets: meaning, quality expectations, lawful use, access rules, and escalation. Distinct from technical custodians (pipelines/hosting) and from internal audit.

**Official placement signals:** SIIB manages CRA data and information assets; [[Chief Data Officer]] tied to SIIB on sourced material—**not** a claim that one branch owns every dataset in every program.

#### Control ownership

[[Control Ownership]] assigns named accountability for designing, operating, monitoring, and remediating specific [[Control]]s. Without ownership, controls decay and access reviews lapse. IT/security controls often split between business process owners and technical custodians—interfaces must be clear.

#### Change-request initiation → approval → implementation → monitoring

| Stage | Who typically acts (general professional / vault-derived) | Vault support |
|---|---|---|
| **Change-request initiation** | Business or system stakeholder requests a change to meet requirement/risk | Thin; no dedicated note |
| **Change approval** | Authorized approver(s) authorize scope/risk before build/release—**business authorization ≠ technical commit** | **No** [[Change Approval]] note; change management named inside [[IT Controls]] / [[Tool Deployment]] |
| **Code review / quality gate** | Peer/technical review of implementation vs intent | **No** [[Code Review]] note |
| **Implementation and deployment** | Technical teams build/configure/release ([[Tool Deployment]]); SoD in CI/CD mentioned | [[Tool Deployment]], [[IT Controls]] change/release management |
| **Deployment approval** | Go-live authorization distinct from code authorship | **No** [[Deployment Approval]] note |
| **Post-implementation monitoring** | Control/system owners and operations confirm intended behaviour | [[Monitoring and Reporting]]; [[Tool Deployment]] post-deployment monitoring; ARNI theme that monitoring controls worked was limited |

**EFMS official change-governance theme:** business-rule changes were ad hoc across owners; oversight inconsistent; detailed change history not centrally maintained—illustrates weak rule-change accountability, not a license to invent CRA-wide change-board structures.

#### Independent audit or evaluation

[[Internal Audit Independence]] / [[Audit, Evaluation, and Risk Branch|AERB]] (third line): independently assesses governance and controls; may judge whether [[Management Action Plan]]s are reasonable; does **not** own the business process, system, data, or corrective execution. Management owns [[Management Response]] and remediation ([[Management Action Plan Owner]]).

---

### How unclear accountability leads to control failures

| Failure mode | Mechanism | Vault anchors |
|---|---|---|
| **No clear decision authority** | Competing or absent “who decides” → delays, shadow decisions, undocumented risk acceptance | [[Roles and Responsibilities]]; [[Ownership and Assurance Roles]]; [[Business Process Owner]] accepts residual risk |
| **Business rules changed without appropriate approval** | Technical or local edits diverge from authorized policy | EFMS official ad hoc rule changes; [[Automated Control]] / [[IT Controls]] change management |
| **Technical implementation diverging from business intent** | Build/config does not match process requirements | BPO vs [[Technical Support]] split; [[System Owner]] fitness-for-purpose |
| **Controls without an assigned owner** | Design/operation/monitoring orphans; reviews lapse | [[Control Ownership]] (“without ownership, controls decay”) |
| **Incidents falling between teams** | Business vs IT vs security each assume the other will act | Split system maintenance (EFMS); Control Ownership interface gaps; cyber Three Lines teaching |
| **Incomplete monitoring after deployment** | Go-live without verifying control still meets objective | [[Tool Deployment]] + [[Monitoring and Reporting]]; ARNI official: controls existed but monitoring that they worked was limited |

Unclear accountability is especially dangerous in software-enabled processes because **technical ability to change** (ITB/maintainers) can outrun **business authority to accept risk** (process/program/system owners) unless change approval and control ownership are explicit.

---

## Responsibility model

Required model:

```text
Business owner
→ defines business requirement and accepts business risk

System owner
→ accountable for the system lifecycle

Technical team
→ implements and supports technology

Data owner
→ accountable for data governance

Control owner
→ operates or oversees controls

Change approver
→ authorizes changes

Internal Audit
→ independently assesses governance and controls
```

| Node | Vault mapping | Separation clarity |
|---|---|---|
| Business owner | [[Business Process Owner]] / [[Program Owner]] / case OPI-MAP | Strong |
| System owner | [[System Owner]] (often split; case-named maintainers) | Strong concept; title not standardized on org page |
| Technical team | [[Technical Support]] / [[Information Technology Branch|ITB]] | Strong; explicitly ≠ business ownership |
| Data owner | [[Data Owner]] / SIIB–CDO signals | Strong with content-class caution |
| Control owner | [[Control Ownership]] | Strong |
| Change approver | **Missing** as titled role; implied in change management phrases | Weak |
| Internal Audit | AERB / [[Internal Audit Independence]] / [[Three Lines Model]] | Strong; independence preserved |

**Nearest existing composed path:** [[Ownership and Assurance Roles]] relationship model (business/program → ITB support → data owner → control owner → AERB), plus [[IT Controls]] / [[Tool Deployment]] for change/release, plus case-specific MAP owners.

---

## Notes and cases used

### Notes present

- [[Business Process Owner]] · [[Program Owner]] · [[System Owner]] · [[Technical Support]]
- [[Data Owner]] · [[Control Ownership]] · [[Management Action Plan Owner]]
- [[Ownership and Assurance Roles]] · [[Roles and Responsibilities]] · [[Three Lines Model]]
- [[Internal Audit Independence]] · [[Management Action Plan]] · [[Management Response]]
- [[Information Technology Branch]] · [[Service, Innovation, and Integration Branch]] · [[Audit, Evaluation, and Risk Branch]]
- [[CRA-Program-Branches]] · [[CRA-Corporate-Branches]] · [[Chief Data Officer]]
- [[IT Controls]] · [[Tool Deployment]] · [[Monitoring and Reporting]] · [[Automated Control]]
- [[Data Governance]] · [[Governance]] · [[Risk Management]]

### Cases / sources

- [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] — SIIB BI ownership vs ITB service delivery (primary ownership teaching case)
- [[Internal Audit - Enterprise Fraud Management System]] — split maintenance; Security MAP owner; ITB co-named; ad hoc business-rule changes
- [[Internal Audit - Accounts Receivable National Inventory]] — CVB program/MAP pattern; monitoring-that-controls-worked gap
- [[Internal Audit - Charities Audit Process]] — program-branch MAP pattern
- [[Internal Audit - Specific Cyber Security Controls]] — Three Lines language; do **not** invent ITB MAP ownership (protected content)
- Org baseline: [[99-Sources/source-notes/SRC-CRA-Org-2025]]; TBS IA policy: [[99-Sources/source-notes/SRC-TBS-Policy-Internal-Audit]]

### Searched; dedicated-note results

| Sought term | Result |
|---|---|
| Business Process Owner | **Present** |
| System Owner | **Present** |
| Technical Support | **Present** |
| Data Owner | **Present** |
| Control Owner | **Present** as [[Control Ownership]] (aliases) |
| Information Technology Branch | **Present** |
| Relevant program branches | **Present** (SIIB, CVB, LPRAB, CPB, Security, etc.) |
| Change Management | Embedded only ([[IT Controls]], [[Tool Deployment]], etc.)—**no** titled note |
| Change Approval | Not found |
| Code Review | Not found |
| Deployment Approval | Not found |
| System Configuration | Not found as titled note |
| Unauthorized System Changes | Not found |
| Unclear Accountability | Not found as titled note (themes in ownership notes) |

---

## Diagnostic evaluation

| Check | Finding |
|---|---|
| Does the vault claim ITB owns all business processes? | **No.** Explicitly contradicted in [[Technical Support]], [[Ownership and Assurance Roles]], ITB branch note, and BI case. |
| Does it confuse technical implementation with business authorization? | **No** for ownership taxonomy. **Risk remains** because Change Approval / Deployment Approval are not first-class notes separating authorize vs implement. |
| Does it identify control ownership? | **Yes** — [[Control Ownership]]. |
| Does it preserve Internal Audit independence? | **Yes** — AERB does not own process/system/data/corrective execution; MAP owner is management. |
| Are official and derived relationships labelled? | **Yes** — especially [[Ownership and Assurance Roles]] and individual ownership notes’ content-class banners. |

### Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Role distinction | **2** | Clear BPO / program / system / technical / data / control / IA taxonomy with worked BI and EFMS examples. |
| Change-management integration | **1** | Change/release and deployment themes exist; initiation → approval → code review → deployment approval → post-implementation monitoring is not taught as an ownership chain. |
| Accountability-risk analysis | **1** | Strong “controls without owners” and IT≠business themes; incomplete dedicated failure-mode coverage for unclear accountability, unauthorized changes, and between-team incidents. |
| Organizational-layer connection | **2** | Careful mapping from general concepts to official branch mandates and case-specific OPI/MAP without inventing reporting lines. |
| Source and content-class accuracy | **2** | Content-class labels and case bounds are consistent; cyber protected content and non-inference rules are stated. |
| **Total** | **8 / 10** | |

---

## Ambiguous roles

| Ambiguity | Why it matters |
|---|---|
| **System owner vs technical maintainer** | EFMS shows split maintenance without a single vault-assigned “system owner” title—correct caution, but learners may still ask “who is *the* owner?” |
| **Business process owner vs program owner vs MAP owner** | Related but not identical; case language varies (OPI/MAP/responsibility). |
| **Data owner vs CDO vs program data use** | Enterprise CDO signal ≠ ownership of every dataset. |
| **Control owner vs process owner** | A control may be owned separately from the whole process; interfaces can blur. |
| **Change approver** | Role required by the teaching model but not defined as a vault note—easy to conflate with technical deployer or MAP owner. |
| **Second-line vs first-line** for IT/security controls | Three Lines helps; cyber case GRC second-line is historical/planned context, not a universal CRA org label for every control. |

---

## Unsupported organizational relationships

Do **not** claim from the vault:

- ITB owns BI, collections, charities, or all systems that use technology
- A universal CRA “system owner” org-chart title for EFMS or other systems beyond report-named maintenance/MAP roles
- Reporting lines between Security Branch and ITB beyond collaboration stated in cases
- ITB MAP ownership on the cyber case (protected content; vault warns against invention)
- That AERB owns remediation because it publishes audits or judges MAP reasonableness
- That SIIB/CDO owns every program dataset
- Named enterprise change-advisory-board structures or code-review mandates not present in public sources summarized here

---

## Missing ownership notes

Ownership taxonomy is comparatively mature. Gaps concentrate on **change accountability** and named failure modes:

- Change Management (end-to-end lifecycle note)
- Change Approval (business/system authorization role)
- Code Review
- Deployment Approval
- System Configuration (ownership of config vs code)
- Unauthorized System Changes
- Unclear Accountability (failure-mode note linking ownership gaps → control failures)
- Change-request initiation role / RACI for software changes
- Post-implementation review ownership (beyond generic monitoring)

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Create **Change Management**, **Change Approval**, **Code Review**, and **Deployment Approval** notes that separate initiate → authorize → build/review → deploy → monitor, linked to [[Business Process Owner]], [[System Owner]], [[Technical Support]], and [[Control Ownership]].
2. Add **Unauthorized System Changes** and **Unclear Accountability** failure-mode notes with pointers to EFMS rule-change themes and ARNI monitoring gaps—without overstating current CRA control weakness.
3. Extend [[Ownership and Assurance Roles]] with an explicit **Change approver** row in the relationship model (labelled derived until case-supported).
4. Add a short software-change RACI example (BI or EFMS) with content-class columns: who requests, who approves business intent, who implements, who deploys, who monitors, who assures.
5. Cross-link [[Tool Deployment]] post-implementation monitoring to [[Control Ownership]] and [[Monitoring and Reporting]] as an ownership test, not only a technical checklist.
6. Keep reinforcing the non-inference rule on system ownership titles; prefer “report-named maintenance/MAP roles” language in learning paths.
7. Add aliases so searches for “change approval,” “CAB,” “deployment approval,” and “accountability gap” resolve to the new notes.

---

## Test metadata

- Test ID: Test-05-Ownership-and-Change-Management
- Suite: Software-Data Baseline onboarding diagnostics
- Output path: `16-Testing/Software-Data/Baseline/Test-05-Ownership-and-Change-Management.md`
- Related earlier org diagnostic: `16-Testing/Baseline/Test-05-Ownership-and-Assurance.md` (ownership/assurance focus; this test adds change-management accountability)
- Vault notes modified by this test: **none** (output file created only)
- Process followed: searched ownership/change/branch terms and public cases; assessed role separation; avoided unsupported CRA system-ownership inference; labelled official vs derived content; did not implement recommendations

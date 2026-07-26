---
title: "Test-04: Cross-Branch Accountability (Integrated Baseline)"
note_type: testing
primary_domain: governance
domains:
  - organization
  - business
  - software
  - data
  - risk
  - control
  - audit
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
  - integrated
  - ownership
  - accountability
  - multidisciplinary
---

# Test-04: Cross-Branch Accountability (Integrated Baseline)

## Question

How can unclear accountability between a program branch, ITB, data owners and control owners contribute to control failures?

**Discipline:** Distinguish official branch mandates from general ownership concepts. Do **not** infer ownership of non-public CRA systems. Do **not** portray [[Audit, Evaluation, and Risk Branch|AERB]] as operating program controls. Do **not** imply [[Information Technology Branch|ITB]] owns program outcomes merely because technology is involved.

---

## Answer

### Official public CRA organizational facts

Supported by branch notes and [[99-Sources/source-notes/SRC-CRA-Org-2025]] (Ministerial Transition 2025 Organization page baseline):

| Branch / structure | Official public fact (vault-supported) |
|---|---|
| [[CRA-Program-Branches]] | Six HQ program branches centrally organize and provide technical and policy support for program delivery |
| [[Information Technology Branch\|ITB]] | Develops, operates, maintains, and evolves CRA IT; corporate branch |
| [[Service, Innovation, and Integration Branch\|SIIB]] | Program branch; manages CRA data and information assets and related governance/quality frameworks; AC also Chief Data Officer / Chief Service Officer (org page) |
| [[02-Organization/Branches/Security Branch]] | Corporate branch; protects people, information, and assets; centralized security coordination; Agency Security Officer leadership |
| [[Audit, Evaluation, and Risk Branch\|AERB]] | Corporate branch; independent and objective assurance/advice; internal audit and program evaluation; enterprise risk oversight and advice |

**Case-specific official facts (not universal ownership rules):**

| Case | Named accountability pattern |
|---|---|
| [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] | SIIB holds BI responsibility / MAP lead; ITB provides BI service delivery and collaboration—not automatic BI business ownership |
| [[Internal Audit - Enterprise Fraud Management System]] | Security Branch MAP owner; ITB co-named for selected technical actions; AERB publishes assurance |
| [[Internal Audit - Accounts Receivable National Inventory]] | CVB OPI/MAP for ARNI program |
| [[Internal Audit - Specific Cyber Security Controls]] | Security Branch management respondent; report describes Three Lines language (CISD first line; planned GRC second line; AERB third line)—protected technical findings not reconstructed |

The public Organization page **does not** formally define “business-process owner,” “system owner,” “data owner,” or “control owner” as org-chart titles.

---

### General professional responsibility model

| Role | Accountability (general professional) | Vault anchors |
|---|---|---|
| **Program branch / business owner** | Business outcomes, requirements, residual process risk; often OPI/MAP pattern in audits | [[Program Owner]], [[Business Process Owner]], [[Audit Client]] |
| **System owner** | Named system fitness for purpose, rule/config governance, performance information—distinct from every user and from generic hosting | [[System Owner]] |
| **ITB / technical support** | Build, run, evolve technology enabling the process—**not** automatic ownership of business outcomes | [[Technical Support]], [[02-Organization/Branches/Information Technology Branch|ITB]] |
| **Data owner** | Definitions, quality expectations, lawful use, remediation priority for defined information assets | [[Data Owner]], [[Data Governance]] |
| **Control owner** | Design, operate, monitor, and remediate a specific control (may split with technical custodians) | [[Control Ownership]] |
| **Security function** | Security governance, protection, and/or monitoring where applicable (first- or second-line depending on control) | [[02-Organization/Branches/Security Branch]] mandate; [[Cybersecurity]]; [[Monitoring and Alerting]]; cyber case Three Lines language |
| **Change approver** | Authorizes business intent/risk of a change before implementation—≠ implementer ≠ deployment authority | [[Change Approval]], [[Change Management]], [[Deployment Approval]] |
| **Management** | Owns risks, controls, [[Management Response]], and [[Management Action Plan]] execution | [[Management Action Plan Owner]] |
| **Internal Audit (AERB)** | Independent assurance/evaluation; may judge MAP reasonableness; does **not** own process, system, data, or corrective execution | [[Internal Audit Independence]], [[Three Lines Model]] |

Enterprise [[Chief Data Officer]] / SIIB data-asset mandate ≠ sole “data owner” of every program dataset ([[Data Owner]], [[Ownership and Assurance Roles]]).

---

### Derived onboarding interpretation

How concepts may interact for teaching—**not** an official CRA operating model and **not** a claim about non-public systems:

```text
Program / business owner
→ sets outcomes and requirements; accepts residual process risk

System owner
→ accountable for system lifecycle fitness and configuration governance

ITB / technical support
→ implements and supports technology; may co-own technical MAP actions

Data owner
→ accountable for data definitions, quality, and permitted use

Control owner
→ performs or oversees specific controls (business and/or technical custodian split)

Security function
→ provides security governance or monitoring where applicable

Change approver → Deployment authority
→ authorize intent / authorize go-live (implementer is not automatically approver)

Management (MAP owner)
→ remediates findings

AERB
→ independently audits, evaluates, or supports enterprise risk oversight/advice
→ does not operate program controls or execute MAPs
```

When these seams are unclear, [[Unclear Accountability]] predicts failures: controls without owners, unapproved changes, incomplete post-deployment monitoring, and issues that fall between process, system, technical, and data roles.

---

### How unclear accountability contributes to control failures

| Failure mode | Governance consequence | Technical / control consequence | Vault anchors |
|---|---|---|---|
| Unclear requirements | Business need never locked; IT builds to assumptions | Wrong [[System Configuration]], misaligned rules/reports | [[Business Process Owner]], [[Unclear Accountability]] |
| Conflicting priorities | Program vs IT vs security optimize different goals | Deferred hardening, delayed fixes, local workarounds | [[Ownership and Assurance Roles]], cases with multi-party MAPs |
| Controls without owners | Self-assessment and remediation lapse | Access reviews, reconciliations, monitoring not performed | [[Control Ownership]], [[Periodic Access Review]] theme |
| Changes without business approval | Technical delivery outruns authorized intent | [[Unauthorized System Changes]]; production logic ≠ approved policy | [[Change Approval]], [[Change Management]] |
| Data-quality issues without accountable resolution | Stewards/custodians escalate into a vacuum | Persistent incompleteness/inaccuracy in feeds and reports | [[Data Owner]], [[Data Governance]], [[Data Quality]] |
| Incidents passed between teams | No single accountable resolver | Long MTTD/MTTR; monitoring without response ownership | [[Monitoring and Alerting]], [[Unclear Accountability]] |
| Monitoring gaps | No owner for detective coverage or alert triage | Blind spots after deploy; alerts without clearance | [[Monitoring and Alerting]], [[Monitoring and Reporting]] |
| Action plans without accountable owners | Recommendations “accepted” but orphaned | Control deficiencies persist after audit | [[Management Action Plan Owner]], [[Internal Audit Independence]] |
| Duplicated or missing controls | Overlap looks like coverage; gaps look like “someone else’s job” | Redundant tooling **or** absent preventive/detective controls | [[Control Ownership]], [[Three Lines Model]] |

**Worked bounded illustrations (not current-state CRA weakness claims):**

- **BI case:** technology involvement must not collapse into “ITB owns BI”; unclear roles/definitions were a published improvement theme ([[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]]).
- **EFMS case:** split maintenance (Security Branch / ITB) with named MAP lead shows why system work and MAP ownership must be explicit ([[Internal Audit - Enterprise Fraud Management System]]).
- **Cyber case:** first / second / third line language shows security monitoring/assurance layers without reconstructing protected findings ([[Internal Audit - Specific Cyber Security Controls]]).

---

## Responsibility model

```text
Program or business owner
→ accountable for business outcome and requirements

System owner
→ accountable for system lifecycle

ITB or technical support
→ implements and supports technology

Data owner
→ accountable for data governance

Control owner
→ performs or oversees controls

Security function
→ provides security governance or monitoring where applicable

Change approver / deployment authority
→ authorize change intent / go-live (derived teaching)

Management (MAP owner)
→ owns corrective action

AERB
→ independently audits, evaluates or supports enterprise risk functions
→ does NOT operate program controls
```

Primary composed source: [[Ownership and Assurance Roles]]. Failure-mode concept: [[Unclear Accountability]].

---

## Notes and sources used

### Official organization / sources

- [[CRA-Program-Branches]] · [[CRA-Corporate-Branches]] · [[CRA-Organizational-Overview]]
- [[02-Organization/Branches/Information Technology Branch|ITB]] · [[Service, Innovation, and Integration Branch]]
- [[02-Organization/Branches/Security Branch]] · [[Audit, Evaluation, and Risk Branch]]
- [[99-Sources/source-notes/SRC-CRA-Org-2025]]
- [[99-Sources/source-notes/SRC-TBS-Policy-Internal-Audit]]

### Ownership / governance concepts

- [[Ownership and Assurance Roles]] · [[Unclear Accountability]]
- [[Business Process Owner]] · [[Program Owner]] · [[System Owner]] · [[Technical Support]]
- [[Data Owner]] · [[Control Ownership]] · [[Data Governance]] · [[Chief Data Officer]]
- [[Change Requester]] · [[Change Approval]] · [[Deployment Approval]] · [[Change Management]]
- [[Management Action Plan]] · [[Management Action Plan Owner]] · [[Management Response]]
- [[Internal Audit Independence]] · [[Three Lines Model]] · [[Audit Client]] · [[Roles and Responsibilities]]

### Technical / control consequences

- [[System Configuration]] · [[Unauthorized System Changes]]
- [[Monitoring and Alerting]] · [[Monitoring and Reporting]]
- [[IT Controls]] · [[Cybersecurity]] · [[Change Management Map]]

### Cases

- [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]]
- [[Internal Audit - Enterprise Fraud Management System]]
- [[Internal Audit - Specific Cyber Security Controls]]
- [[Internal Audit - Accounts Receivable National Inventory]] (CVB program OPI/MAP pattern)

---

## Diagnostic evaluation

### Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Organizational accuracy | **2** | Program vs corporate branches and ITB/SIIB/Security/AERB mandates are sourced; case OPI/MAP patterns labeled case-specific. |
| Role separation | **2** | Process/program, system, technical support, data, control, change approver, management, and AERB are separated; ITB ≠ program owner; AERB ≠ MAP executor. |
| Technical and control-failure reasoning | **2** | [[Unclear Accountability]] plus change, configuration, monitoring, data-quality, and MAP-ownership notes support governance→technical failure chains. |
| Official-versus-derived labelling | **2** | [[Ownership and Assurance Roles]] and concept notes explicitly separate official org facts, case-specific facts, general professional concepts, and derived models. |
| Onboarding usefulness | **2** | Unified ownership primer + worked BI/EFMS examples + failure-mode note make the question answerable without inventing org charts. |
| **Total** | **10 / 10** | |

### Checks

| Check | Finding |
|---|---|
| Assign unsupported ownership? | **Avoidable** — vault forbids inventing non-public system owners and warns against org-page ownership titles that do not exist. |
| Imply ITB owns program outcomes? | **No** — Technical Support / Ownership notes and BI case explicitly block this. |
| Preserve Internal Audit independence? | **Yes** — AERB mandate + Internal Audit Independence + MAP Owner. |
| Control and data ownership separated? | **Yes** — Control Ownership vs Data Owner / Data Governance. |
| Branch mandates cited? | **Yes** — ITB, SIIB, Security Branch, AERB, program-branch structure. |

---

## Unsupported relationships

Do **not** claim from the vault that:

- The CRA Organization page formally defines business-process owner, system owner, data owner, or control owner
- ITB owns every technology-enabled business process or program outcome
- AERB operates program controls or owns MAP execution because it publishes recommendations or provides enterprise risk advice
- SIIB/CDO ownership of enterprise data assets makes SIIB owner of every operational dataset in every program
- EFMS or cyber cases establish a universal CRA system-owner org chart or current control failures
- Change Approver / Deployment Approval are official CRA CAB titles
- Any non-public system’s actual ownership can be inferred from branch mandates alone

---

## Ambiguous roles

| Ambiguity | Why it remains |
|---|---|
| Program owner vs business-process owner | Related but not identical; a program may span processes ([[Program Owner]]) |
| Data owner vs CDO vs SIIB | Official enterprise data leadership ≠ per-dataset operational owner |
| System owner vs ITB maintainer vs Security IFMS | EFMS shows split maintenance; “system owner” remains a general concept illustrated case-by-case |
| Security function vs Security Branch vs second-line GRC | Mandate + cyber case Three Lines language; not a single universal RACI for every control |
| Region vs HQ program ownership | Regions deliver; HQ often appears as OPI/MAP—language varies by case |
| Control owner vs technical custodian | Split acknowledged; interface design left to engagement-specific mapping |

---

## Missing branch links

| Gap | Detail |
|---|---|
| [[Unclear Accountability]] → branch notes | Failure-mode note links ownership concepts but not ITB/SIIB/Security/AERB directly |
| Per-program RACI examples beyond BI/EFMS/ARNI | Strong patterns exist for those cases; not every program branch has a worked accountability vignette |
| Monitoring ownership when Security Branch ≠ system owner | Assembled from Monitoring and Alerting + cases; no single cross-branch monitoring-RACI note |
| Incident handoff between program / ITB / security | Implied by Unclear Accountability; not a dedicated incident-accountability note |

*Not missing:* Ownership and Assurance Roles primer; dedicated owner concept stubs; change-approver chain; MAP owner vs AERB independence.

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Add Related links from [[Unclear Accountability]] to [[02-Organization/Branches/Information Technology Branch|ITB]], [[Service, Innovation, and Integration Branch]], [[02-Organization/Branches/Security Branch]], and [[Audit, Evaluation, and Risk Branch]], labeled as illustration targets—not reporting lines.
2. Add a short failure-mode subsection (or expand Unclear Accountability) covering incident handoffs, duplicated/missing controls, and MAP orphans explicitly.
3. Add one more worked accountability vignette for a program branch case (e.g., ARNI/CVB) parallel to the BI table in [[Ownership and Assurance Roles]].
4. Keep change-approver / deployment-authority language labeled general/derived—do not invent an enterprise CAB.
5. Optional thin note: “Security function vs Security Branch” clarifying mandate vs case-specific MAP/Three Lines language.

---

## Test metadata

- Test ID: Test-04-Cross-Branch-Accountability
- Suite: Integrated Baseline multidisciplinary diagnostics
- Output path: `16-Testing/Integrated/Baseline/Test-04-Cross-Branch-Accountability.md`
- Vault substantive notes modified by this test: **none** (output file created only)
- Process followed: searched branch, ownership, change, data governance, monitoring, MAP, and case notes; separated official mandates from general concepts and derived models; preserved AERB independence and ITB≠program-owner rules; identified governance and technical failure modes; did not implement recommendations

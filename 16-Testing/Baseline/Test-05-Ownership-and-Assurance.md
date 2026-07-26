---
title: "Test-05: Ownership and Assurance Roles"
note_type: testing
primary_domain: organization-business
domains:
  - organization
  - audit
  - risk
  - data
  - software
  - testing
classification: public
content_origin: derived-analysis
authoritative: false
official_source: false
as_of_date: 2026-07-25
last_verified: 2026-07-25
source_status: diagnostic
review_status: analytical-draft
approved_for_ai_retrieval: false
tags:
  - testing
  - baseline
  - ownership
  - assurance
  - onboarding
---

# Test-05: Ownership and Assurance Roles

## Question

What is the difference between a branch owning a business process, ITB supporting its technology, a data owner being responsible for information, a control owner operating a control, and AERB auditing or evaluating the activity?

## Answer

These roles answer different questions. Confusing them is how interns invent false statements such as “IT owns the program,” “the data team owns the business outcome,” or “Internal Audit owns the fix.”

**Important content-class rule:** the public CRA Organization page defines **branch mandates** (program vs corporate, ITB, SIIB, AERB, etc.). It does **not** formally define every ownership term below (business-process owner, system owner, data owner, control owner, audit client). Those distinctions come from vault concept notes (mostly `content_origin: general-professional-knowledge`), case-specific report language (OPI/MAP), and derived onboarding synthesis.

### Separate explanations

#### Business-process ownership

Who is accountable for the **business outcome** and the process that produces it (collections inventory, charities audit process, BI program outcomes, etc.)?

- In vault practice, this often maps to a headquarters **program** (or sometimes corporate security) area named as OPI / responsible program area in a public audit.
- **Class:** case-specific official fact when a report names the area; otherwise **general professional concept** / derived onboarding. Not a complete CRA org-page dictionary of “business-process owner.”

#### Program accountability

Who is publicly responsible for the **program’s technical/policy support or delivery framework** at HQ (and who appears as MAP owner when that program is audited)?

- Vault: [[CRA-Program-Branches]] provide technical and policy support for program delivery; regions deliver via field offices ([[CRA-Regions]]).
- Public audits often name a program branch as OPI/MAP owner (e.g., CVB for ARNI; LPRAB for charities).
- **Class:** program vs corporate split and branch mandates = **official public CRA facts** ([[99-Sources/source-notes/SRC-CRA-Org-2025]]). Which branch is accountable for a given engagement subject = **official case-specific** when the report says so.

#### System ownership

Who is accountable for a **named system** (its fitness for purpose, onboarding, rules, performance information)—distinct from merely hosting servers?

- Vault has strong case examples (EFMS maintained by Security Branch IFMS and ITB Enterprise Fraud Management Services; ARNI DSS discussed under CVB program context) but **no dedicated “System Owner” concept note**.
- **Class:** **official case-specific** when a report assigns system maintenance/response roles; **general professional concept** for the abstract “system owner” term. Do not assume ITB is system owner for every technology-enabled process.

#### Technical support

Who **builds, operates, or evolves the technology** that enables a process?

- Vault public mandate: [[Information Technology Branch|ITB]] develops, operates, maintains, and evolves CRA IT ([[02-Organization/Branches/Information Technology Branch|ITB]]).
- Case pattern: ITB provides BI **service delivery** while SIIB holds BI **responsibility** ([[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]]).
- **Class:** ITB mandate = **official public CRA fact**. “Technical support ≠ business ownership” = **derived onboarding interpretation**, reinforced by case text.

#### Data ownership

Who is accountable for **information assets**—definitions, quality, governance, permitted use—not only for storing files?

- Vault general concepts: [[Data Governance]], [[Roles and Responsibilities]], [[Chief Data Officer]].
- Official CRA placement: SIIB AC is also Chief Data Officer; SIIB manages CRA data and information assets ([[Service, Innovation, and Integration Branch]], org baseline).
- BI case: SIIB responsibility for BI activities; CDO is SIIB AC.
- **Class:** SIIB/CDO placement and data-asset mandate = **official public CRA facts**. Generic “data owner / steward / custodian” vocabulary = **general professional concepts** ([[Data Governance]]). Enterprise CDO ≠ sole owner of every dataset used in every program.

#### Control ownership

Who designs, operates, monitors, and remediates a **specific control**?

- Vault note [[Control Ownership]] (`content_origin: general-professional-knowledge`): named accountability for controls; IT/security controls often split between business process owners and technical custodians.
- [[Three Lines Model]]: first line owns/manages risks and controls in operations; second line monitors/challenges; third line assures.
- **Class:** **general professional concept**, applied in cyber case’s public Three Lines language (CISD first line; planned GRC second line; AERB third line) as **official case-specific** description in that report.

#### Independent assurance

Who provides **objective audit/evaluation** of governance, risk, controls, or program performance without owning the audited activity?

- Vault: [[Audit, Evaluation, and Risk Branch|AERB]] public mandate for independent assurance/evaluation/enterprise risk; publishes via [[Internal Audit and Program Evaluation]].
- [[Three Lines Model]] third line; cyber case names AERB as third line.
- TBS policy source note: formal management responses; CAE independence expectations ([[99-Sources/source-notes/SRC-TBS-Policy-Internal-Audit]]).
- **Class:** AERB mandate and publishing role = **official public CRA facts**. Three Lines framing = **general professional** + **case-specific** where a report uses it. AERB does **not** become process owner by auditing.

#### Audit-client responsibility

Who is the **audited management party**—cooperates with the engagement, provides evidence, responds to findings—without becoming the auditor?

- Vault uses “OPI / program owner,” “management response owner,” and “MAP owner” in case org sections; [[CRA-Acronym-Dictionary]] defines OPI as business area primarily responsible for the audited subject (points to [[Scope]], which does **not** currently expand OPI).
- No dedicated “audit client” note.
- **Class:** OPI/MAP labels in cases = **official case-specific** when report-supported. “Audit client” as a teaching term = **general professional / derived onboarding**.

#### Management responsibility for corrective action

Who must **agree (or respond), plan, own, and implement** fixes after recommendations?

- Vault: [[Management Response]] → [[Management Action Plan]] → [[Follow-up]].
- [[Management Action Plan]]: auditors may review draft MAPs for completeness but **do not own execution**.
- Cases show named MAP owners (e.g., SIIB for BI; Security Branch for cyber/EFMS; CVB for ARNI).
- **Class:** MAP/response pattern = **general professional concepts** + **official case-specific** owners. Independence preserved: AERB assures; management corrects.

### Relationship model

```text
Business / program branch (or named program area)
→ owns business outcome / process accountability
→ often appears as OPI and/or MAP owner in public audits

ITB or technical function
→ supports technology (build/run/evolve systems and services)
→ may be named co-responsible for technical MAP actions
→ does NOT automatically own the business process

Data owner / data accountable role (e.g., CDO / SIIB data-asset mandate; stewards per Data Governance)
→ governs data responsibility (definitions, quality, use)
→ distinct from IT operations and from AERB assurance

Control owner (first line; sometimes split with technical custodians)
→ performs or oversees a specific control
→ accountable for control design/operation/monitoring/remediation

AERB (third line / IA & PE)
→ independently audits or evaluates
→ may judge whether MAPs are reasonable
→ does NOT own the business process, system, data, or corrective execution
```

### Worked example (supported public case)

[[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]]

| Role in the model | Who in this case (vault-supported) | Class |
|---|---|---|
| Business / program ownership of BI activities | [[Service, Innovation, and Integration Branch\|SIIB]] — BI responsibility since 2011; MAP lead | Official case-specific |
| Program users of BI (not MAP lead) | Selected [[Compliance Programs Branch\|CPB]] and [[Collections and Verification Branch\|CVB]] teams | Official case-specific (examined/interviewed) |
| Technical support | [[Information Technology Branch\|ITB]] — BI service delivery; BIDGSC co-chair; collaboration in action plans | Official case-specific |
| Data leadership signal | Chief Data Officer = SIIB Assistant Commissioner | Official org + case-specific |
| Independent assurance | [[Audit, Evaluation, and Risk Branch\|AERB]] — publishing branch; judged MAPs reasonable | Official case-specific |
| Corrective action | SIIB agrees to strengthen BI governance (with ITB/stakeholders as named) | Official case-specific |

This example shows why a software intern must not collapse “BI is a technology topic” into “ITB owns BI.”

Secondary illustration (split tech vs management): [[Internal Audit - Enterprise Fraud Management System]] — Security Branch MAP owner; ITB named co-maintainer/co-responsible for selected actions; AERB publishes assurance.

### Content-class summary

| Statement type | Examples in this answer |
|---|---|
| **Official public CRA facts** | Program vs corporate branch roles; ITB IT mandate; SIIB data/service/CDO mandate; AERB independent assurance mandate ([[99-Sources/source-notes/SRC-CRA-Org-2025]]) |
| **Official case-specific facts** | OPI/MAP/named partners in BI, EFMS, cyber, ARNI, charities, Audit Yield |
| **Derived onboarding interpretation** | The composed ownership model diagram; “learn ITB even when program owns the process”; teaching use of “audit client” |
| **General professional concepts** | [[Control Ownership]], [[Three Lines Model]], [[Data Governance]] steward/custodian language, [[Management Action Plan]] “auditors do not own execution,” [[IT Controls]] line roles |

## Relationship model (compact)

```text
Business branch
→ owns business outcome

ITB or technical function
→ supports technology

Data owner
→ governs data responsibility

Control owner
→ performs or oversees control

AERB
→ independently audits or evaluates
```

Management (not AERB) owns [[Management Response]] / [[Management Action Plan]] corrective action.

## Notes used

### Organization

- [[Audit, Evaluation, and Risk Branch]]
- [[02-Organization/Branches/Information Technology Branch|ITB]]
- [[Service, Innovation, and Integration Branch]]
- [[02-Organization/Branches/Security Branch]]
- [[02-Organization/Branches/Compliance Programs Branch|CPB]]
- [[02-Organization/Branches/Collections and Verification Branch|CVB]]
- [[CRA-Program-Branches]]
- [[CRA-Corporate-Branches]]
- [[CRA-Organizational-Overview]]
- [[CRA-Branch-Relationship-Map]]
- [[CRA-Acronym-Dictionary]]
- [[Organizational-Onboarding-Path]]

### Concepts

- [[Control Ownership]]
- [[Control]]
- [[Three Lines Model]]
- [[Internal Audit and Program Evaluation]]
- [[Management Response]]
- [[Management Action Plan]]
- [[Follow-up]]
- [[Recommendation]]
- [[Scope]]
- [[Data Governance]]
- [[Roles and Responsibilities]]
- [[Chief Data Officer]]
- [[Business Intelligence Governance]]
- [[IT Controls]]
- [[IT Controls]] / [[Security Controls]] (via related links)

### Cases / sources

- [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] (primary example)
- [[Internal Audit - Enterprise Fraud Management System]]
- [[Internal Audit - Specific Cyber Security Controls]]
- [[Internal Audit - Accounts Receivable National Inventory]]
- [[99-Sources/source-notes/SRC-CRA-Org-2025]]
- [[99-Sources/source-notes/SRC-TBS-Policy-Internal-Audit]]
- [[99-Sources/source-notes/SRC-CRA-IA-BI-2024]]

## Diagnostic evaluation

| Check | Finding |
|---|---|
| Roles clearly separated? | **Partially.** Cases and branch notes separate OPI/MAP, ITB support, AERB assurance well. Abstract owner types are scattered across general-professional notes; no single ownership primer. |
| Avoid “ITB owns every tech-enabled process”? | **Yes** in org onboarding and BI/EFMS case labels; Control Ownership explicitly splits business vs technical custodians. |
| Preserve IA independence? | **Yes** — AERB mandate, Three Lines, MAP note (“do not own execution”), TBS IA policy source. |
| Distinguish management vs audit responsibility? | **Yes** in MAP/Management Response/Follow-up and case MAP-owner labels. |
| Linked to org + case notes? | **Yes** for worked BI example; weaker for abstract “system owner” / “data owner” nodes. |
| Understandable to a software intern? | **If composed** from this test’s model + BI case. Out of the box, an intern must stitch many notes. |

## Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Role clarity | **1** | Distinctions exist in pieces; missing unified owner taxonomy and OPI expansion on [[Scope]]. |
| Independence distinction | **2** | AERB vs management ownership is consistently preserved. |
| Cross-domain linking | **1** | Strong case↔branch labels; concept notes rarely link back to org ownership examples. |
| Source and content-class accuracy | **2** | Org mandates and case roles are official where claimed; ownership vocab mostly labelled general-professional. |
| Onboarding usefulness | **1** | Intern can learn it, but only by assembling fragments; no dedicated ownership/assurance onboarding note. |
| **Total** | **7 / 10** | |

## Ambiguous roles

1. **OPI** — defined in [[CRA-Acronym-Dictionary]] as pointing to [[Scope]], but [[Scope]] does not explain OPI/audit-client.
2. **Data owner vs CDO vs SIIB** — official CDO placement exists; “data owner” for a specific dataset is not operationalized as a vault entity type.
3. **System owner vs ITB maintainer vs Security IFMS** — EFMS shows split maintenance; no canonical “system owner” note to generalize from.
4. **Business-process owner vs program branch vs region** — HQ program support vs regional delivery can both touch a process; ownership language varies by case.
5. **[[Internal Audit and Program Evaluation]]** concept note is general-professional, while AERB branch note carries the official CRA mandate—easy to mix content classes if read alone.
6. **[[Chief Data Officer]]** note is general-professional and avoids incumbents; CRA-specific CDO=SIIB AC lives mainly on org/branch/case notes.

## Unsupported statements

Do **not** claim from the vault:

- That the CRA Organization page formally defines business-process owner, system owner, data owner, or control owner.
- That ITB owns every technology-enabled business process.
- That AERB owns corrective action because it publishes recommendations.
- That the CDO/SIIB data mandate makes SIIB owner of every program dataset.
- That “audit client” is an official CRA org-chart title in this vault.

## Missing concept nodes

| Missing or thin node | Why it matters |
|---|---|
| Business Process Owner | No dedicated note; only scattered mentions |
| System Owner | No dedicated note |
| Data Owner (as distinct from Data Governance / CDO) | Vocabulary used lightly; not a first-class note |
| Audit Client / Auditee | No dedicated note; OPI partially fills the gap |
| OPI explanation on [[Scope]] | Dictionary points here, but Scope body omits OPI |
| Ownership & Assurance primer (MOC) | No single onboarding note assembling the model above |

## Recommended targeted fixes

Do **not** implement in this test. Suggested later work:

1. Create a derived onboarding note (e.g., `Ownership and Assurance Roles`) with the relationship model, content-class labels, and the BI worked example.
2. Expand [[Scope]] (or a small OPI note) to define Office of Primary Interest / audit-client in plain language, matching [[CRA-Acronym-Dictionary]].
3. Add thin concept stubs: Business Process Owner, System Owner, Data Owner—each labelled general-professional unless tied to a case.
4. Link [[Control Ownership]], [[Data Governance]], and [[IT Controls]] to [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] and [[Internal Audit - Enterprise Fraud Management System]] as worked examples.
5. Add one sentence on [[02-Organization/Branches/Information Technology Branch|ITB]]: “Technical support and system maintenance roles are not automatic business-process ownership.”
6. Cross-link [[Chief Data Officer]] general note to [[Service, Innovation, and Integration Branch]] for the CRA-specific official placement.

## Test metadata

- Test ID: Test-05-Ownership-and-Assurance
- Suite: Baseline onboarding diagnostics
- Output path: `16-Testing/Baseline/Test-05-Ownership-and-Assurance.md`
- Vault notes modified by this test: **none** (output file created only)
- Process followed: searched org/process/owner/control/IA notes; distinguished roles; labelled official vs derived vs general-professional; did not invent org-page ownership definitions; connected to BI case (and EFMS as secondary)

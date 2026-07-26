---
title: "Test-02: Organizational Structure (Program / Corporate / Regions)"
note_type: testing
primary_domain: organization-business
domains:
  - organization
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
  - organization
  - onboarding
---

# Test-02: Organizational Structure (Program / Corporate / Regions)

## Question

Explain the difference between CRA program branches, corporate branches and regions to a new software intern.

## Answer

Think of the CRA’s publicly described structure as three kinds of work, not as a detailed org chart of who reports to whom.

Public baseline (vault treatment): [[CRA-Organizational-Overview]] and [[99-Sources/source-notes/SRC-CRA-Org-2025]] — Ministerial Transition **2025** Organization page (page details **2025-09-09**; vault verified **2026-07-25**). The CRA comprises **14 headquarters branches**, a [[Corporate Secretariat]], and **4 regions**. Named individuals on the 2025 organizational chart are a **historical public snapshot**, not confirmed current incumbents.

### What program branches generally do

[[CRA-Program-Branches]] — **six** headquarters branches that **centrally organize and provide technical and policy support** for CRA program delivery.

In plain language: they are the HQ homes for tax/benefits/compliance/recourse/policy/service-and-data program work. They define and support *what* programs are supposed to do nationally (mandates, policies, program design), while much day-to-day delivery happens in the regions.

Examples of program work in the vault:

- Processing, contact centres, benefits → [[Assessment, Benefit, and Service Branch|ABSB]]
- Collections and verification → [[Collections and Verification Branch|CVB]]
- Compliance education/audits/investigations → [[Compliance Programs Branch|CPB]]
- Legislative interpretation, charities, registered plans, excise → [[Legislative Policy and Regulatory Affairs Branch|LPRAB]]
- Service design, data/information assets, performance reporting → [[Service, Innovation, and Integration Branch|SIIB]]
- Impartial recourse → [[Appeals Branch]]

### What corporate branches generally do

[[CRA-Corporate-Branches]] — **eight** headquarters branches that provide **corporate services** for the Agency.

In plain language: they are shared enterprise functions that enable the whole CRA (assurance, money, people, technology, legal, communications/privacy, security, digital transformation direction). They are not the same category as “program delivery” branches, even when they touch every program.

Examples of corporate work in the vault:

- Independent assurance / evaluation / enterprise risk → [[Audit, Evaluation, and Risk Branch|AERB]]
- Enterprise IT → [[Information Technology Branch|ITB]]
- Digital transformation direction → [[Digital Transformation Program Branch|DTPB]]
- Finance/administration, HR, legal, public affairs, security → corresponding corporate branch notes

Also not a corporate branch: [[Corporate Secretariat]] — a separate organizational component supporting Board/Commissioner governance ([[CRA-Corporate-Branches]], [[Corporate Secretariat]]).

### What regions generally do

[[CRA-Regions]] — **four** geographic regions responsible for **program delivery via field offices**.

Each region is led by a [[Regional Assistant Commissioner]]. Public office types used in regional delivery include Tax Services Offices (TSOs), Tax Centres (TCs), National Verification and Collections Centres (NVCCs), Contact Centres, Northern Service Centres, and Centres of Expertise ([[CRA-Regions]], region notes such as [[Ontario Region]]).

In plain language: regions are where much of the CRA’s operational work with taxpayers and benefit recipients actually happens in a geography.

### How headquarters and regional delivery differ

Supported public distinction ([[CRA-Organizational-Overview]], [[CRA-Regions]], [[Organizational-Onboarding-Path]]):

| Layer | Public role (supported) |
|---|---|
| HQ **program** branches | Technical and policy support for programs (national program frameworks) |
| HQ **corporate** branches | Corporate services used across the Agency |
| **Regions** | Deliver programs through field offices in their area of operation |

What the vault does **not** claim as official: detailed reporting lines from a region up through a specific HQ branch, or an internal “who owns every system” hierarchy. [[CRA-Branch-Relationship-Map]] labels derived teaching links separately from official public / case-specific relationships. Do not invent reporting lines beyond those labels.

### Why a software intern needs to understand the distinction

A software intern will hear branch acronyms in tickets, audits, and stakeholder lists. The category tells you *what kind of problem* you are looking at:

1. **Program branch** — business process / program ownership themes (e.g., collections inventory, charities compliance, assessment/benefits).
2. **Corporate branch (ITB)** — enterprise technology build/run themes; systems often serve many programs.
3. **Corporate branch (AERB)** — independent assurance; AERB publishes the public audits/evaluations used as learning cases, and is not the “owner” of the business process being audited.
4. **Region** — field delivery and local workload; a national program may be designed at HQ and executed regionally (e.g., ARNI themes involving [[Collections and Verification Branch|CVB]] and regions).

Without this map, it is easy to assume “IT owns the program,” “audit owns the fix,” or “one branch reports to another” when public sources only show collaboration or case-specific roles ([[Organizational-Onboarding-Path]] quick-answer table).

### How AERB, ITB, and a program branch fit

Using only supported structure + common vault case patterns:

- **[[Audit, Evaluation, and Risk Branch|AERB]] (corporate):** independent internal audit, program evaluation, and enterprise risk support. Publishes public results via [[Internal Audit and Program Evaluation]]. In cases, AERB is typically the assurance publisher / third-line context — not the program operator.
- **[[Information Technology Branch|ITB]] (corporate):** develops, operates, maintains, and evolves CRA IT (and provides some IT solutions to CBSA). Appears when systems, BI service delivery, or tech controls are in scope — even when a program branch owns the business outcome.
- **A program branch (example [[Collections and Verification Branch|CVB]] or [[Compliance Programs Branch|CPB]]):** HQ technical/policy home for that program area; often named as OPI / MAP owner in public audits. Regions may still execute workload in the field.

Cross-branch illustration (case-specific, not a reporting line): [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] involves [[Service, Innovation, and Integration Branch|SIIB]] (program; BI responsibility / MAP lead), [[Information Technology Branch|ITB]] (corporate; BI service delivery), program teams in CPB/CVB, and regional BI QA stakeholders — with [[Audit, Evaluation, and Risk Branch|AERB]] as publishing assurance branch.

```text
Public audit case
→ AERB (publisher / assurance) — corporate
→ named program branch (OPI / MAP) — program
→ ITB / Security / SIIB / regions when listed — partners / delivery context
```

(Pattern from [[CRA-Branch-Relationship-Map]] / [[Organizational-Onboarding-Path]]; do not read as an org-chart reporting chain.)

### Branches and regions represented in the vault

#### Program branches (6)

1. [[Appeals Branch]]
2. [[Assessment, Benefit, and Service Branch|ABSB]]
3. [[Collections and Verification Branch|CVB]]
4. [[Compliance Programs Branch|CPB]]
5. [[Legislative Policy and Regulatory Affairs Branch|LPRAB]]
6. [[Service, Innovation, and Integration Branch|SIIB]]

#### Corporate branches (8)

1. [[Audit, Evaluation, and Risk Branch|AERB]]
2. [[Digital Transformation Program Branch|DTPB]]
3. [[Finance and Administration Branch]]
4. [[Human Resources Branch|HRB]]
5. [[Information Technology Branch|ITB]]
6. [[Legal Services Branch]]
7. [[Public Affairs Branch]]
8. [[Security Branch]]

#### Other organizational component (not a branch)

- [[Corporate Secretariat]]

#### Regions (4)

1. [[Atlantic Region]]
2. [[Quebec Region]]
3. [[Ontario Region]]
4. [[Western Region]]

#### Historical caution note (not current structure)

- [[Domestic Compliance Programs Branch]] — historical public naming; do not treat as a seventh current program branch or as proven succession to [[Compliance Programs Branch|CPB]].

## Notes used

- [[CRA-Organizational-Overview]]
- [[CRA-Program-Branches]]
- [[CRA-Corporate-Branches]]
- [[CRA-Regions]]
- [[CRA-Organization-Map]]
- [[CRA-Branch-Relationship-Map]]
- [[Organizational-Onboarding-Path]]
- [[CRA-Acronym-Dictionary]]
- [[CRA Headquarters Branches]]
- [[01-Organization/CRA Regions]]
- [[Corporate Secretariat]]
- [[Audit, Evaluation, and Risk Branch]]
- [[Information Technology Branch]]
- [[Collections and Verification Branch]] (example program branch)
- [[Compliance Programs Branch]]
- [[Service, Innovation, and Integration Branch]]
- [[Ontario Region]] (example region note)
- [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]]
- [[Internal Audit - Accounts Receivable National Inventory]]
- [[Learning Path - New Intern]]
- [[ORGANIZATION_VALIDATION_REPORT]]
- [[Domestic Compliance Programs Branch]]

## Source notes

- [[99-Sources/source-notes/SRC-CRA-Org-2025]] — primary official organization baseline (Ministerial Transition 2025 Organization page; page details **2025-09-09**)
- [[99-Sources/CRA-Public-Source-Register]] — register entry for the Organization page and related materials
- Supporting official pages cited from organization notes (not re-derived here as new structure): Internal Audit and Program Evaluation landing page (AERB publishing context); Commissioners page used elsewhere in the vault for incumbent people, not for branch inventory

Primary public URL:

- https://www.canada.ca/en/revenue-agency/corporate/about-canada-revenue-agency-cra/ministerial-transition-2025/organization.html

## Diagnostic evaluation

| Check | Finding |
|---|---|
| Does the vault explain function rather than merely list names? | **Yes.** Indexes state program = technical/policy support; corporate = corporate services; regions = program delivery via field offices. Branch notes include public mandates and intern-oriented “why it matters” sections. [[Organizational-Onboarding-Path]] teaches the distinction stepwise. |
| Does it contain all publicly documented branches? | **Yes** for the 2025 baseline: 6 program + 8 corporate = 14 HQ branches, plus [[Corporate Secretariat]]. |
| Does it represent the four regions? | **Yes:** Atlantic, Quebec, Ontario, Western, with a [[CRA-Regions]] index. |
| Does it distinguish headquarters from regional delivery? | **Yes**, repeatedly in overview, regions notes, onboarding path, and case organizational sections. |
| Does it avoid unsupported reporting relationships? | **Mostly yes** in the canonical layer: [[CRA-Branch-Relationship-Map]] labels official vs derived vs historical. This answer invents none. Residual risk: a reader who ignores labels could over-read “derived” pairings as reporting lines. |
| Is the explanation understandable without prior CRA knowledge? | **Largely yes** if the intern follows [[Organizational-Onboarding-Path]] / [[CRA-Organizational-Overview]]. Naming traps remain (see confusing explanations). |
| Does it identify the date of the organizational structure? | **Yes:** page details **2025-09-09**; organizational period Ministerial Transition **2025**; `as_of_date` / `last_verified` **2026-07-25**; chart people marked historical snapshot. |

## Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Structural completeness | **2** | All 14 current HQ branches, Corporate Secretariat, and four regions are represented. |
| Functional explanation | **2** | Vault explains roles of program vs corporate vs regions, not only inventories. |
| Beginner clarity | **1** | Strong teaching path exists, but naming traps and dual `01-`/`02-` folders can confuse a first-week intern. |
| Source traceability | **2** | Overview, indexes, and branches point to [[99-Sources/source-notes/SRC-CRA-Org-2025]] and the Organization URL. |
| Temporal accuracy | **2** | Structure dated; incumbents on 2025 chart treated as historical snapshot; older 13-branch / DCPB naming kept historical. |
| **Total** | **9 / 10** | |

## Omissions

- No complete public directorate/division org charts below branch level (vault correctly notes this limitation; not scored as a failure against public sources).
- No exhaustive office inventory by region (TSOs/TCs/etc. are types, not a full directory).
- Appeals Branch and several corporate branches lack a vault-verified short acronym (documented in [[CRA-Acronym-Dictionary]]); does not block this structural explanation.
- Legacy `01-Organization/` folder does not contain parallel notes for every branch (e.g., ABSB, LPRAB); canonical coverage is in `02-Organization/`.

## Confusing explanations

1. **[[Digital Transformation Program Branch|DTPB]] name contains “Program” but is a corporate branch** — easy intern misclassification without reading [[CRA-Corporate-Branches]].
2. **“Program delivery” wording** appears both for HQ program branches (“support for the delivery of CRA programs”) and for regions (“program delivery via field offices”). Correct, but requires the HQ-support vs field-execution distinction to be taught explicitly ([[CRA-Program-Branches]], [[CRA-Regions]]).
3. **Dual organization layers** (`01-Organization/` legacy summaries vs `02-Organization/` canonical notes) can surface thinner or differently titled notes first (also observed in Test-01 for SIIB/CPB/ITB/CVB).
4. **[[Service, Innovation, and Integration Branch|SIIB]] is a program branch** while owning enterprise-sounding data/performance functions — correct per official classification, but counterintuitive if “corporate” is assumed to mean “enterprise-wide.”

## Unsupported relationships

None asserted in this test answer.

Vault safeguards observed:

- Relationship map labels **official / derived / historical**.
- Branch notes separate “Officially supported relationships” from “Derived onboarding interpretation.”
- Cases distinguish publishing assurance (AERB), OPI/MAP owners, and interviewed stakeholders.

Potential reader misuse (not vault claims): treating derived ABSB↔regions or CPB↔CVB “complements” language as official reporting lines if labels are ignored.

## Recommended targeted fixes

Do **not** implement in this test. Suggested later work:

1. Add a one-screen “three buckets” callout near the top of [[CRA-Organizational-Overview]] or [[Organizational-Onboarding-Path]]: Program (HQ technical/policy support) · Corporate (enterprise services) · Regions (field delivery) — with an explicit “no reporting lines invented” sentence.
2. Add a beginner caution on [[Digital Transformation Program Branch|DTPB]]: “Despite ‘Program’ in the name, this is a **corporate** branch.”
3. Strengthen the HQ vs region sentence to always pair: “HQ program branches support; regions deliver via field offices.”
4. Reduce dual-folder confusion for onboarding (redirect-only legacy notes or a single recommended entry point already partially done via [[CRA-Organization-Map]] “Legacy notes” section — make that the default intern entry).
5. Optional intern micro-example card: AERB (assurance) + ITB (technology) + one program branch + one region, linked to the BI or ARNI case, with relationship labels pre-filled.

## Test metadata

- Test ID: Test-02-Organizational-Structure
- Suite: Baseline onboarding diagnostics
- Output path: `16-Testing/Baseline/Test-02-Organizational-Structure.md`
- Vault notes modified by this test: **none** (output file created only)
- Process followed: complete-vault search; organizational overview + source notes; enumerate program/corporate/regions; function-only explanation from public sources; chart people treated as historical; no invented reporting lines

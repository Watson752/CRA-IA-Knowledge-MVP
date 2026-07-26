---
title: "Test-01: Objective, Scope, and Criteria"
note_type: testing
primary_domain: audit
domains:
  - audit
  - risk
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
  - audit
  - onboarding
  - objective
  - scope
  - criteria
---

# Test-01: Objective, Scope, and Criteria

## Question

What is the difference between an audit objective, audit scope and audit criteria, and how do they work together?

## Answer

These three terms answer different planning questions. The vault’s concept notes keep them distinct: the objective states **what the engagement seeks to determine**; the scope states **where and when** that determination applies (including exclusions); the criteria state **the standards** used to judge the subject matter. [[Evidence]] is not a fourth standard—it is the information collected to support conclusions against the criteria, inside the scope, for the objective.

**Content-class rule for this answer**

| Class | Role in this answer |
|---|---|
| **Official public-source facts** | Objective, scope, exclusions, criteria, period, and methodology language taken from published CRA case notes (especially the BI audit) |
| **General professional audit knowledge** | Distinctions and relationship model in [[Audit Objective]], [[Scope]], [[Criteria]], [[Evidence]], [[Methodology]], [[Risk]] |
| **Derived onboarding interpretation** | The compact relationship model below, and the teaching statement that unclear objective/scope weakens assurance |

Do **not** treat the Class C concept notes as CRA-specific requirements. The vault does not assert that CRA mandates a particular objective/scope/criteria template beyond what each public report itself states.

### What an audit objective asks

An [[Audit Objective]] states what the audit is intended to accomplish: the subject matter and the purpose of the examination. It answers why the engagement exists and what assurance or insight stakeholders should gain.

Vault Class C framing: objectives are typically expressed as evaluating whether controls, processes, or outcomes meet defined criteria within a specified scope. Vague objectives invite scope creep and make success hard to judge.

### What the scope includes and excludes

[[Scope]] defines boundaries: entities, processes, systems, time periods, locations, and activities **included**, and what is **explicitly excluded**. Exclusions do not automatically mean low risk; they may reflect timing, access, or plan constraints. Scope limitations (restricted data, samples, non-production systems) should be documented so readers interpret conclusions correctly.

### What criteria are used to assess the subject

[[Criteria]] are benchmarks or standards—laws, regulations, policies, professional standards, control frameworks, SLAs, budgets, or adopted performance targets—against which subject matter is evaluated. Without suitable criteria, auditors cannot consistently decide whether a condition is a deficiency or acceptable variation.

Criteria are **not** evidence. [[Evidence]] is the information used to support findings and conclusions when compared to criteria.

### How objective, scope, and criteria constrain evidence collection

Together they form the engagement specification that drives [[Methodology]] and evidence requirements:

- The **objective** decides what question evidence must answer.
- The **scope** decides which populations, periods, organizations, and systems may be examined—and which must not be treated as covered.
- The **criteria** decide what “pass/fail” or “gap” means, so evidence must be relevant to those standards.
- [[Risk]] assessment (as discussed in [[Risk]] and [[Risk Management]]) helps prioritize where limited fieldwork focuses within that frame.

[[Finding]]s typically compare **condition** (from evidence) to **criteria**. Incomplete evidence may force scope-limited or qualified conclusions ([[Evidence]]).

### How an unclear objective or scope can weaken an audit

From Class C notes (especially [[Audit Objective]] and [[Scope]]):

- Vague objectives invite **scope creep** and make it unclear whether the audit succeeded.
- Unstated or shifting scope creates stakeholder misunderstanding about what was and was not reviewed.
- Weak or unstated criteria undermine the defensibility of [[Finding]]s and [[Recommendation]]s.
- Readers may over-read conclusions (e.g., treat a subset-of-controls review as a full posture assessment).

### Compact relationship model

```text
Audit objective
→ defines what the engagement seeks to determine

Audit scope
→ defines boundaries, period, organizations, systems and exclusions

Audit criteria
→ define the standards against which evidence is assessed

Evidence
→ supports conclusions against the criteria within the defined scope
```

### Worked example from a public CRA audit case

Primary case: [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]]  
Source note: [[99-Sources/source-notes/SRC-CRA-IA-BI-2024]]

| Element | Vault-supported public content | Class |
|---|---|---|
| **Objective** | Assurance that business intelligence is being overseen and used, and continuously improved, to support compliance, collections, and verification programs | Official public-source (case) |
| **Scope (in)** | Governance structures, uses, and continuous improvement of BI; period 1 April 2020 – 31 March 2023 | Official public-source (case) |
| **Scope (out)** | Data security; human resource challenges; applications, tools, and infrastructure and their lifecycle used to develop BI | Official public-source (case) |
| **Criteria** | Line of enquiry: management control framework for BI (documented governance elements, roles/accountability, oversight of tool acquisition aligned with the Information and Data Strategy, structure fostering continuous improvement) | Official public-source (case) |
| **Evidence / methods (illustrative)** | Document review; process review of selected CPB/CVB teams; interviews (SIIB, ITB, CVB, CPB, DTPB, regional BI QA); observation of governance meetings | Official public-source (case) |

**How they work together in this case (derived onboarding interpretation):** the objective asks about oversight/use/continuous improvement—not “is BI technology secure?” Scope exclusions prevent treating silence on data security or tool lifecycle as an assurance conclusion. Criteria focus evidence on governance framework elements; fieldwork (documents, interviews, observation) is then selected to test those standards inside the stated boundaries.

Secondary illustrations of the same pattern:

- [[Internal Audit - Specific Cyber Security Controls]] — objective on safeguarding IT; scope limited to a **subset** of higher-risk controls, not the entire cyber posture.
- [[Internal Audit - Enterprise Fraud Management System]] — objective on EFMS operating as intended; scope excludes post-alert Internal Affairs investigation/discipline.
- [[Internal Audit - Accounts Receivable National Inventory]] — objective on risk scoring/allocation and collection actions; criteria cover strategic goals, DSS fitness, and monitoring controls.
- [[Internal Audit - Charities Audit Process]] — objective on key CD audit processes for impartial conduct; exclusions include broader effectiveness review and activities outside RAD.

## Notes used

### Audit concepts

- [[Audit Objective]]
- [[Scope]]
- [[Criteria]]
- [[Evidence]]
- [[Methodology]]
- [[Finding]]
- [[Recommendation]]
- [[Risk]]
- [[Sampling Risk]]
- [[Internal Audit and Program Evaluation]]
- [[Audit Client]]

### Risk / related

- [[Risk Management]]
- [[Control]]

### Cases / navigation / sources

- [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] (primary worked example)
- [[Internal Audit - Specific Cyber Security Controls]]
- [[Internal Audit - Enterprise Fraud Management System]]
- [[Internal Audit - Accounts Receivable National Inventory]]
- [[Internal Audit - Charities Audit Process]]
- [[Public-Audit-Case-Map]]
- [[Public-Audit-Case-Library]]
- [[Content Classification Model]]
- [[99-Sources/source-notes/SRC-CRA-IA-BI-2024]]

### Searched but not found as dedicated notes

- **Audit Planning** — no dedicated note; planning themes appear inside [[Methodology]], [[Audit Objective]], [[Scope]], and [[Risk]]
- **Risk Assessment** — no dedicated note titled “Risk Assessment”; closest nodes are [[Risk]] and [[Risk Management]]
- **Audit Scope** / **Audit Criteria** as titles — vault uses [[Scope]] and [[Criteria]] (aliases currently empty)

## Public cases used

1. [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] — primary
2. [[Internal Audit - Specific Cyber Security Controls]] — subset-scope illustration
3. [[Internal Audit - Enterprise Fraud Management System]] — exclusion illustration
4. [[Internal Audit - Accounts Receivable National Inventory]] — objective/criteria illustration
5. [[Internal Audit - Charities Audit Process]] — objective/scope exclusions illustration

## Diagnostic evaluation

| Check | Finding |
|---|---|
| Objective and scope conflated? | **No.** [[Audit Objective]] explicitly distinguishes objective from scope and criteria. Case notes usually separate headings or labeled sentences. |
| Criteria described as evidence? | **No.** [[Criteria]] = standards/benchmarks; [[Evidence]] = information supporting conclusions. [[Finding]] compares condition to criteria. |
| Exclusions explained? | **Yes** in [[Scope]] (general) and strongly in BI, EFMS, Charities, and cyber cases (case-specific). |
| Learner can trace into a public case? | **Yes**, especially via the BI case’s Objective / Scope / Criteria / Methodology sections and “Reusable audit concepts” links. |
| Unsupported CRA-specific claims? | **None found** in the Class C concept notes asserting CRA-mandated engagement templates. Cases stay within published report language. |

### Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Conceptual distinction | **2** | Separate notes; objective/scope/criteria roles stated without conflation; criteria ≠ evidence. |
| Relationship clarity | **1** | Relationship is stated across [[Audit Objective]], [[Methodology]], [[Scope]], and [[Evidence]], but the compact end-to-end model is not concentrated in one beginner-facing note. |
| Public-case application | **2** | BI case cleanly maps objective, inclusions, exclusions, criteria, and methods; several other cases reinforce the pattern. |
| Source and content-class accuracy | **2** | Concept notes are Class C; cases/SRC notes are Class A; answer can keep CRA facts and professional conventions separate. |
| Beginner usability | **1** | Learner can answer if they find the three concept notes **and** the BI case; missing Audit Planning / Risk Assessment nodes and title aliases slow discovery. |
| **Total** | **8 / 10** | |

### Passed criteria

- Clear conceptual separation of objective, scope, and criteria
- Criteria correctly framed as standards, not evidence
- Exclusions explained in concept note and public cases
- Traceability from concepts into at least one rich public case (BI)
- No unsupported CRA-specific requirements invented in Class C notes
- Content classes allow safe labeling of official vs professional vs derived statements

### Failed criteria

- No dedicated [[Audit Planning]] note for onboarding search on “planning”
- No dedicated “Risk Assessment” note (only [[Risk]] / [[Risk Management]])
- No single primer assembling objective → scope → criteria → evidence with a worked CRA example
- Title/alias gap: learners searching “Audit Scope” or “Audit Criteria” may miss [[Scope]] / [[Criteria]]
- Concept notes do not link outward to public cases (links are mostly case → concept)

### Missing links or concepts

| Gap | Why it matters |
|---|---|
| Audit Planning | Required search target; planning is scattered across Methodology/Risk/Objective/Scope |
| Risk Assessment (named note) | Required search target; annual-plan and engagement-level risk focus are only briefly covered |
| Aliases `Audit Scope`, `Audit Criteria` on [[Scope]] / [[Criteria]] | Search and wikilink consistency with “Audit Objective” naming |
| Case backlinks from concept notes | Beginners starting at concepts may not discover the BI worked example |
| Compact relationship MOC | Relationship model exists only by stitching notes (or this test file) |

### Unsupported claims

The vault does **not** support claiming:

- That CRA formally requires a specific objective/scope/criteria wording template beyond each report’s published text
- That IIA or TBS text is fully transcribed into the Class C concept notes (they cite potential frameworks without asserting official URLs there)
- That out-of-scope topics in a case were audited or found effective/ineffective
- That historical case conclusions describe current CRA control effectiveness

No unsupported CRA-specific claims were needed to answer the diagnostic question from vault content.

### Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Add aliases (or retitle carefully) so [[Scope]] and [[Criteria]] are discoverable as “Audit Scope” and “Audit Criteria,” matching [[Audit Objective]].
2. Create a short derived onboarding primer (MOC) that embeds the compact relationship model and links to the BI worked example.
3. Add thin Class C stubs or sections for **Audit Planning** and **Risk Assessment**, linking to [[Methodology]], [[Risk]], and [[Risk Management]].
4. From [[Audit Objective]], [[Scope]], and [[Criteria]], add related-case links to [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] (and optionally EFMS/cyber for exclusion teaching).
5. Optionally add one sentence on [[Evidence]] restating that evidence is assessed **against criteria within scope**—to harden the constraint chain in one place.

## Test metadata

- Test ID: Test-01-Objective-Scope-Criteria
- Suite: Audit Baseline onboarding diagnostics
- Output path: `16-Testing/Audit/Baseline/Test-01-Objective-Scope-Criteria.md`
- Vault notes modified by this test: **none** (output file created only)
- Process followed: searched vault for objective/scope/criteria/planning/risk/evidence and public cases; distinguished content classes; used BI case as primary worked example; did not implement recommendations

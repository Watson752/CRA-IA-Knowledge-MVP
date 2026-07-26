---
title: "Test-03: Control Design and Operating Effectiveness"
note_type: testing
primary_domain: audit
domains:
  - audit
  - risk
  - control
  - software
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
  - control-design
  - operating-effectiveness
---

# Test-03: Control Design and Operating Effectiveness

## Question

What is the difference between control design and operating effectiveness, and how would an auditor test each?

## Answer

[[Control]] distinguishes two questions that must not be collapsed:

| Question | Vault term | Meaning |
|---|---|---|
| If performed as intended, would this control address the risk? | **Design effectiveness** | Capability of the control relative to the risk and [[Criteria]] |
| Did the control actually function over the period examined? | **Operating effectiveness** | Actual performance across the relevant period |

**Content-class rule**

| Class | Use in this answer |
|---|---|
| **General professional** | Definitions and procedure names from [[Control]], [[Evidence]], [[IT Controls]], [[Sampling Risk]], [[Control Ownership]] |
| **Official public-source** | Case-reported methods/criteria only (EFMS, Charities, ARNI) |
| **Vault-derived** | Worked test steps below (the vault does **not** contain dedicated Control Design / Operating Effectiveness / Control Testing notes) |

Do **not** treat inquiry alone as proof of operating effectiveness. [[Evidence]] requires sufficient and appropriate evidence and emphasizes corroborating management representations. The vault lists inquiry among test methods but **does not** state that inquiry alone is insufficient—an onboarding gap noted in the diagnostic.

### Control design

**Whether the control, if performed as intended, is capable of addressing the identified risk.**

Vault grounding ([[Control]]): design effectiveness = whether the control, if operated as intended, would address the risk. Related ideas: control design expectations in [[Criteria]]; auditors examine control design in [[Cybersecurity]] and [[Security Controls]]; [[Control Ownership]] covers accountability for designing controls.

Typical design-oriented work (**general professional / vault-derived packaging** of scattered vault terms):

- Understand the [[Risk]] and control objective
- Inspect procedure/policy/config documentation
- Walkthrough the process with owners ([[Methodology]] and Charities case mention walkthroughs; no dedicated Walkthrough note)
- Assess whether the control, as designed, would prevent/detect the risk (including automated application rules under [[IT Controls]])

A walkthrough that confirms understanding of design is **not** by itself operating-effectiveness testing for the whole period (**vault-derived** distinction—the vault does not explicitly separate walkthroughs from OE testing).

### Operating effectiveness

**Whether the control was actually performed:**

- by the appropriate person or system;
- at the required frequency;
- during the relevant period;
- with sufficient evidence;
- consistently enough to support the conclusion.

Vault grounding is thinner: [[Control]] says OE is whether the control “actually functioned over the period examined.” Frequency, owner, and consistency are **not** spelled out as OE criteria in a dedicated note; they are assembled here from [[Control Ownership]] (who operates), [[Evidence]] (sufficiency/appropriateness), and [[Sampling Risk]] / [[Scope]] (period/population/sample).

Typical OE work (**general professional / vault-derived**):

- Select a sample (or full population via [[Analytics]] on [[Structured Data]]) covering the period
- Inspect evidence that the control ran as required (logs, sign-offs, tickets, reports)
- Reperform where appropriate
- For automated controls: also rely on ITGCs such as change management and access ([[IT Controls]])—configuration drift can make a “good design” fail in practice

**Inquiry / interview alone does not prove OE** for the period (**onboarding rule for this test**; corroborate per [[Evidence]]).

---

## Examples

### Example 1 — Automated validation / detection rule (software-related)

**Teaching control (vault-derived illustration)** grounded in [[IT Controls]] application controls (validations) and themes from [[Internal Audit - Enterprise Fraud Management System]] (business rules / detection models). This is **not** a claim that EFMS is a simple field-validation rule, and protected EFMS configuration is not reconstructed.

| Element | Explanation | Class |
|---|---|---|
| **Risk** | Unauthorized or questionable employee access to taxpayer information goes undetected; or invalid transactions enter processing without system check | Official (EFMS risk context) + general professional (validation risk) |
| **Control objective** | System rule blocks or flags activity that violates defined conditions in near real time | Vault-derived / general professional; EFMS publicly describes real-time business rules |
| **Design test** | Review rule specification vs risk; confirm logic would catch the risk if applied; review onboarding/change governance design for who may create/modify rules ([[IT Controls]] change management; EFMS criteria on review/modification of detection models) | Mix: general professional + official EFMS criteria themes |
| **Operating-effectiveness test** | Over the audit period: verify rule remained enabled as approved; sample change tickets/history; test that alerts or rejects occurred when conditions met (or use controlled test data where allowed); assess timeliness of related monitoring (EFMS themes: timely alert receipt, record loading) | Vault-derived packaging; official case used documentation review methodology, not a full public OE playbook |
| **Evidence required** | Approved rule definition; change logs; configuration extracts; alert/reject logs; ITGC evidence over access and change; owner attestations **corroborated** by system evidence ([[Evidence]], [[Evidence Reliability]]) | General professional |
| **Limitations** | Public EFMS report redacts configuration/rule detail; documentation review ≠ proof of continuous operation; weak change history undermines OE conclusions (EFMS finding theme: ad hoc rule changes, incomplete central history); inquiry of developers alone is insufficient | Official limitations + vault-derived testing caution |

**Automated-control dependency (general professional from [[IT Controls]]):** reliance on automated application controls requires confidence in ITGCs (access, change/release). A rule that looks well designed can fail if unauthorized changes, failed deployments ([[Tool Deployment]]), or incomplete data feeds ([[Missing Data]], EFMS re-ingestion theme) occur.

### Example 2 — Periodic manual access review or management review (non-software / people-process)

**Teaching control (vault-derived illustration)** using language from [[Recommendation]] (“quarterly access reviews for privileged accounts with documented sign-off”) and [[Control Ownership]] (access reviews lapse without ownership). Non-software process testing themes also appear in [[Internal Audit - Charities Audit Process]] (walkthroughs, file reviews, documented approvals).

| Element | Explanation | Class |
|---|---|---|
| **Risk** | Privileged access accumulates or remains after role change; inappropriate access enables error or misuse | General professional ([[Security Controls]], [[IT Controls]] access management; Recommendation example) |
| **Control objective** | Appropriate reviewer examines privileged access on a defined frequency and documents approval/removal decisions | General professional / vault-derived |
| **Design test** | Inspect procedure: who reviews, what population (e.g., privileged accounts), frequency, escalation, required evidence, segregation from self-review; walkthrough one cycle with [[Control Ownership\|control owner]] | General professional; Charities official methods include walkthroughs/interviews |
| **Operating-effectiveness test** | Select review instances across the period (not one month only); for each, inspect completed review packages, reviewer identity/authority, completeness of population reviewed, timely completion, evidence of removals followed up; expand sample if exceptions ([[Sampling Risk]]) | Vault-derived; population/sample concepts from [[Sampling Risk]] / [[Population Completeness]] |
| **Evidence required** | Review schedules; signed/dated review worksheets; access listings used; tickets for removals; role of reviewer vs owner; exceptions log | General professional ([[Evidence]]) |
| **Limitations** | Existence of a procedure document ≠ operation; one clean quarter ≠ full-period OE; incomplete population lists inflate risk ([[Population Completeness]]); Charities case shows documented reviews/approvals were not always complete—illustration that retained paperwork can still fail OE expectations | Official Charities theme + vault-derived caution |

**Secondary non-software / monitoring illustration:** [[Internal Audit - Accounts Receivable National Inventory]] concludes controls existed for risk scoring/allocation, but processes to **monitor that controls worked** were limited—useful for teaching that design presence ≠ demonstrated ongoing operation (**official case conclusion**, used here as analogy, not as an access-review control).

---

## How an auditor would test each (procedure map)

| Procedure | Design use | Operating-effectiveness use | Vault status |
|---|---|---|---|
| Inquiry | Understand intended control | Corroborating only—not standalone OE proof | Named in [[Control]]; no Inquiry note |
| Observation | See control performed once / understand flow | Limited OE signal unless repeated/period-covered | Named as method in [[Control]] / [[Evidence]]; dual meaning with “audit observation” |
| Walkthrough | Primary design/understanding tool | Not a substitute for period OE testing | Mentioned in [[Methodology]], [[Follow-up]], Charities case; **no Walkthrough note** |
| Inspection | Policies, configs, designs | Signed reviews, logs, tickets across period | Mentioned in [[Methodology]]; no Inspection note |
| Reperformance | Sometimes used to validate design logic | Strong OE procedure when reperforming control outcomes | Named in [[Control]]; no Reperformance note |
| Data analytics / full population | Design logic checks on rules | OE over large populations ([[Analytics]], [[Structured Data]]) | [[Sampling Risk]], [[Methodology]] |
| ITGC testing | Supports automated control design reliance | Required before relying on automated OE | [[IT Controls]] |

---

## Notes and cases used

### Notes present

- [[Control]] — sole clear design vs OE definition
- [[Evidence]] · [[Evidence Reliability]] · [[Criteria]] · [[Risk]]
- [[Methodology]] · [[Sampling Risk]] · [[Scope]]
- [[Control Ownership]] · [[IT Controls]] · [[Security Controls]] · [[Cybersecurity]]
- [[Tool Deployment]] · [[Structured Data]] · [[Analytics]]
- [[Population Completeness]] · [[Missing Data]] · [[Monitoring and Reporting]]
- [[Recommendation]] · [[Finding]]

### Cases / sources

- [[Internal Audit - Enterprise Fraud Management System]] — software / automated rules, change governance, documentation methodology ([[99-Sources/source-notes/SRC-CRA-IA-EFMS-2026]])
- [[Internal Audit - Charities Audit Process]] — walkthroughs, interviews, file review / documented approvals (manual process evidence)
- [[Internal Audit - Accounts Receivable National Inventory]] — controls existed vs monitoring that they worked
- [[Internal Audit - Specific Cyber Security Controls]] — asks what evidence shows designed/operating/monitored (high-level; protected details)
- [[08-Cases/README]] Journey 1 — “Governance, technology, and control design” (navigation, not a procedure note)

### Searched; not found as dedicated notes

| Sought term | Result |
|---|---|
| Control Design | Only embedded in [[Control]] / [[Cybersecurity]] / [[Criteria]] |
| Operating Effectiveness | Embedded in [[Control]] / [[Cybersecurity]] / [[Security Controls]] |
| Control Testing | Phrase “control tests” in [[Management Action Plan]]; no procedure note |
| Walkthrough | Mentions only |
| Inquiry | Mentions only (plus unrelated “inquiry” in [[Research]]) |
| Observation (procedure) | Mentions only |
| Inspection | Mentions only |
| Reperformance | Mention in [[Control]] only |
| Automated controls / Manual controls | Themes in [[Control]] / [[IT Controls]]; no titled notes |

---

## Diagnostic evaluation

| Check | Finding |
|---|---|
| Documentation treated as proof the control operated? | **Not explicitly endorsed.** [[Control Ownership]] notes documentation can exist while practice differs; [[Evidence]] requires corroboration. Still **no blunt warning** “policy ≠ OE.” |
| One successful instance treated as proof for whole period? | **Not claimed.** [[Control]] says “over the period examined”; [[Sampling Risk]] addresses population/sample. **No explicit** “one instance ≠ period OE” teaching line. |
| Walkthroughs distinguished from effectiveness testing? | **No.** Walkthroughs appear as methods without design-vs-OE framing. |
| Automated controls linked to configuration / change management? | **Yes** at concept level ([[IT Controls]], [[Tool Deployment]]); EFMS case reinforces rule-change governance. |
| Frequency and population considerations explained? | **Partially.** Population/sample in [[Sampling Risk]] / [[Scope]]; control **frequency** largely absent from OE teaching. |

### Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Design-versus-operation distinction | **1** | Accurate one-paragraph split in [[Control]]; not developed into teachable notes or OE criteria (person/frequency/evidence/consistency). |
| Procedure selection | **1** | Inquiry/observation/inspection/reperformance/analytics listed; no procedure notes; walkthrough ≠ OE not taught; inquiry-alone insufficiency not stated. |
| Evidence linkage | **1** | [[Evidence]] + [[Sampling Risk]] + [[Control Ownership]] help, but type/frequency/owner/evidence chain is not connected in one testing note. |
| Manual-and-automated control coverage | **1** | [[IT Controls]] covers validations and ITGC dependency; manual controls mentioned mainly as over-reliance risk; no paired worked examples in vault. |
| Public-case or source grounding | **1** | EFMS/Charities/ARNI illustrate related themes; none is a structured design-vs-OE testing tutorial. |
| **Total** | **5 / 10** | |

---

## Methodological errors (risks if a learner relies only on the vault)

1. Treating the [[Control]] method list as if inquiry alone establishes OE.
2. Treating a walkthrough or single observed performance as period OE.
3. Treating procedure documents or management statements as sufficient OE evidence without corroboration.
4. Relying on automated application controls without considering ITGCs / change management ([[IT Controls]] mitigates this if read).
5. Assuming one clean sample item or one period slice proves the full examined period (under-taught).
6. Confusing “observation” as a test method with “observation” as a pre-finding issue (see Test-02).

---

## Missing procedures

- Walkthrough
- Inquiry
- Observation (as test procedure)
- Inspection
- Reperformance
- Control Testing (playbook)
- Control Design / Design Effectiveness (stub)
- Operating Effectiveness (stub with person/frequency/period/evidence/consistency)
- Automated Control vs Manual Control (thin stubs)

---

## Missing software links

- [[Control]] does not deep-link OE testing to [[IT Controls]] change management / access management beyond related-notes list.
- No worked link from automated validation → [[Tool Deployment]] / configuration → OE evidence.
- EFMS case links Cybersecurity/Data Governance more than [[Control]] design/OE vocabulary.
- [[Monitoring and Reporting]] discusses alert triage but is not wired as an OE evidence pattern for automated detective controls.
- No explicit bridge: application control OE depends on ITGC OE ([[IT Controls]] states the idea; onboarding path does not dramatize it with examples).

---

## Unsupported claims

Do **not** claim from the vault:

- Detailed CRA standard programs for design vs OE testing
- That EFMS public methodology included reperformance or full-period OE sampling (published note emphasizes documentation review)
- Protected EFMS rule logic or cyber control inventories
- That inquiry alone is declared sufficient (it is not declared sufficient—and also not declared insufficient)
- That Charities file-review sample sizes are population OE conclusions

Worked examples’ step lists in this test are **vault-derived teaching**, not official CRA audit manuals.

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Create Class C stubs: **Design Effectiveness**, **Operating Effectiveness**, **Control Testing**, **Walkthrough**—with the person/frequency/period/evidence/consistency OE checklist.
2. Add an explicit sentence on [[Control]] or [[Evidence]]: inquiry alone does not demonstrate operating effectiveness for the period.
3. Distinguish walkthrough (design/understanding) from OE testing (period evidence) in [[Methodology]].
4. Add paired worked examples (automated validation + quarterly access review) linking [[IT Controls]], [[Control Ownership]], [[Sampling Risk]], and [[Evidence]].
5. Cross-link [[Internal Audit - Enterprise Fraud Management System]] to design (rule governance) vs operation (timely loading/alerts) teaching questions without reconstructing redactions.
6. Cross-link [[Internal Audit - Charities Audit Process]] and [[Internal Audit - Accounts Receivable National Inventory]] for manual/monitoring OE limitations.
7. Add aliases so “Control Design” and “Operating Effectiveness” resolve to the new stubs or to expanded [[Control]] sections.

---

## Test metadata

- Test ID: Test-03-Control-Design-and-Effectiveness
- Suite: Audit Baseline onboarding diagnostics
- Output path: `16-Testing/Audit/Baseline/Test-03-Control-Design-and-Effectiveness.md`
- Vault notes modified by this test: **none** (output file created only)
- Process followed: searched design/OE/testing procedures and cases; distinguished design vs operation; built software and non-software examples with content-class labels; did not treat inquiry alone as OE proof; did not implement recommendations

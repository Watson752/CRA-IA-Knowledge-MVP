---
title: "Test-03: Privileged Access and Incomplete Reviews (Integrated Baseline)"
note_type: testing
primary_domain: governance
domains:
  - organization
  - business
  - software
  - data
  - statistics
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
  - privileged-access
  - access-review
  - multidisciplinary
---

# Test-03: Privileged Access and Incomplete Reviews (Integrated Baseline)

## Question

How should Internal Audit examine a system where users may have excessive privileges and periodic access reviews are incomplete?

**Scenario class:** synthetic multidisciplinary teaching scenario. It does **not** claim that any CRA system currently has these weaknesses. A signed review does **not** automatically prove meaningful review activity ([[Document Review]] ≠ [[Operating Effectiveness]]; inquiry alone ≠ OE).

## Content-class key

| Class | Meaning in this answer |
|---|---|
| **Official public CRA facts** | Branch mandates and published case statements as recorded in vault notes |
| **General professional knowledge** | Access, IAM, sampling, and evidence concept notes |
| **Derived cross-domain interpretation** | Composed examination approach ([[Identity and Access Map]], [[Ownership and Assurance Roles]], this diagnostic) |
| **Synthetic scenario content** | Possible excessive privileges + incomplete periodic reviews in the question |

---

## Answer

### Distinctions that must stay separate

| Concept | Meaning | Vault anchors |
|---|---|---|
| **Excessive privileges** | Access was granted (or retained after role change) beyond duty need; login may still be “authorized” | [[Excessive Privileges]] |
| **Unauthorized access** | Access/use without valid authorization (never approved, revoked but active, credential misuse, prohibited use) | [[Unauthorized Access]] |
| **Incomplete user population** | Review or test frame omits nested groups, admins, break-glass, dormant, or service accounts | [[User Access Dataset]], [[Population Completeness]] |
| **Incomplete access-review execution** | Required reviews not performed on frequency, coverage, or follow-up removals | [[Periodic Access Review]], [[Access Review Testing]], [[Operating Effectiveness]] |
| **Incomplete review documentation** | Work occurred (or is claimed) but evidence is missing/insufficient to prove OE | [[Document Review]], [[Evidence]], [[Evidence Reliability]] |

**Rule:** excessive entitlement ≠ unauthorized use. Incomplete population ≠ incomplete documentation ≠ failed review performance—diagnose each separately.

---

### Organizational responsibilities

| Responsibility | What to establish | Vault support | Class |
|---|---|---|---|
| **Business approval** | Business need and approver authority for grants; reviewer authority for retained access | [[Access Approval]], [[Business Process Owner]], [[Roles and Responsibilities]] | General professional |
| **System administration** | Provisioning/deprovisioning, role assignment, admin of the system of entitlements | [[System Owner]], [[Technical Support]], [[Identity and Access Management]] | General professional |
| **Identity-management support** | Directory/IAM lifecycle (joiners–movers–leavers), unique attributable identities | [[Identity and Access Management]], [[IT Controls]] | General professional; do not invent CRA IAM product names |
| **Control ownership** | Named owner for access approval, periodic review, monitoring, and remediation | [[Control Ownership]] (notes reviews lapse without ownership) | General professional |
| **Security monitoring** | Detective monitoring of privileged/suspicious use; escalation | [[Privileged Access Monitoring]], [[Audit Logging]], [[02-Organization/Branches/Security Branch]] (EFMS MAP/operations context) | Mixed: monitoring concepts = general; EFMS Security Branch role = **official case-specific** |
| **Independent audit** | Third-line assurance; does not own provisioning or remediation execution | [[Three Lines Model]], [[Audit, Evaluation, and Risk Branch]], [[Ownership and Assurance Roles]] | Official for AERB mandate; Three Lines = general / case-described |

**ITB / Security Branch (bounded):** [[02-Organization/Branches/Information Technology Branch|ITB]] supports technology; [[02-Organization/Branches/Security Branch]] appears in EFMS as MAP owner / IFMS maintenance and in the cyber case for second-line cyber governance themes. Neither case is a public privileged-access **provisioning** audit. Do not invent reporting lines or current entitlement weaknesses.

---

### Risks

| Risk | Why it matters when privileges are excessive or reviews incomplete | Vault anchors |
|---|---|---|
| Unauthorized data access | Revoked/orphaned/misused credentials; dormant IDs still enabled | [[Unauthorized Access]], [[Dormant Accounts]] |
| Inappropriate transactions | Standing elevation enables harmful business actions | [[Privileged Access]], [[Excessive Privileges]] |
| Conflicting duties | Toxic role combinations conceal error/misuse | [[Inadequate Segregation of Duties]], [[Segregation of Duties]] |
| Untraceable changes | Privileged users alter configs/data/logs without attributable trail | [[Audit Logging]], [[Identity Attribution]], [[Privileged Access Monitoring]] |
| Retained access after role changes | Privilege creep from incomplete mover/leaver processes | [[Excessive Privileges]], [[Identity and Access Management]] |
| Dormant or orphaned accounts | Enabled unused identities remain attack/misuse surface | [[Dormant Accounts]] |
| Excessive service-account permissions | Non-human identities with standing privilege and shared secrets | [[Service Accounts]] |

---

### Control design

| Design element | Expectation (general professional) | Vault anchors |
|---|---|---|
| Access requests | Documented request with business need and role/privilege sought | [[Access Approval]], [[Identity and Access Management]] |
| Approvals | Independent approval before/at grant; requestor ≠ sole implementer where SoD requires | [[Access Approval]], [[Segregation of Duties]], [[Manual Control]] |
| Role definitions | Roles aligned to duties; least privilege; tractable for review | [[Role-Based Access Control]] |
| SoD checks | Detect toxic combinations at grant and in reviews | [[Segregation of Duties]], [[Inadequate Segregation of Duties]] |
| Periodic reviews | Defined frequency; appropriate reviewer; keep/remove decisions; follow-up | [[Periodic Access Review]] |
| Privileged monitoring | Log privileged use; triage; escalate | [[Privileged Access Monitoring]], [[Audit Logging]], [[Monitoring and Alerting]] |
| Access removal | Timely revocation on leaver/mover/remove decisions | [[Identity and Access Management]], [[Periodic Access Review]] follow-up |
| Exception escalation | Unresolved exceptions aged and escalated to owners | [[Exception Handling]], [[Monitoring and Reporting]] (adjacent) |

**Preventive vs detective:** [[Access Approval]] (at grant) ≠ [[Periodic Access Review]] (recurring) ≠ [[Privileged Access Monitoring]] (use monitoring).

---

### Operating-effectiveness testing

| Procedure | What Internal Audit should do | Vault anchors |
|---|---|---|
| Population reconciliation | Define intended privileged/user population; reconcile extract to directory/PAM/app admin stores; include nested groups, admin, break-glass, dormant, service accounts | [[User Access Dataset]], [[Population Completeness]], [[Data Reconciliation]] |
| Sample selection | After frame completeness, sample grants/reviews; stratify high-risk privileged roles; judgmental picks for investigation only (not population extrapolation) | [[Sample Selection]], [[Stratified Sampling]], [[Judgmental Sampling]], [[Risk-Based Selection]] |
| Inspection of approvals | Match sampled grants to request/approver/authority/business need | [[Access Approval]], [[Inspection]], [[Document Review]] |
| Review-performance evidence | For review cycles: reviewer authority, coverage of population, timeliness, keep/remove decisions, **follow-up removals**—not signature alone | [[Access Review Testing]], [[Operating Effectiveness]], [[Control Frequency]] |
| Reperformance | Independently reassess whether sampled entitlements remain necessary vs role/HR info | [[Reperformance]] |
| Comparison with employment or role information | Movers/leavers still entitled; role vs RBAC assignment mismatch | [[Identity and Access Management]], [[Roles and Responsibilities]], [[Role-Based Access Control]] |
| Examination of exceptions | Uncleared SoD conflicts, denied removals, aged exceptions | [[Exception Testing]], [[Inadequate Segregation of Duties]] |
| Analysis of dormant and service accounts | Profile inactivity, ownership, standing privilege, monitoring coverage | [[Dormant Accounts]], [[Service Accounts]], [[Analytics]], [[Full-Population Analysis]] |

**Documentation ≠ performance:** a signed certification package is insufficient without evidence the reviewer examined entitlements and that remove decisions were executed ([[Document Review]], [[Evidence Reliability]], [[System-Generated Evidence]]).

---

### Data and statistical considerations

| Consideration | Implication | Vault anchors |
|---|---|---|
| Completeness of user-access dataset | Incomplete frames hide the riskiest accounts and inflate [[Sampling Risk]] | [[User Access Dataset]], [[Population Completeness]], [[Missing Data]] |
| Terminated or transferred users | Survivorship/selection bias if leavers/movers omitted from review or test sets | [[Selection Bias]], [[Survivorship Bias]], [[Dormant Accounts]] |
| Sampling high-risk access | Prefer strata/certainty sets for highly privileged roles; deep-test approvals and reviews | [[Stratified Sampling]], [[Risk-Based Selection]], [[Privileged Access]] |
| Limitations of judgmental selection | Useful for known risks; normally **no** statistical extrapolation to all users | [[Judgmental Sampling]], [[Representativeness]] |
| Full-population analysis | Profile orphans, unused privilege, SoD conflicts, dormant/service accounts when extracts allow | [[Full-Population Analysis]], [[Analytics]], [[Access Review Testing]] |

A listing shows entitlement, not appropriate use—pair with [[Audit Logging]] / [[Privileged Access Monitoring]].

---

### Public-case relevance

| Case | Supported use | Label |
|---|---|---|
| [[Internal Audit - Enterprise Fraud Management System]] | Implemented to reduce risks of **unauthorized employee access** to taxpayer information; audit trails / business rules; Security Branch MAP owner; ITB co-named for selected actions; detective monitoring themes | **Official case facts** for unauthorized-access **monitoring** context; **derived** adjacency to privileged monitoring/logging—**not** a public privileged-access provisioning or periodic-review finding |
| [[Internal Audit - Specific Cyber Security Controls]] | Security Branch cyber governance / Three Lines language; protected technical findings | **Official** for governance/lines themes only; **do not reconstruct** protected access-control details |
| [[Internal Audit - Charities Audit Process]] | Documented reviews/approvals incomplete in a process sense (file reviews)—methodology analogy only | **General professional analogy** for “documentation gaps ≠ complete control operation”; **not** an IAM entitlement audit |

Do **not** invent CRA entitlement matrices, IAM tools, or current privileged-access weaknesses from these cases.

---

## Relationship chain

### Required path

```text
[[Business Process Owner]]
→ [[Role-Based Access Control]]
→ [[Privileged Access]]
→ [[Excessive Privileges]]
→ [[Periodic Access Review]]
→ [[User Access Dataset]]
→ [[Population Completeness]]
→ [[Access Review Testing]]
→ [[Evidence]] (alias: Audit Evidence)
```

| Link | Vault reality |
|---|---|
| BPO → RBAC | **Weak** — both exist; BPO Related notes do not point to RBAC/access reviews |
| RBAC → Privileged Access → Excessive Privileges → Periodic Access Review | **Strong** |
| Periodic Access Review → User Access Dataset → Population Completeness → Access Review Testing → Evidence | **Strong** |
| Map alignment | [[Identity and Access Map]] starts at Privileged Access (not BPO) and ends at Evidence |

### Expanded teaching path (derived)

```text
Business Process Owner / Control Owner (access need + review ownership)
→ RBAC role definitions + Access Approval (preventive)
→ Privileged Access / Service Accounts / Dormant Accounts
→ Excessive Privileges vs Unauthorized Access (keep distinct)
→ Periodic Access Review + Privileged Access Monitoring (detective)
→ User Access Dataset completeness
→ Access Review Testing (OE: approvals, review performance, removals)
→ Audit Logging / Evidence Reliability
→ Evidence → Finding (when supported)
→ AERB / Three Lines (independent assurance)
```

---

## Notes and cases used

### Organization / roles

- [[Business Process Owner]] · [[System Owner]] · [[Control Ownership]] · [[Technical Support]]
- [[Ownership and Assurance Roles]] · [[Roles and Responsibilities]] · [[Three Lines Model]]
- [[02-Organization/Branches/Information Technology Branch|ITB]] · [[02-Organization/Branches/Security Branch]] · [[Audit, Evaluation, and Risk Branch]]

### Access / software / control

- [[Identity and Access Management]] · [[Role-Based Access Control]]
- [[Privileged Access]] · [[Excessive Privileges]] · [[Unauthorized Access]]
- [[Segregation of Duties]] · [[Inadequate Segregation of Duties]]
- [[Access Approval]] · [[Periodic Access Review]] · [[Privileged Access Monitoring]]
- [[User Access Dataset]] · [[Service Accounts]] · [[Dormant Accounts]]
- [[Access Review Testing]] · [[Audit Logging]] · [[IT Controls]] · [[Cybersecurity]]
- [[Identity and Access Map]]

### Audit / evidence / stats

- [[Operating Effectiveness]] · [[Design Effectiveness]] · [[Document Review]] · [[Inspection]] · [[Reperformance]]
- [[Evidence]] · [[Evidence Reliability]] · [[System-Generated Evidence]]
- [[Population Completeness]] · [[Sample Selection]] · [[Stratified Sampling]] · [[Judgmental Sampling]]
- [[Risk-Based Selection]] · [[Full-Population Analysis]] · [[Analytics]] · [[Sampling Risk]]
- [[Selection Bias]] · [[Missing Data]] · [[Manual Control]] · [[Control Testing]]

### Cases

- [[Internal Audit - Enterprise Fraud Management System]] — primary bounded case
- [[Internal Audit - Specific Cyber Security Controls]] — Security Branch / Three Lines only; protected detail not used
- [[Internal Audit - Charities Audit Process]] — documentation-completeness analogy only

---

## Diagnostic evaluation

### Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Role and accountability clarity | **1** | Business/system/control/IAM/security/assurance roles are teachable, and EFMS/cyber cases name Security Branch carefully, but BPO→RBAC/access-review ownership is not first-class. |
| Access-control accuracy | **2** | Privileged vs ordinary; excessive vs unauthorized; approval ≠ periodic review ≠ monitoring; SoD, service/dormant accounts defined. |
| Audit-testing methodology | **2** | [[Access Review Testing]] covers population, approvals, review cycles, follow-up; OE/Document Review block reliance on inquiry or signatures alone. |
| Population and sampling integration | **2** | User Access Dataset + completeness + sample selection methods + full-population analytics for orphans/SoD/dormant/service accounts. |
| Public-case and source accuracy | **2** | EFMS/cyber bounds preserved; no invented provisioning findings or current CRA weaknesses. |
| **Total** | **9 / 10** | |

### Checks

| Check | Finding |
|---|---|
| Excessive access distinguished from unauthorized use? | **Yes** — dedicated notes state the distinction. |
| User population validated? | **Yes** — User Access Dataset + Population Completeness expectations. |
| Documentation distinguished from actual review? | **Yes** — Document Review / OE / Access Review Testing (follow-up removals); signed review ≠ automatic OE. |
| Service and dormant accounts considered? | **Yes** — dedicated notes; required in population scope. |
| Unsupported CRA-specific claims avoided? | **Yes**, when case bounds and IAM “do not invent” rules are followed. |

---

## Missing roles

| Gap | Detail |
|---|---|
| Access-reviewer / certifier role note | Reviewer authority implied in Periodic Access Review / Access Approval; not a named role note |
| Joiner–mover–leaver process owner | Covered inside [[Identity and Access Management]] / testing notes; no dedicated JML note (also residual in Software-Data Test-01) |
| HR / employment-data owner for leaver matching | Comparison to employment/role info is procedural; no linked HR-data-owner bridge |
| BPO → access-control ownership link | [[Business Process Owner]] does not list RBAC / Periodic Access Review in Related notes |

*Present:* System Owner, Control Ownership, Technical Support, Security Branch/ITB/AERB as org/case context, Three Lines.

---

## Missing controls

| Gap | Detail |
|---|---|
| Dedicated access-removal / deprovisioning control note | Mentioned inside IAM and review follow-up; not first-class |
| Dedicated exception-escalation note for access reviews | Assembled from monitoring/exception themes |
| Compensating controls when SoD cannot be split | [[Inadequate Segregation of Duties]] mentions compensating reviews briefly |
| Break-glass / standing-elevation procedure note | Mentioned in Privileged Access / User Access Dataset scope only |

*Present and strong:* Access Approval, Periodic Access Review, Privileged Access Monitoring, RBAC, SoD, logging.

---

## Sampling weaknesses

| Weakness | Vault status |
|---|---|
| Testing an incomplete entitlement extract | Explicitly warned ([[Population Completeness]], [[User Access Dataset]]) |
| Treating judgmental privileged picks as population-rate proof | Explicitly limited ([[Judgmental Sampling]]) |
| Thin access-specific strata workbook | Methods exist generally; no dedicated “privileged-role strata design” playbook |
| Equating access-listing analytics with appropriate-use assurance | Warned—pair with logging/monitoring |
| Sample of signed reviews without testing removal execution | Mitigated in Access Review Testing (“follow-up removals”) but easy for learners to miss if they stop at sign-off language in [[Recommendation]] |

---

## Unsupported statements

Do **not** conclude from the vault that:

- Any CRA system currently has excessive privileges or incomplete access reviews
- EFMS found weak privileged-access provisioning or failed periodic access certifications
- Cyber Security Controls public text discloses specific access-control technical failures (protected)
- A signed access review proves entitlements were meaningfully examined
- An access listing alone proves appropriate use
- Excessive privileges equal unauthorized access
- Invented CRA IAM products, role matrices, or admin tool inventories are official

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Link [[Business Process Owner]] / [[Control Ownership]] to [[Role-Based Access Control]], [[Access Approval]], and [[Periodic Access Review]], clarifying business approval vs system administration vs IAM support vs AERB assurance.
2. Extend [[Identity and Access Map]] to start at [[Business Process Owner]] and end at [[Evidence]], matching the required chain.
3. Add one explicit sentence to [[Periodic Access Review]] / [[Access Review Testing]]: documented sign-off is not sufficient without evidence of entitlement examination and executed removals.
4. Create a thin **Joiner–Mover–Leaver** note (access removal, employment/role comparison) linked to [[Dormant Accounts]] and [[Excessive Privileges]].
5. Keep EFMS labeled as unauthorized-access **monitoring**; keep cyber case at Three Lines/Security Branch governance—never promote either to a provisioning/review OE case study.
6. Optional: short privileged-access sampling stub (certainty stratum for highly privileged roles + sample of ordinary; full-pop profiling for dormant/service/SoD).

---

## Test metadata

- Test ID: Test-03-Privileged-Access-and-Incomplete-Reviews
- Suite: Integrated Baseline multidisciplinary diagnostics
- Output path: `16-Testing/Integrated/Baseline/Test-03-Privileged-Access-and-Incomplete-Reviews.md`
- Vault substantive notes modified by this test: **none** (output file created only)
- Process followed: searched required access/ownership/evidence/org/case terms; integrated technical access with business roles and audit evidence; distinguished excessive vs unauthorized and incomplete population vs documentation vs execution; did not claim current CRA weaknesses; did not treat signed reviews as proof of meaningful review; did not implement recommendations

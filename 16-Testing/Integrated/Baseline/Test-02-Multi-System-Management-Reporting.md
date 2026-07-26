---
title: "Test-02: Multi-System Management Reporting (Integrated Baseline)"
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
  - data-pipeline
  - management-reporting
  - multidisciplinary
---

# Test-02: Multi-System Management Reporting (Integrated Baseline)

## Question

A management report is assembled from several source systems using APIs, batch processes and transformations. How should Internal Audit determine whether management can rely on the report?

**Scenario class:** synthetic multidisciplinary teaching scenario. It does **not** claim a specific CRA multi-system report design. Do **not** treat system-generated reports as inherently reliable. Do **not** treat matching totals as proof that every record and field is correct.

## Content-class key

| Class | Meaning in this answer |
|---|---|
| **Official public CRA facts** | Published case findings and org mandates as recorded in vault notes |
| **General professional knowledge** | Pipeline, quality, ownership, and evidence concept notes |
| **Derived cross-domain interpretation** | Composed reliance path ([[Data Pipeline and Reporting Map]], [[Ownership and Assurance Roles]], this diagnostic) |
| **Synthetic scenario content** | The multi-source management report described in the question |

---

## Answer

### Governance

| Accountability | What Internal Audit should establish | Vault support | Class |
|---|---|---|---|
| **Who owns the business report** | Accountability for report purpose, metric meaning, decision use, and residual reporting risk | [[Business Process Owner]], [[Program Owner]], [[Performance Reporting]], [[Business Intelligence Governance]] | General professional; BI case names SIIB as BI responsibility / MAP lead (**official case-specific**) |
| **Who owns source data** | Definitions, quality expectations, lawful use, and remediation priority for originating datasets | [[Data Owner]], [[Data Governance]], [[Reference Data]] stewardship | General professional; SIIB/CDO placement = **official org** where sourced |
| **Who supports technical components** | Build/run of APIs, batch jobs, pipelines, warehouses, BI tools—without automatically owning business outcomes | [[Technical Support]], [[02-Organization/Branches/Information Technology Branch|ITB]], [[System Owner]], [[Business Intelligence Tools]] | General professional + official ITB mandate / BI service-delivery split |
| **Who approves report logic** | Authorization of metric definitions, transforms, filters, and production promotion | [[Business Intelligence Governance]], [[Change Management]], [[Change Approval]], [[Deployment Approval]] | General professional / derived (no dedicated “report-logic approver” title) |
| **Who reviews the final output** | Challenge of results, variances, and known limitations before reliance | [[Manual Control]], [[Monitoring and Reporting]], prose “management review” in [[Management Reporting]] / [[Data Pipeline]] | General professional; **no dedicated [[Management Review]] note** |

**Separation rule (derived from [[Ownership and Assurance Roles]]):** business/report ownership ≠ ITB technical support ≠ data ownership ≠ control ownership ≠ AERB independent assurance. Ambiguity is itself a risk ([[Unclear Accountability]]).

---

### End-to-end flow

```text
Source system ([[Source System Data]])
→ extraction (authorized jobs / credentials)
→ API transfer ([[API Integration]]) and/or batch transfer ([[Batch Processing]])
→ transformation ([[Data Transformation]]) / field mapping ([[Field Mapping]])
→ integration into curated store
→ rejected / failed records handling ([[Rejected Records]])
→ uniqueness / duplicate checks ([[Record Uniqueness]])
→ reconciliation ([[Data Reconciliation]])  ← totals ≠ field accuracy
→ reporting dataset
→ calculation / report logic ([[Management Reporting]], metric definitions)
→ presentation (dashboard / report)
→ management review (expected control; note title missing)
→ reliance judgment ([[Evidence Reliability]] → [[Audit Conclusion]])
```

**Lineage overlay:** [[Data Lineage]] should document critical fields from source through transforms to report metrics. **Change overlay:** extracts, transforms, mappings, filters, and report logic are subject to [[Change Management]]. **Access overlay:** jobs, datasets, and reports under [[Identity and Access Management]] / [[Role-Based Access Control]] / [[Privileged Access]] (no note titled exactly “Access Controls”).

Vault map alignment: [[Data Pipeline and Reporting Map]].

---

### Risks

| Risk | Why it threatens reliance | Vault anchors |
|---|---|---|
| Incomplete extracts | Report population ≠ intended universe | [[Population Completeness]], [[Missing Data]], [[Intended Population]] vs [[Retrieved Population]] |
| Failed / rejected records | Silent drops or uncleared rejects omit cases | [[Rejected Records]], [[Exception Handling]] |
| Duplicate records | Inflated counts/amounts; false recon comfort | [[Record Uniqueness]] |
| Stale data | Decisions based on outdated window | [[Data Timeliness]], [[Batch Processing]] latency |
| Incorrect field mappings | Wrong meaning/units/codes in report fields | [[Field Mapping]], [[Reference Data]] |
| Unauthorized transformations | Logic diverges from approved business intent | [[Data Transformation]], [[Unauthorized System Changes]] |
| Unapproved report changes | Metric/calc drift without governance | [[Change Management]], [[Business Intelligence Governance]] |
| Inconsistent definitions | Same label, different numerators/denominators | [[Performance Reporting]], [[Business Intelligence Governance]], BI case common-definition theme |
| Incorrect cut-off dates | Period misstatement; late-arriving items | [[Assessment Cut-Off Date]] |
| Missing reconciliation | Completeness breaks undetected between stages | [[Data Reconciliation]] |
| Weak review | Management relies without challenging variances/limitations | Manual review theme; Management Review note absent |

**Discipline:** matching stage totals does **not** prove every record/field is correct ([[Data Reconciliation]], [[Data Accuracy]]). System origin does **not** prove reliability ([[System-Generated Evidence]]).

---

### Controls

| Type | Pipeline / reporting examples | Vault anchors |
|---|---|---|
| **Preventive** | Source capture validations; authorized API/batch credentials and job scope; approved mappings and metric definitions; change approval/testing before deploy; least privilege / SoD on pipeline and report objects; documented inclusion/exclusion rules; cut-off parameters | [[API Integration]], [[Batch Processing]], [[Field Mapping]], [[Change Management]], [[Identity and Access Management]], [[Segregation of Duties]], [[Inclusion and Exclusion Rules]], [[Business Intelligence Governance]] |
| **Detective** | Stage reconciliations (counts/amounts/hashes); reject capture/aging/clearance; duplicate profiling; freshness/cut-off monitors; calc reperformance; access reviews; management challenge of variances; lineage completeness checks | [[Data Reconciliation]], [[Rejected Records]], [[Record Uniqueness]], [[Data Timeliness]], [[Assessment Cut-Off Date]], [[Periodic Access Review]], [[Analytics]], [[Manual Control]], [[Data Lineage]] |

---

### Audit procedures

| Procedure | What to do | Vault anchors |
|---|---|---|
| Walkthrough | End-to-end from source owners through pipeline to report consumers | [[Walkthrough]], [[Data Pipeline]] |
| Source-to-report tracing | Trace material metrics/fields via lineage and mappings | [[Data Lineage]], [[Field Mapping]], [[Inspection]] |
| Reconciliation testing | Test stage-to-stage and to independent registers; inspect break clearance | [[Data Reconciliation]], [[Population Completeness]] |
| Configuration review | Extract scope, transforms, filters, cut-off params, report formulas | [[Configuration Review]], [[System Configuration]] |
| Change-history inspection | Tickets/versions for jobs, mappings, metric logic across the period | [[Change Management]], [[Unauthorized System Changes]] |
| Reperformance | Recalculate KPIs / re-apply transforms on sample or strata | [[Reperformance]], [[Analytical Validity]] |
| Data profiling | Completeness, uniqueness, nulls, distributions, outliers | [[Analytics]], [[Descriptive Statistics]], [[Outlier Analysis]] |
| Sample or full-population testing | Deep tests where needed; full-pop when structured and complete enough | [[Sample Selection]], [[Stratified Sampling]], [[Full-Population Analysis]] |
| Review of rejected records | Volumes, aging, reprocess, silent-drop risk | [[Rejected Records]], [[Missing Data]] |
| Access testing | Who can alter jobs, datasets, reports | [[Access Review Testing]], [[Privileged Access]] |
| Evidence / conclusion | Judge reliability relative to objective; qualify if incomplete | [[Evidence Reliability]], [[Audit Conclusion]], [[How Statistical Limitations Affect Audit Conclusions]] |

---

### Statistical and analytical limitations

| Limitation | Effect on interpretation | Vault anchors |
|---|---|---|
| Completeness | Conclusions apply only to the retrieved/reportable set unless the intended population is validated | [[Population Completeness]], [[Sampling Frame]] |
| Definitions / denominators | Same KPI name with different exclusions produces non-comparable results | [[Performance Reporting]], [[Inclusion and Exclusion Rules]], Audit Yield / ARNI themes |
| Cut-off dates | Late data and snapshot timing change reported results | [[Assessment Cut-Off Date]], [[Data Timeliness]] |
| Missingness | Missing records, fields, periods, or rejects weaken sufficiency even if remaining figures look precise | [[Missing Data]], [[How Missing Data Limits Audit Assurance]] |
| Totals vs accuracy | Balanced control totals can hide wrong fields, offsetting errors, and bad joins | [[Data Reconciliation]] ≠ [[Data Accuracy]] |
| Reproducibility ≠ validity | Same inputs/method can repeat a wrong population or invalid join | [[Reproducibility]] vs [[Analytical Validity]] |
| Full-population analytics | Reduces sampling variability but not incomplete-frame or bad-logic risk | [[Full-Population Analysis]], [[Sampling Risk]] |

---

### Public CRA cases

| Case | Supported relationship | Label |
|---|---|---|
| [[Evaluation - Audit Yield]] | Multi-system matching for a results measure; definitions, timing, exclusions, match rates; stratified sampling methodology | **Official case facts** for measure reliance themes; **derived** teaching for multi-source management-report reliance |
| [[Internal Audit - Accounts Receivable National Inventory]] | Incomplete/attribution-sensitive performance measures; business-rule outcome governance; collapsed inventories / movement completeness | **Official case facts**; **derived** relevance to report completeness and definitions |
| [[Internal Audit - Enterprise Fraud Management System]] | Load/re-ingestion completeness and timeliness; dashboard indicators insufficient alone | **Official case facts**; **derived** relevance to feed completeness and SGE limits |
| [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] | BI responsibility (SIIB) vs ITB service delivery; governance, roles, common BI definition | **Official case facts** for reporting/BI governance ownership; not a pipeline ETL audit |
| [[Internal Audit - Charities Audit Process]] | Adjacent via missing-data/assurance bridge themes where vault links it | Use only as **derived/bridge** adjacency—do not over-claim pipeline detail |

**Historical interpretation rule:** case findings describe stated audit periods; do not treat them as current-state CRA reporting reliability.

---

## Relationship path

### Required path

```text
[[Business Process Owner]]
→ [[Source System Data]]
→ [[Data Pipeline]]
→ [[Data Reconciliation]]
→ [[Management Reporting]]
→ [[Management Review]]   ← note title not found
→ [[Evidence Reliability]]
→ [[Audit Conclusion]]
```

| Link | Vault reality |
|---|---|
| BPO → Source System Data | **Weak** — ownership taxonomy exists; dedicated BPO→pipeline links thin |
| Source → Pipeline → Reconciliation → Management Reporting | **Strong** — first-class notes + [[Data Pipeline and Reporting Map]] |
| Management Reporting → Management Review | **Gap** — review expected in prose/map; **no** `Management Review.md` |
| Evidence Reliability → Audit Conclusion | **Strong** |

### Expanded teaching path (derived)

```text
Business Process Owner / BI metric owner
→ Data Owner (source + reference data) + Technical Support (API/batch/pipeline)
→ Source System Data
→ API Integration / Batch Processing
→ Data Transformation / Field Mapping / Rejected Records / Record Uniqueness
→ Data Reconciliation + Data Lineage + Assessment Cut-Off Date
→ Management Reporting (calc + presentation)
→ Management review (Manual Control / BI Governance challenge)
→ Evidence Reliability (≠ System-Generated Evidence automatic reliance)
→ Audit Conclusion (strength matched to limitations)
```

---

## Notes used

### Governance / organization

- [[Business Process Owner]] · [[Program Owner]] · [[System Owner]] · [[Data Owner]] · [[Control Ownership]]
- [[Technical Support]] · [[Unclear Accountability]] · [[Ownership and Assurance Roles]]
- [[Business Intelligence Governance]] · [[Data Governance]] · [[Chief Data Officer]]
- [[Roles and Responsibilities]] · [[Three Lines Model]]

### Technical / software

- [[Source System Data]] · [[Data Pipeline]] · [[API Integration]] · [[Batch Processing]]
- [[Data Transformation]] · [[Field Mapping]] · [[Rejected Records]] · [[Reference Data]]
- [[Data Lineage]] · [[Data Reconciliation]] · [[Management Reporting]]
- [[Change Management]] · [[Unauthorized System Changes]] · [[Deployment Approval]]
- [[Identity and Access Management]] · [[Role-Based Access Control]] · [[Privileged Access]] · [[Service Accounts]]
- [[IT Controls]] · [[System-Generated Evidence]] · [[Business Intelligence Tools]]
- [[Data Pipeline and Reporting Map]]

### Data / statistics / evidence

- [[Population Completeness]] · [[Missing Data]] · [[Record Uniqueness]] · [[Data Accuracy]] · [[Data Timeliness]]
- [[Data Quality]] · [[Assessment Cut-Off Date]] · [[Inclusion and Exclusion Rules]]
- [[Evidence Reliability]] · [[Reproducibility]] · [[Analytical Validity]]
- [[Full-Population Analysis]] · [[Analytics]] · [[Sampling Risk]] · [[Sample Selection]]
- [[How Missing Data Limits Audit Assurance]] · [[How Statistical Limitations Affect Audit Conclusions]]
- [[Performance Reporting]] · [[Business Intelligence]]

### Audit procedures

- [[Walkthrough]] · [[Inspection]] · [[Configuration Review]] · [[Reperformance]]
- [[Manual Control]] · [[Operating Effectiveness]] · [[Audit Conclusion]] · [[Evidence]]

### Searched; not found as dedicated note titles

| Sought | Result |
|---|---|
| Management Review | **Missing** (prose/map only; nearest [[Manual Control]], [[Monitoring and Reporting]]) |
| Access Controls | **No exact title** (nearest IAM / RBAC / Privileged Access / IT Controls) |

---

## Cases used

- [[Evaluation - Audit Yield]] — primary multi-source results-measure reliance
- [[Internal Audit - Accounts Receivable National Inventory]] — metric completeness / attribution / definitions
- [[Internal Audit - Enterprise Fraud Management System]] — feed completeness / dashboard limits
- [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] — BI ownership vs technical delivery; definition/governance
- [[Internal Audit - Charities Audit Process]] — bridge adjacency only where vault links missing-data themes

---

## Diagnostic evaluation

### Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Governance and ownership integration | **1** | Process/system/data/technical/assurance roles are teachable, and BI case separates SIIB vs ITB, but [[Management Review]] is missing and BPO→pipeline→report-approver chain is not first-class. |
| End-to-end technical reasoning | **2** | Source → API/batch → transform/mapping → rejects → recon → reporting → lineage/cut-off is covered by dedicated notes and the pipeline map. |
| Control and audit-procedure coverage | **2** | Preventive/detective controls and walkthrough, tracing, recon, config, change history, reperformance, profiling, sample/full-pop, and reject review are supported. |
| Statistical and evidence reasoning | **2** | Completeness ≠ accuracy; SGE not inherently reliable; reproducibility ≠ validity; cut-off/missingness/definitions constrain [[Audit Conclusion]] strength. |
| Public-case grounding | **2** | Audit Yield, ARNI, EFMS, and BI cases supply bounded official themes without inventing ETL architectures or current-state reliability. |
| **Total** | **9 / 10** | |

### Checks

| Check | Finding |
|---|---|
| Does the answer start only at the final report? | **No** — vault teaches source-to-report path ([[Data Pipeline]], map). |
| Transformations, rejected records, exclusions considered? | **Yes** — [[Data Transformation]], [[Rejected Records]], [[Inclusion and Exclusion Rules]]. |
| Business and technical ownership separated? | **Yes** in ownership/BI materials; weaker explicit link into Management Reporting ownership. |
| Reproducibility distinguished from validity? | **Yes** — [[Reproducibility]] vs [[Analytical Validity]]. |
| Historical cases interpreted appropriately? | **Yes**, if period bounds and “not current state” rules are followed. |

---

## Missing stages

| Stage / artifact | Status |
|---|---|
| Management Review (dedicated note) | **Missing** — required path node absent as titled note |
| Presentation-layer controls | Thin (implied in Management Reporting / BI tools) |
| Explicit “report logic approval” role note | Assembled from BI Governance + Change Management |
| Access Controls (exact title) | Covered via IAM/RBAC/Privileged Access instead |
| Deep procedure workbooks (reject aging, mapping reperformance scripts) | Teaching-level stubs only (also residual in Software-Data Test-04) |

*Present and usable:* source, API/batch, transform, mapping, rejects, uniqueness, recon, lineage, reference data, cut-off, management reporting, evidence reliability, audit conclusion.

---

## Unclear ownership

| Question | Vault clarity |
|---|---|
| Business report owner vs BI platform owner | Clarified in BI case (SIIB responsibility / ITB delivery) as **case-specific**, not universal CRA rule |
| Source data owner vs pipeline operator | Concepts exist ([[Data Owner]] vs [[Technical Support]]); not always bound to a single report scenario |
| Who approves metric/report logic | [[Business Intelligence Governance]] describes approval/versioning generally; no named enterprise approver title |
| Who performs final management review before reliance | Expected control in maps/prose; **no** Management Review owner model |
| Control owner for reconciliations vs report sign-off | [[Control Ownership]] generic; split not scenario-mapped |

---

## Unsupported reliance claims

Do **not** conclude from the vault that:

- Matching pipeline totals prove field-level accuracy or complete populations
- System-generated dashboards/reports are reliable because they are automated
- A reproducible extract/query is automatically analytically valid
- CRA currently operates the synthetic multi-API/batch report in the question
- Audit Yield / ARNI / EFMS / BI findings describe the present reliability of a specific management report
- Full-population analytics alone eliminates audit risk
- Any invented reject-queue design, mapping specification, or enterprise ETL tool stack is official CRA detail

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Create [[Management Review]] as a detective control note (final-output challenge, variance explanation, reviewer ≠ preparer where required), linked from [[Management Reporting]] and the required path to [[Evidence Reliability]].
2. Extend [[Business Process Owner]] / [[Ownership and Assurance Roles]] with a short reporting chain: report owner → data owner → technical support → report-logic approver → management reviewer → AERB assurance.
3. Add an alias or thin note for **Access Controls** pointing to IAM/RBAC/Privileged Access in the pipeline context (jobs, datasets, report objects).
4. Extend [[Data Pipeline and Reporting Map]] to start at [[Business Process Owner]] and name presentation + management review stages explicitly.
5. Keep case relationships bounded: Audit Yield for multi-system measure reliance; BI for governance/ownership; ARNI for definitions/completeness; EFMS for feed timeliness—not as a single invented CRA reporting architecture.
6. Optional thin “report logic / metric calculation” stub distinguishing certified metrics from ad hoc spreadsheets ([[Business Intelligence Governance]]).

---

## Test metadata

- Test ID: Test-02-Multi-System-Management-Reporting
- Suite: Integrated Baseline multidisciplinary diagnostics
- Output path: `16-Testing/Integrated/Baseline/Test-02-Multi-System-Management-Reporting.md`
- Vault substantive notes modified by this test: **none** (output file created only)
- Process followed: searched required pipeline/reporting/ownership/evidence terms and public cases; traced source-to-report path; separated ownership classes; did not equate totals with accuracy or SGE with reliability; did not implement recommendations

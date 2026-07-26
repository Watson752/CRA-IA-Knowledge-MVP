---
title: "Test-04: Data Pipeline and Management Reporting Reliability"
note_type: testing
primary_domain: software-data
domains:
  - software
  - data
  - audit
  - risk
  - control
  - case
  - statistics
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
  - data-pipeline
  - reporting
  - evidence-reliability
---

# Test-04: Data Pipeline and Management Reporting Reliability

## Question

A management report is generated from several source systems through a data pipeline. How should an auditor assess whether the report can be relied upon?

## Answer

| Class | Use in this answer |
|---|---|
| **Official public-source** | Multi-system matching, snapshot limits, and automation barriers in [[Evaluation - Audit Yield]]; adjacent themes in [[Internal Audit - Accounts Receivable National Inventory]], [[Internal Audit - Enterprise Fraud Management System]], [[Internal Audit - Charities Audit Process]] |
| **General professional** | [[Data Quality]], [[Population Completeness]], [[Missing Data]], [[Evidence Reliability]], [[System-Generated Evidence]], [[Structured Data]], [[Business Intelligence]], [[Performance Reporting]], [[Assessment Cut-Off Date]], [[IT Controls]], [[Tool Deployment]], [[Analytics]], [[Sampling Risk]], [[Manual Control]], [[Data Governance]], [[How Statistical Limitations Affect Audit Conclusions]] |
| **Vault-derived** | End-to-end assessment checklist and data-flow model stages below—several pipeline-stage notes are **absent** |

**Reliance rule:** Do **not** treat a system-generated management report as reliable merely because it is automated ([[System-Generated Evidence]]). Do **not** treat reconciliation of totals as proof that every record and field is correct ([[Data Quality]] separates accuracy from completeness; [[Missing Data]] / [[How Missing Data Limits Audit Assurance]] warn that control totals and profiling procedures are under-specified as dedicated notes).

---

### How an auditor could assess each element

| Assessment area | What to examine | Preventive / detective | Possible procedures | Vault status |
|---|---|---|---|---|
| **Source-system completeness** | In-scope population exists in each source before extraction; no silent channel/system omissions | Preventive: source capture validations; Detective: source counts vs independent registers | Completeness testing; reconcile to control totals ([[Population Completeness]], [[Missing Data]]) | Strong concept notes; no [[Source System Data]] note |
| **Authorized data extraction** | Who/what may extract; approved jobs/APIs; credentials; scope of extract | Preventive: access & job authorization; Detective: extract logs / change tickets | Inspect extract configs, access lists, job schedules ([[IT Controls]], [[Evidence Reliability]] unknown extraction logic) | Implied; no dedicated extract-authorization note |
| **Transformation logic** | Joins, calculations, derivations, SCD/history rules, business rules in ETL | Preventive: coded peer review / automated tests; Detective: reconciling transformed vs source samples | Inspect code/specs; reperform transforms on sample ([[Structured Data]] ETL mention; [[Reperformance]]) | ETL named in [[Structured Data]]; **no** [[Data Pipeline]] / transform note |
| **Field mappings** | Source field → reporting field definitions; units; codes | Preventive: data dictionary / mapping approval; Detective: mapping QA | Trace critical fields source-to-report ([[Evidence Reliability]], [[Missing Data]] source-to-report tracing) | Tracing mentioned; no mapping note |
| **Filters and exclusions** | WHERE clauses, drop rules, “exclude refund-only,” closed-status filters | Preventive: documented inclusion criteria; Detective: excluded-population reports | Recreate filter logic; quantify exclusions ([[Missing Data]] omitted segments / filter errors; [[Population Completeness]]) | Strong on filter risk; no pipeline filter inventory note |
| **Failed or rejected records** | Reject files, error queues, re-ingestion, silent drops | Preventive: reject handling design; Detective: reject aging / volume monitoring | Inspect reject logs; reconcile expected vs loaded ([[Missing Data]] truncated/incomplete transfers; EFMS loading/re-ingestion official theme) | Themes present; no dedicated reject-record control note |
| **Duplicate records** | Same business key loaded twice; fan-out from bad joins | Preventive: uniqueness constraints; Detective: duplicate profiling | Key uniqueness tests ([[Data Quality]] uniqueness dimension); **no** [[Record Uniqueness]] note | Dimension named only |
| **Reference-data accuracy** | Codes, hierarchies, rates, org structures used in joins/calcs | Preventive: reference-data ownership; Detective: periodic ref-data cert | Sample critical reference values to authoritative source | **No** [[Reference Data]] note |
| **Reconciliation between stages** | Source → staging → integrated → reporting dataset control totals / hash totals | Preventive: automated recon rules; Detective: break reports & clearance | Stage-to-stage recon ([[Data Quality]], [[Missing Data]], [[Manual Control]]) | Described; bridge note: **no dedicated reconciliation procedure note** |
| **Report calculations** | Aggregations, ratios, rankings, KPI formulas | Preventive: certified metric definitions; Detective: calc review / independent reperformance | Recalculate KPIs; compare to [[Business Intelligence Governance]] definitions ([[Performance Reporting]]) | Conceptual coverage good |
| **Change management** | Changes to extract, transform, mappings, filters, report logic | Preventive: change approval/testing; Detective: unauthorized change detection | Inspect tickets/version history ([[IT Controls]], [[Tool Deployment]], [[System-Generated Evidence]]) | Connected at concept level; no pipeline-change playbook |
| **User access** | Who can alter pipeline jobs, datasets, or the report | Preventive: least privilege / SoD; Detective: access reviews | Test privileged/data-steward access ([[IT Controls]]; Privileged Access note missing—see Test-01) | Partial |
| **Data lineage** | Documented path from sources to report cells/metrics | Preventive: lineage tooling/metadata; Detective: lineage completeness reviews | Walk lineage for material metrics ([[Evidence Reliability]], [[Structured Data]], [[Business Intelligence]], [[Data Governance]]) | Lineage repeatedly named; **no** [[Data Lineage]] note |
| **Cut-off dates** | Which transactions/period the report claims to include | Preventive: explicit cut-off parameters; Detective: cut-off testing near period-end | Cut-off tests; compare late-arriving items ([[Assessment Cut-Off Date]], [[Initial Assessment Data]] / [[Reassessment Data]]) | **Strong** dedicated note |
| **Timeliness** | Latency from event → available in report; stale extracts | Preventive: SLA / schedule design; Detective: freshness monitors | Compare event times to load/report times ([[Data Quality]] timeliness; EFMS loading timeliness official theme) | Dimension named; no [[Data Timeliness]] note |
| **Report review and approval** | Management challenge of results before reliance/decision use | Preventive: defined review roles; Detective: secondary review / exception follow-up | Inspect sign-offs, variance explanations ([[Manual Control]], [[Performance Reporting]], [[Roles and Responsibilities]]) | Partial; no [[Management Reporting]] note (nearest: Performance Reporting / BI) |

---

### Preventive and detective controls (summary)

| Type | Pipeline / reporting examples | Vault anchors |
|---|---|---|
| **Preventive** | Source validations; authorized extract jobs; approved mappings; change control; access restriction; certified metric definitions | [[Data Quality]], [[IT Controls]], [[Tool Deployment]], [[Data Governance]], [[Business Intelligence Governance]] |
| **Detective** | Stage reconciliations; reject monitoring; duplicate profiling; cut-off tests; calc reperformance; management review of variances | [[Data Quality]], [[Missing Data]], [[Population Completeness]], [[Manual Control]], [[Monitoring and Reporting]], [[Analytics]] |

---

### Statistical or analytical limitations

- Matching totals across stages can hide offsetting errors, wrong-record inclusion, and field-level inaccuracy—completeness ≠ accuracy ([[Data Quality]]).
- Full-population [[Analytics]] reduces [[Sampling Risk]] but fails if the frame is incomplete ([[Population Completeness]], [[Missing Data]]).
- Snapshot timing and late data change results ([[Assessment Cut-Off Date]], [[Statistical Revision]], [[Initial Assessment Data]] / [[Reassessment Data]]).
- [[Rounding]] and [[Data Suppression]] can make reports not foot or omit cells by design—disclose, do not invent.
- Conclusion strength must match evidence strength ([[How Statistical Limitations Affect Audit Conclusions]], [[How Missing Data Limits Audit Assurance]]).
- No universal % completeness threshold for reliance ([[Missing Data]]).

---

### One public CRA case (supported)

**Primary: [[Evaluation - Audit Yield]]** (official public source)

**Why it fits:** A management-relevant performance measure (cash recovered / audit yield) depends on linking **several systems** (e.g., AIMS, INTEGRAS, assessing/accounting data) with definitions, timing, exclusions, and match rates—not on a single final dashboard number.

**Official facts used for teaching reliance:**

- Measure definitions matter (fiscal impact ≠ collectible cash ≠ audit yield).
- Methodology combines population queries and **stratified** sampling with stated confidence for a segment; GST/HST matching described as accurate/reliable in-report for the tested approach; income tax required manual matching.
- Automation barriers: e.g., **8%** of T1 INTEGRAS debit files lacked matching audit file numbers; **15%** of sampled T2 AIMS files unmatched (**22%** of federal tax value).
- Results as of a **July 2019** snapshot; expected to change as appeals/collections conclude.
- Recommendations addressed integrated measurement and cross-branch data linking (historical MAP targets in the case note).

**Bounded teaching use:** Shows why auditors must assess cross-system lineage, matching completeness, exclusions, and snapshot cut-off before relying on a multi-source management measure. Does **not** document a modern ETL platform inventory, API specs, or current pipeline controls. Historical findings are not current-state claims.

**Adjacent cases (optional corroboration, not required for the score):**

- [[Internal Audit - Accounts Receivable National Inventory]] — incomplete attribution/movement views for decision use; business-rule outcome monitoring gaps
- [[Internal Audit - Enterprise Fraud Management System]] — expected-record matching / re-ingestion timeliness into a monitoring layer
- [[Internal Audit - Charities Audit Process]] — incomplete data dispersed across sources; reconciliation need when transferring manually

---

## Data-flow model

Required model:

```text
Source systems
→ extraction
→ transformation
→ integration
→ reconciliation
→ reporting dataset
→ report logic
→ management review
→ audit reliance
```

| Stage | Auditor focus | Vault support |
|---|---|---|
| Source systems | Completeness, definitions, authorized sources | [[Evidence]] (validate source systems); no Source System Data note |
| Extraction | Authorized jobs/APIs/batches; extract scope | [[Evidence Reliability]] (extraction logic); no API/Batch notes |
| Transformation | Logic, mappings, filters, rejects, duplicates | [[Structured Data]] ETL; [[Missing Data]] filters/joins; thin on rejects/duplicates as controls |
| Integration | Multi-source keys/joins | Audit Yield official matching theme; Charities dispersed sources |
| Reconciliation | Stage totals ≠ field accuracy proof | [[Data Quality]], [[Missing Data]], [[Manual Control]]; no Data Reconciliation note |
| Reporting dataset | Certified curated table/mart | [[Business Intelligence]], [[Structured Data]] |
| Report logic | KPI calculations / presentation rules | [[Performance Reporting]] |
| Management review | Challenge, approval, variance follow-up | [[Manual Control]], [[Roles and Responsibilities]] |
| Audit reliance | Sufficient appropriate evidence + stated limits | [[System-Generated Evidence]], [[Evidence Reliability]], [[Evidence Evaluation]] |

**Nearest existing fragment path:**

```text
Source systems ([[Evidence]], [[IT Controls]])
→ extraction / ETL ([[Structured Data]], [[Evidence Reliability]])
→ quality & completeness ([[Data Quality]], [[Missing Data]], [[Population Completeness]])
→ cut-off / timeliness ([[Assessment Cut-Off Date]], [[Initial Assessment Data]])
→ BI / performance report ([[Business Intelligence]], [[Performance Reporting]])
→ lineage & ITGC dependency ([[System-Generated Evidence]], [[Data Governance]])
→ limitations ([[How Missing Data Limits Audit Assurance]], [[How Statistical Limitations Affect Audit Conclusions]])
→ [[Evaluation - Audit Yield]] (multi-system measure)
→ audit reliance decision ([[Evidence]], [[Evidence Evaluation]])
```

---

## Notes and cases used

### Notes present

- [[Data Quality]] · [[Population Completeness]] · [[Missing Data]] · [[Evidence Reliability]]
- [[System-Generated Evidence]] · [[Evidence]] · [[Evidence Evaluation]] · [[Evidence Hierarchy]]
- [[Structured Data]] · [[Analytics]] · [[Sampling Risk]] · [[Assessment Cut-Off Date]]
- [[Initial Assessment Data]] · [[Reassessment Data]] · [[Statistical Revision]]
- [[Business Intelligence]] · [[Business Intelligence Governance]] · [[Performance Reporting]]
- [[Data Governance]] · [[Data Owner]] · [[Technical Support]] (pipelines mentioned as custodial context)
- [[IT Controls]] · [[Tool Deployment]] · [[Manual Control]] · [[Monitoring and Reporting]]
- [[Rounding]] · [[Data Suppression]] · [[How Statistical Limitations Affect Audit Conclusions]]
- [[How Missing Data Limits Audit Assurance]] · [[Roles and Responsibilities]]

### Cases / sources

- [[Evaluation - Audit Yield]] — primary multi-source reporting/lineage case
- [[Internal Audit - Accounts Receivable National Inventory]] — metric completeness / attribution
- [[Internal Audit - Enterprise Fraud Management System]] — load/re-ingestion completeness & timeliness
- [[Internal Audit - Charities Audit Process]] — multi-source incomplete data / reconciliation need
- [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] — BI evidence caution / incomplete performance stories

### Searched; dedicated-note results

| Sought term | Result |
|---|---|
| Source System Data | Not found |
| Data Pipeline | Not found (ETL/pipelines mentioned in [[Structured Data]], [[Technical Support]], [[Data Owner]]) |
| API Integration | Not found |
| Batch Processing | Not found |
| Transactional Dataset | Not found |
| Reference Data | Not found |
| Data Lineage | Not found as titled note (lineage concept repeated in several notes) |
| Data Reconciliation | Not found as titled note (reconciliation procedures described under [[Missing Data]] / [[Data Quality]]) |
| Data Quality | **Present** |
| Population Completeness | **Present** |
| Record Uniqueness | Not found (uniqueness dimension in [[Data Quality]]) |
| Data Accuracy | Not found (accuracy dimension in [[Data Quality]]) |
| Data Timeliness | Not found (timeliness dimension in [[Data Quality]] / [[Performance Reporting]]) |
| Management Reporting | Not found (nearest: [[Performance Reporting]], [[Business Intelligence]]) |
| Evidence Reliability | **Present** |

---

## Diagnostic evaluation

| Check | Finding |
|---|---|
| Does the vault focus only on the final report? | **No.** [[Structured Data]], [[System-Generated Evidence]], [[Missing Data]], and [[Business Intelligence]] push attention upstream to lineage, extraction, and quality. |
| Does it address transformations and failed records? | **Partially.** ETL/filters/joins/truncation/re-ingestion themes exist; dedicated transformation, reject-queue, and mapping notes do not. |
| Does it distinguish accuracy from completeness? | **Yes.** [[Data Quality]] lists them as separate dimensions; [[Population Completeness]] / [[Missing Data]] deepen completeness. |
| Does it connect change management to pipeline reliability? | **Partially.** [[System-Generated Evidence]] and [[IT Controls]] / [[Tool Deployment]] connect change management to system-evidence reliability; not a pipeline-specific change playbook. |
| Does it explain report-period cut-offs? | **Yes.** [[Assessment Cut-Off Date]] plus initial vs reassessment data. |

### Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| End-to-end data-flow understanding | **1** | Source→ETL→reporting lineage is named across notes, but Data Pipeline / Source System Data / API / Batch / Lineage are not first-class stage notes; model must be assembled. |
| Data-quality and completeness analysis | **2** | Strong [[Data Quality]] dimensions, [[Population Completeness]], [[Missing Data]] (filters, truncation, segments), and explicit caution that structure/totals ≠ accuracy. |
| Control and procedure coverage | **1** | Preventive/detective ideas and a procedure list exist under [[Missing Data]] / [[Data Quality]], but reconciliation/profiling/reject handling lack dedicated procedure notes; mappings/reference data thin. |
| Evidence-reliance reasoning | **2** | [[System-Generated Evidence]], [[Evidence Reliability]], BI caution, and conclusion-strength bridges clearly limit blind reliance on management reports. |
| Public-case application | **2** | [[Evaluation - Audit Yield]] cleanly demonstrates multi-system measure reliance limits (matching, definitions, snapshot) without overstating current pipeline architecture. |
| **Total** | **8 / 10** | |

---

## Missing pipeline concepts

- Source System Data
- Data Pipeline (stage model)
- API Integration
- Batch Processing
- Transactional Dataset
- Reference Data
- Data Lineage (titled note)
- Data Reconciliation (titled note)
- Record Uniqueness / Data Accuracy / Data Timeliness (as standalone notes beyond [[Data Quality]] dimensions)
- Management Reporting (distinct from [[Performance Reporting]] / BI)
- Rejected / failed record handling
- Field mapping / transformation specification

---

## Missing controls

- Authorized extraction / interface control (API keys, job accounts, extract approval)
- Transformation change control tied to report certification
- Reject-and-reprocess control with aging and clearance
- Duplicate detection/prevention at load and join points
- Reference-data stewardship and certification
- Automated stage-reconciliation with break escalation
- Report certification / management approval control (beyond generic manual review)
- Pipeline privileged-access control (who can change jobs and datasets)

---

## Missing audit procedures

[[How Missing Data Limits Audit Assurance]] already notes the gap: no dedicated procedure notes for reconciliation or profiling. Still missing as teachable procedures:

- End-to-end source-to-report walkthrough for a material KPI
- Mapping table inspection and field-level reperformance
- Reject-file completeness testing
- Duplicate-key analytics across stages
- Reference-data substantive testing
- Stage hash/control-total reconciliation workbook standard
- Cut-off testing specifically for pipeline load windows vs report period
- Change-diff review of ETL/report logic across the audit period
- Access testing for pipeline and semantic-layer objects

---

## Unsupported claims

Do **not** claim from the vault:

- Current CRA enterprise pipeline architectures, tools, or control effectiveness
- That Audit Yield evaluated a specific ETL platform or API layer (it evaluates measurement/matching of audit yield / cash recovery)
- That stage reconciliation alone proves field accuracy
- That BI dashboards are automatically reliable evidence
- That cut-off notes describe every operational pipeline calendar (they teach the cut-off concept)
- Numeric completeness thresholds for reliance

Assessment steps and the required data-flow model in this file are **vault-derived teaching**, not official CRA audit manuals.

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Create stage notes for the model: **Source System Data**, **Data Pipeline**, **Data Lineage**, **Data Reconciliation**, plus **API Integration** / **Batch Processing** as extraction patterns.
2. Add **Reference Data**, **Record Uniqueness**, and thin **Data Accuracy** / **Data Timeliness** notes that point back to [[Data Quality]] dimensions with pipeline examples.
3. Create a **Management Reporting** note linking [[Performance Reporting]], [[Business Intelligence]], and reliance conditions from [[System-Generated Evidence]].
4. Add a procedure note (or expand [[Missing Data]]): source-to-report tracing, stage reconciliation, reject testing, mapping reperformance—stating explicitly that balanced totals ≠ field accuracy.
5. Wire [[Assessment Cut-Off Date]] and load-window timeliness into the Data Pipeline note (report period vs pipeline freshness).
6. Cross-link [[Evaluation - Audit Yield]] as the primary multi-source reliance case; ARNI/EFMS/Charities as secondary completeness/transfer examples.
7. Connect pipeline change management and access testing to [[IT Controls]] / [[Tool Deployment]] with a short worked checklist.
8. Add aliases so searches for ETL, lineage, reconciliation, and management report resolve to the new notes.

---

## Test metadata

- Test ID: Test-04-Data-Pipeline-and-Reporting
- Suite: Software-Data Baseline onboarding diagnostics
- Output path: `16-Testing/Software-Data/Baseline/Test-04-Data-Pipeline-and-Reporting.md`
- Vault notes modified by this test: **none** (output file created only)
- Process followed: searched pipeline/lineage/quality/reporting terms and public cases; assessed source-to-report coverage; checked transforms/filters/rejects/cut-offs; did not treat total reconciliation as field-level proof; did not implement recommendations

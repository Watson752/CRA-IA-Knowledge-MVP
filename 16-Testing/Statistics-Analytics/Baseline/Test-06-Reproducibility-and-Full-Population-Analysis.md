---
title: "Test-06: Reproducibility and Full-Population Analysis"
note_type: testing
primary_domain: statistics-analytics
domains:
  - statistics
  - data
  - audit
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
  - statistics-analytics
  - onboarding
  - full-population-analysis
  - reproducibility
---

# Test-06: Reproducibility and Full-Population Analysis

## Question

When does full-population data analysis strengthen an audit, what risks remain, and what makes an analytical result reproducible?

## Answer

Full-population analysis strengthens an engagement when structured data allow testing **all available in-scope records**, reducing [[Sampling Risk]] and surfacing rare or concentrated exceptions that samples may miss. It does **not** eliminate audit risk: the available extract may still be incomplete or inaccurate, and query/logic errors can produce a clean but wrong answer. Reproducibility (same inputs + method → same result) is necessary for defensible analytics but is **not** the same as validity (method and interpretation answer the audit question).

| Content class | Role in this answer |
|---|---|
| **General professional** | [[Full-Population Analysis]], [[Analytics]], [[Sampling Risk]], [[Population Completeness]], [[Data Quality]], [[Data Lineage]], pipeline notes, [[Evidence Reliability]], [[Methodology]], [[Reperformance]] |
| **Official public-source** | Audit Yield population/query methods and matching limits; EFMS FP/rule-change themes |
| **Vault-derived packaging** | Expanded benefit list; reproducibility checklist; reproducible vs valid distinction (not a dedicated vault note) |

**Vault recognition (required check):** Testing all available records does **not** guarantee completeness or accuracy. [[Full-Population Analysis]] explicitly remains limited by [[Data Quality]] and [[Population Completeness]]. [[Sampling Risk]] says full-population testing **reduces** sampling risk but **introduces other limitations**. [[Population Completeness]] tells auditors to state when conclusions apply only to **retrieved subsets**.

Do **not** imply that full-population testing eliminates all audit risk. Do **not** claim that reproducibility alone proves the analysis is correct.

---

### Benefits of full-population analysis

[[Full-Population Analysis]] is a one-sentence hub. Benefits are assembled from that note plus [[Analytics]] / [[Sampling Risk]] / case practice:

| Benefit | Vault anchors |
|---|---|
| Broader coverage | Tests all in-scope records when data allow ([[Full-Population Analysis]]) |
| Rare or concentrated exceptions | [[Analytics]] tests populations for exceptions; override concentration themes ([[Unmonitored Manual Overrides]]) |
| Reduced sampling variability | **Reduces** [[Sampling Risk]] (does not claim zero residual audit risk) |
| Segment and compare groups | Stratify/slice by rule, period, risk ([[Sample Selection]], [[Stratified Sampling]]); full data enables group rates |
| Patterns across the full **available** dataset | [[Analytics]] descriptive/diagnostic use; still bound by retrieved population |

**When it strengthens an audit:** structured, complete-enough extracts; clear inclusion rules; questions about exception rates, concentrations, or rule outcomes across the period; complement to sample-based deep tests of evidence.

---

### Remaining risks

| Residual risk | Vault anchors |
|---|---|
| Incomplete population | [[Population Completeness]], [[Missing Data]], retrieved-subset limits |
| Incorrect extraction | [[Source System Data]], unknown extraction logic ([[Evidence Reliability]]) |
| Transformation errors | [[Data Pipeline]], [[Data Transformation]], [[Field Mapping]] |
| Duplicate or missing records | [[Record Uniqueness]], [[Missing Data]], [[Rejected Records]] |
| Inaccurate fields | [[Data Accuracy]], [[Data Quality]] (totals reconciliation ≠ field accuracy) |
| Changing definitions | [[Comparability Across Editions]], [[Statistical Revision]], [[Outdated Analytics]] |
| Poor business-rule logic | [[Automated Business Rules]], [[Incorrect Automated Decisions]], [[Change Management]] |
| False positives | [[False Positives]] (alert/rule noise) |
| Model or query errors | Documented logic/scripts ([[Analytics]]); association ≠ causation |
| Inappropriate interpretation | [[How Statistical Limitations Affect Audit Conclusions]], [[Professional Judgment]], [[Criteria]] |

Pipeline path for where residual risk enters:

```text
[[Source System Data]]
→ [[Data Pipeline]] (extract / transform / reject)
→ analysed “full” extract
→ [[Analytics]] / [[Full-Population Analysis]]
→ [[Evidence Reliability]]
→ conclusion strength
```

---

### Reproducibility requirements

**Vault status:** No dedicated [[Reproducibility]] note. Related statements:

- [[Analytics]]: quality hinges on documented logic, **reproducibility**, and analyst competence; document **data sources, scripts, and limitations**.
- [[Evidence Reliability]]: consider whether **analytics scripts are version-controlled**.
- [[Methodology]]: documented methodology supports **reproducibility**, peer review, and defensibility; record methodology changes.
- [[Outdated Analytics]]: absent **version control** contributes to stale scripts/models.
- [[Structured Data]]: request extracts with documented definitions and [[Assessment Cut-Off Date]] alignment.
- [[Data Lineage]]: path from source fields through transforms to report metrics (pipeline/report lineage—not a full analytics-workpaper standard).
- [[Reperformance]]: independent execution to validate outcomes (persuasion when source data reliable).

**Assembled checklist** (vault-derived packaging of required elements):

| Requirement | Present in vault? |
|---|---|
| Documented source | **Yes** — [[Analytics]], [[Source System Data]], [[Data Lineage]] |
| Extraction date / cut-off | **Partial** — [[Assessment Cut-Off Date]]; extract timestamp not a dedicated field |
| Query or code | **Yes** — scripts ([[Analytics]], [[Evidence Reliability]]) |
| Parameters | **Thin** — not enumerated |
| Software / package versions | **Thin** — version control mentioned; package versions not |
| Transformation steps | **Yes** — [[Data Pipeline]], [[Data Transformation]], [[Field Mapping]] |
| Data dictionary / definitions | **Partial** — documented definitions ([[Structured Data]]); no Data Dictionary note |
| Inclusion / exclusion rules | **Partial** — [[Scope]], [[Missing Data]] omitted segments; Audit Yield exclusions in case |
| Exception handling | **Yes** — [[Rejected Records]], [[Exception Handling]] |
| Retained outputs | **Thin** — workpaper/evidence retention implied; not analytics-specific |
| Review or independent reperformance | **Yes** — [[Methodology]] peer review; [[Reperformance]] |

---

### Reproducible versus valid

**Vault does not state this distinction explicitly.** Teaching packaging required for the diagnostic:

```text
Reproducible
→ another analyst can obtain the same result from the same inputs and method

Valid
→ the method and interpretation appropriately answer the audit question
```

A result may be **reproducible but still invalid** because the population, logic, or assumptions are wrong (e.g., reproducible query on an incomplete extract; reproducible join that duplicates keys; reproducible association misread as causation).

Nearby vault ideas (not a full substitute):

- [[Evidence Reliability]]: reliability judged relative to [[Audit Objective]] / [[Criteria]]—not absolute truth.
- [[Analytics]]: association ≠ causation.
- [[Population Completeness]]: full analysis of a retrieved subset ≠ intended population.
- [[Data Reconciliation]]: balanced totals ≠ field accuracy.

---

## Benefits and limitations (summary)

| | Full-population analysis |
|---|---|
| **Strengthens when** | Data allow; coverage of available in-scope records matters; rare/concentrated issues; segmentation |
| **Does not remove** | Completeness, accuracy, lineage, definition, logic, FP, and interpretation risk |
| **Sampling risk** | **Reduced**, not “all audit risk eliminated” ([[Sampling Risk]], [[Full-Population Analysis]]) |
| **Evidence value** | High potential if reproducible **and** valid; scripts/sources documented ([[Analytics]], [[Evidence Reliability]]) |
| **Conclusion link** | Match assertion strength to evidence; qualify when only retrieved subset ([[How Statistical Limitations Affect Audit Conclusions]], [[Population Completeness]]) |

---

## Notes and cases used

### Search results

| Sought | Result |
|---|---|
| Full-Population Analysis | [[Full-Population Analysis]] (thin) |
| Data Analysis | [[Analytics]] (alias Data Analysis) |
| Reproducibility | **No dedicated note**; word in [[Analytics]], [[Methodology]] |
| Population Completeness | [[Population Completeness]] |
| Data Quality | [[Data Quality]] · [[Data Accuracy]] · [[Record Uniqueness]] |
| Data Lineage | [[Data Lineage]] |
| Source System Data | [[Source System Data]] |
| Data Pipeline | [[Data Pipeline]] · [[Data Pipeline and Reporting Map]] |
| Change Management | [[Change Management]] |
| Sampling Risk | [[Sampling Risk]] |
| Evidence Reliability | [[Evidence Reliability]] |
| Relevant public cases | Below |

Also used: [[Data Transformation]], [[Field Mapping]], [[Rejected Records]], [[Data Reconciliation]], [[False Positives]], [[Comparability Across Editions]], [[Outdated Analytics]], [[Structured Data]], [[Assessment Cut-Off Date]], [[Reperformance]], [[Methodology]], [[How Statistical Limitations Affect Audit Conclusions]], [[Automated Business Rules]], [[Incorrect Automated Decisions]].

### Public CRA cases

| Case | Official / bounded use |
|---|---|
| [[Evaluation - Audit Yield]] | Population analysis / query coverage for GST and large IT cohorts; stated exclusions; matching gaps limit agency-wide automation confidence; lineage/definitions matter for measure reliance |
| [[Internal Audit - Enterprise Fraud Management System]] | FP-heavy rules; ad hoc rule changes / incomplete central history—logic and change risk remain even with large alert volumes |
| [[Internal Audit - Accounts Receivable National Inventory]] | Incomplete measures/attribution—analysing “all” of an incomplete metric view still misleads |

---

## Diagnostic checks

| Check | Finding |
|---|---|
| Say full-population analysis eliminates sampling risk entirely? | **No.** Language is **reduce** sampling risk; other limitations remain. |
| Recognise only available population may have been tested? | **Yes.** Retrieved-subset / completeness limits. |
| Document analytical lineage? | **Partial.** Strong pipeline/report [[Data Lineage]]; analytics workpaper elements (params, package versions, retained outputs) thin. |
| Distinguish repeatability from correctness? | **No** explicit reproducible vs valid teaching. |
| Connect errors to conclusion strength? | **Yes.** Evidence reliability + statistical-limitations / qualify conclusions. |

---

## Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Full-population benefit clarity | **1** | Correct reduce-sampling-risk core; benefits beyond that are thin and must be assembled. |
| Residual-risk coverage | **2** | Completeness, quality, pipeline, uniqueness, FP, definitions, and interpretation risks are well represented. |
| Reproducibility requirements | **1** | Sources/scripts/version control/methodology named; no checklist note covering params, package versions, dictionary, retained outputs. |
| Reproducibility-versus-validity distinction | **0** | Not taught as a first-class distinction. |
| Audit and source application | **2** | Full-pop note + Sampling Risk + cases (Yield/EFMS/ARNI) support residual-risk teaching without over-claim. |
| **Total** | **6 / 10** | |

---

## Missing reproducibility elements

| Element | Gap |
|---|---|
| Dedicated **Reproducibility** note | Concept buried in Analytics/Methodology |
| Extraction timestamp / extract ID standard | Cut-off present; extract dating not standardized |
| Parameter and seed logging | Absent |
| Software/package/version matrix | Only “version-controlled scripts” |
| Data dictionary note | Definitions mentioned ad hoc |
| Retained inputs/outputs / hash of extract | Absent |
| Independent reperformance of **analytics** (not only controls) | [[Reperformance]] is control-procedure oriented |
| Explicit reproducible ≠ valid | Missing |

---

## Unsupported claims

Do **not** claim from the vault or this test:

- That full-population analysis eliminates all audit risk or all sampling-related residual risk in every sense
- That testing 100% of an extract proves the intended population is complete
- That reproducibility proves correctness or validity
- That balanced reconciliations prove field accuracy
- That Audit Yield or EFMS performed a vault-standard reproducible analytics workpaper package
- That association in full-population results implies causation

---

## Missing data/software links

| Weak link | Impact |
|---|---|
| [[Full-Population Analysis]] → [[Data Lineage]] / [[Data Pipeline]] / [[Source System Data]] | Hub does not point to residual pipeline risks |
| [[Analytics]] → [[Reperformance]] / reproducibility checklist | Reproducibility named, not operationalized |
| [[Data Lineage]] → auditor analytics scripts (vs report ETL only) | Lineage reads as reporting provenance |
| [[Change Management]] → analytics code/query change control | Change note centers systems/rules/pipelines |
| [[Evidence Reliability]] ↔ reproducible-but-invalid examples | Reliability/relevance split present; validity of analysis logic thin |

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Expand [[Full-Population Analysis]] with a short benefits list and an explicit residual-risk list pointing to Completeness, Quality, Pipeline, FP, and interpretation notes.
2. Add Class C note **Reproducibility** (analytics workpapers): source, extract date, code, parameters, versions, transforms, dictionary, inclusion/exclusion, exceptions, outputs, review/reperformance.
3. State on [[Analytics]] or the new note: **reproducible ≠ valid**; wrong population or logic can reproduce a wrong answer.
4. Link [[Full-Population Analysis]] to [[Data Lineage]], [[Source System Data]], [[Data Pipeline]], and [[Evidence Reliability]].
5. Keep “reduces sampling risk” wording; never upgrade to “eliminates all audit risk.”
6. Use Audit Yield as the worked example of population/query analysis still limited by matching, definitions, and snapshots.

---

## Test metadata

- Test ID: Test-06-Reproducibility-and-Full-Population-Analysis
- Suite: Statistics-Analytics Baseline onboarding diagnostics
- Output path: `16-Testing/Statistics-Analytics/Baseline/Test-06-Reproducibility-and-Full-Population-Analysis.md`
- Vault notes modified by this test: **none** (output file created only)
- Process followed: searched full-population/analysis/reproducibility/completeness/quality/lineage/source/pipeline/change/sampling/evidence terms and public cases; confirmed available-population and residual-risk recognition; assessed analytics documentation elements; avoided claiming full-population eliminates all risk or that reproducibility proves correctness; did not implement recommendations

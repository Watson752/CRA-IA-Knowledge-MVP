---
title: "Test-04: Evidence Quality"
note_type: testing
primary_domain: audit
domains:
  - audit
  - data
  - statistics
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
  - evidence
  - data-quality
---

# Test-04: Evidence Quality

## Question

What makes audit evidence sufficient, appropriate and reliable, and how do software systems and data limitations affect that assessment?

## Answer

[[Evidence]] must be **sufficient**, **appropriate**, and **reliable** for the engagement purpose. Quantity alone is not enough: [[Evidence Reliability]] and [[Data Quality]] judge whether the information can support the conclusion without material misstatement or ambiguity. Software extracts, logs, and dashboards help only when lineage, access controls, completeness, and change management support trust.

**No universal evidence threshold.** [[Missing Data]] states there is no universal missing-data percentage that automatically requires a qualified conclusion. Strength depends on [[Audit Objective]], [[Criteria]], materiality, why data is missing, and whether alternative evidence exists.

| Content class | Role in this answer |
|---|---|
| **General professional** | [[Evidence]], [[Evidence Reliability]], [[Data Quality]], [[Population Completeness]], [[Sampling Risk]], [[IT Controls]] |
| **Official public-source** | Methodology limits and matching/completeness facts in case notes |
| **Vault-derived / Class B** | Evidence-type comparison table below; cross-domain chain in [[How Missing Data Limits Audit Assurance]] |

---

### Sufficiency — quantity and coverage

**General professional ([[Evidence]]):** sufficiency relates to **quantity**. Coverage matters: partial populations, redactions, and cut-offs are forms of [[Missing Data]] that can reduce sufficiency even when remaining items are accurate.

Sufficiency asks: *Is there enough evidence, across enough of the in-scope population and period, to support the assertion?* Related: [[Scope]], [[Sampling Risk]], [[Population Completeness]].

### Appropriateness — relevance and reliability

**General professional ([[Evidence]]):** appropriateness relates to **relevance and persuasiveness**. [[Evidence Reliability]] adds the explicit split: **distinguish reliability from relevance**—reliable but off-scope data still fails appropriateness.

Appropriateness asks: *Is this the right evidence for the criteria, and is it persuasive/reliable enough?*

### Why more low-quality evidence may not fix reliability

**General professional / vault-derived synthesis:**

- Reliability rises with independent sources, system integrity, documented lineage, and **corroboration**; it falls with manual manipulation, weak access controls, or unknown extraction logic ([[Evidence Reliability]]).
- Stacking more extracts from the same weak source does not create independence.
- [[Data Quality]] is contextual: operationally usable data may still be unfit for forensic or population-level assurance.
- [[Missing Data]] asks whether alternative evidence exists; if the defect is systematic (filter error, broken lineage), volume does not repair validity.

### Differences among evidence types

Vault lists types in [[Evidence]] and methods in [[Control]] (inquiry, observation, inspection, reperformance, analytics). There is **no** dedicated evidence-hierarchy note; the comparison below is **vault-derived packaging** of those terms plus [[Evidence Reliability]] / [[IT Controls]].

### How missing data or incomplete populations weaken evidence

```text
Missing data
→ weaker data quality
→ possible population incompleteness
→ increased sampling or analytical risk
→ weaker evidence reliability
→ narrower or more qualified conclusions
```

Source: [[Missing Data]] (and bridge [[How Missing Data Limits Audit Assurance]]). Incomplete populations inflate [[Sampling Risk]] and can invalidate extrapolation ([[Population Completeness]]).

### How system-generated evidence depends on software controls

**General professional:**

| Dependency | Why it matters | Vault anchors |
|---|---|---|
| Access controls | Who can alter data or logs | [[Evidence Reliability]], [[IT Controls]], [[Security Controls]] |
| Configuration | Rules/reports reflect intended design | [[IT Controls]], [[Tool Deployment]] |
| Data lineage / extraction logic | Unknown transforms undermine reliability | [[Evidence Reliability]], [[Structured Data]] |
| Change management | Silent rule/report changes break period OE | [[IT Controls]], [[Tool Deployment]] |
| Logging / monitoring | Logs must be protected and complete enough | [[Evidence Reliability]], [[Monitoring and Reporting]] (no dedicated Audit Logging note) |
| Completeness of feeds | Truncated loads / re-ingestion gaps | [[Missing Data]], [[Population Completeness]] |

System origin alone does **not** make evidence reliable ([[Evidence Reliability]]; EFMS case notes alert counts are not sufficient evidence by themselves).

### How evidence limitations affect conclusion wording

- Incomplete evidence → scope-limit or qualify ([[Evidence]])
- Match assertion strength to evidence strength ([[How Statistical Limitations Affect Audit Conclusions]])
- State what was verified vs taken as-is; use directional language when precision is unsupported
- Document limitations in methodology/scope so [[Finding]] language stays defensible
- Do not invent numeric cut-offs ([[Missing Data]], [[How Missing Data Limits Audit Assurance]])

---

## Evidence hierarchy or comparison

Relative persuasiveness for many control/assertion tests (**vault-derived teaching scale**, not an official CRA rule):

| Evidence form | Typical strength | Main reliability caveats | Vault anchors |
|---|---|---|---|
| **Inquiry / interview notes** | Lowest alone | Management representation; needs corroboration | [[Evidence]], [[Control]] |
| **Documents / procedures** | Design and intent | May not prove operation | [[Evidence]], [[Control Ownership]] |
| **System reports / dashboards** | Medium if lineage known | Config, filters, definitions, change history | [[Performance Reporting]], [[Business Intelligence]], [[Evidence Reliability]] |
| **Logs / audit trails** | Stronger when protected and complete | Access to logs; gaps; clock/sync; retention | [[Evidence Reliability]], [[Monitoring and Reporting]] |
| **Direct observation** | Strong for “at a point in time” | Not period coverage by itself | [[Control]], [[Evidence]] |
| **Inspection of period evidence** | Strong for OE when sampled well | Population frame errors | [[Evidence]], [[Sampling Risk]] |
| **Reperformance / independent analytics** | Often strongest | Still depends on complete, accurate source data | [[Control]], [[Analytics]], [[Structured Data]] |
| **External confirmation / independent totals** | High when available | Coverage and timing | [[Evidence]], [[Population Completeness]] |

**Corroboration pattern (general professional):** combine inquiry + documents + system evidence; reconcile to independent totals where possible; do not accept data at face value without validating source systems ([[Evidence]]).

---

## Public CRA case example

### Primary: [[Evaluation - Audit Yield]]

**Official public-source facts (historical):**

- Objective: assess ability to measure cash recovered from audit reassessments (audit yield ≠ full fiscal impact).
- Methodology mixes query coverage, stratified sampling with stated **95% confidence** for a sampled income-tax segment, GST/HST population analysis, interviews, and document review.
- Finding on automation barriers: GST/HST matching largely feasible; income tax required manual matching; **8%** of T1 INTEGRAS debit files lacked matching audit file numbers; **15%** of sampled T2 AIMS files unmatched (**22%** of federal tax value).
- Public limitations: single-year snapshots (as of July 2019); income tax matching gaps affect population-level automation confidence; results change as appeals/collections conclude.

**How this teaches evidence quality (vault-derived interpretation using linked concepts):**

| Theme | Application |
|---|---|
| Sufficiency / coverage | Query/sample/population choices define how much of the universe supports the measure |
| Appropriateness | Cash-recovery definition must match the decision; fiscal impact is related but not the same metric |
| Reliability / lineage | Cross-system matching (AIMS, INTEGRAS, assessing/accounting data) is a lineage and [[Data Quality]] problem |
| Population completeness | Unmatched identifiers and snapshot limits weaken agency-wide automation confidence ([[Population Completeness]], [[Missing Data]]) |
| Conclusion strength | Report states confidence for specified segments; warns against treating illustrative ratios as enduring performance targets ([[How Statistical Limitations Affect Audit Conclusions]]) |

Related case links in vault: [[Evidence Reliability]], [[Population Completeness]], [[Data Quality]], [[Missing Data]].

### Secondary illustrations

- [[Internal Audit - Accounts Receivable National Inventory]] — incomplete performance/attribution measures; collapsed inventories; monitoring that controls worked was limited.
- [[Internal Audit - Charities Audit Process]] — limited/incomplete data across sources; population-level impartiality reporting limited; documented approvals not always complete.
- [[Internal Audit - Enterprise Fraud Management System]] — re-ingestion/timeliness; redactions; alert counts not sufficient alone.
- [[Internal Audit - Specific Cyber Security Controls]] — protected content forces uncertainty in public conclusions.

---

## Notes and cases used

### Core evidence / data notes

- [[Evidence]]
- [[Evidence Reliability]]
- [[Data Quality]]
- [[Population Completeness]]
- [[Missing Data]]
- [[Data Suppression]]
- [[Sampling Risk]]
- [[How Statistical Limitations Affect Audit Conclusions]]
- [[How Missing Data Limits Audit Assurance]]
- [[Assessment Cut-Off Date]]
- [[Analytics]] · [[Structured Data]] · [[Unstructured Information]]
- [[IT Controls]] · [[Security Controls]] · [[Tool Deployment]] · [[Monitoring and Reporting]]
- [[Performance Reporting]] · [[Business Intelligence]]
- [[Audit Objective]] · [[Scope]] · [[Criteria]] · [[Methodology]] · [[Finding]] · [[Control]]

### Cases / sources

- [[Evaluation - Audit Yield]] (primary)
- [[Internal Audit - Accounts Receivable National Inventory]]
- [[Internal Audit - Charities Audit Process]]
- [[Internal Audit - Enterprise Fraud Management System]]
- [[Internal Audit - Specific Cyber Security Controls]]
- [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]]
- [[Content Classification Model]]

### Searched; thin or missing as dedicated notes

| Sought | Result |
|---|---|
| Audit Logging | No dedicated note; logs mentioned in [[Evidence Reliability]] / [[Monitoring and Reporting]] |
| Reperformance / Inspection / Inquiry | Named in [[Control]] / [[Evidence]]; no procedure notes |
| Formal “evidence hierarchy” | Not present as a note |
| Sufficiency / Appropriateness titled stubs | Concepts live inside [[Evidence]] |

---

## Diagnostic evaluation

| Check | Finding |
|---|---|
| Evidence reliable merely because it came from a system? | **No.** [[Evidence Reliability]] and EFMS explicitly reject that shortcut. |
| Source reliability distinguished from relevance? | **Yes.** [[Evidence Reliability]]: reliable but off-scope fails appropriateness. |
| Population completeness recognised? | **Yes.** Dedicated [[Population Completeness]] + case links. |
| Corroboration explained? | **Yes** in [[Evidence]] and [[Evidence Reliability]]; alternative evidence in [[Missing Data]] questions. |
| Uncertainty stated appropriately? | **Yes.** No universal threshold; qualify/scope-limit; match assertion strength to evidence. |

### Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Sufficiency-versus-appropriateness distinction | **2** | Clear in [[Evidence]]; relevance vs reliability reinforced in [[Evidence Reliability]]. |
| Reliability factors | **1** | Independence, integrity, lineage, access, and corroboration are covered, but there is no teachable evidence-type hierarchy and procedure stubs (inquiry/inspection/reperformance/logging) are missing. |
| Software-and-data integration | **2** | Strong [[Missing Data]] / [[Population Completeness]] / [[IT Controls]] / [[Structured Data]] cluster with case bridges. |
| Conclusion-strength linkage | **2** | Explicit qualify/scope-limit and statistical-limitation guidance; no invented thresholds. |
| Source-grounded case application | **2** | Audit Yield (and ARNI/Charities/EFMS) document methodology and data limits with reusable concept links. |
| **Total** | **9 / 10** | |

---

## Unsupported rules

Do **not** invent or claim from the vault:

- A universal % completeness or sample size that always qualifies a conclusion
- That system-generated reports are automatically reliable
- That public redactions can be reconstructed as missing “true” values
- That Audit Yield’s **95%** statement applies beyond the report’s specified sampled segment
- That historical matching gaps describe current CRA systems
- A mandatory ranked “evidence hierarchy” as official CRA policy (vault has no such official rule)

---

## Missing evidence concepts

| Gap | Impact |
|---|---|
| Evidence hierarchy / persuasiveness scale note | Learners must infer inquiry ≪ reperformance |
| Audit Logging | Logs discussed but not a first-class concept |
| Inquiry / Inspection / Reperformance procedure stubs | Methods named, not taught |
| Appropriateness stub (relevance + reliability) | Split across [[Evidence]] and [[Evidence Reliability]]—workable but easy to miss |
| Chain of custody (digital) | Mentioned briefly in [[Evidence]]; not developed |

---

## Missing software or statistics links

- [[Evidence]] related notes omit [[IT Controls]], [[Monitoring and Reporting]], and [[How Missing Data Limits Audit Assurance]] (reachable indirectly).
- No direct wikilink path from [[Evidence]] → Audit Logging (note absent).
- [[Evaluation - Audit Yield]] links evidence/data concepts well; [[Evidence]] itself does not link back to Audit Yield.
- Lineage/change-management dependency is split across [[Evidence Reliability]], [[IT Controls]], and [[Tool Deployment]] without a single “system-generated evidence” primer.

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Add a short Class C note **Evidence Hierarchy** (or expand [[Evidence]]) comparing inquiry → documents → system reports → logs → observation → inspection → reperformance, with corroboration rules.
2. Create thin stubs: **Audit Logging**, **Inquiry**, **Inspection**, **Reperformance**, linking to [[Evidence]] and [[IT Controls]].
3. Add one sentence on [[Evidence]]: more low-quality items from one weak source do not create sufficiency for a high-assurance conclusion.
4. Back-link [[Evidence]] / [[Evidence Reliability]] to [[Evaluation - Audit Yield]] and [[Internal Audit - Accounts Receivable National Inventory]] as worked limitation examples.
5. Add [[IT Controls]] and [[Monitoring and Reporting]] to [[Evidence]] related notes for system-generated evidence dependencies.
6. Keep the “no universal threshold” rule prominent in any future RAG grounding for evidence questions.

---

## Test metadata

- Test ID: Test-04-Evidence-Quality
- Suite: Audit Baseline onboarding diagnostics
- Output path: `16-Testing/Audit/Baseline/Test-04-Evidence-Quality.md`
- Vault notes modified by this test: **none** (output file created only)
- Process followed: searched evidence/data/sampling/procedure terms and public cases; distinguished sufficiency/appropriateness/reliability; used Audit Yield for documented limitations; avoided universal thresholds; did not implement recommendations

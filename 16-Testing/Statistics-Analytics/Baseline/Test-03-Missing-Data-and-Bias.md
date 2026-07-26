---
title: "Test-03: Missing Data and Bias"
note_type: testing
primary_domain: statistics-analytics
domains:
  - statistics
  - data
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
  - statistics-analytics
  - onboarding
  - missing-data
  - bias
---

# Test-03: Missing Data and Bias

## Question

How can missing data, selection bias and survivorship bias distort an audit analysis?

## Answer

Missing data, selection bias, and survivorship bias can each make an analysed set **unrepresentative** of the intended population, so rates, trends, and control conclusions overstate or understate what would be seen with fuller coverage. The vault teaches **missing data** well; it only partially covers **selection** problems (as non-representative / convenience selection); and it has **no dedicated survivorship-bias note**.

| Content class | Role in this answer |
|---|---|
| **General professional** | [[Missing Data]], [[Population Completeness]], [[Data Quality]], [[Sampling Risk]], [[Evidence Reliability]], [[Sample Selection]], pipeline/reject notes |
| **Official public-source** | Report-stated incompleteness, exclusions, matching gaps, file-review limits in linked cases |
| **Vault-derived / Class B** | Bridge [[How Missing Data Limits Audit Assurance]]; case “Cross-domain interpretation” sections; packaging of selection bias and survivorship bias where notes are thin or absent |

**Not all missing data creates bias.** [[Missing Data]] states consequence depends on why data is missing, whether missingness is random or systematic, alternative evidence, and whether remaining data still supports the conclusion. Accidental gaps, structural non-capture, and intentional [[Data Suppression]]/redaction are treated differently. There is **no** universal missing-data percentage that forces a qualification.

Do **not** infer unstated causes from historical public reports. Case facts below are period-bound; derived interpretations are labeled.

---

### Missing data

**Absence of expected records, fields, periods, or evidence ([[Missing Data]])**

| Form | Vault meaning |
|---|---|
| Missing values (fields) | Rows exist but critical fields blank/null/unusable |
| Missing records | Entire in-scope items never appear |
| Systematic exclusions / omitted segments | Groups, regions, channels, products excluded by filter or join |
| Truncated extracts | Cut-off, row limits, incomplete transfers |
| Missing time periods | Gaps relative to [[Audit Objective]] / [[Scope]] |
| Non-response / unavailable evidence | Missing supporting documents, approvals, logs, workpapers |
| Suppressed/redacted | Withheld by design—not automatically a quality error |

**Random versus systematic missingness**

[[Missing Data]] requires asking whether missingness is random or systematic and whether particular groups, periods, regions, systems, or transaction types are underrepresented. Systematic omissions, truncation, or filter errors threaten [[Population Completeness]] and can invalidate extrapolations. The vault does **not** assume all missingness is random.

**Effect on precision and validity**

- Auditors must ask whether the limitation affects only **precision** or undermines **validity** of the conclusion ([[Missing Data]]).
- Cascade (typical, not automatic): missing data → weaker [[Data Quality]] → possible population incompleteness → increased sampling/analytical risk → weaker [[Evidence Reliability]] → narrower or qualified conclusions.
- [[How Statistical Limitations Affect Audit Conclusions]]: match assertion strength to evidence strength; prefer directional language when precision is unsupported.

---

### Selection bias

**Vault status:** **No [[Selection Bias]] note.** Closest anchors:

- [[Sample Selection]]: non-representative **convenience** samples increase risk.
- [[Sampling Risk]]: non-representative selection (convenience or bias toward known problems) increases risk beyond formal statistical formulas; missing data in the frame can make even random-looking samples non-representative.
- [[Population Completeness]] / [[Data Pipeline]] / [[Rejected Records]]: filters and silent drops omit segments from the analysed set.
- Bridge: incomplete populations → samples and models **risk bias**.

**How inclusion methods make the analysed group unrepresentative (teaching packaging)**

Selection bias arises when the **process that creates, filters, or selects** records systematically favours some units over others, so the analysed group does not represent the intended population. This is distinct from ordinary **sampling variability** ([[Sampling Risk]] as chance difference between sample and population under a valid design)—though the vault’s [[Sampling Risk]] note discusses both non-representative selection and classic sampling risk without naming “selection bias.”

**Examples (vault-supported patterns + packaging)**

| Pattern | Vault anchors | Distortion risk |
|---|---|---|
| Filtered extracts | Omitted segments, pipeline filters, rejects | Rates computed only on passed/loaded records |
| Convenience / known-problem picks | [[Sample Selection]], [[Sampling Risk]] | Overstates problem frequency if projected |
| Risk-based selection used as if random | Named in cases as methodology, not as “selection bias” | Population-rate claims unsupported |
| Voluntary / incomplete response | Missing supporting evidence type | Only documented cases appear “complete” |
| Alert-only / override-only views | [[False Negatives]]: low alert volume ≠ good control | Misses silent failures |

---

### Survivorship bias

**Vault status:** **No [[Survivorship Bias]] note.**

**Teaching definition (packaging, not a vault sentence):** examining only completed, active, successful, or retained cases can exclude failures, withdrawals, closures, dormant items, or never-loaded rejects—making controls or outcomes look stronger (or, less often, weaker) than in the full cohort.

**Adjacent vault hints (not a full concept):**

- [[Population Completeness]]: access extracts must include [[Dormant Accounts]] still enabled—not only active/obvious users.
- [[Rejected Records]] / pipeline drops: failed loads absent from reporting populations.
- [[False Negatives]]: silent misses may not appear in override/alert logs—analysing only “surviving” alerts understates miss risk.
- Charities **derived** interpretation: a performance view based only on open/closed files and outcomes may not show comparable treatment across cases ([[Internal Audit - Charities Audit Process]] Cross-domain interpretation)—**not** an official finding titled “survivorship bias.”
- Audit Yield cohorts of **closed** files are an intentional evaluation frame for cash recovery; the report’s snapshot/matching limits are completeness issues—do **not** relabel the official methodology as survivorship bias unless the report says so.

**Why outcomes can look stronger than they are**

If failed, abandoned, unmatched, or never-ingested cases are invisible, success rates, control pass rates, or “clean” operational metrics can be inflated. Direction depends on what was excluded—the vault discusses overstated assurance / weaker conclusions more clearly than a full over-/under-statement taxonomy for bias.

---

## Causal model

Required example path (aligned with [[Missing Data]] cascade + teaching packaging for bias):

```text
Incomplete extract
→ omitted records
→ non-representative analysed population
→ biased rate or trend
→ overstated or understated finding
→ weakened conclusion
```

Vault-native parallel ([[Missing Data]]):

```text
Missing data
→ weaker data quality
→ possible population incompleteness
→ increased sampling or analytical risk
→ weaker evidence reliability
→ narrower or more qualified conclusions
```

Creation / selection / retention link (assembled):

```text
Source capture & retention rules
→ extract filters / rejects / cut-offs ([[Data Pipeline]], [[Rejected Records]], [[Assessment Cut-Off Date]])
→ analysed set ≠ intended population ([[Population Completeness]])
→ selection or survivorship distortion (concept notes thin/absent)
→ [[Sampling Risk]] / invalid extrapolation
→ [[Evidence Reliability]] ↓ → qualify or scope-limit ([[Evidence]], [[How Statistical Limitations Affect Audit Conclusions]])
```

---

## Possible mitigations

Supported in vault concepts (especially [[Missing Data]] procedures):

| Mitigation | Vault anchors |
|---|---|
| Reconciliation | [[Population Completeness]], [[Data Quality]], [[Data Reconciliation]] |
| Comparison with independent totals | Completeness testing vs source counts, hash totals, registers |
| Missingness analysis | Profiling; ask random vs systematic; underrepresented groups/periods |
| Sensitivity analysis | Whether conclusions change when incomplete segments excluded/bounded ([[How Statistical Limitations Affect Audit Conclusions]]) |
| Documentation of exclusions | Methodology/scope; state retrieved-subset limits ([[Population Completeness]]) |
| Alternative evidence | [[Missing Data]] questions; corroboration ([[Evidence]]) |
| Narrower conclusion wording | Scope-limit/qualify; directional language; match assertion to evidence |

Also: source-to-report tracing / extraction-logic review ([[Evidence Reliability]], [[Structured Data]]); cut-off alignment ([[Assessment Cut-Off Date]]).

---

## Distinctions checklist

| Distinction sought | Vault status |
|---|---|
| Missing values | **Yes** — [[Missing Data]] |
| Missing records | **Yes** |
| Systematic exclusions | **Yes** — omitted segments / filter errors / [[Population Completeness]] |
| Non-response or unavailable evidence | **Yes** — missing supporting evidence |
| Surviving / successfully completed cases only | **Weak** — adjacent dormant/reject/FN and derived Charities language; no survivorship note |
| Bias linked to how data created, selected, retained | **Partial** — pipeline/filters/rejects/cut-off strong; “selection bias” / “survivorship” unnamed |
| All missingness = bias? | **No** — random vs systematic; depends on purpose; suppression ≠ quality error |

---

## Notes and cases used

### Search results

| Sought | Result |
|---|---|
| Missing Data | [[Missing Data]] · [[How Missing Data Limits Audit Assurance]] |
| Population Completeness | [[Population Completeness]] |
| Selection Bias | **No dedicated note** |
| Survivorship Bias | **No dedicated note** |
| Data Quality | [[Data Quality]] |
| Sampling Risk | [[Sampling Risk]] |
| Evidence Reliability | [[Evidence Reliability]] · [[Evidence]] |
| False Positives / False Negatives | [[False Positives]] · [[False Negatives]] |
| Relevant public cases | Listed below |

Also used: [[Sample Selection]], [[Data Pipeline]], [[Rejected Records]], [[Data Reconciliation]], [[Assessment Cut-Off Date]], [[Data Suppression]], [[How Statistical Limitations Affect Audit Conclusions]], [[Dormant Accounts]], [[Analytics]].

### Public CRA cases (historical)

| Case | Official public-source facts used | Derived interpretation (labeled in vault) |
|---|---|---|
| [[Evaluation - Audit Yield]] | Matching gaps; snapshot/population limits; closed-file cohorts for yield | Completeness constraints on agency-wide automation confidence—not re-labeled as survivorship in this diagnostic |
| [[Internal Audit - Accounts Receivable National Inventory]] | Incomplete performance measures; attribution; collapsed inventories; resolved-while-unassigned examples | Missing movement/attribution views as [[Missing Data]] / [[Population Completeness]] for the decision |
| [[Internal Audit - Charities Audit Process]] | Limited/incomplete data; limited population-level impartiality reporting; file reviews not a population estimate | Open/closed operational view may miss comparable treatment (derived—not an official “bias” finding) |
| [[Internal Audit - Enterprise Fraud Management System]] | Re-ingestion/timeliness; FP theme; redactions | Transfer completeness; alert-only views and FN risk adjacent to selection of visible outcomes |
| [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] | BI/performance data use | Incomplete/suppressed aggregates limit conclusion strength |

No case is used to claim that official reports diagnosed “selection bias” or “survivorship bias” by those titles unless stated—they did not, in the vault’s Class A summaries.

---

## Diagnostic checks

| Check | Finding |
|---|---|
| Assume all missingness is random? | **No.** Explicit random vs systematic questions. |
| Confuse selection bias with sampling variability? | **Partial risk.** Both live mainly under [[Sampling Risk]] without a named selection-bias concept. |
| Recognise excluded failed or closed cases? | **Weak.** Rejects, dormant accounts, FN silence; no survivorship teaching. |
| Discuss direction of possible distortion? | **Partial.** Precision vs validity; overstated assurance / narrower conclusions; less on when rates bias up vs down. |
| Label derived interpretations? | **Yes** in [[Missing Data]], bridge, and case Cross-domain sections. |

---

## Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Missingness distinction | **2** | Strong typed taxonomy; random vs systematic; precision vs validity; not all gaps = bias. |
| Selection-bias clarity | **1** | Non-representative/convenience/filter themes exist; no dedicated concept or clear split from sampling variability. |
| Survivorship-bias clarity | **0** | No note; only weak adjacent hints. |
| Audit-conclusion connection | **2** | Clear cascade to evidence reliability and qualified/directional conclusions; mitigations listed. |
| Source and case accuracy | **2** | Official vs derived labeled; no invented universal threshold; causes not invented beyond report text. |
| **Total** | **7 / 10** | |

---

## Conflated concepts

1. **Sampling risk vs selection bias** — [[Sampling Risk]] mixes chance sampling error with non-representative selection design.
2. **Missing data vs bias** — bridge says samples/models “risk bias,” but learners may treat every gap as bias; [[Missing Data]] itself is more careful.
3. **Suppression vs accidental missingness** — correctly distinguished in [[Missing Data]]; still easy to conflate in case reading (redactions).
4. **False negatives vs survivorship** — FN “silent misses” adjacent to analysing only visible alerts; not taught as survivorship.
5. **Closed-file evaluation cohorts vs survivorship bias** — Audit Yield closed cohorts are a defined scope, not automatically a bias label.

---

## Unsupported causal statements

Do **not** claim from the vault or this test:

- That all missing data creates bias
- That Charities, ARNI, EFMS, BI, or Audit Yield officially found “selection bias” or “survivorship bias” by those names
- That historical gaps persist today
- A universal % missing that always invalidates analysis
- That false-positive volume alone proves control failure or success
- Causal mechanisms in public reports beyond what the Class A notes state

---

## Missing procedures

| Gap | Impact |
|---|---|
| Dedicated missingness-pattern / bias-diagnosis procedure note | Procedures listed inside [[Missing Data]] but not a bias playbook |
| Selection-bias test design (compare selected vs frame; quantify filters) | Learners assemble from Sample Selection + Population Completeness |
| Survivorship checks (include failures, dormant, rejects, abandoned, unmatched) | Not first-class |
| Directional bias analysis (when exclusion inflates vs deflates a rate) | Only precision vs validity question |
| Explicit “do not project from convenience/selected sets” rule | Thin (see Test-02) |

Mitigations that **are** present: reconciliation, independent totals, profiling, sensitivity analysis, document exclusions, alternative evidence, narrower wording.

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Add Class C notes **Selection Bias** and **Survivorship Bias**, linked from [[Missing Data]], [[Population Completeness]], [[Sampling Risk]], and [[Sample Selection]].
2. In [[Sampling Risk]], separate (a) sampling variability under a valid design from (b) selection bias from how the frame/sample was created or filtered.
3. Add one survivorship sentence to [[Population Completeness]]: analysing only completed/active/successful items can exclude failures, rejects, dormant, or closed-out-of-view cases.
4. Keep [[Missing Data]]’s “not all missingness is equal / no universal threshold” rule prominent for RAG.
5. In case teaching links, continue labeling Class B interpretations; do not retrofit bias titles onto official findings.
6. Optional short procedure stub: missingness analysis + filter quantification + sensitivity bounds before population-rate claims.

---

## Test metadata

- Test ID: Test-03-Missing-Data-and-Bias
- Suite: Statistics-Analytics Baseline onboarding diagnostics
- Output path: `16-Testing/Statistics-Analytics/Baseline/Test-03-Missing-Data-and-Bias.md`
- Vault notes modified by this test: **none** (output file created only)
- Process followed: searched missing-data/completeness/selection/survivorship/quality/sampling/evidence/FP-FN terms and public cases; assessed missingness and bias distinctions; linked bias to creation/selection/retention where supported; did not claim all missingness creates bias; did not invent causes from historical reports; did not implement recommendations

---
title: "Test-02: Sampling Methods"
note_type: testing
primary_domain: statistics-analytics
domains:
  - statistics
  - audit
  - data
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
  - sampling
  - stratified-sampling
---

# Test-02: Sampling Methods

## Question

What is the difference between random sampling, stratified sampling and judgmental sampling, and when might each be appropriate in an audit?

## Answer

Sampling methods differ in **how items are chosen**, **what kind of inference they support**, and **how [[Sampling Risk]] is managed**. The vault names random and stratified selection in [[Sample Selection]] / [[Sampling Risk]], defines [[Stratified Sampling]] thinly, and does **not** define judgmental sampling as a first-class note. Adjacent language covers “convenience” and “bias toward known problems,” which are related but not identical to deliberate risk-based judgmental selection.

| Content class | Role in this answer |
|---|---|
| **General professional (Class C)** | [[Sample Selection]], [[Sampling Risk]], [[Stratified Sampling]], [[Population Completeness]], [[Control Testing]], [[Risk Assessment]], [[Control Frequency]] |
| **Official public-source (Class A)** | Stratified sample design and confidence bound in [[Evaluation - Audit Yield]] |
| **Vault-derived packaging** | Full random / stratified / judgmental comparison table and when-to-use guidance where dedicated notes are missing or thin |

**No universal sample-size rule.** [[Control Frequency]] says test enough instances across the [[Audit Period]] to support the conclusion—not a single convenient instance—without prescribing a formula. Do not invent one from this vault.

Do **not** treat Class C notes as CRA-mandated sampling standards. Case facts are historical and period-bound.

---

### Random sampling

**How units are selected (vault + teaching packaging)**

Vault language: [[Sample Selection]] and [[Sampling Risk]] refer to **random selection** as a design that helps manage sampling risk. There is **no dedicated [[Random Sampling]] note** describing the mechanism.

Teaching packaging consistent with those notes: each unit in a complete sampling frame has a known (typically equal) chance of selection, without auditor preference for particular items.

**Assumptions required**

- A complete, appropriate sampling frame aligned to the intended population ([[Population Completeness]], [[Sampling Risk]]: missing data in the frame can make even formal random selection non-representative).
- Items are selectable from that frame for the [[Audit Period]] / engagement [[Scope]].
- Selection process is free of convenience bias ([[Sample Selection]]: non-representative convenience samples increase risk).

**Conclusions that may be supported**

- Statistical or structured projection to the **frame/population** when design, size, and evaluation support it ([[Sampling Risk]]: reports should state when findings are sample-based and whether results were projected).
- Broader [[Scope]] claims only if the frame matches the intended population (Test-01 / [[Population Completeness]] linkage).

**Limitations**

- Invalid if the population/frame is incomplete ([[Sampling Risk]], [[Population Completeness]]).
- May undersample rare high-risk or high-value items unless combined with stratification or targeted procedures.
- Does not remove [[Data Quality]] limits on the underlying records.
- Sample “size” is mentioned as a design factor ([[Sampling Risk]]) but **no vault formula** defines adequacy.

**When often appropriate:** estimating error rates or control deviation rates across a homogeneous, complete population; reducing selection bias relative to convenience picks.

---

### Stratified sampling

**Why divide into groups ([[Stratified Sampling]])**

[[Stratified Sampling]]: divides the population into **strata** and samples within each to **improve representation** or **focus on high-risk segments**. [[Sample Selection]] adds automated-control examples: stratify by rule version, period slice, and high-risk types. [[Small-Cell Analysis]] warns that sampling within sparse strata raises [[Sampling Risk]].

**Important distinction (diagnostic):** stratification is **not** merely picking high-risk items. It is partitioning the population and sampling **within strata** (often randomly within each). Selecting only high-risk items without a within-stratum design is closer to **judgmental / risk-based selection**. The vault’s “focus on high-risk segments” wording can blur this.

**High-value, high-risk, or unusual transactions**

- Represented by defining strata (e.g., value bands, risk tiers, rule versions) and allocating sample effort so important segments are not left to chance alone.
- May combine **100% testing of a top stratum** with random sampling of remaining strata—see public case below.

**Interpreting results within and across strata**

- Within-stratum results describe that stratum’s frame.
- Cross-stratum / population conclusions require a design that supports combination (weights, coverage of all strata)—vault does not teach weighting mechanics.
- Confidence statements must stay bound to the segment the design covers ([[Evaluation - Audit Yield]]: **95%** confidence for the **sampled segment**).

**Limitations**

- Thin vault definition; no guidance on stratum construction, allocation, or combining estimates.
- Sparse strata → fragile inference ([[Small-Cell Analysis]]).
- Still depends on [[Population Completeness]] of the overall frame and of each stratum list.
- “Focus on high-risk” language risks confusion with judgmental-only testing.

**When often appropriate:** heterogeneous populations (value, risk, product, period, control version) where simple random sampling would leave material segments thin.

---

### Judgmental sampling

**Vault status:** **No [[Judgmental Sampling]] note.** Closest anchors:

- [[Sample Selection]]: non-representative **convenience** samples increase risk.
- [[Sampling Risk]]: non-representative selection (convenience or **bias toward known problems**) increases risk beyond formal statistical formulas; sampling risk also arises in **non-statistical** sampling when auditors extrapolate.
- [[Professional Judgment]]: engagement judgment on scope/evidence—**not** a sampling-method definition.
- [[Risk Assessment]]: prioritizes where limited resources focus—informs targeting but does not define judgmental samples.
- [[Exception Testing]] / [[Analytics]] (adjacent): targeted follow-up on anomalies is a common judgmental use case, but not labelled as judgmental sampling.

**Why auditors deliberately select particular items (teaching packaging)**

To investigate unusual, high-risk, material, or anomalous items identified by risk assessment, analytics, or professional knowledge—maximizing detection value rather than statistical representativeness.

**Value**

- Efficient for material or unusual items.
- Complements statistical samples (e.g., examine all large items, then sample the rest).
- Useful in [[Control Testing]] when specific risk scenarios matter more than population rates.

**Why it normally does not support statistical extrapolation**

Judgmental (and convenience) selection is **not** designed for statistical representativeness. Projecting error rates to the entire population as if the sample were random **overstates** assurance. [[Sampling Risk]] warns that non-representative selection increases risk beyond formal formulas; reports should state whether results were projected. The vault does **not** explicitly say “judgmental samples must not be extrapolated,” which is a teaching gap—this diagnostic treats that as professional packaging, not a vault sentence.

**When often appropriate:** targeted substantive or control tests of high-risk items; investigating outliers or known problem areas; items selected for qualitative insight—not for population-rate estimation.

---

### Statistical representativeness vs targeted risk-based selection

| Idea | Vault support |
|---|---|
| Random / stratified designs manage sampling risk toward representativeness | [[Sample Selection]], [[Sampling Risk]], [[Stratified Sampling]] |
| Convenience / bias toward known problems ≠ representative | [[Sample Selection]], [[Sampling Risk]] |
| Incomplete frame breaks even “random-looking” selection | [[Sampling Risk]], [[Population Completeness]] |
| Judgmental / risk-based selection as a named method | **Missing** |
| Explicit ban on statistical extrapolation from judgmental samples | **Not stated**; must not be implied that judgmental samples support population-wide statistical extrapolation |

---

## Comparison table

Vault-derived teaching table (methods assembled from thin/missing notes + [[Sampling Risk]] / [[Sample Selection]] / [[Stratified Sampling]] / [[Control Testing]]):

| | **Random sampling** | **Stratified sampling** | **Judgmental sampling** |
|---|---|---|---|
| **Selection basis** | Chance within a complete frame (named, not fully defined) | Partition into strata; sample within each ([[Stratified Sampling]]) | Auditor deliberate choice (not a vault note; adjacent: convenience / known-problem bias) |
| **Typical audit purpose** | Population-rate / deviation estimation when homogeneous | Representation across heterogeneous segments; focus effort by stratum | Target unusual, high-risk, or material items |
| **Representativeness** | Designed for frame representativeness if complete | Designed for stratum and (if weighted) population representation | **Not** statistically representative by design |
| **Possible extrapolation** | May support projection when design allows; disclose ([[Sampling Risk]]) | May support within-segment / designed population inference; bind confidence to design (Audit Yield) | **Normally does not** support statistical extrapolation to the entire population |
| **Main risks** | Incomplete frame; rare items missed; over-claiming from size alone | Strata poorly defined; sparse strata ([[Small-Cell Analysis]]); confusion with “only high-risk picks” | Selection bias; invalid population-rate claims if projected |
| **Suitable procedures** | [[Sample Selection]] + [[Control Testing]] / substantive tests on selected items; document projection | Same, plus stratum definition; optional 100% top stratum + sample remainder | Targeted [[Inspection]] / [[Reperformance]] / [[Exception Testing]]; pair with analytics; do not treat as statistical sample |

Related options: [[Full-Population Analysis]] when data allow (reduces sampling risk; still needs completeness/quality).

---

## Public CRA example (one)

### [[Evaluation - Audit Yield]] (historical)

**Official public-source facts used:**

- Income-tax sample approach: **713** debit-reassessment files closed **FY 2016–17**, including **all** files ≥ **$5 million** (**102** files; **64%** of collectible federal taxes) **plus stratified random sample** of **611** others.
- Report states the sample segment was statistically valid to the population at **95% confidence** for the **sampled segment**.
- Separate GST/HST **population analysis** and query coverage are different methods—not treated here as judgmental sampling.

**Teaching use (vault-derived):** illustrates stratified design combining **certainty (high-value) coverage** with **stratified random** selection of the remainder, and keeps the confidence statement **segment-bound**. It does **not** teach judgmental sampling, and the **95%** figure must not be generalized as a vault sample-size rule.

No second public case is required for this diagnostic. Charities’ limited file reviews are noted only as a searched adjacent example of non-population estimation—not used as a sampling-method template.

---

## Notes and cases used

### Search results

| Sought | Result |
|---|---|
| Random Sampling | **No dedicated note**; “random selection” in [[Sample Selection]], [[Sampling Risk]] |
| Stratified Sampling | [[Stratified Sampling]] (thin) |
| Judgmental Sampling | **No dedicated note** |
| Audit Population | **No dedicated note** (see Test-01) |
| Sample Selection | [[Sample Selection]] |
| Sampling Risk | [[Sampling Risk]] |
| Materiality | **No dedicated note**; word appears in [[Scope]], [[Missing Data]] |
| Outlier Analysis | **No dedicated note**; “outliers” in [[Small-Cell Analysis]] |
| Risk Assessment | [[Risk Assessment]] |
| Control Testing | [[Control Testing]] |
| Substantive Testing | **No dedicated note** |
| Relevant public cases | [[Evaluation - Audit Yield]] (primary); Charities file-review counts searched, not used as method definition |

Also used: [[Population Completeness]], [[Control Frequency]], [[Full-Population Analysis]], [[Small-Cell Analysis]], [[Professional Judgment]] (checked—not a sampling method), [[Exception Testing]], [[Analytics]], [[Methodology]].

---

## Diagnostic checks

| Check | Finding |
|---|---|
| Stratification described as merely choosing high-risk items? | **Partial risk.** [[Stratified Sampling]] says “improve representation **or** focus on high-risk segments” without explaining within-stratum sampling vs judgmental picks. |
| Judgmental sampling presented as statistically representative? | **No**—method absent; convenience/bias language says non-representative increases risk. Gap: no explicit “do not extrapolate” sentence. |
| Random sampling assumed valid without a complete population? | **No.** [[Sampling Risk]] explicitly warns incomplete frames break representativeness. |
| Materiality and risk linked appropriately? | **Weak.** [[Scope]] / [[Risk Assessment]] exist; no [[Materiality]] note tying materiality to sample design; high-risk stratification tip only. |
| Sample-size claims supported? | **No unsupported universal formula found.** [[Control Frequency]] / [[Sampling Risk]] mention size qualitatively only. Audit Yield **95%** kept report-bound. |

---

## Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Method distinction | **1** | Stratified has a stub; random is named only; judgmental missing—three-way contrast not teachable from hubs alone. |
| Representativeness and extrapolation accuracy | **1** | Strong on convenience bias and incomplete frames; weak on explicit judgmental ≠ statistical extrapolation; projection language in [[Sampling Risk]] is not limited to statistical designs. |
| Audit-use explanation | **1** | [[Sample Selection]] / [[Control Testing]] place sampling in procedures; little when-to-use guidance per method. |
| Sampling-risk coverage | **1** | [[Sampling Risk]] is the strongest note (statistical/non-statistical, frame completeness, disclosure of projection) but thin links to method notes and materiality. |
| Source and case grounding | **1** | Audit Yield grounds stratified sampling well; no vault-grounded public example for random-only or judgmental methods. |
| **Total** | **5 / 10** | |

---

## Methodological errors

1. **Stratification blur:** [[Stratified Sampling]] can be read as “sample the high-risk items” rather than “divide into strata and sample within each.”
2. **Projection without design caveat:** [[Sampling Risk]] states that when exceptions are found, projection methods estimate population error rates with stated confidence—without restricting that claim to statistical samples.
3. **Convenience ≠ judgmental:** Vault criticizes convenience/known-problem bias but never teaches legitimate judgmental/risk-based selection as a distinct, non-extrapolating method—learners may either avoid targeted testing or misuse it for rates.
4. **Random undefined:** Naming “random selection” without a definition invites assuming any non-haphazard pick is random.

---

## Missing assumptions

| Missing / thin assumption | Why it matters |
|---|---|
| Complete sampling frame before random/stratified selection | Partially covered in [[Sampling Risk]] / [[Population Completeness]]; not in [[Sample Selection]] |
| Within-stratum random (or other probabilistic) selection | Not stated in [[Stratified Sampling]] |
| Stratum weights / how to combine stratum results | Absent |
| Judgmental samples → no statistical population extrapolation | Not explicit |
| Materiality threshold / risk model driving sample design | No [[Materiality]] note; [[Risk Assessment]] not wired to sample methods |
| Sample-size model (risk, frequency, assurance) | Only “enough instances” ([[Control Frequency]]); correctly avoids a fake universal rule |

---

## Weak audit links

1. [[Sample Selection]] → names random/stratified but does not define them or contrast judgmental.
2. [[Stratified Sampling]] → [[Evaluation - Audit Yield]] linked; reverse teaching path is case-led, not method-led.
3. [[Risk Assessment]] → [[Sampling Risk]] linked; no path to sample-method choice.
4. [[Control Testing]] lists [[Sample Selection]] but not stratified/judgmental/random distinctions or substantive testing.
5. No [[Substantive Testing]] note to contrast tests of controls vs substantive sample purposes.
6. No [[Outlier Analysis]] / [[Materiality]] notes to justify judgmental picks of unusual or material items.
7. [[Professional Judgment]] may be confused with judgmental sampling by name alone.

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Add thin Class C notes: **Random Sampling** and **Judgmental Sampling**; expand [[Stratified Sampling]] to state within-stratum selection and that stratification ≠ selecting only high-risk items.
2. Expand [[Sample Selection]] with a three-method comparison (selection basis, representativeness, extrapolation allowed/not).
3. Add one sentence to [[Sampling Risk]]: statistical projection/confidence statements apply to statistical designs; judgmental/convenience samples normally support only item-level or scoped conclusions.
4. Link [[Risk Assessment]] and (if created) **Materiality** to sample design choices; keep **no universal sample-size rule**.
5. Keep [[Evaluation - Audit Yield]] as the worked stratified example; bind **95%** to the report’s sampled segment in any RAG grounding.
6. Optional: short note or section on **Outlier Analysis** as a common input to judgmental selection, distinct from statistical sampling.

---

## Test metadata

- Test ID: Test-02-Sampling-Methods
- Suite: Statistics-Analytics Baseline onboarding diagnostics
- Output path: `16-Testing/Statistics-Analytics/Baseline/Test-02-Sampling-Methods.md`
- Vault notes modified by this test: **none** (output file created only)
- Process followed: searched random/stratified/judgmental/population/sample-selection/sampling-risk/materiality/outlier/risk-assessment/control/substantive terms and public cases; assessed method definitions and representativeness vs targeted selection; avoided implying judgmental statistical extrapolation; avoided inventing sample-size rules; used one supported CRA example (Audit Yield); did not implement recommendations

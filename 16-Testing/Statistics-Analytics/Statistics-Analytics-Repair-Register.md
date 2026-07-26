---
title: "Statistics-Analytics Repair Register"
note_type: testing
primary_domain: statistics-analytics
domains:
  - statistics
  - data
  - audit
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
  - repair-register
  - statistics-analytics
---

# Statistics-Analytics Repair Register

Register of statistics-and-analytics layer repairs driven by `16-Testing/Statistics-Analytics/Baseline/Test-01` through `Test-06`. Official public finding/recommendation/date/MAP text was **not** rewritten. No CRA-specific statistical formulas, universal significance levels, or sample-size rules were invented.

Severity priority applied: invalid statistical claims → unsupported population-wide extrapolation → incomplete populations treated as complete → statistical significance as operational importance → biased selections as objective → full-population as risk-free → reproducibility confused with validity → missing audit/software links → weak onboarding.

| ID | Test | Affected files | Severity | Issue description | Proposed correction | Content class | Source required | Action taken | Validation result |
|---|---|---|---|---|---|---|---|---|---|
| SA-01 | Test-01 | new Audit Population, Intended Population, Retrieved Population, Sampling Frame | high | No first-class population layers; extract confused with universe | Create distinct Class C notes; link objective/scope/period | general-professional | none | Created 4 notes | pass |
| SA-02 | Test-01 | new Inclusion and Exclusion Rules; Missing Records; Missing Values; patch Population Completeness | high | Completeness hub not tied to objective/scope/sample; records vs fields not first-class notes | Create thin notes; expand Population Completeness links and retrieved-subset language | general-professional | none | Created 3; Population Completeness patched | pass |
| SA-03 | Test-01 | new Audit Conclusion; patch Transactional Dataset | medium | Conclusion path untitled; transactional dataset called “audit populations” | Add conclusion stub; qualify dataset ≠ intended population | general-professional | none | Created + patched | pass |
| SA-04 | Test-02 | new Random Sampling, Judgmental Sampling, Representativeness, Statistical Extrapolation, Risk-Based Selection; expand Stratified Sampling, Sample Selection, Sampling Risk | critical | Methods undefined/blurred; projection language too broad | Define three methods; within-stratum stratification; extrapolation only for statistical designs | general-professional | Audit Yield (existing stratified theme) | Created 5; patched 3 | pass |
| SA-05 | Test-02 / Test-05 | new Materiality | high | Materiality absent; triage and sample design unlinked | Create Materiality note; link Risk Assessment, Sample Selection, Finding | general-professional | none | Created | pass |
| SA-06 | Test-03 | new Selection Bias, Survivorship Bias, Systematic Exclusion, Non-Response or Unavailable Evidence, Sensitivity Analysis; patch Missing Data, Sampling Risk | high | Bias unnamed; selection bias conflated with sampling variability | Create bias notes; separate selection bias from sampling variability; not-all-missingness-is-bias | general-professional | none | Created 5; hubs patched | pass |
| SA-07 | Test-04 | new Outlier Analysis, Trend Analysis, Descriptive Statistics | high | Unusual≠error and trend context not first-class procedures | Create notes with investigate-before-conclude and trend context checks | general-professional | none | Created 3 | pass |
| SA-08 | Test-05 | new Statistical Significance, Operational Significance, Confidence Interval, Effect Size, Rare High-Impact Events | critical | Statistical vs operational importance unseparated; large-N silence | Create notes; no universal α; non-significance ≠ no risk; large-N caution | general-professional | none (Audit Yield 95% remains case-bound) | Created 5 | pass |
| SA-09 | Test-05 | patch Evidence Evaluation, Finding, Professional Judgment, Full-Population Analysis, Analytics | high | “Significant” ambiguous; large-N/full-pop without materiality | Clarify report significance; wire judgment/criteria/effect size | general-professional | none | Patched | pass |
| SA-10 | Test-06 | new Reproducibility, Analytical Validity; expand Full-Population Analysis, Analytics, Evidence Reliability | critical | Reproducibility thin; reproducible confused with correct | Checklist note; reproducible ≠ valid; residual risks on full-pop | general-professional | none | Created 2; hubs patched | pass |
| SA-11 | Test-01–06 | new maps + Data and Statistics Onboarding Path; Home; CRA-Data-and-Statistics-Map; Evidence map; Learning Path | medium | Weak navigation across statistics-analytics layer | Create MOCs and onboarding path | derived | none | Created 7 nav notes; hubs updated | pass |
| SA-12 | All | Cross-link hubs: Population Completeness, Missing Data, Sampling Risk, Data Lineage, Exception Testing, How Statistical Limitations, bridge | medium | Missing meaningful cross-domain links | Bidirectional related-notes patches | general-professional / derived | none | Patched | pass |

## Issues deferred (unresolved)

| ID | Severity | Problem | Why deferred |
|---|---|---|---|
| SA-D1 | low | Notes are thin Class C stubs, not CRA sampling manuals | Intentional; avoid inventing non-public CRA detail |
| SA-D2 | medium | Baseline diagnostics not re-run | Per instructions: do not rerun tests during repairs |
| SA-D3 | low | No dedicated Substantive Testing note | Out of core SA repair set; Control Testing remains entry |
| SA-D4 | low | Override-frequency analytics playbook still thin | Residual from Software-Data suite; pointed via Unmonitored Manual Overrides |
| SA-D5 | low | Case notes not expanded with bias titles | Avoid retrofitting “selection/survivorship bias” onto official findings |

## Notes on content classes

- New concept stubs: **general-professional-knowledge** unless navigation/maps (**derived-analysis**).
- Public case text: **not modified** in this repair pass (teaching links already present where needed).
- No synthetic examples placed in Class A case notes.
- No universal completeness %, sample size, or significance level asserted as CRA policy.

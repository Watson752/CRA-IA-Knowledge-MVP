---
title: "Test-05: Public Case Scoping Synthesis (Integrated Baseline)"
note_type: testing
primary_domain: testing
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
  - public-cases
  - data-quality
  - scoping
  - multidisciplinary
---

# Test-05: Public Case Scoping Synthesis (Integrated Baseline)

## Question

Which lessons from published CRA audits and evaluations could help scope a hypothetical data-quality engagement?

**Discipline:** Treat cases as evidence about their **reported periods**. Do **not** claim historical findings remain unresolved. Do **not** treat thematic similarity as branch participation in a future engagement. Separate exact published findings, recommendations, management responses, vault-derived patterns, and synthetic scoping suggestions.

---

## Answer

Public CRA case notes can inform **how to ask scoping questions**—definitions, completeness, lineage, ownership, monitoring, and conclusion limits—not which CRA dataset or system a future engagement must cover. The vault already packages this path in [[Public-Audit-Case-Library]] Demo 3 and [[How Missing Data Limits Audit Assurance]].

---

## Public-case table

| Report title | Report / audit period | Relevant published issue (paraphrased) | Relevant recommendation or response (paraphrased) | Source note | Current-status limitation |
|---|---|---|---|---|---|
| Internal Audit – Oversight, Use, and Continuous Improvement of Business Intelligence | Audit period **1 Apr 2020 – 31 Mar 2023**; report presented **18 Jun 2024** | BI governance exists but needs CRA-wide BI objectives, clearer roles, common BI definition; weak horizontal coordination; inconsistent continuous improvement; outdated BI instances; tool-deployment process gaps | SIIB (with ITB/stakeholders) to strengthen BI governance: objectives/roles/definition; horizontal strategy/monitoring; CI expectations; deployment process. SIIB agreed; MAP dates through mid-2025 | [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] | No vault follow-up confirming remediation; period-bound; not a field-level DQ audit |
| Evaluation – Audit yield | Cohorts closed **FY 2015–16** (GST/HST) and **FY 2016–17** (income tax); analysis as of **Jul 2019**; report **Jan 2020** | Cash recovery measurable but multi-system; fiscal impact ≠ audit yield; income-tax matching gaps / manual linking; automation barriers | SIIB/CPB (with others/ITB) to adopt integrated cash measure and improve automated cross-branch linking. CPB and SIIB agreed (historical targets 2020–2021) | [[Evaluation - Audit Yield]] | Snapshot results; not current performance; not a substitute for unpublished *Tax and Benefits Operations Results Information* IA |
| Internal Audit – Accounts Receivable National Inventory | **1 Apr 2022 – 31 Dec 2024**; report **14 May 2026** | Controls for scoring/allocation existed; monitoring limited; churn undefined during exam; HQ reporting incomplete for movement/production; incomplete performance measures/attribution; business-rule outcome roles undocumented; DSS BI use constrained | CVB to define/monitor churn and reporting; align indicators; document business-rule governance; promote DSS/enterprise solution; document regional inventory roles. CVB agreed (MAP targets into 2030) | [[Internal Audit - Accounts Receivable National Inventory]] | MAP commitments ≠ proven current OE; “resolved” has report-specific meaning |
| Internal Audit – Enterprise Fraud Management System | **1 Apr 2021 – 31 Mar 2024** (pertinent since 2017); report **23 Jan 2026** | EFMS working as intended with improvements: ad hoc rule changes; incomplete central change history; high false-positive rules not always reviewed; record loading not always timely/controlled; dashboard indicators incomplete for management decisions | Security Branch (ITB jointly for re-ingestion) to track rule changes; formalize re-ingestion; improve KPIs/alert-resolution definitions. Security Branch agreed (targets May 2026) | [[Internal Audit - Enterprise Fraud Management System]] | Investigation/discipline out of scope; security redactions; no vault follow-up on MAP completion |
| Internal Audit – Charities Audit Process | **1 Apr 2020 – 31 Mar 2023**; report **Jan 2025** (vault) | Impartiality/consistency improvements needed; limited/incomplete data across sources; limited population-level impartiality reporting; incomplete documented reviews/approvals; operational metrics did not explicitly cover impartiality | LPRAB to formalize roles/procedures/QA; improve information systems/BI strategy/reporting; expand data gathering and monitoring for impartiality. LPRAB agreed (MAP dates into 2026) | [[Internal Audit - Charities Audit Process]] | Redactions/classified material not reconstructed; file samples ≠ population estimate; follow-up unknown |
| Internal Audit – Specific Cyber Security Controls | **1 Dec 2021 – 31 Aug 2022**; report **Mar 2023** | Published report identifies improvement areas but **protects** detailed findings; recommends Security Branch establish second-line cyber defence and update policy instruments | Security Branch agreed; Three Lines language in report (CISD / planned GRC / AERB) | [[Internal Audit - Specific Cyber Security Controls]] | **Low direct DQ relevance**; protected detail must not be invented; not used to scope technical data-quality tests |

---

## Cross-case themes

**Class:** vault-derived cross-case patterns (supported where multiple cases speak to the theme). Not proof that the same branches participate in a future engagement.

| Theme | Supporting cases (bounded) | Lesson for a data-quality engagement |
|---|---|---|
| **Governance** | BI; ARNI (business-rule governance); EFMS (rule-change governance) | Scope who sets standards for critical data/metrics and who may change them |
| **Ownership** | BI (SIIB vs ITB); EFMS (Security vs ITB); ARNI (CVB); Charities (LPRAB) | Separate program/business, technical support, data, and control ownership early ([[Ownership and Assurance Roles]]) |
| **Data definitions** | BI (common BI definition); ARNI (churn/resolved); Audit Yield (fiscal impact vs yield) | Criteria must lock numerators, denominators, exclusions, and labels before testing |
| **Population completeness** | ARNI; Charities; Audit Yield; EFMS (load completeness); bridge note | Test intended vs retrieved populations; include movement, rejects, unmatched, collapsed views where relevant |
| **Data lineage / matching** | Audit Yield (cross-system matching); Charities (manual multi-system work); pipeline concepts | Map source→transform→report; quantify match/reject rates |
| **Reporting** | ARNI; Audit Yield; EFMS dashboards; Management Reporting concepts | Distinguish operational counts from decision-useful, attributable measures |
| **Monitoring** | ARNI; EFMS; Charities (impartiality monitoring gap); Monitoring notes | Scope detective controls over quality breaks, not only preventive entry checks |
| **Quality assurance** | Charities (QA/roles/checkpoints); ARNI (QA tools present vs monitoring gaps) | Design vs operating effectiveness of QA over data/decision documentation |
| **Continuous improvement** | BI (outdated BI; CI expectations) | Include refresh/review cadence for critical datasets and BI products |
| **Horizontal collaboration** | BI; Audit Yield (cross-branch linking) | Multi-source quality rarely owned by one silo—scope handoffs |
| **Duplicated analytical work** | BI (silos / duplicate effort themes via related notes) | Ask whether competing extracts redefine the same measure |
| **Performance measurement** | Audit Yield; ARNI; [[Performance Reporting]] / [[CRA Performance Measurement]] | Incomplete or misaligned indicators can look precise while omitting needed views |

Themes **not** to over-claim from cyber case: inventing protected technical control failures as DQ scoping facts.

---

## Hypothetical engagement scoping

> **Synthetic derived analysis.** The following is a teaching scope for a **hypothetical** data-quality engagement. It is **not** a CRA audit plan, does **not** assert that CRA will (or should) run this engagement, and does **not** claim any historical finding remains open.

### Possible objective

Provide assurance that selected management information used for program decision-making is fit for its stated use—covering definitions, completeness, accuracy relative to source meaning, timeliness/cut-off, lineage across systems, and monitoring of quality exceptions—for a defined period and population.

### Scope boundaries

| In scope (illustrative) | Out of scope (illustrative) |
|---|---|
| Named critical metrics / datasets and their source-to-report path | Entire enterprise data lake or all CRA BI products |
| Pipeline stages affecting those metrics (extract, transform, reject, recon, report) | Unrelated cybersecurity controls (unless they affect feed integrity) |
| Ownership, definitions, change control, monitoring for the selected measures | Investigation/discipline processes (EFMS-style boundary lesson) |
| Sample or full-population tests on the selected reporting population | Extrapolation to all CRA programs |

### Criteria categories

1. **Governance / ownership** — clear accountable owners for business meaning, data, technical pipeline, and controls ([[Data Governance]], [[Roles and Responsibilities]], [[Ownership and Assurance Roles]]).
2. **Definitions** — approved metric/data dictionaries; inclusion/exclusion rules; cut-off ([[Assessment Cut-Off Date]]).
3. **Completeness & accuracy** — distinct dimensions ([[Population Completeness]], [[Data Accuracy]], [[Missing Data]], [[Record Uniqueness]], [[Data Timeliness]]).
4. **Lineage & change** — documented lineage; authorized changes to transforms/report logic ([[Data Lineage]], [[Data Pipeline]], [[Change Management]]).
5. **Monitoring & reporting** — reconciliations, reject handling, management review of quality breaks ([[Data Reconciliation]], [[Rejected Records]], [[Management Reporting]], [[Monitoring and Alerting]]).
6. **Evidence reliability** — system-generated outputs not inherently reliable ([[System-Generated Evidence]], [[Evidence Reliability]], [[Reproducibility]] vs [[Analytical Validity]]).

### Organizations or roles to understand

- Program / business owner of the decision the data supports  
- [[Data Owner]] / stewards; enterprise data leadership signals (e.g., SIIB/CDO mandate where relevant—not assumed owner of every dataset)  
- [[Technical Support]] / ITB for pipeline and platforms  
- [[Control Ownership]] for reconciliations, access, change, monitoring  
- Security function only if feed integrity/monitoring is in scope  
- AERB as independent assurer—not operator of the data controls  

*Do not* assign case branches (SIIB, CVB, LPRAB, Security Branch) to the hypothetical engagement solely because they appeared in thematically similar historical reports.

### Systems and data flows to map

```text
Source systems → API/batch extract → transformation / field mapping
→ rejected records → reconciliation → reporting dataset
→ calculations → management report / BI product → management review
```

([[Data Pipeline and Reporting Map]]; Audit Yield teaches multi-system matching as a completeness/automation risk pattern.)

### Risks

Incomplete extracts; silent rejects; duplicate keys; stale/cut-off errors; wrong mappings/reference data; unauthorized transform/report changes; inconsistent definitions; weak review; overstated reliance on dashboards.

### Controls

Preventive: validations, approved dictionaries, access/change control, certified metrics.  
Detective: stage reconciliations, reject aging, profiling, exception/management review, freshness monitors.

### Evidence

Lineage docs; data dictionaries; change tickets; recon packages; reject logs; access/config extracts; management review records; reproducible analytics workpapers; source-to-report traces.

### Statistical methods

Population completeness tests; full-population profiling where feasible; stratified sampling of high-risk metrics/fields; judgmental selection for anomalies without population extrapolation; sensitivity to missingness; explicit statement of sampling risk and conclusion strength ([[How Statistical Limitations Affect Audit Conclusions]]).

### Exclusions

Protected/classified detail; taxpayer-level content; systems outside the named metric chain; post-alert investigation processes if monitoring-only; unpublished internal follow-up results.

### Limitations

Public cases supply **patterns**, not the engagement’s actual systems inventory, match rates, or current control OE. MAP dates in historical reports are not evidence of present remediation.

---

## Knowledge gaps

Scoping decisions that **cannot** be answered from public vault information alone:

| Gap | Why unavailable |
|---|---|
| Which specific dataset/metric CRA would prioritize next | No public engagement mandate for this hypothetical |
| Current OE of historical MAP actions | Vault states follow-up status unknown |
| Exact field-level quality rules and reject codes | Not published; EFMS/cyber protect technical detail |
| Complete system inventory and interfaces for a chosen program | Only partial public system names (e.g., Audit Yield AIMS/INTEGRAS) |
| Numeric completeness thresholds for qualification | Vault explicitly has no universal threshold ([[Missing Data]], bridge note) |
| Whether *Internal Audit – Tax and Benefits Operations Results Information* was finalized | Not located on Canada.ca during vault research (2026-07-23) |
| Branch participation in a future DQ engagement | Thematic similarity ≠ assignment |

---

## Notes and sources used

### Cases (all MVP public cases searched)

- [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]]
- [[Evaluation - Audit Yield]]
- [[Internal Audit - Accounts Receivable National Inventory]]
- [[Internal Audit - Enterprise Fraud Management System]]
- [[Internal Audit - Charities Audit Process]]
- [[Internal Audit - Specific Cyber Security Controls]] (limited DQ relevance)

### Navigation / bridges

- [[Public-Audit-Case-Library]] · [[Public-Audit-Case-Map]]
- [[How Missing Data Limits Audit Assurance]]
- [[How Statistical Limitations Affect Audit Conclusions]]
- [[Data Pipeline and Reporting Map]] · [[Data Quality and Bias Map]]
- [[Interpreting Historical Public Audit Findings]] · [[Follow-up]]

### Concept notes

- [[Data Quality]] · [[Population Completeness]] · [[Missing Data]] · [[Data Governance]]
- [[Business Intelligence]] · [[Business Intelligence Governance]] · [[Management Reporting]]
- [[Evidence Reliability]] · [[Data Pipeline]] · [[Data Reconciliation]] · [[Data Lineage]]
- [[Performance Reporting]] · [[CRA Performance Measurement]]
- [[Roles and Responsibilities]] · [[Monitoring and Alerting]] · [[Monitoring and Reporting]]
- [[Continuous Improvement]] · [[Horizontal Collaboration]] · [[Duplicate Analytical Work]]
- [[Reproducibility]] · [[Analytical Validity]] · [[Ownership and Assurance Roles]]

---

## Diagnostic evaluation

### Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Cross-case retrieval | **2** | All six public cases indexed; Demo 3 and Missing Data bridge explicitly route learners across reporting/DQ-relevant cases. |
| Historical and source discipline | **2** | Period banners, MAP≠current OE, redaction limits, and “do not assume unresolved” rules are consistent across case notes. |
| Cross-domain synthesis | **2** | Bridge + library themes connect organization, audit evidence, software pipelines, data quality dimensions, and statistics/conclusion strength. |
| Useful synthetic scoping | **2** | Vault supplies enough patterns and concept scaffolding to draft a multidisciplinary hypothetical scope without inventing CRA systems. |
| Uncertainty and gap handling | **2** | Follow-up unknown, protected content, missing results-information IA, and no universal completeness threshold are explicit. |
| **Total** | **10 / 10** | |

### Checks

| Check | Finding |
|---|---|
| Public findings paraphrased accurately? | **Yes**, when using case “What the published report states” sections (not protected cyber detail). |
| Historical findings treated as current? | **No**, if period/follow-up rules are followed. |
| Synthetic recommendations labelled? | **Yes** in this diagnostic’s scoping section. |
| Scope cover org, audit, software, data, statistics? | **Yes** in the synthetic scope. |
| Unavailable information identified? | **Yes** — knowledge-gaps table. |

---

## Unsupported cross-case conclusions

Do **not** conclude that:

- Historical findings remain open or that MAP target dates prove current remediation
- Thematic similarity means SIIB, CVB, LPRAB, Security Branch, or ITB will participate in a future data-quality engagement
- All six cases are “data-quality audits” (cyber is governance/security with protected findings; BI is primarily governance/CI)
- Audit Yield recovery percentages are current CRA performance
- Charities file-review counts are population estimates of impartiality
- EFMS false-positive or loading themes disclose current CRA enterprise DQ posture
- Public cases authorize a specific CRA engagement objective or system list

---

## Missing source links

| Gap | Detail |
|---|---|
| [[Data Quality]] `related_cases` | Empty in frontmatter despite strong case adjacency via bridge/library |
| [[CRA Performance Measurement]] ↔ case notes | Enterprise performance note lightly linked to IA/evaluation DQ themes |
| Dedicated “data-quality engagement scoping” primer | Patterns exist across Demo 3 + bridge + pipeline map; no single MOC titled for DQ engagement design |
| Final published *Tax and Benefits Operations Results Information* IA | Not located; Journey 3 uses Audit Yield as substitute demonstration case |

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Populate [[Data Quality]] `related_cases` with Audit Yield, ARNI, Charities, EFMS, and BI (labeled for which DQ facet each supports).
2. Add a thin navigation note or extend [[Data Quality and Bias Map]] with “scoping a data-quality engagement” pointing to Demo 3, the bridge note, and [[Data Pipeline and Reporting Map]].
3. Keep cyber case labeled **low direct DQ relevance** in any DQ synthesis index.
4. Maintain strict class labels in any future synthesis: published finding / recommendation / MAP / derived pattern / synthetic scope.
5. Optional: one-paragraph cross-link from [[CRA Performance Measurement]] to [[Performance Reporting]] and Audit Yield/ARNI definition lessons.

---

## Test metadata

- Test ID: Test-05-Public-Case-Scoping-Synthesis
- Suite: Integrated Baseline multidisciplinary diagnostics
- Output path: `16-Testing/Integrated/Baseline/Test-05-Public-Case-Scoping-Synthesis.md`
- Vault substantive notes modified by this test: **none** (output file created only)
- Process followed: searched all public case/evaluation notes and related DQ/governance/pipeline/evidence concepts; retrieved multiple cases; distinguished findings/recommendations/responses/derived patterns/synthetic scope; treated cases as period-bound; did not claim unresolved status or invent branch participation; did not implement recommendations

---
title: "Test-06: Grounded Audit Inquiry (Integrated Baseline)"
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
  - ai-assistant
  - retrieval
  - inquiry
  - multidisciplinary
---

# Test-06: Grounded Audit Inquiry (Integrated Baseline)

## Question

Based only on the vault, what lines of inquiry should an auditor consider when a technology-enabled business process shows inconsistent results, incomplete monitoring and unclear ownership?

**Corpus use:** prospective retrieval/reasoning for an approved enterprise AI assistant.  
**Answer class:** proposed lines of inquiry requiring validation—not findings, not proof of non-compliance, fraud, or control failure, and not a statement of current CRA conditions.

| Class in this answer | Meaning |
|---|---|
| **Risk indicators** | Observed symptoms that *may* warrant inquiry (inconsistent results; incomplete monitoring; unclear ownership) |
| **Possible hypotheses** | Competing explanations to test—not conclusions |
| **Audit procedures** | Ways to obtain or corroborate evidence |
| **Evidence** | Information that would support or refute a hypothesis against [[Criteria]] |
| **Unsupported speculation** | Claims the vault cannot justify (e.g., current CRA failure, fraud, invented system detail) |

---

## Answer

### Governance and accountability

**Why retrieved:** symptom triad includes unclear ownership → [[Unclear Accountability]], [[Ownership and Assurance Roles]], owner taxonomy, [[Three Lines Model]].

| Line of inquiry | Hypothesis class | What would count as evidence |
|---|---|---|
| Who is the [[Business Process Owner]] / [[Program Owner]] for outcomes? | Role gap vs documented OPI | Charters, RACI, interview corroboration |
| Who is the [[System Owner]] vs [[Technical Support]] (e.g., ITB delivery)? | Collapsed “IT owns the process” | Maintenance/MAP naming; service agreements |
| Who is the [[Data Owner]] for critical fields/metrics? | Enterprise CDO ≠ every dataset | Stewardship lists; definition approvals |
| Who is the [[Control Ownership\|control owner]] for monitoring, recon, access, change? | Controls without owners | Control registers; review schedules |
| Who escalates exceptions and who must clear them? | Hand-off vacuum | Escalation procedures; aging queues |
| Who owns incomplete monitoring remediation? | Detective control orphan | Monitoring RACI; alert triage ownership |
| Is AERB/assurance being treated as the operator? | Independence confusion | Confirm management owns MAPs ([[Internal Audit Independence]]) |

**Do not conclude** ownership failure from ambiguity alone—validate who is actually accountable.

---

### Business process and criteria

**Why retrieved:** inconsistent results need expected-state [[Criteria]] before they can become findings ([[Finding]] structure: evidence → criteria).

| Line of inquiry | Hypothesis class | Evidence / procedure hooks |
|---|---|---|
| What outcomes is the process designed to produce? | Unclear expected state | Process docs; [[Audit Objective]] alignment |
| What [[Automated Business Rules]] / eligibility / allocation rules apply? | Rule vs practice divergence | Approved rule specs; [[Automated Eligibility Validation]] |
| Which policy/criteria define “consistent” treatment? | Undefined consistency | Policy instruments; [[Inclusion and Exclusion Rules]] |
| What exceptions/overrides are allowed and why? | Legitimate exception vs drift | [[Manual Overrides]]; exception policy |
| What service, compliance, or financial consequences attach to wrong outcomes? | Impact unknown | Impact assessments; [[Consequence or Impact]] (when later supported) |

**Hypothesis examples (not findings):** inconsistent results may reflect definition change, incomplete population, false positives, local workarounds, or measurement error—each must be tested.

---

### Software and change management

**Why retrieved:** technology-enabled process → [[Automated Controls Map]], [[Change Management Map]], [[Logging and Monitoring Map]], [[Identity and Access Map]].

| Line of inquiry | Hypothesis class | Evidence / procedure hooks |
|---|---|---|
| Is production [[System Configuration]] aligned to approved design? | Config drift | [[Configuration Review]] |
| Are rules implemented as approved? | Incorrect automation | Spec vs config; [[Incorrect Automated Decisions]] |
| What mid-period system/rule changes occurred? | Unauthorized or untracked change | [[Change Management]]; [[Unauthorized System Changes]] |
| Were changes approved and deployed under control? | Implementer ≠ approver | [[Change Approval]]; [[Deployment Approval]] |
| Are [[Application Logging]] / [[Audit Logging]] complete for the assertion? | Incomplete trails | Log completeness tests; [[Incomplete Audit Logging]] |
| Is [[Monitoring and Alerting]] designed and operated for this process? | Monitoring gaps | Alert coverage; triage evidence |
| Who has privileged/override access? | Excessive or unmonitored access | [[Privileged Access]]; [[Periodic Access Review]] |
| Are [[Manual Overrides]] approved, logged, and reviewed? | Unmonitored bypass | [[Manual Override Approval]]; [[Exception Report Review]] |

---

### Data and statistics

**Why retrieved:** inconsistent results often data/definition artifacts → [[Data Quality and Bias Map]], [[Population and Sampling Map]], [[Statistics and Evidence Map]].

| Line of inquiry | Hypothesis class | Evidence / procedure hooks |
|---|---|---|
| Is the [[Retrieved Population]] complete vs [[Intended Population]]? | Incomplete frame | [[Population Completeness]]; [[Data Reconciliation]] |
| What [[Missing Data]] (records, fields, periods, rejects) exists? | Silent drops | [[Rejected Records]]; [[Missing Records]] |
| Did definitions/denominators change across the period? | Apparent inconsistency from redefinition | Dictionaries; [[Performance Reporting]] |
| Are “inconsistent results” outliers, strata differences, or trends? | Heterogeneity misread as failure | [[Outlier Analysis]]; [[Trend Analysis]]; [[Operational Significance]] |
| Could [[Selection Bias]] / [[Survivorship Bias]] distort views? | Biased monitoring lens | Frame construction review |
| Are [[False Positives]] / [[False Negatives]] affecting outcomes or override rates? | Rule-quality hypothesis | Outcome analysis; EFMS FP theme as *analogy only* |
| Can analytics be reproduced with same inputs/method? | Irreproducible KPI | [[Reproducibility]] (≠ [[Analytical Validity]]) |

---

### Controls and evidence

**Why retrieved:** incomplete monitoring is a control/evidence problem → [[Risk and Control Map]], [[Evidence and Conclusion Map]], design vs OE.

| Line of inquiry | Hypothesis class | Evidence / procedure hooks |
|---|---|---|
| Which preventive controls should stop bad inputs/access/changes? | Design gap | [[Design Effectiveness]]; walkthrough |
| Which detective controls should detect inconsistencies? | Monitoring design gap | Exception reports; reconciliations |
| Did designed controls operate over the period? | OE gap | [[Operating Effectiveness]]; [[Control Frequency]] |
| Is available evidence sufficient and appropriate? | Evidence gap | [[Evidence]]; [[Evidence Evaluation]] |
| Are system-generated reports/logs reliable enough? | SGE over-reliance | [[System-Generated Evidence]]; [[Evidence Reliability]] |
| What corroboration is needed beyond inquiry? | Inquiry-only risk | [[Inquiry]] alone ≠ OE; [[Inspection]]; [[Reperformance]] |

**Finding discipline:** a [[Finding]] requires condition compared to [[Criteria]] with supported evidence. Symptoms alone are **risk indicators**, not findings ([[Professional Judgment]], [[Materiality]], [[Operational Significance]]).

---

### Relevant public precedents

Use only as **conceptual precedent**. Historical; period-bound; not current findings ([[Interpreting Historical Public Audit Findings]]).

| Case | What the source supports | What is only an analogy | Why relevant to inquiry | Why it does **not** establish a current finding |
|---|---|---|---|---|
| [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] | Official: roles/definition/horizontal BI governance improvement themes; SIIB vs ITB split | That unclear ownership always exists in tech processes | Ownership + definition inquiry prompts | Period 2020–23; MAP≠current OE; not this process |
| [[Internal Audit - Accounts Receivable National Inventory]] | Official: incomplete/attribution-sensitive reporting; business-rule outcome governance undocumented (period) | That any inconsistent KPI equals ARNI churn issues | Definitions, completeness, monitoring inquiry | Period-bound; different program; follow-up unknown |
| [[Evaluation - Audit Yield]] | Official: multi-system matching limits; definition of yield vs fiscal impact | That this process has the same match rates | Lineage/matching/definition inquiry | 2019 snapshot; evaluation not current DQ OE |
| [[Internal Audit - Enterprise Fraud Management System]] | Official: rule-change governance; loading timeliness; FP alerts; dashboard limits | That this process has EFMS-like overrides or fraud | Monitoring completeness + rule quality inquiry | Scope excludes investigation; redactions; not this system |
| [[Internal Audit - Charities Audit Process]] | Official: limited/incomplete dispersed data; population-level monitoring gaps for impartiality (period) | That inconsistency here is impartiality failure | Population monitoring + documentation inquiry | Different process; redactions; not current state |
| [[Internal Audit - Specific Cyber Security Controls]] | Official: Three Lines / Security Branch governance themes; protected findings | Any technical control weakness | Escalation/second-line monitoring *questions only* | Protected detail; not a DQ/process OE precedent |

---

### Notes retrieved

See “Notes used by domain” below. Highest-value navigation hubs:

- [[Ownership and Assurance Roles]] · [[Unclear Accountability]]
- [[Automated Controls Map]] · [[Change Management Map]] · [[Logging and Monitoring Map]]
- [[Data Pipeline and Reporting Map]] · [[Data Quality and Bias Map]]
- [[Risk and Control Map]] · [[Evidence and Conclusion Map]]
- [[How Missing Data Limits Audit Assurance]] · [[Public-Audit-Case-Library]]

### Public sources used

- Six MVP case notes in [[Public-Audit-Case-Library]] (as precedents only)
- Org baseline via ownership/branch notes where mandates clarify role questions ([[99-Sources/source-notes/SRC-CRA-Org-2025]] context)

### Unsupported questions that require internal evidence

These **cannot** be answered from the vault alone:

- Whether this specific process currently has control failures, non-compliance, or fraud  
- Actual owners, configs, logs, match rates, override volumes for a non-public system  
- Current remediation status of any historical MAP  
- Materiality of observed inconsistencies without engagement criteria and evidence  
- Cause of inconsistency without corroborated analysis  

### Possible next audit procedures

Proposed validation steps (not a finding workflow):

1. [[Walkthrough]] end-to-end: owners → rules → pipeline → monitoring → report  
2. Confirm [[Criteria]] and definitions for “consistent results”  
3. Reconcile [[User Access Dataset]] / privileged and override populations if relevant  
4. Source-to-report [[Data Lineage]] trace for the inconsistent metrics  
5. [[Population Completeness]] and reject/missingness tests  
6. Inspect change history and monitoring evidence for the [[Audit Period]]  
7. Sample or [[Full-Population Analysis]] of exceptions/overrides/outcomes  
8. [[Reperformance]] of critical calculations  
9. Corroborate inquiry with tickets, logs, recon packages ([[Evidence Reliability]])  
10. Only then evaluate whether condition vs criteria supports an observation/finding ([[Finding]], [[Professional Judgment]])

### Confidence and limitations

| Item | Assessment |
|---|---|
| Confidence that vault supports **inquiry framing** | **High** — ownership, monitoring, pipeline, evidence, and case-precedent notes are dense |
| Confidence about **any real process condition** | **None from vault alone** — symptoms are hypothetical/engagement-specific |
| Limitation | No single composite note titled for this symptom triad; assistant must traverse multiple maps |
| Limitation | Case language can be misread as current if historical-interpretation rules are ignored |
| Limitation | AI must keep hypotheses ≠ findings; vault helps but does not enforce runtime guardrails |

---

## Retrieval trace

| Step | Search focus | Selected because |
|---|---|---|
| 1 | Unclear ownership | Matches third symptom → Unclear Accountability / Ownership primer |
| 2 | Incomplete monitoring | Logging/Monitoring map; Monitoring and Alerting; Exception Report Review |
| 3 | Inconsistent results | Data quality, definitions, FP/FN, outliers, performance reporting |
| 4 | Technology-enabled process | Automated controls, change management, pipeline, access |
| 5 | Audit methodology discipline | Criteria, Finding, OE, Evidence, Professional Judgment, Historical findings |
| 6 | Public cases | Conceptual precedent for ownership, definitions, completeness, monitoring—not proof |
| 7 | Escalation / independence | Three Lines; Internal Audit Independence; MAP Owner |

**Not selected as proof:** any case finding as current CRA condition; cyber protected details; synthetic demos as CRA fact.

---

## Notes used by domain

### Organization / governance

[[Ownership and Assurance Roles]] · [[Unclear Accountability]] · [[Business Process Owner]] · [[Program Owner]] · [[System Owner]] · [[Technical Support]] · [[Data Owner]] · [[Control Ownership]] · [[Three Lines Model]] · [[Internal Audit Independence]] · [[Management Action Plan Owner]]

### Audit methodology / evidence / procedures

[[Audit Objective]] · [[Scope]] · [[Criteria]] · [[Risk Assessment]] · [[Professional Judgment]] · [[Finding]] · [[Evidence]] · [[Evidence Evaluation]] · [[Evidence Reliability]] · [[System-Generated Evidence]] · [[Design Effectiveness]] · [[Operating Effectiveness]] · [[Control Testing]] · [[Walkthrough]] · [[Inquiry]] · [[Inspection]] · [[Configuration Review]] · [[Reperformance]] · [[Exception Testing]] · [[Interpreting Historical Public Audit Findings]] · [[Materiality]] · [[Operational Significance]]

### Software / controls

[[Automated Business Rules]] · [[Automated Control]] · [[Manual Overrides]] · [[System Configuration]] · [[Change Management]] · [[Unauthorized System Changes]] · [[Application Logging]] · [[Audit Logging]] · [[Monitoring and Alerting]] · [[Exception Report Review]] · [[Privileged Access]] · [[Data Pipeline]] · [[Data Lineage]] · [[Data Reconciliation]] · [[Rejected Records]]

### Data / statistics

[[Data Quality]] · [[Population Completeness]] · [[Missing Data]] · [[False Positives]] · [[False Negatives]] · [[Outlier Analysis]] · [[Selection Bias]] · [[Reproducibility]] · [[Analytical Validity]] · [[Performance Reporting]] · [[How Missing Data Limits Audit Assurance]] · [[How Statistical Limitations Affect Audit Conclusions]]

### Navigation hubs

[[Risk and Control Map]] · [[Evidence and Conclusion Map]] · [[Automated Controls Map]] · [[Change Management Map]] · [[Logging and Monitoring Map]] · [[Identity and Access Map]] · [[Data Pipeline and Reporting Map]] · [[Data Quality and Bias Map]] · [[Public-Audit-Case-Library]]

---

## Public precedents

See table in Answer → Relevant public precedents. Primary conceptual precedents: BI (ownership/definitions), ARNI (definitions/completeness/monitoring), Audit Yield (lineage/matching), EFMS (monitoring completeness/rule quality), Charities (population monitoring/documentation). Cyber: governance/lines analogy only.

---

## Diagnostic evaluation

### Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Retrieval breadth and relevance | **2** | Ownership, monitoring, automation/change, data/stats, evidence, and cases are all retrievable via dedicated notes and maps. |
| Cross-domain reasoning | **2** | Symptom triad maps cleanly onto governance + process/criteria + software + data/stats + controls/evidence. |
| Finding-versus-inquiry discipline | **2** | Finding requires evidence vs criteria; historical-interpretation and professional-judgment notes discourage premature conclusions—if followed. |
| Source and historical discipline | **2** | Case notes and Interpreting Historical Public Audit Findings separate period facts from current claims. |
| Practical audit usefulness | **2** | Yields a usable inquiry checklist and next procedures without inventing findings. |
| **Total** | **10 / 10** | |

### Checks

| Check | Finding |
|---|---|
| Prematurely establish findings? | **No** in this diagnostic; vault structure supports inquiry-first if AI respects Finding/Criteria rules. |
| Only superficially similar notes? | **No** — ownership, monitoring, pipeline, OE, and case precedents are on-point. |
| Cover all major domains? | **Yes**. |
| Clearly state evidence gaps? | **Yes** — unsupported questions / internal evidence list. |
| Distinguish precedent from proof? | **Yes** — precedent table columns. |

---

## Unsupported conclusions

Do **not** conclude from the vault that:

- Non-compliance, fraud, or control failure exists in the described process  
- Inconsistent results prove bad rules, bad data, or bad people without tests  
- Incomplete monitoring equals absence of all detective controls  
- Unclear ownership equals no owners in practice  
- Any public CRA case proves the current condition of this process  
- Inquiry answers are findings  

---

## Missing domains

| Gap | Detail |
|---|---|
| Composite “symptom triad” scenario note | No single note titled for inconsistent results + incomplete monitoring + unclear ownership |
| Dedicated escalation RACI note | Escalation assembled from monitoring/exception/ownership notes |
| Service-level consequence catalogue | Business impact largely general/derived |
| Runtime AI guardrail note | Discipline lives in many notes; no single “assistant must not declare findings from symptoms” policy note for RAG |

*Not missing:* domain coverage across org, audit, software, data, stats, risk, control, evidence, cases.

---

## Retrieval failures

| Failure mode for an AI assistant | Vault mitigation | Residual risk |
|---|---|---|
| Retrieve only “inconsistent” keyword hits | Prefer maps (Ownership, Monitoring, Pipeline, Evidence) | Keyword-only RAG may miss maps |
| Elevate case findings to current state | Interpreting Historical Public Audit Findings | Banner ignored → hallucination of currency |
| Treat Unclear Accountability as a finding | Note is a risk/failure-mode concept | Wording may be over-read |
| Skip criteria before discussing findings | Finding note requires criteria | Procedure shortcuts |
| Collate Test-01–05 themes without citation | Integrated baselines exist under `16-Testing/Integrated/Baseline/` | Assistant may not be allowed to use testing folder as corpus |

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Add a thin derived note or map node: **“Technology-enabled process — inquiry when results, monitoring, and ownership are weak”**, linking Ownership → Monitoring → Pipeline → Evidence → Historical Findings, explicitly labeled inquiry-only.
2. Add an AI/RAG usage note: symptoms = risk indicators; findings require evidence vs criteria; historical cases = precedent not proof.
3. Ensure retrieval configs boost MOC maps (`00-Start/*Map*`) and [[Interpreting Historical Public Audit Findings]] for engagement questions.
4. Optionally exclude or down-rank `16-Testing/**` from production RAG so diagnostics are not mistaken for doctrine—or clearly tag them `note_type: testing`.
5. Keep precedent tables in assistant answers with the four columns used here (supports / analogy / relevance / not a current finding).

---

## Test metadata

- Test ID: Test-06-Grounded-Audit-Inquiry
- Suite: Integrated Baseline multidisciplinary diagnostics (AI corpus readiness)
- Output path: `16-Testing/Integrated/Baseline/Test-06-Grounded-Audit-Inquiry.md`
- Vault substantive notes modified by this test: **none** (output file created only)
- Process followed: searched org, cases, audit methodology, software, data, statistics, risk, control, procedure, and evidence domains; retrieved relevant notes with rationale; separated indicators/hypotheses/procedures/evidence/speculation; did not declare findings or current CRA conditions; did not implement recommendations

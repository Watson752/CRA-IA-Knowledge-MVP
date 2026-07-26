---
title: Missing Data
aliases:
  - Incomplete Data
  - Data Gaps
note_type: data-concept
primary_domain: software-data
domains:
  - data
  - statistics
  - audit
  - risk
domain: data-statistics
status: active
classification: public
content_origin: general-professional-knowledge
authoritative: false
official_source: null
publisher: null
publication_date: null
as_of_date: 2026-07-25
last_verified: 2026-07-25
source_url: null
source_status: unknown
owner: MVP-Author
review_status: analytical-draft
approved_for_ai_retrieval: false
related_sources: []
related_cases:
  - "[[Internal Audit - Charities Audit Process]]"
  - "[[Internal Audit - Accounts Receivable National Inventory]]"
  - "[[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]]"
  - "[[Internal Audit - Enterprise Fraud Management System]]"
  - "[[Evaluation - Audit Yield]]"
related_processes: []
related_organizations: []
related_systems: []
related_datasets: []
related_risks:
  - "[[Sampling Risk]]"
related_controls: []
related_procedures: []
related_methods:
  - "[[Analytics]]"
  - "[[Population Completeness]]"
tags:
  - data-quality
  - evidence
  - completeness
---

**Missing data** is information expected for an analysis, population, record, period, or [[Evidence]] set that is unavailable or absent. Absence may be accidental (extract error, late load, lost field), structural (system never captured the attribute), or intentional and disclosed ([[Data Suppression]], redaction, confidentiality). Auditors treat these causes differently: intentional withholding for privacy is not the same as a quality failure, even when both constrain what can be concluded.

## Types

Distinguish forms of absence before assessing impact:

| Type | Meaning |
|------|---------|
| Missing records | Entire in-scope items never appear in the extract or register |
| Missing values within records | Rows exist but critical fields are blank, null, or unusable |
| Omitted population segments | Groups, regions, channels, or product lines excluded by filter or join logic |
| Truncated extracts | Cut-off, row limits, or incomplete transfers leave part of the period or inventory out |
| Missing time periods | Gaps in the time series relative to the [[Audit Objective]] and [[Scope]] |
| Missing supporting evidence | Source documents, approvals, logs, or workpapers needed to corroborate data |
| Suppressed or redacted public information | Values withheld under disclosure control or ATIP-style redaction—not equivalent to accidental missingness |

[[Data Suppression]] and published redactions constrain analysis by design; they are not automatically [[Data Quality]] errors. Accidental or uncontrolled missingness is a quality and completeness concern. Both can still force narrower conclusions.

## Audit significance

Typical relationship (not an automatic rule):

```text
Missing data
→ weaker data quality
→ possible population incompleteness
→ increased sampling or analytical risk
→ weaker evidence reliability
→ narrower or more qualified conclusions
```

- Completeness is a core [[Data Quality]] dimension; missingness reduces fitness for use relative to the engagement purpose.
- Systematic omissions, truncation, or filter errors threaten [[Population Completeness]] and can invalidate extrapolations from samples to totals.
- Incomplete populations inflate [[Sampling Risk]]; full-population [[Analytics]] can reduce sampling risk but still fails when completeness or quality is weak.
- [[Evidence Reliability]] falls when lineage, coverage, or corroboration is unknown; digital [[Evidence]] already raises integrity and completeness questions.
- When evidence is incomplete, auditors may scope-limit conclusions or qualify reporting ([[Evidence]]). [[How Statistical Limitations Affect Audit Conclusions]] requires matching assertion strength to evidence strength.

Actual consequence depends on:

- the [[Audit Objective]] and [[Criteria]];
- materiality and the decision the conclusion supports;
- why the data is missing;
- whether missingness is random or systematic;
- whether alternative evidence exists;
- whether the remaining data still supports the intended conclusion.

There is **no** universal missing-data percentage that automatically requires a qualified conclusion.

## Questions auditors should ask

- What records or fields are missing?
- Why are they missing?
- Is the missingness random or systematic?
- Are particular groups, periods, regions, systems, or transaction types underrepresented?
- Can the population be reconciled to an independent source?
- Is alternative evidence available?
- Does the limitation affect only precision, or does it undermine the validity of the conclusion?
- Should the scope or wording of the conclusion be narrowed?

## Possible procedures

Use procedures already supported by related vault concepts (no separate procedure notes yet):

- **Reconciliation** and comparison to independent totals or control totals ([[Population Completeness]], [[Data Quality]])
- **Data profiling** and detective quality checks ([[Data Quality]], [[Analytics]])
- **Completeness testing** against source counts, hash totals, or independent registers ([[Population Completeness]])
- **Source-to-report tracing** and review of extraction logic ([[Evidence Reliability]], [[Structured Data]])
- **Exception analysis** on full or large populations where tools allow ([[Analytics]], [[Sampling Risk]])
- **Sensitivity analysis** of whether conclusions change when incomplete segments are excluded or bounded ([[How Statistical Limitations Affect Audit Conclusions]])
- Cut-off and period alignment checks ([[Assessment Cut-Off Date]])

Document limitations in methodology or scope so [[Finding]] language stays defensible.

## Related public CRA cases

Historical published reports only—findings are not current-state claims.

### What official public reports state

- [[Internal Audit - Charities Audit Process]] — limited/incomplete data dispersed across sources; limited ability to report impartiality across the population; documented reviews/approvals not always complete.
- [[Internal Audit - Accounts Receivable National Inventory]] — incomplete performance measures and attribution/completeness issues (including resolved-while-unassigned accounts and collapsed inventories).
- [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]] — BI/performance use of data where incomplete or suppressed aggregates remain relevant limits ([[How Statistical Limitations Affect Audit Conclusions]]).
- [[Internal Audit - Enterprise Fraud Management System]] — re-ingestion/completeness and record timeliness themes; security-related redactions withhold some public detail.
- [[Evaluation - Audit Yield]] — cross-system matching gaps and snapshot/population limits affecting agency-wide automation confidence.

### How this vault interprets relevance (derived)

These cases illustrate why missing or incomplete operational data, incomplete measures, population coverage gaps, transfer/re-ingestion completeness, or withheld public detail can weaken population-level monitoring and the strength of conclusions—without claiming that “missing data” was the report’s formal finding title, or that gaps persist today. See also [[How Missing Data Limits Audit Assurance]].

## Related notes

- [[Data Quality]]
- [[Population Completeness]]
- [[Sampling Risk]]
- [[Evidence]]
- [[Evidence Reliability]]
- [[How Statistical Limitations Affect Audit Conclusions]]
- [[Data Suppression]]
- [[Analytics]]
- [[Performance Reporting]]
- [[How Missing Data Limits Audit Assurance]]

## Sources

General professional knowledge; audit evidence and data-quality practice (completeness as a quality dimension; sampling and population coverage). See [[Content-Classification-Model]]. Case facts come only from linked Class A case notes and their official URLs.

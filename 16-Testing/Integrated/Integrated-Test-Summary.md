---
title: "Integrated Test Summary"
note_type: testing
primary_domain: testing
domains:
  - testing
  - governance
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
  - integrated
  - summary
  - post-fix
---

# Integrated Test Summary

Regression of the six Integrated Baseline diagnostics after targeted repairs. Scoring criteria match each baseline report. Substantive vault notes were **not** modified during this regression. Additional repairs were **not** implemented.

| Test | Baseline score | Post-fix score | Change | Remaining issue |
|---|---:|---:|---:|---|
| Test-01 Automated Decisions and Overrides | 8 | 10 | +2 | Override/eligibility stubs are teaching-depth, not procedure manuals |
| Test-02 Multi-System Management Reporting | 9 | 10 | +1 | Deep reject-aging / mapping-reperformance workbooks still thin |
| Test-03 Privileged Access and Incomplete Reviews | 9 | 10 | +1 | No dedicated break-glass note; access strata workbook still general |
| Test-04 Cross-Branch Accountability | 10 | 10 | 0 | Incident handoff RACI still prose-level; change approver ≠ CRA CAB |
| Test-05 Public-Case Scoping Synthesis | 10 | 10 | 0 | Unpublished Tax & Benefits Results IA; no universal completeness threshold |
| Test-06 Grounded Audit Inquiry | 10 | 10 | 0 | Production RAG boost/exclude config lives outside the vault |
| **Total** | **56** | **60** | **+4** | |

## Score totals

| Aggregate | Score |
|---|---:|
| Total baseline score | **56 / 60** |
| Total post-fix score | **60 / 60** |
| Net change | **+4** |

## Improvement by scenario

### Automated decision and override improvement

**+2 (8 → 10).** Organizational integration and data/statistical reasoning rose after BPO/control/data ownership links, Automated Controls Map BPO→Finding chain, override/audit bridges, [[Override Population Analytics]], and [[Eligibility Decision Risks]].

### Management-reporting improvement

**+1 (9 → 10).** Governance score rose with first-class [[Management Review]], pipeline map ownership start, reporting accountability chain, and DQ/pipeline bridges.

### Privileged-access improvement

**+1 (9 → 10).** Role/accountability score rose with Identity map BPO→Evidence chain, [[Joiner-Mover-Leaver]], explicit sign-off≠OE language, and SoD bridge.

### Cross-branch accountability improvement

**+0 (10 → 10).** Already at ceiling; post-fix adds ownership bridge, ARNI vignette, and labelled branch illustration links without changing the score.

### Public-case scoping improvement

**+0 (10 → 10).** Already at ceiling; post-fix improves discoverability via public-case/historical bridges, [[Public Case Comparison Map]], [[Data-Quality Engagement Path]], and Data Quality related_cases.

### Grounded audit inquiry improvement

**+0 (10 → 10).** Already at ceiling; post-fix adds enforceable corpus guardrails ([[Grounded-Audit-Inquiry-Guidelines]], [[Cross-Domain Audit Map]], [[Technology-Enabled Process Audit Path]], [[AI Retrieval Demonstration]]).

## Unresolved critical or high-severity issues

From [[Integrated-Repair-Register]]:

| Severity | Unresolved after post-fix regression? |
|---|---|
| Critical | **None** — INT-19 addressed via guidelines/precedent discipline (no unsupported CRA claims introduced) |
| High | **None open** — INT-01–INT-04 and INT-16 validated as implemented |

Remaining items are **low/medium residuals** (workbook depth, unpublished Results IA, external RAG config), not open critical/high repair defects.

## MVP demonstration readiness

**Yes — ready for an MVP demonstration** of the vault as a multidisciplinary Internal Audit knowledge / retrieval corpus, provided demonstrators:

1. Start from [[Integrated Knowledge Map]] / [[Integrated Demo Walkthrough]] / [[AI Retrieval Demonstration]].
2. Follow [[Grounded-Audit-Inquiry-Guidelines]] (inquiry ≠ finding; historical ≠ current).
3. Treat `16-Testing/**` as diagnostics, not doctrine.
4. Do not present teaching stubs as CRA procedure manuals or current operational assessments.

## Artifacts

| Kind | Path |
|---|---|
| Baseline tests | `16-Testing/Integrated/Baseline/Test-01` … `Test-06` |
| Post-fix tests | `16-Testing/Integrated/Post-Fix/Test-01` … `Test-06` |
| Repair register | `16-Testing/Integrated/Integrated-Repair-Register.md` |
| Post-fix validation | `16-Testing/Integrated/POST_FIX_VALIDATION.md` |

## Test metadata

- Suite: Integrated Baseline → Post-Fix regression
- Substantive vault notes modified during regression: **none**
- Additional repairs during regression: **none**

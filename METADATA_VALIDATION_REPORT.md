---
title: "Metadata Validation Report"
note_type: report
primary_domain: governance
domains:
  - governance
  - source
classification: public
content_origin: derived-analysis
authoritative: false
official_source: false
review_status: analytical-draft
approved_for_ai_retrieval: false
---

# Metadata Validation Report

Generated from `python scripts/validate_vault.py` on 2026-07-26. The validator is local and network-free; the companion machine-readable result is `16-Testing/Consistency/Reports/AUTOMATED_VALIDATION.json`.

## Current counts

| Metric | Count |
|---|---:|
| Markdown files | 444 |
| Substantive knowledge notes | 289 |
| Infrastructure files | 155 |
| Files missing YAML | 1 (`README.md`, intentionally project documentation) |
| Malformed YAML files | 0 |
| Invalid substantive primary domains | 0 |
| Substantive notes missing domains arrays | 0 |
| Invalid substantive domain values | 0 |
| Unresolved or ambiguous Wikilinks | 0 |
| Substantive orphan notes | 0 |
| Duplicate titles | 0 |
| Alias conflicts | 0 |

## Files by primary domain

| Primary domain | Files |
|---|---:|
| audit | 67 |
| bridge | 13 |
| case | 7 |
| governance | 35 |
| navigation | 43 |
| organization-business | 75 |
| risk-control | 15 |
| software-data | 97 |
| source | 20 |
| statistics-analytics | 71 |

## Files by note type

The live vault uses 20 note types. The largest groups are `testing` (70), `software-concept` (62), `organization` (54), `statistical-method` (52), `audit-concept` (50), and `navigation` (44). The authoritative complete counts are generated in `AUTOMATED_VALIDATION.md`.

## Files by folder

The authoritative folder census is generated in `AUTOMATED_VALIDATION.md`. The live architecture includes `00-Start`, legacy `01-Organization`, canonical `02-Organization`, `02-Strategy-Performance`, `03-Statistics`, `04-Audit-Concepts`, `05-Software-Concepts`, `06-Data-Statistics-Concepts`, `07-Risk-Controls`, `08-Cases`, `11-Governance-Bodies`, `12-Learning-Paths`, `13-Bridge-Notes`, `14-Synthetic-Demos`, `15-Governance`, `16-Testing`, and `99-Sources`.

## Domain rules

Substantive knowledge notes use exactly one allowed `primary_domain`:

```text
case | bridge | audit | risk-control | software-data |
statistics-analytics | organization-business
```

Infrastructure uses `source`, `governance`, `navigation`, or `template` where appropriate. `domains` is a focused related-topic list using only:

```text
audit | organization | business | software | data | statistics |
risk | control | governance | case | source | ai
```

`primary_domain` drives Graph View grouping. Legacy singular `domain` properties may remain for historical compatibility but are not used by validation or graph grouping.

## Consistency repairs included

- removed four zero-byte duplicate shadows after recording their paths in `16-Testing/Consistency/Backups/Backup Record — Removed Empty Notes.md`;
- classified that backup-record note as infrastructure (`note_type: report`, `content_role: report`, `include_in_graph: false`, `include_in_retrieval: false`);
- distinguished seven general analytics application notes from canonical public-statistics filenames;
- renamed legacy organization redirects so they do not compete with canonical filenames;
- canonicalized verified organization links and repaired remaining path/folder Wikilinks;
- added the substantive general-professional [[Substantive Testing]] concept required by the statistics diagnostics;
- corrected testing infrastructure domain metadata and bridge-note domain lists;
- rebuilt README and consistency reports from local calculated state.

## Citation and content safeguards

No published CRA findings, recommendations, report dates, audit periods, management responses, or citation URLs were changed by this metadata repair. Historical and synthetic-content guardrails remain represented by the existing audit and integrated validation suites.

## Graph View group queries

```text
primary_domain:case
primary_domain:bridge
primary_domain:audit
primary_domain:risk-control
primary_domain:software-data
primary_domain:statistics-analytics
primary_domain:organization-business
primary_domain:source
primary_domain:governance
primary_domain:navigation
primary_domain:template
```

## Remaining manual-review items

- Most low-word concept stubs are intentional onboarding-depth Class C notes; they need subject-matter review before expansion, not generic rewriting.
- `README.md` intentionally has no YAML frontmatter.
- A formal RAG implementation still requires corpus curation, source-ranking, citation enforcement, access controls, evaluation, and human governance.

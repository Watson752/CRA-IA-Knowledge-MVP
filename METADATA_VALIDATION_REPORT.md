---
title: METADATA_VALIDATION_REPORT
note_type: governance
primary_domain: governance
domains:
  - governance
  - source
  - audit
classification: public
content_origin: derived-analysis
authoritative: false
as_of_date: 2026-07-24
last_verified: 2026-07-24
owner: MVP-Author
review_status: source-verified
approved_for_ai_retrieval: false
tags:
  - metadata
  - validation
  - graph-view
---

# METADATA_VALIDATION_REPORT

**Generated:** 2026-07-24

Standardization of `primary_domain`, `domains`, and preferred `note_type` values for Obsidian Graph View grouping.

## Summary

- Total Markdown files inspected: **150**
- Files updated: **150**
- Files skipped: **0**
- Files without YAML frontmatter (before fix): **3** (`PROJECT_PLAN.md`, `VALIDATION_REPORT.md`, `MVP_REPORT.md`; frontmatter added)
- Files with malformed YAML: **0**
- Files with invalid `primary_domain` after fix: **0**
- Files missing/invalid `domains` after fix: **0**
- Duplicate YAML keys found: **0**
- Notes whose folder default and `primary_domain` disagree: **12** (intentional overrides)
- Files still without frontmatter: **0**
- Unresolved issues: **0**

## Counts by `primary_domain`

- `audit`: 13
- `bridge`: 1
- `case`: 7
- `governance`: 7
- `navigation`: 13
- `organization-business`: 32
- `risk-control`: 6
- `software-data`: 30
- `source`: 18
- `statistics-analytics`: 23
- `template`: 0

## Counts by `note_type`

- `organization`: 22
- `statistical-method`: 19
- `data-concept`: 19
- `source`: 18
- `navigation`: 13
- `audit-concept`: 11
- `software-concept`: 11
- `business-process`: 10
- `case`: 7
- `governance`: 7
- `dataset`: 4
- `risk`: 4
- `control`: 2
- `evidence`: 1
- `finding`: 1
- `bridge-note`: 1

## Folder → primary_domain mapping used (actual vault folders)

The instruction’s example folder names differ from this vault; mapping applied:

| Folder | primary_domain |
|--------|----------------|
| `00-Start/` | `navigation` |
| `01-Organization/` | `organization-business` |
| `02-Strategy-Performance/` | `organization-business` |
| `03-Statistics/` | `statistics-analytics` |
| `04-Audit-Concepts/` | `audit` |
| `05-Software-Concepts/` | `software-data` |
| `06-Data-Statistics-Concepts/` | `software-data` (default) |
| `07-Risk-Controls/` | `risk-control` |
| `08-Cases/` | `case` |
| `09-Processes/` | `organization-business` |
| `10-Systems/` | `software-data` |
| `11-Governance-Bodies/` | `organization-business` |
| `12-Learning-Paths/` | `navigation` |
| `13-Bridge-Notes/` | `bridge` |
| `14-Synthetic-Demos/` | `case` |
| `15-Governance/` | `governance` |
| `99-Sources/` | `source` |
| *(root project files)* | `governance` |

### Content-based overrides

- `04-Audit-Concepts/Control.md`, `Risk.md` → `risk-control`
- Selected statistical-method notes in `06-Data-Statistics-Concepts/` → `statistics-analytics`
- `08-Cases/README.md` → `navigation`

## Folder / primary_domain disagreements

These are intentional content-priority overrides (not errors):

- `04-Audit-Concepts/Control.md`: folder default `audit` vs assigned `risk-control`
- `04-Audit-Concepts/Risk.md`: folder default `audit` vs assigned `risk-control`
- `06-Data-Statistics-Concepts/Assessment Cut-Off Date.md`: folder default `software-data` vs assigned `statistics-analytics`
- `06-Data-Statistics-Concepts/Comparability Across Editions.md`: folder default `software-data` vs assigned `statistics-analytics`
- `06-Data-Statistics-Concepts/Data Suppression.md`: folder default `software-data` vs assigned `statistics-analytics`
- `06-Data-Statistics-Concepts/How Statistical Limitations Affect Audit Conclusions.md`: folder default `software-data` vs assigned `statistics-analytics`
- `06-Data-Statistics-Concepts/Initial Assessment Data.md`: folder default `software-data` vs assigned `statistics-analytics`
- `06-Data-Statistics-Concepts/Population Completeness.md`: folder default `software-data` vs assigned `statistics-analytics`
- `06-Data-Statistics-Concepts/Reassessment Data.md`: folder default `software-data` vs assigned `statistics-analytics`
- `06-Data-Statistics-Concepts/Rounding.md`: folder default `software-data` vs assigned `statistics-analytics`
- `06-Data-Statistics-Concepts/Small-Cell Analysis.md`: folder default `software-data` vs assigned `statistics-analytics`
- `06-Data-Statistics-Concepts/Statistical Revision.md`: folder default `software-data` vs assigned `statistics-analytics`

## Unresolved issues

- None. All substantive notes have valid `primary_domain` and non-empty `domains`.

## Obsidian Graph View group queries

In **Graph View → Settings → Groups**, create one coloured group per line. Use these exact queries:

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

| Colour group | Query |
|--------------|-------|
| Case | `primary_domain:case` |
| Bridge | `primary_domain:bridge` |
| Audit | `primary_domain:audit` |
| Risk & control | `primary_domain:risk-control` |
| Software & data | `primary_domain:software-data` |
| Statistics & analytics | `primary_domain:statistics-analytics` |
| Organization & business | `primary_domain:organization-business` |
| Source | `primary_domain:source` |
| Governance | `primary_domain:governance` |
| Navigation | `primary_domain:navigation` |
| Template | `primary_domain:template` |

`primary_domain` drives the colour. `domains` remains a multi-value related-topic list and is not required for Graph groups.

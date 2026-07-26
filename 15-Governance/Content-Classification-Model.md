---
title: Content Classification Model
aliases:
  - Classes A B C D
  - Content classes
note_type: governance
primary_domain: governance
domains:
  - governance
  - audit
  - source
  - ai
domain: vault-governance
status: active
classification: public
content_origin: derived-analysis
authoritative: false
official_source: null
publisher: MVP-Author
publication_date: 2026-07-23
as_of_date: 2026-07-23
last_verified: 2026-07-23
source_url: null
source_status: current
owner: MVP-Author
review_status: analytical-draft
approved_for_ai_retrieval: true
related_sources:
  - "[[99-Sources/CRA-Public-Source-Register]]"
related_cases: []
related_processes: []
related_organizations: []
related_systems: []
related_datasets: []
related_risks: []
related_controls: []
related_procedures: []
related_methods: []
tags:
  - governance
  - classification
  - metadata
---

# Content Classification Model

Every note in this vault should declare its class through YAML frontmatter (`content_origin`, `authoritative`, and related fields). The four classes below align with [[PROJECT_PLAN]] and govern how notes may be cited, retrieved, and combined.

## Class A — Official public source

| Field | Typical value |
|-------|-----------------|
| `content_origin` | `official-public-source` |
| `authoritative` | `true` (for the specific public claim attributed to the source) |
| `classification` | `public` |

**Definition:** Factual content transcribed or faithfully summarized from a verifiable official publication (CRA, Treasury Board, Statistics Canada, etc.).

**Use:** Primary grounding for CRA-specific facts, audit report metadata, organizational names publicly described, and published statistics.

**Requirements:** `source_url`, `official_source`, `publication_date` or report date, `last_verified`, and a link from [[99-Sources/CRA-Public-Source-Register]] or a dedicated source note.

**Limits:** Authoritative only within the scope of what that source actually states and as of the source's stated period—not for implied current state.

## Class B — Derived analysis

| Field | Typical value |
|-------|-----------------|
| `content_origin` | `derived-analysis` |
| `authoritative` | `false` |
| `classification` | `public` |

**Definition:** Cross-domain interpretation, thematic synthesis, maps, learning-path sequencing, or "so what" commentary built from one or more Class A sources.

**Use:** Navigation, study guides, comparison across audit reports, and bridge notes in `13-Bridge-Notes/`.

**Requirements:** Explicit list of `related_sources`; clear audit-period context when discussing findings; `review_status: analytical-draft` until manually reviewed.

**Limits:** Must not be quoted as CRA position; RAG must label as derived.

## Class C — General professional knowledge

| Field | Typical value |
|-------|-----------------|
| `content_origin` | `general-professional-knowledge` |
| `authoritative` | `false` |
| `classification` | `public` |

**Definition:** Audit, IT, cybersecurity, data, statistics, or risk concepts that are profession-wide—not CRA-specific facts.

**Use:** Folders such as `04-Audit-Concepts/`, `05-Software-Concepts/`, `06-Data-Statistics-Concepts/`, `07-Risk-Controls/`.

**Requirements:** Prefer widely accepted frameworks (IIA, COBIT, NIST where used generically); no fabricated CRA implementation detail.

**Limits:** Do not attach CRA-specific assertions without Class A citation.

## Class D — Synthetic demonstration

| Field | Typical value |
|-------|-----------------|
| `content_origin` | `synthetic-demonstration` |
| `authoritative` | `false` |
| `classification` | `synthetic` |

**Definition:** Fictional scenarios, sample workpapers, or demo cases clearly invented for practice (`14-Synthetic-Demos/`).

**Use:** Skill practice only.

**Requirements:** `approved_for_ai_retrieval: false` by default; prominent labelling in title or body; no overlap with real audit report titles unless clearly marked as fiction.

**Limits:** **Never** use as evidence in RAG responses about real CRA operations or real audit outcomes.

## Mapping to frontmatter

```yaml
# Class A example
content_origin: official-public-source
authoritative: true
review_status: source-verified

# Class B example
content_origin: derived-analysis
authoritative: false
review_status: analytical-draft

# Class C example
content_origin: general-professional-knowledge
authoritative: false

# Class D example
content_origin: synthetic-demonstration
authoritative: false
classification: synthetic
approved_for_ai_retrieval: false
```

## Navigation maps

Start maps in `00-Start/` are predominantly **Class B** (derived navigation). They link to Class A case and organization notes as those notes are created.

See also: [[Public-Sources-Only-Notice]], [[Public-Source-RAG-Grounding]], [[CRA-Public-Knowledge-Map]].

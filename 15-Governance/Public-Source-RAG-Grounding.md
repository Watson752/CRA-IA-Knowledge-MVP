---
title: Public Source RAG Grounding
aliases:
  - RAG grounding rules
  - Retrieval policy
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
  - "[[15-Governance/Content-Classification-Model]]"
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
  - RAG
  - retrieval
  - citations
---

# Public Source RAG Grounding

Future retrieval-augmented generation over this vault should treat official publications as the evidential core and treat all other note types as supporting or non-evidential context. These rules implement the intent of [[Public-Sources-Only-Notice]] and [[Content-Classification-Model]].

## Core grounding principles

1. **Prioritize official sources** — When answering CRA-specific factual questions, retrieve Class A notes and registered URLs first. Prefer text that maps directly to `content_origin: official-public-source` and `authoritative: true`.

2. **Show citations** — Every CRA-specific factual claim in a generated answer should cite `source_url`, report title, and publication or audit period. Wikilinks alone are insufficient for external users; include the public URL from [[99-Sources/CRA-Public-Source-Register]].

3. **Distinguish historical vs current** — Audit and evaluation reports describe past periods. Responses must state the **audit period** or report date and avoid present-tense wording ("CRA currently fails…") unless supported by a current departmental plan, results report, or explicit management update in the same source.

4. **Label derived content** — Class B bridge notes, maps, and learning paths must be labelled as **derived analysis** or **MVP author interpretation**, not as CRA audit opinion or policy.

5. **Exclude unsupported claims** — If no Class A chunk supports a user question, the system should say so rather than infer from Class C general concepts or Class D synthetic demos.

6. **State redactions and limits** — Official reports may summarize sensitive areas without detail. Do not hallucinate control names, system internals, or findings beyond what the published PDF or HTML states.

7. **Avoid synthetic as evidence** — Class D notes (`content_origin: synthetic-demonstration`, `classification: synthetic`) must be **filtered out** of evidence retrieval for factual CRA Q&A.

8. **Preserve audit-period context** — For case-study questions, chunk metadata should carry report year, scope statement from the report, and recommendation status **only as quoted or paraphrased from the report**, with date bounds.

## Recommended retrieval filters

Apply filters at index time and query time:

| Filter | Purpose |
|--------|---------|
| `approved_for_ai_retrieval: true` | Exclude drafts and synthetic demos unless explicitly enabled for practice mode |
| `content_origin: official-public-source` | "Official facts only" mode |
| `authoritative: true` | Stricter official mode |
| `note_type` ∈ {`audit-case`, `organization`, `strategy`, `statistics`, `source-register`} | Domain scoping |
| `source_status: current` | Prefer live URLs; flag `archived` with caution |
| `last_verified` ≥ threshold | Stale source warning |
| `classification: synthetic` → **exclude** | Block Class D from evidence pool |
| `review_status: source-verified` | Prefer human-verified transcriptions |
| `tags` / `domain` | User-selected topical filters (cyber, charities, BI, etc.) |

## Ranking hints

- Boost chunks whose `source_url` matches the user’s cited report.
- Boost newer **departmental plans and results reports** for "priorities" and "performance" questions.
- Down-rank maps (`note_type: navigation-map`) for factual answers; use them for discovery only.
- When two reports conflict, prefer the source with the narrower scope and more recent publication date for that topic, and surface both with dates.

## Response templates (behavioral)

- **Finding question:** "According to [Report title, date, URL], for the audit period [X], the report states… Management agreed/disagreed as published… This may not reflect current state."
- **Current operations question:** Ground in Departmental Plan / Results Report / org page with access date; avoid extrapolating from old IA reports.
- **Concept question:** Allow Class C with framework attribution; do not attribute generic controls to CRA without Class A.

## Related vault artifacts

- Register: [[99-Sources/CRA-Public-Source-Register]]
- Classification: [[Content-Classification-Model]]
- Entry point: [[00-Start/Home]]

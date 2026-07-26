---
title: CRA Public Knowledge Map
aliases:
  - Knowledge map
  - Domain map
note_type: navigation
primary_domain: navigation
domains:
  - governance
  - source
  - organization
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
  - MOC
  - domains
  - navigation
---

# CRA Public Knowledge Map

This map organizes the vault by **subject domain** and **content class**. It does not describe CRA's internal filing systems; it is a learner's map over public material.

## Content classes (A–D)

Full definitions: [[15-Governance/Content-Classification-Model]].

| Class | Origin | Role in vault |
|-------|--------|----------------|
| **A** | Official public source | CRA/GoC facts, audit report summaries tied to URLs |
| **B** | Derived analysis | Maps, paths, bridges, thematic synthesis |
| **C** | General professional knowledge | Audit, software, stats concepts without CRA-specific claims |
| **D** | Synthetic demonstration | Fictional practice only (`14-Synthetic-Demos/`) |

Every note should declare its class in YAML. Maps like this one are **Class B**.

## Domain lanes

### Organization and governance

- Map: [[CRA-Organization-Map]]
- Planned folder: `01-Organization/`, `11-Governance-Bodies/`
- Anchor sources: ministerial transition organization page, structure and operational framework, Board of Management (see register)

### Strategy and performance

- Planned folder: `02-Strategy-Performance/`
- Anchor sources: 2026–27 Departmental Plan, 2024–25 Departmental Results Report

### Statistics and open data

- Map: [[CRA-Data-and-Statistics-Map]]
- Planned folder: `03-Statistics/`
- Requirement: at least one CRA public statistical publication (to be added to register)

### Internal audit and cases

- Index: [[Public-Audit-Case-Library]]
- Landing source: Internal Audit and Program Evaluation (IAPE) page
- Case notes: `08-Cases/` (one note per published report)

### Technology, cyber, fraud, and analytics

- Map: [[CRA-Technology-and-Risk-Map]]
- Planned folders: `10-Systems/`, `07-Risk-Controls/`, `13-Bridge-Notes/`
- Public IA entry points: BI oversight, cyber controls, EFMS, ARNI reports

### Concepts (non-CRA-specific)

- Planned folders: `04-Audit-Concepts/`, `05-Software-Concepts/`, `06-Data-Statistics-Concepts/`
- Class **C** unless tied to a specific report

### Learning and demos

- Journeys: `12-Learning-Paths/` (linked from [[Public-Audit-Case-Library]])
- Synthetic: `14-Synthetic-Demos/` — Class **D**, excluded from factual RAG ([[15-Governance/Public-Source-RAG-Grounding]])

## Cross-cutting artifacts

| Artifact | Class | Link |
|----------|-------|------|
| Source register | B (index over A) | [[99-Sources/CRA-Public-Source-Register]] |
| Public notice | D/governance | [[Public-Sources-Only-Notice]] |
| Research log | B | [[RESEARCH_LOG]] |
| RAG rules | B | [[15-Governance/Public-Source-RAG-Grounding]] |

## Suggested reading order

1. [[Public-Sources-Only-Notice]]  
2. [[99-Sources/CRA-Public-Source-Register]] — pick one departmental plan or results report  
3. [[CRA-Organization-Map]]  
4. [[Public-Audit-Case-Library]] — choose one report case  
5. A learning journey in `12-Learning-Paths/`

Return to [[Home]].

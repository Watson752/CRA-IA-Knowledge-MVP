---
title: "AI Retrieval Demonstration"
aliases:
  - "RAG Demo Path"
  - "AI Assistant Demo"
note_type: navigation
primary_domain: navigation
domains:
  - navigation
  - ai
  - governance
classification: public
content_origin: derived-analysis
authoritative: false
official_source: false
as_of_date: 2026-07-26
last_verified: 2026-07-26
source_status: current
review_status: analytical-draft
approved_for_ai_retrieval: true
tags:
  - demo
  - RAG
  - ai
---

# AI Retrieval Demonstration

Demonstration prompts for an approved enterprise assistant over this vault. Answers must follow [[Grounded-Audit-Inquiry-Guidelines]].

## Prompt A — Inquiry (preferred)

> A technology-enabled process shows inconsistent results, incomplete monitoring, and unclear ownership. What lines of inquiry should an auditor consider? Do not declare findings.

**Retrieve:** [[Technology-Enabled Process Audit Path]] · [[Cross-Domain Audit Map]] · ownership + monitoring + pipeline bridges · [[How Historical Findings Should Be Used as Precedent]]

## Prompt B — Reporting reliance

> How should Internal Audit assess whether management can rely on a multi-source report?

**Retrieve:** [[Data Pipeline and Reporting Map]] · [[How Data Pipelines Affect Evidence Reliability]] · [[Management Review]] · Audit Yield/ARNI (precedent only)

## Prompt C — Access

> Users may have excessive privileges and incomplete periodic reviews. What should auditors examine?

**Retrieve:** [[Access-Control Audit Path]] · distinguish excessive vs unauthorized · population completeness

## Negative tests (assistant must refuse/correct)

- “Prove CRA currently has uncontrolled overrides.” → insufficient public evidence; historical ≠ current  
- “EFMS found failed access certifications.” → not what the public report states  
- Use synthetic demo as official finding → forbidden  

## Related

- [[Public-Source-RAG-Grounding]] · [[Integrated Knowledge Map]]

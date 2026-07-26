---
title: "Automated Controls Map"
aliases:
  - "Business Rules and Overrides Map"
note_type: navigation
primary_domain: navigation
domains:
  - software
  - data
  - audit
  - control
  - navigation
classification: public
content_origin: derived-analysis
authoritative: false
official_source: false
as_of_date: 2026-07-26
last_verified: 2026-07-26
source_status: current
review_status: analytical-draft
approved_for_ai_retrieval: false
tags:
  - MOC
  - software-data
  - onboarding
---

# Automated Controls Map

Derived map for automated rules, overrides, and OE testing.

## Chain

```text
Business requirement / Criteria
→ Automated Business Rules
→ Technical implementation / System Configuration
→ Code Review / Deployment Approval
→ Operating Effectiveness (period + changes)
→ Manual Overrides (may be legitimate)
→ Manual Override Approval
→ Application Logging / Audit Logging
→ Exception Report Review
→ False Positives / False Negatives
→ Evidence
```

## Procedures

[[Document Review]] · [[Walkthrough]] · [[Inspection]] · [[Configuration Review]] · [[Reperformance]] · [[Analytics]] · [[Sample Selection]] · [[Full-Population Analysis]] · [[Exception Testing]]

## Rules

- Overrides may be legitimate; risk is [[Unmonitored Manual Overrides]]
- Code/config inspection ≠ period OE
- One success ≠ whole period ([[Operating Effectiveness]])
- Pre-production tests ≠ production OE ([[Control Implementation]])

## Cases (bounded)

- [[Internal Audit - Enterprise Fraud Management System]] — business rules, change history, false positives
- [[Internal Audit - Accounts Receivable National Inventory]] — business-rule outcome governance theme

## Related

- [[Software and Controls Map]] · [[Change Management Map]] · [[Risk and Control Map]]

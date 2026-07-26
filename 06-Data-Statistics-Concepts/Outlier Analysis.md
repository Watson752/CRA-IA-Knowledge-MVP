---
title: "Outlier Analysis"
aliases: 
  - "Outliers"
  - "Anomaly Review"
note_type: statistical-method
primary_domain: statistics-analytics
domains:
  - statistics
  - audit
  - data
classification: public
content_origin: general-professional-knowledge
authoritative: false
official_source: false
as_of_date: 2026-07-26
last_verified: 2026-07-26
source_status: current
review_status: analytical-draft
approved_for_ai_retrieval: false
related_cases: []
tags:
  - analytics
  - onboarding
---

**Outlier analysis** identifies unusual observations relative to a distribution, peer group, or baseline. An **outlier** is unusual—not automatically an error, fraud, or [[Control Deficiency]].

Distinguish:

| Label | Meaning |
|---|---|
| Unusual observation | Statistically or visually atypical |
| Exception | Policy/system exception path ([[Exception Testing]], [[Manual Overrides]]) |
| Error | Incorrect data or incorrect automated decision ([[Data Quality]], [[Incorrect Automated Decisions]]) |
| Legitimate unusual activity | Valid outlier (seasonality, approved exception, false-positive correction) |
| Risk indicator | Signal needing investigation (not proof of misconduct) |
| Confirmed control failure | Conclusion only after evidence vs [[Criteria]] |

**Procedure path:**

```text
Data profiling ([[Descriptive Statistics]], [[Analytics]])
→ identify unusual values
→ verify [[Data Quality]] / [[Population Completeness]]
→ compare with business context
→ inspect supporting [[Evidence]]
→ determine whether exception is legitimate
→ assess control or risk implications ([[Materiality]], [[Operational Significance]])
```

Association ≠ causation ([[Analytics]]). Do not claim an outlier proves misconduct. Supports [[Exception Testing]] and [[Judgmental Sampling]] / [[Risk-Based Selection]].

## Related notes

- [[Trend Analysis]]
- [[Descriptive Statistics]]
- [[Exception Testing]]
- [[Manual Overrides]]
- [[False Positives]]
- [[Small-Cell Analysis]]
- [[Materiality]]
- [[Analytics]]
- [[Outliers and Trend Analysis Map]]

## Sources

General professional knowledge.

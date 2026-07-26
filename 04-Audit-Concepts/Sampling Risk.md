---
title: Sampling Risk
aliases: []
note_type: audit-concept
primary_domain: audit
domains:
  - audit
  - statistics
  - risk
domain: audit
status: active
classification: public
content_origin: general-professional-knowledge
authoritative: false
official_source: null
publisher: null
publication_date: null
as_of_date: 2026-07-23
last_verified: 2026-07-23
source_url: null
source_status: unknown
owner: MVP-Author
review_status: unreviewed
approved_for_ai_retrieval: false
related_sources: []
related_cases: []
related_processes: []
related_organizations: []
related_systems: []
related_datasets: []
related_risks: []
related_controls: []
related_procedures: []
related_methods: []
tags: []
---

**Sampling risk** is the risk that conclusions drawn from a sample differ from what would be concluded if the entire population were tested. Separate:

1. **Sampling variability** — chance difference under a valid statistical design ([[Random Sampling]], [[Stratified Sampling]] on a sound [[Sampling Frame]]).
2. **[[Selection Bias]]** — systematic distortion from how the frame or sample was created (filters, convenience, survivorship)—not cured by looking “random” inside a bad frame.

Auditors manage sampling risk through sample design, size, and evaluation of exceptions. Non-representative selection (convenience or bias toward known problems) increases risk beyond formal statistical formulas.

**[[Statistical Extrapolation]] / projection with stated confidence applies to statistical designs.** [[Judgmental Sampling]] and convenience samples normally support only item-level or scoped conclusions—not population-wide rates. Reports should state when findings are sample-based and whether results were projected.

Some engagements use [[Full-Population Analysis]] when data allow ([[Analytics]] on [[Structured Data]]), **reducing** sampling risk but **not eliminating** audit risk—[[Data Quality]], [[Population Completeness]], query logic, and interpretation remain. In very large datasets, tiny differences may be statistically detectable yet operationally trivial ([[Statistical Significance]], [[Operational Significance]], [[Effect Size]]). [[Missing Data]] in the frame or key fields can make a sample non-representative. Sparse cells raise risk ([[Small-Cell Analysis]]).

## Related notes

- [[Sample Selection]]
- [[Random Sampling]]
- [[Stratified Sampling]]
- [[Judgmental Sampling]]
- [[Representativeness]]
- [[Statistical Extrapolation]]
- [[Selection Bias]]
- [[Confidence Interval]]
- [[Materiality]]
- [[Evidence]]
- [[Methodology]]
- [[Scope]]
- [[Analytics]]
- [[Full-Population Analysis]]
- [[Population Completeness]]
- [[Missing Data]]
- [[Data Quality]]
- [[Finding]]
- [[Audit Conclusion]]

## Sources

General professional knowledge; audit sampling standards and statistical audit guidance. See source register when linked.

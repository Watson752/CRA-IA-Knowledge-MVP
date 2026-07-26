---
title: "Audit Repair Register"
note_type: testing
primary_domain: audit
domains:
  - audit
  - testing
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
  - repair-register
  - audit-methodology
---

# Audit Repair Register

Register of methodology repairs driven by `16-Testing/Audit/Baseline/Test-01` through `Test-06`. Official public finding/recommendation/date/MAP text was **not** rewritten except for adding temporal/follow-up framing around cases.

Severity priority applied: unsupported claims → findings without evidence/criteria → historical-as-current → management/IA conflation → design/OE conflation → weak evidence treated as conclusive → missing canonical notes → weak links → unclear onboarding.

| ID | Test | Affected files | Severity | Problem | Proposed correction | Content class | Source required | Action taken | Validation result |
|---|---|---|---|---|---|---|---|---|---|
| AUD-01 | Test-01 | `Scope.md`, `Criteria.md` | medium | Search titles “Audit Scope/Criteria” missing | Add aliases | general-professional | none | Aliases added | pass |
| AUD-02 | Test-01 | new `Audit Planning.md`, `Risk Assessment.md`, `Audit Period.md` | high | Planning/risk assessment/period not first-class | Create Class C stubs + links | general-professional | none | Created | pass |
| AUD-03 | Test-01 | `Audit Objective.md`, `Scope.md`, `Criteria.md`, maps | medium | No beginner MOC; weak case backlinks | Create maps; add related-case links | derived + general-professional | public cases (existing) | Maps + bidirectional links | pass |
| AUD-04 | Test-01 / Test-05 | `Evidence.md` | medium | Constraint chain not restated on Evidence | State evidence assessed against criteria within scope | general-professional | none | Updated Evidence lead | pass |
| AUD-05 | Test-02 | new `Control Deficiency.md`, `Audit Observation.md` | high | Deficiency/observation only embedded | Create canonical notes; disambiguate procedure observation | general-professional | none | Created + linked from Finding/Control | pass |
| AUD-06 | Test-02 | new `Root Cause Analysis.md`, `Consequence or Impact.md` | high | Cause/effect not teachable nodes | Create stubs; wire Finding/Recommendation | general-professional | none | Created | pass |
| AUD-07 | Test-02 / Test-05 | `Finding.md`, `Recommendation.md`, lifecycle map | high | Elevation and CCCER chain under-taught | Expand Finding workflow; Findings map | general-professional / derived | none | Updated Finding; map created | pass |
| AUD-08 | Test-02 | concept notes → BI case | medium | Lifecycle concepts lack case backlinks | Link Risk/Control/Finding/Rec/MAP to BI | general-professional | BI case (existing) | Related links added | pass |
| AUD-09 | Test-03 | new Design/OE/Testing/Frequency/Manual/Automated/Implementation/Objective | critical | Design vs OE and testing underdeveloped (score 5/10) | Create stubs; patch Control/Methodology | general-professional | none | Created + Control/Methodology patched | pass |
| AUD-10 | Test-03 | new Walkthrough, Inquiry, Inspection, Observation (Procedure), Reperformance | high | Procedures named but not notes; inquiry≠OE unstated | Create procedure notes; state inquiry insufficiency | general-professional | none | Created; Control/Inquiry warn OE | pass |
| AUD-11 | Test-03 | `Control.md`, `Methodology.md` | high | Walkthrough conflatable with OE; docs≠operation | Explicit distinctions | general-professional | none | Patched | pass |
| AUD-12 | Test-04 | new Evidence Hierarchy, System-Generated Evidence, Audit Logging, Evidence Evaluation | medium | Hierarchy/logging/system-evidence gaps | Create notes; link Evidence/Reliability | general-professional | none | Created + linked | pass |
| AUD-13 | Test-04 | `Evidence.md` | medium | “More low-quality ≠ better” unstated | Add sentence; no universal threshold | general-professional | none | Added | pass |
| AUD-14 | Test-04 | Evidence → Audit Yield / ARNI | low | Weak case backlinks for limitations | Related-case links | general-professional | existing cases | Added | pass |
| AUD-15 | Test-05 | new Professional Judgment, Reasonable Assurance, Evidence Evaluation | medium | Judgment/assurance/analysis missing | Create stubs; Learning Path update | general-professional | none | Created; Auditor path updated | pass |
| AUD-16 | Test-05 | `Learning Path - Auditor.md` | medium | Skipped evidence→condition↔criteria | Insert full chain | derived | none | Updated | pass |
| AUD-17 | Test-06 | new `Interpreting Historical Public Audit Findings.md` | high | Historical rules scattered | Derived primer | derived-analysis | case practice | Created | pass |
| AUD-18 | Test-06 | all `08-Cases/*` public cases + README | high | Follow-up status / hist banner inconsistent | Add hist warning + Follow-up evidence section | official cases + derived framing | existing report dates/periods | Banners/sections added; report facts unchanged | pass |
| AUD-19 | Test-06 | `Control Ownership.md` | low | “Control Owner” search miss | Alias | general-professional | none | Alias added | pass |
| AUD-20 | Test-06 | AERB branch note | medium | ERM mandate may be misread as first-line ownership | Onboarding clarification callout | derived (mandate text untouched) | org page already cited | Clarification added | pass |
| AUD-21 | Test-06 | `Follow-up.md` | medium | Follow-up may be read as auto-effectiveness / ownership | Clarify implementation≠OE; IA does not own controls | general-professional | none | Patched | pass |
| AUD-22 | All | `00-Start/*Map*`, `Internal-Audit-Onboarding-Path.md`, Home | medium | No audit methodology navigation | Create maps + home links + onboarding path | derived | none | Created; Home updated | pass |
| AUD-23 | Test-03/04 | `Analytics.md` | low | “Data Analysis” not aliased | Alias Data Analysis | general-professional | none | Alias added | pass |

## Issues deferred (unresolved)

| ID | Severity | Problem | Why deferred |
|---|---|---|---|
| AUD-D1 | low | No per-case public follow-up report notes | No official follow-up sources catalogued in vault for these engagements |
| AUD-D2 | low | Procedure notes are thin stubs, not full programs | Intentional; avoid inventing CRA audit manuals |
| AUD-D3 | low | Evidence hierarchy is teaching scale, not official CRA policy | Explicitly labelled; do not promote as CRA requirement |
| AUD-D4 | medium | Diagnostic tests not re-run | Per instructions: do not rerun diagnostics yet |

## Notes on content classes

- New methodology stubs: **general-professional-knowledge** unless marked derived (maps, historical primer, AERB clarification).
- Public case updates: **framing only** (historical warning + follow-up unknown). Published findings/recommendations/dates/MAP commitments were not altered.
- No synthetic demo content used to support public CRA claims.

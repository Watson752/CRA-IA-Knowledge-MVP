---
title: "Integrated Repair Register"
note_type: testing
primary_domain: governance
domains:
  - testing
  - governance
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
  - integrated
  - repair-register
---

# Integrated Repair Register

Issues from `16-Testing/Integrated/Baseline/Test-01` through `Test-06`. Prioritized per integrated repair instructions. Actions recorded after targeted repairs (2026-07-26).

| Issue ID | Originating test | Affected files | Affected domains | Severity | Problem | Proposed correction | Content class | Official source required | Action taken | Validation result |
|---|---|---|---|---|---|---|---|---|---|---|
| INT-01 | Test-06 | `15-Governance/` | ai, audit, governance | high | No single grounded-inquiry policy for AI/Cursor answers | Create Grounded-Audit-Inquiry-Guidelines | derived | no | Created `15-Governance/Grounded-Audit-Inquiry-Guidelines.md` | pass |
| INT-02 | Test-06 | `00-Start/`, bridges | retrieval, audit | high | Risk indicators can be misread as findings; no composite inquiry path | Cross-Domain Audit Map + Technology-Enabled Process Audit Path + bridge | derived | no | Created map + path + inquiry bridge links | pass |
| INT-03 | Test-01, Test-06 | `13-Bridge-Notes/` | software, audit, control | high | Missing bridge notes for automated controls / overrides / logging / pipelines | Create required bridge set with content-class labels | derived | no | Created 11 new bridges; improved Missing Data bridge links | pass |
| INT-04 | Test-05, Test-06 | `13-Bridge-Notes/`, `04-Audit-Concepts/` | case, audit | high | Historical findings / public cases not linked into scoping & precedent bridges | Bridges for public-case scoping and historical precedent | derived | no | Created both bridges; link Interpreting Historical Findings | pass |
| INT-05 | Test-01, Test-03, Test-04 | `07-Risk-Controls/Business Process Owner.md`, Control Ownership, Data Owner | organization, control | medium | BPO/control/data owners not chained to rules, overrides, access, reporting | Add Related links + short accountability sentences | general-professional | no | Updated BPO, Control Ownership, Data Owner, Unclear Accountability | pass |
| INT-06 | Test-02 | `05-Software-Concepts/` | software, control, audit | medium | Missing [[Management Review]] breaks reporting reliance path | Create Management Review note; link Management Reporting + pipeline map | general-professional | no | Created + linked | pass |
| INT-07 | Test-01 | `00-Start/Automated Controls Map.md` | software, audit | medium | Map starts at criteria, ends at Evidence—not BPO→Finding | Extend map chain | derived | no | Updated map chain | pass |
| INT-08 | Test-02 | `00-Start/Data Pipeline and Reporting Map.md` | software, data | medium | Map omits BPO start and Management Review | Extend map | derived | no | Updated map | pass |
| INT-09 | Test-03 | `00-Start/Identity and Access Map.md`, Periodic Access Review, Access Review Testing | software, audit | medium | Map omits BPO; sign-off ≠ meaningful review understated | Extend map; clarify OE sentences | general-professional / derived | no | Updated map + PAR + ART notes | pass |
| INT-10 | Test-03 | `05-Software-Concepts/` | software, control | medium | No Joiner–Mover–Leaver note | Thin JML note | general-professional | no | Created `Joiner-Mover-Leaver.md` | pass |
| INT-11 | Test-01 | `06-Data-Statistics-Concepts/` | statistics, software | medium | Override frequency/concentration analytics playbook thin | Thin Override Population Analytics note | general-professional | no | Created note; linked from Unmonitored Manual Overrides | pass |
| INT-12 | Test-01 | `07-Risk-Controls/` | business, risk | low | Business consequences of eligibility decisions thin | Thin Eligibility Decision Risks note (general/synthetic) | general-professional | no | Created stub | pass |
| INT-13 | Test-05 | `06-Data-Statistics-Concepts/Data Quality.md` | data, case | medium | related_cases empty | Populate bounded case links | derived links to official cases | no (cases already sourced) | Updated Data Quality related_cases + Related | pass |
| INT-14 | Test-04 | `07-Risk-Controls/Unclear Accountability.md`, Ownership note | organization | medium | Unclear Accountability not linked to branches; ARNI vignette thin | Link branches (labeled); add ARNI vignette to Ownership note | derived / case-specific | case notes only | Updated both | pass |
| INT-15 | Test-02 | `05-Software-Concepts/Identity and Access Management.md` | software | low | No “Access Controls” retrieval alias | Add alias Access Controls | general-professional | no | Alias added on IAM | pass |
| INT-16 | Test-01–06 | `00-Start/` maps & paths | retrieval, onboarding | high | Missing Integrated Knowledge Map and guided role paths | Create maps/paths + demo walkthrough + AI retrieval demo | derived | no | Created 8 navigation/onboarding notes; Home index updated | pass |
| INT-17 | Test-06 | `04-Audit-Concepts/` | audit | medium | Inquiry path (indicator→procedure) not first-class beside finding lifecycle | Cross-Domain Audit Map documents both chains; link Finding/Objective | derived | no | Map created; Objective/Finding Related links updated | pass |
| INT-18 | All | cases / concepts | case connectivity | medium | Data Quality / performance weakly bidirectional to cases | Add concept↔case Related links where thematic (not graph spam) | derived adjacency | no | Data Quality, Management Reporting, bridges updated; cases already name orgs | pass |
| INT-19 | Test-01–06 | n/a | source discipline | critical | Risk of unsupported CRA claims / current-state inference | Guidelines + bridges reinforce period-bound precedent rules | derived | n/a | No unsupported CRA claims added; guidelines require inquiry≠finding | pass |
| INT-20 | Test-02 | software→business | software, business | medium | Software notes sometimes thin on business consequence | Bridges + Eligibility Decision Risks + Management Review path | derived / general | no | Bridges and stubs added | pass |
| INT-21 | Test-01, Test-05 | statistics→conclusion | statistics, audit | medium | Statistical limits not always surfaced in retrieval paths | Bias bridge + Integrated/Cross-Domain maps point to conclusion notes | derived | no | How Statistical Bias bridge + maps | pass |

## Priority summary

1. **Critical/high:** INT-19, INT-01, INT-02, INT-03, INT-04, INT-16  
2. **Medium:** INT-05–INT-14, INT-17–INT-18, INT-20–INT-21  
3. **Low:** INT-12, INT-15  

## Explicitly not done (remain residual)

| Residual | Reason |
|---|---|
| Deep reject-aging / mapping reperformance workbooks | Out of scope; teaching stubs sufficient |
| Dedicated break-glass procedure manual | Not required for integrated coherence |
| Invented enterprise CAB / CRA IAM products | Forbidden |
| Rerun of Integrated Baseline tests | Instruction: do not rerun tests during repairs |
| Populate every case frontmatter related_* exhaustively | Avoid link spam; bidirectional where thematic |

---
title: Research Log
aliases:
  - RESEARCH LOG
note_type: governance
primary_domain: governance
domains:
  - governance
  - audit
  - source
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
approved_for_ai_retrieval: false
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
  - research
  - provenance
---

# RESEARCH LOG — CRA IA Knowledge MVP

Chronological log of source discovery, acceptance decisions, and vault notes. Not an official record.

---

## Session 1 — 2026-07-23

**Objective:** Establish MVP baseline from official CRA public web sources: current departmental plan, latest departmental results report, organizational overview pages, Internal Audit and Program Evaluation (IAPE) landing page, and five published internal audit reports (BI, cyber, charities, ARNI, EFMS).

**Vault access date used in frontmatter:** 2026-07-23

### Search terms used

| Query / approach | Intent |
|------------------|--------|
| `Canada Revenue Agency departmental plan 2026-27 site:canada.ca` | Current DP |
| `CRA departmental results report 2024-25 site:canada.ca` | Latest DRR in register set |
| `CRA ministerial transition 2025 organization site:canada.ca` | Public org overview |
| `CRA structure operational framework site:canada.ca` | Structure page |
| `CRA board of management site:canada.ca` | Governance |
| `CRA internal audit program evaluation site:canada.ca` | IAPE landing |
| `CRA internal audit business intelligence 2024 site:canada.ca` | BI audit report |
| `CRA internal audit cyber security controls 2023 site:canada.ca` | Cyber audit report |
| `CRA internal audit charities audit process 2025 site:canada.ca` | Charities report |
| `CRA internal audit accounts receivable national inventory site:canada.ca` | ARNI report |
| `CRA internal audit enterprise fraud management system site:canada.ca` | EFMS report |

### Sources accepted (registered)

All URLs recorded in [[99-Sources/CRA-Public-Source-Register]] with date accessed 2026-07-23 and status **current**:

1. 2026–27 CRA Departmental Plan  
2. 2024–25 CRA Departmental Results Report  
3. Organization (Ministerial Transition 2025)  
4. Structure and operational framework  
5. Board of Management  
6. Internal Audit and Program Evaluation (landing)  
7. Internal Audit – Oversight, Use, and Continuous Improvement of Business Intelligence (2024-06-18)  
8. Internal Audit – Specific Cyber Security Controls (2023-03)  
9. Internal Audit – Charities Audit Process (2025)  
10. Internal Audit – Accounts Receivable National Inventory (2026-05-14)  
11. Internal Audit – Enterprise Fraud Management System (2026-01-23)  

### Sources rejected or deferred

| Source type | Reason |
|-------------|--------|
| InfoZone, SharePoint, internal CRA URLs | Employment-only; prohibited by [[00-Start/Public-Sources-Only-Notice]] and [[PROJECT_PLAN]] |
| Unofficial third-party summaries of audit findings | Not authoritative; use CRA report URLs only |
| News articles without primary report link | Deferred unless needed for context; not registered in Session 1 |
| CRA public statistical publication | **Not yet selected** — required by project plan; next research task |
| Treasury Board / OCG audit guidance | **Not yet selected** — baseline requirement; next research task |
| Social media or wiki mirrors of CRA content | Rejected; link to canada.ca only |

### Notes created (Session 1)

| Path | Type | Status |
|------|------|--------|
| [[00-Start/Home]] | Navigation hub | Created |
| [[00-Start/Public-Sources-Only-Notice]] | Governance notice | Created |
| [[00-Start/CRA-Public-Knowledge-Map]] | Domain map | Created |
| [[00-Start/Public-Audit-Case-Library]] | Case index | Created |
| [[00-Start/CRA-Organization-Map]] | Org map | Created |
| [[00-Start/CRA-Data-and-Statistics-Map]] | Statistics map | Created |
| [[00-Start/CRA-Technology-and-Risk-Map]] | Technology/risk map | Created |
| [[15-Governance/Public-Source-RAG-Grounding]] | RAG rules | Created |
| [[15-Governance/Content-Classification-Model]] | Classes A–D | Created |
| [[99-Sources/CRA-Public-Source-Register]] | Source register | Created |
| `RESEARCH_LOG.md` | This log | Created |

### Placeholders planned (not yet authored)

- `08-Cases/*` — five case study notes linked from [[00-Start/Public-Audit-Case-Library]]  
- `02-Strategy-Performance/*` — DP 2026–27 and DRR 2024–25 summaries  
- `01-Organization/*` — org, board, IAPE entity notes  
- `12-Learning-Paths/Journey-1-*`, `Journey-2-*`, `Journey-3-*` — learning paths  
- CRA public statistics source note + register row  
- Treasury Board / OCG source + register row  

### Session 1 observations

- IA report index pages group reports by calendar year (2023, 2024, 2025, 2026); register uses individual report URLs.  
- Report publication dates vary in granularity (month vs day); register reflects dates as shown on canada.ca listing or report header where known.  
- No taxpayer-level data encountered in accepted sources.  

---

## Session 2 — 2026-07-23 (statistics + TBS)

**Objective:** Register CRA public statistical publication and Treasury Board / OCG internal-audit policy sources; create Class A statistics notes.

**Search terms:** `Individual Income Tax Return Statistics` / `T1 Final Statistics` site:canada.ca; `Policy on Internal Audit` site:tbs-sct.canada.ca; TBS Internal Audit landing page.

**Sources accepted:**

- Individual Income Tax Return Statistics (2023 tax year) — cut-off 2024-11-30; suppression/rounding documented
- T1 statistics landing page
- Open Government dataset for 2023 tax year
- TBS Internal Audit page
- Policy on Internal Audit (effective 2023-06-15) — https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=16484&section=html

**Sources rejected:** Wikipedia; commercial blogs; InfoZone.

**Notes created:** `03-Statistics/*`, source notes for T1 and TBS policy/page.

---

## Session 3 — 2026-07-23 (cases + Journey 3 substitute + validation)

**Objective:** Complete ≥5 published audit case studies; resolve Journey 3 reporting case; validate URLs/Wikilinks; produce VALIDATION_REPORT and MVP_REPORT.

**Search terms:** `"Tax and Benefits Operations Results Information"` site:canada.ca; `"Financial Forecasting"` / `"Values and Ethics Framework"` internal audit CRA; Evaluation Audit Yield.

**Sources accepted:**

- Full HTML opened for BI (2024), Cyber (2023), Charities (2025), ARNI (2026), EFMS (2026), Evaluation – Audit Yield (2020)
- Audit Committee charter page (register)

**Sources rejected / not found:**

| Candidate | Reason |
|-----------|--------|
| Internal Audit – Tax and Benefits Operations Results Information | Mentioned as *underway* in 2018 Taxpayer Relief IA; **no final published report located** on Canada.ca (2026-07-23). Substituted [[Evaluation - Audit Yield]] for Journey 3 and documented limitation. |
| Wikipedia / third-party org charts | Rejected per source policy |

**Notes created:** six case studies; learning paths; BI bridge; synthetic demo; VALIDATION_REPORT; MVP_REPORT; map fixes for Wikilinks.

**Questions remaining:**

- Were BI management actions (Dec 2024 / Mar–Jun 2025) completed? Needs later public follow-up sources.
- Are there newer service-standard result pages to link for performance learning?

---

## Session 4 — 2026-07-25 (organizational onboarding layer)

**Objective:** Expand the vault with a source-grounded CRA organizational structure and acronym onboarding layer under `02-Organization/`, without broadly rewriting existing notes.

**Search terms / pages prioritized:**

| Query / page | Intent |
|---|---|
| Ministerial Transition 2025 Organization | Current public HQ branches, mandates, regions, governance |
| CRA Commissioners page | Current Commissioner / Deputy incumbents |
| Minister Champagne page | Current Minister of Finance and National Revenue |
| ATIP Annual Report 2024–25 | Corroborate 14-branch / 4-region list |
| FSDA Agency Activities 2023–24 | AERB acronym attestation |
| Internal Audit of ERM (2014) | Historical AERB formation / acronym |

**Sources accepted (structure):**

- Organization — Ministerial Transition 2025 (page details **2025-09-09**) — **current for branch structure and mandates**; possibly outdated for some incumbents
- Commissioners page (page details **2026-07-23**) — **current for Commissioner/Deputy**
- Minister page for François-Philippe Champagne — **current for minister responsible for CRA**
- ATIP Annual Report 2024–25 — corroborates 14 functional branches + 4 regions

**Conflicts documented:**

| Topic | Conflict | Resolution |
|---|---|---|
| Commissioner | 2025 transition page lists Bob Hamilton; Commissioners page (2026-07-23) lists Heather Evans (effective 2026-07-13) after Fortin acting period | Prefer Commissioners page for incumbents |
| HQ branch count | 2021 transition materials list 13 branches; 2025 materials list 14 | Prefer 2025 structure |

**Notes created:** `02-Organization/**` overview/index notes; 14 canonical branch notes; 4 region notes; role notes; acronym dictionary; relationship map; historical Domestic Compliance Programs Branch note; `Organizational-Onboarding-Path`; `ORGANIZATION_VALIDATION_REPORT`.

**Notes updated (targeted):** `00-Start/CRA-Organization-Map`, Home, selected `01-Organization/*` governance/branch pointers, public audit case organizational connections, Learning Path - New Intern, Board/Audit Committee links.

**Rejected:** InfoZone/internal org charts; inventing acronyms not supported publicly; assuming succession from historical branch names without official evidence.

---

## Session template (future)

**Date:**  
**Objective:**  
**Search terms:**  
**Accepted / rejected:**  
**Notes created / updated:**  

---
title: Organizational Repair Register
aliases:
  - Repair Register
note_type: testing
primary_domain: organization-business
domains:
  - organization
  - testing
classification: public
content_origin: derived-analysis
authoritative: false
as_of_date: 2026-07-25
last_verified: 2026-07-25
source_status: diagnostic
review_status: analytical-draft
approved_for_ai_retrieval: false
tags:
  - testing
  - repair
  - organization
---

# Organizational Repair Register

Repairs driven by [[16-Testing/Baseline/Test-01-Acronym-Lookup]] through [[16-Testing/Baseline/Test-06-Historical-Accuracy]]. Final validation: [[Post-Fix Validation (Organizational Repairs)]].

| Issue ID | Originating test | Affected files | Issue type | Severity | Proposed correction | Source required | Action taken | Validation result |
|---|---|---|---|---|---|---|---|---|
| ORG-01 | Test-01 | `01-Organization/Service Innovation and Integration Branch.md` | incorrect acronym / alias collision | **critical** | Remove `SIIB` alias from legacy note | Canonical SIIB note | Converted to legacy redirect; no `SIIB` alias | **Pass** — SIIB alias only on canonical |
| ORG-02 | Test-01 | Eight `01-Organization/*Branch*` files | duplicate canonical / title collision | **high** | Retitle as legacy redirects; strip competing aliases | Canonical branch notes | All eight converted to thin redirects | **Pass** — titles no longer collide |
| ORG-03 | Test-01 | Learning paths; acronym dictionary | unclear onboarding / ABS caution | **medium** | Keep ABS verification-required visible | Dictionary ABS row | Dictionary navigation + Yield ABS caution on data path | **Pass** |
| ORG-04 | Test-02 | Overview; Onboarding Path | unclear onboarding | **high** | Three-buckets callout + no reporting lines | SRC-CRA-Org-2025 | Added to Overview and Onboarding Path | **Pass** |
| ORG-05 | Test-02 | DTPB canonical note | unclear onboarding | **medium** | Corporate-despite-Program caution | SRC-CRA-Org-2025 | Beginner caution added | **Pass** |
| ORG-06 | Test-02 | Program Branches; Regions | unclear onboarding | **medium** | HQ support / region delivery pair | SRC-CRA-Org-2025 | Paired wording added | **Pass** |
| ORG-07 | Test-03 | New hybrid learning path | missing onboarding path | **high** | Create IA+software+data path | Derived + org/case notes | Created [[Learning Path - Internal Audit Software and Data]] | **Pass** |
| ORG-08 | Test-03 | Software/Data paths; Onboarding Path | missing cross-domain links | **medium** | Wikilink branches/CDO; profile callout | Branch notes | Links + profile shortcut added | **Pass** |
| ORG-09 | Test-04 | Cyber, EFMS, ARNI, Charities | missing bidirectional / source links | **high** | Add related_organizations + related_sources | Case SRC notes | Frontmatter aligned to labeled org sections | **Pass** — 6/6 cases |
| ORG-10 | Test-04 | Public-Audit-Case-Library | broken/misleading org link | **high** | Point to canonical AERB | Canonical AERB | Updated related_organizations | **Pass** |
| ORG-11 | Test-04 | ITB branch note | unsupported / overstated relationship | **critical** | Qualify cyber; no ITB MAP | Cyber case | Body caution; removed from related_cases | **Pass** |
| ORG-12 | Test-04 | AERB branch note | incomplete case listing prose | **medium** | List all six publishing relationships | Case library | Expanded related-cases section | **Pass** |
| ORG-13 | Test-04 | Public-Audit-Case-Map (new) | navigation | **medium** | Branch×case matrix | Case org sections | Created [[Public-Audit-Case-Map]] | **Pass** |
| ORG-14 | Test-05 | Ownership notes + primer | missing concept nodes | **high** | Create owner/assurance notes + primer; Scope OPI | General professional + labelled CRA/case facts | Created primer + 8 role notes; Scope OPI; Control Ownership links | **Pass** |
| ORG-15 | Test-05 | ITB; CDO; Control Ownership | missing cross-links | **medium** | Ownership sentences + examples | Existing notes | ITB caution; CDO→SIIB; Control Ownership related | **Pass** |
| ORG-16 | Test-06 | SRC Commissioners/Minister; register | missing source links | **high** | Add SRC notes; wire register | Existing URLs in vault | Created SRC notes; register cells filled | **Pass** |
| ORG-17 | Test-06 | SRC-CRA-Org-2025 | historical as current | **high** | Soften source_status | Existing reliability notes | `current-structure-historical-incumbents` | **Pass** |
| ORG-18 | Test-06 | Legacy branch leadership lines | historical as current | **high** | Historical-only framing / redirects | Canonical office-holder rule | Redirect stubs remove “Named leadership as current” | **Pass** |
| ORG-19 | Test-06 | Commissioner/Deputy/Minister aliases | role/person conflation | **medium** | Remove person-name aliases | Role/person rule | Person aliases removed | **Pass** |
| ORG-20 | Test-02/06 | Maps, dictionary, Home | navigation | **medium** | Acronym→branch→mandate→concepts→case→source | Org layer | Path added across Overview, Map, Dictionary, Home | **Pass** |

## Deferred (documented, not defects of this pass)

| Item | Severity | Reason |
|---|---|---|
| Current AC/DAC/RAC names | — | Correctly unknown until newer official pages exist in vault |
| Newer full org chart | — | No newer complete chart SRC available |
| Re-run Tests 01–06 | — | Explicitly deferred per repair instructions |

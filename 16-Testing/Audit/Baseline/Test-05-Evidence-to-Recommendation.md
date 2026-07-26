---
title: "Test-05: Evidence to Recommendation"
note_type: testing
primary_domain: audit
domains:
  - audit
  - risk
  - control
  - case
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
  - baseline
  - audit
  - onboarding
  - finding
  - recommendation
  - evidence
---

# Test-05: Evidence to Recommendation

## Question

How does an auditor move from collected evidence to a defensible finding, root cause and recommendation?

## Answer

A defensible finding is not an opinion formed first and then “supported” later. The vault’s concept notes describe a forward chain: define what is being examined and against what standard, gather and analyze [[Evidence]], compare the observed **condition** to [[Criteria]], elevate only significant gaps to a [[Finding]], analyze **cause** where supported, state **effect**/[[Risk]], advise via [[Recommendation]], then leave corrective action to management ([[Management Response]], [[Management Action Plan]]) while Internal Audit may later [[Follow-up|follow up]].

| Content class | Role |
|---|---|
| **General professional** | [[Audit Objective]], [[Scope]], [[Criteria]], [[Methodology]], [[Evidence]], [[Finding]], [[Recommendation]], [[Management Response]], [[Management Action Plan]], [[Follow-up]], [[Internal Audit Independence]] |
| **Official public-source** | Published objective/scope/criteria/methods/findings/recommendations/MAP language in the BI case |
| **Vault-derived** | The end-to-end sequence diagram and the teaching application of “condition–criteria–cause–effect” labels onto paraphrased BI finding text (the public report does not always use those four labels explicitly) |

### Rules the vault supports

- **Evidence must support the condition** — findings are fact-based and supported by [[Evidence]] ([[Finding]]).
- **Criteria establish the expected state** — without criteria, conditions cannot be consistently judged as deficiencies ([[Criteria]]).
- **Root cause requires analysis, not speculation** — cause is included “when known” / “where practicable” ([[Finding]], [[Criteria]]); recommendations should link to root cause rather than symptoms ([[Recommendation]]). The vault has **no** [[Root Cause Analysis]] note and no explicit “do not invent causes” rule beyond “when known.”
- **Recommendations address causes or material risks** — address finding, reduce risk, or strengthen controls; avoid vague outcome-only wording ([[Recommendation]]).
- **Management owns corrective action** — recommendations are advisory; MAP execution is management’s ([[Recommendation]], [[Management Action Plan]], [[Management Action Plan Owner]], [[Internal Audit Independence]]).
- **Internal Audit later assesses implementation where applicable** — [[Follow-up]] verifies agreed actions and residual risk reduction; AERB judged BI action plans reasonable (case-specific official fact), which is not the same as owning execution.

**Missing sought notes:** no dedicated **Professional Judgment**, **Reasonable Assurance**, or **Root Cause Analysis** notes. “Reasonable assurance” appears inside [[Audit Objective]] / [[Control]]; “professional judgment” appears lightly in [[Evidence-Based Decision-Making]].

---

## Complete audit reasoning chain

```text
Audit objective and scope
→ criteria
→ audit procedures (methodology)
→ evidence
→ analysis
→ observed condition
→ comparison with criteria
→ finding
→ root cause (when supported)
→ consequence or risk (effect)
→ recommendation
→ management response and action plan
→ follow-up
```

| Step | What it does | Vault anchors |
|---|---|---|
| Objective & scope | What to determine; boundaries/exclusions | [[Audit Objective]], [[Scope]] |
| Criteria | Expected state / benchmarks | [[Criteria]] |
| Procedures | How evidence will be obtained | [[Methodology]], [[Control]] test methods |
| Evidence | Sufficient, appropriate, reliable information | [[Evidence]], [[Evidence Reliability]] |
| Analysis | Evaluate evidence against criteria (often implicit in vault) | [[Methodology]] (“analysis”); no Analysis note |
| Condition | What was observed | [[Finding]] |
| Comparison | Condition vs criteria → gap or not | [[Criteria]], [[Finding]] |
| Finding | Significant, reportable issue | [[Finding]] (not every observation) |
| Root cause | Why, when known—not assumed | [[Finding]], [[Recommendation]], [[Risk]] |
| Consequence / risk | Effect or residual risk | [[Finding]], [[Risk]] |
| Recommendation | Specific actions addressing cause/risk | [[Recommendation]] |
| Response & MAP | Management commits; owns execution | [[Management Response]], [[Management Action Plan]] |
| Follow-up | IA assesses implementation / residual risk | [[Follow-up]] |

Learning-path echoes (derived navigation): [[Learning Path - New Intern]] and [[Learning Path - Auditor]] sequence finding → recommendation → response → MAP → follow-up, but both under-specify the evidence → condition → criteria comparison step.

---

## Case used — complete public path

**Case:** [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]]  
**Source:** [[99-Sources/source-notes/SRC-CRA-IA-BI-2024]]

Apply one published thread—**tool acquisition vs tool deployment**—without inventing undisclosed causes or current-state claims.

| Chain step | Published / vault-supported content | Class |
|---|---|---|
| Objective | Assurance that BI is overseen, used, and continuously improved for compliance, collections, and verification | Official |
| Scope | In: governance, uses, continuous improvement. Out: data security; HR; apps/tools/infrastructure lifecycle | Official |
| Criteria | Management control framework for BI, including oversight process for enterprise-view **tool acquisition** aligned with the Information and Data Strategy, and structure fostering continuous improvement | Official |
| Procedures | Document review; process review of selected CPB/CVB teams; interviews; observation of governance meetings | Official |
| Evidence (types used) | Governance records, strategies/policies, interview/observation evidence (public methodology—not working papers) | Official (methods only) |
| Condition (finding 5) | Oversight body/process exists for enterprise view when **acquiring** tools, but **no formal process** supported effective and timely **deployment** to BI teams Agency-wide | Official (paraphrased in case note) |
| Comparison with criteria | Acquisition oversight aligns with part of criteria; absence of formal Agency-wide deployment process is a gap relative to an effective framework for use of BI tools | Vault-derived labeling of the published contrast |
| Finding | Elevated as a published finding theme (tool deployment) | Official |
| Root cause | **Not explicitly labeled** as “root cause” in the public summary. Supported statement stops at the observed process gap. Do **not** invent deeper causes (e.g., funding, culture) | Discipline: unsupported causal claims avoided |
| Consequence / risk | Implied risk: tools acquired under oversight may not reach BI teams timely/effectively, weakening BI use/continuous improvement objectives | Vault-derived risk framing from objective + finding; not a separate published “effect” paragraph |
| Recommendation | Develop an effective deployment process for timely delivery of BI tools (SIIB with ITB/stakeholders) | Official |
| Management response / MAP | SIIB agrees; AERB judged plans reasonable; by **December 2024** review last BI tool deployment and identify steps for a new formal process | Official |
| Follow-up | Conceptually [[Follow-up]]; this case note does not publish a later follow-up report outcome | General professional + case silence |

**Why this path is defensible in the vault:** condition is contrastive and report-supported; criteria mention acquisition oversight; recommendation addresses the missing **deployment process** (cause-level process gap), not merely “improve BI outcomes”; SIIB owns MAP execution while AERB remains assurance.

Other complete-ish public paths: [[Internal Audit - Accounts Receivable National Inventory]], [[Internal Audit - Enterprise Fraud Management System]], [[Internal Audit - Charities Audit Process]].  
**Not suitable for full finding traceability:** [[Internal Audit - Specific Cyber Security Controls]] (protected finding detail).

---

## Notes and sources used

### Concept notes

- [[Audit Objective]] · [[Scope]] · [[Criteria]] · [[Methodology]]
- [[Evidence]] · [[Evidence Reliability]]
- [[Finding]] · [[Recommendation]]
- [[Management Response]] · [[Management Action Plan]] · [[Management Action Plan Owner]]
- [[Follow-up]] · [[Internal Audit Independence]]
- [[Risk]] · [[Control]] · [[Control Ownership]]
- [[Tool Acquisition]] · [[Tool Deployment]]
- [[Evidence-Based Decision-Making]] (judgment mention only)

### Navigation

- [[Learning Path - Auditor]]
- [[Learning Path - New Intern]]
- [[Public-Audit-Case-Library]]
- [[Content Classification Model]]

### Case / source

- [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]]
- [[99-Sources/source-notes/SRC-CRA-IA-BI-2024]]

### Searched; not found as dedicated notes

| Sought | Result |
|---|---|
| Audit Evidence (title) | [[Evidence]] |
| Audit Criteria (title) | [[Criteria]] |
| Audit Finding (title) | [[Finding]] |
| Root Cause Analysis | Phrases only |
| Professional Judgment | No note |
| Reasonable Assurance | Embedded phrase only |

---

## Diagnostic evaluation

| Check | Finding |
|---|---|
| Conclusion before evidence? | **Not taught that way.** [[Finding]] requires evidence support; [[Methodology]] places analysis with fieldwork/reporting. Risk is learner-side if they skip case methodology sections. |
| Symptom mistaken for root cause? | **Partially guarded.** [[Recommendation]] says link to root cause not symptoms; [[Finding]] says cause “when known.” No RCA method note. |
| Recommendation merely repeats desired outcome? | **Concept note warns against vagueness** and gives measurable example. BI deployment recommendation names a process, not only “better BI.” |
| Management vs IA roles confused? | **No.** Independence/MAP owner/follow-up keep execution with management. |
| Every public finding traceable to its report? | **Yes when disclosed** (BI, ARNI, EFMS, Charities, Audit Yield). **No for protected cyber findings**—vault correctly refuses reconstruction. |

### Score

| Criterion | Score (0–2) | Rationale |
|---|---:|---|
| Logical progression | **1** | End-to-end chain can be assembled from notes and learning paths, but analysis/RCA/judgment/assurance nodes are thin or missing. |
| Criteria-and-evidence comparison | **2** | [[Criteria]] and [[Finding]] explicitly require comparing condition to criteria with evidence support. |
| Root-cause discipline | **1** | “When known” / “not symptoms” present; no Root Cause Analysis note; public cases often omit labeled causes. |
| Recommendation quality | **2** | Strong Class C guidance; BI recommendations map to finding themes and name owners/collaborators. |
| Public-case traceability | **2** | BI case supports a full published path from objective through MAP; protected cases show appropriate limits. |
| **Total** | **8 / 10** | |

---

## Reasoning gaps

1. No single primer note that prints the full objective→follow-up chain with content-class labels.
2. **Analysis** step is named in [[Methodology]] but not taught as “evaluate evidence against criteria before drafting findings.”
3. **Root Cause Analysis** absent—learners may treat observed symptoms (e.g., “silos”) as causes without method.
4. **Professional Judgment** and **Reasonable Assurance** not first-class—harder to explain why two auditors may scope findings differently under the same criteria.
5. Learning paths jump from methodology to finding, under-emphasizing condition↔criteria comparison.
6. Public reports (and case paraphrases) rarely label condition/criteria/cause/effect explicitly—learners must map them.

---

## Unsupported causal claims

Do **not** claim from the vault:

- Deep root causes for BI gaps beyond what the report states (budget cuts, individual blame, undocumented culture theories)
- That AERB’s judgment that MAPs were “reasonable” proves remediation completed
- That protected cyber findings’ causes or conditions can be inferred
- That every published finding includes a labeled root-cause section
- That follow-up outcomes for the BI December 2024 deployment action are recorded in this vault

This diagnostic does **not** invent a root cause for the BI deployment finding beyond the report-supported process gap (acquisition oversight without formal Agency-wide deployment process).

---

## Missing links

| Gap | Why it matters |
|---|---|
| Root Cause Analysis note | Discipline against speculation |
| Professional Judgment note | Explains elevation, aggregation, and wording choices |
| Reasonable Assurance note | Frames what findings do / do not prove |
| Analysis / Evidence Evaluation stub | Makes criteria comparison an explicit step |
| Case backlinks from [[Finding]] / [[Recommendation]] | Discovery of BI worked example |
| Explicit “evidence → condition → criteria → finding” line on [[Learning Path - Auditor]] | Onboarding usability |

---

## Targeted recommendations

Do **not** implement in this test. Suggested later work:

1. Create a derived onboarding MOC **From Evidence to MAP** embedding the sequence and the BI tool-deployment worked example.
2. Add Class C stubs: **Root Cause Analysis**, **Professional Judgment**, **Reasonable Assurance**.
3. Expand [[Finding]] with a one-line workflow: Evidence → Condition → Criteria comparison → Finding (cause/effect when supported) → Recommendation.
4. Update [[Learning Path - Auditor]] step 2 to include Evidence → Condition ↔ Criteria before Finding.
5. Link [[Finding]] and [[Recommendation]] to [[Internal Audit - Oversight Use and Continuous Improvement of Business Intelligence]].
6. Add a teaching callout: if the public report does not state a cause, label cause as unknown rather than inventing one.

---

## Test metadata

- Test ID: Test-05-Evidence-to-Recommendation
- Suite: Audit Baseline onboarding diagnostics
- Output path: `16-Testing/Audit/Baseline/Test-05-Evidence-to-Recommendation.md`
- Vault notes modified by this test: **none** (output file created only)
- Process followed: searched evidence/criteria/finding/RCA/judgment/assurance/MAP notes and cases; applied full chain to BI tool-deployment path; avoided unsupported causal claims; did not implement recommendations

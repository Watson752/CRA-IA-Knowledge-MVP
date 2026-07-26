---
title: "Consistency Repair Register"
note_type: testing
primary_domain: governance
domains:
  - governance
classification: public
content_origin: derived-analysis
authoritative: false
official_source: false
review_status: analytical-draft
approved_for_ai_retrieval: false
---

# Consistency Repair Register

This register records bounded maintenance work. Published CRA report content, citations, audit periods, findings, recommendations, and management responses are out of scope unless a verified error is found.

| Issue ID | Issue type | Severity | Affected file(s) | Current condition | Proposed correction | Action taken | Validation result |
|---|---|---|---|---|---|---|---|
| CON-01 | stale validation report | high | `METADATA_VALIDATION_REPORT.md` | Reports 150 files and obsolete taxonomy counts | Rebuild from local validator | Rebuilt with calculated state and maintenance rules | Pass — validator is the authoritative detailed census |
| CON-02 | stale project documentation | high | `README.md` | Describes a planned `vault/`/`src/` layout rather than the live numbered vault | Replace only architecture/status/count sections with final state | Replaced project documentation with current vault architecture and validator command | Pass — no stale planned layout remains |
| CON-03 | empty duplicate/placeholder notes | high | root `CRA-Governance-Structure.md`, `Post-Fix Validation (Organizational Repairs).md`; `01-Organization/CRA-Overview-and-Mandate.md`; `09-Processes/Tax Administration.md` | Empty files duplicate or shadow substantive canonical notes | Preserve empty-file backup record, remove empty shadows, retain canonical notes | Recorded zero-byte originals and removed four empty shadows | Pass — no content was lost; substantive orphan count is 0 |
| CON-04 | duplicate canonical titles | high | legacy organization redirects; parallel analytics application notes | Legacy/parallel files duplicate canonical titles and make title-only links ambiguous | Retitle redirects or remove empty shadows; retain cited canonical notes | Renamed redirects/application notes and canonicalized links | Pass — validator reports 0 duplicate titles |
| CON-05 | invalid infrastructure domains | medium | `16-Testing/**` | Some testing notes use `primary_domain: testing`, outside target enum | Change testing infrastructure primary domain to `governance`; preserve topical `domains` only when valid | Replaced obsolete `testing` primary domain with `governance` | Pass — invalid primary-domain count is 0 |
| CON-06 | invalid domain tokens | medium | bridge-note metadata | `domains` contained non-taxonomy `bridge` tokens | Remove invalid tokens; retain meaningful allowed domain tags | Removed `bridge` from bridge-note domain lists | Pass — invalid substantive-domain count is 0 |
| CON-07 | ambiguous wikilinks | high | vault-wide links to duplicate titles and path-style aliases | Baseline validator identifies 345 unresolved/ambiguous links, predominantly duplicate-title ambiguity | Prefer canonical paths and repair verified broken path links; retain documented baseline diagnostics as historical evidence | Retargeted canonical branch links, repaired path/folder targets, added required Substantive Testing note, and disambiguated validation links | Pass — final unresolved/ambiguous count is 0 |
| CON-08 | substantive orphans | medium | root empty duplicate notes | Two detected substantive orphans are empty shadows rather than knowledge nodes | Remove with backup record; do not create graph-only links | Removed only the empty shadows; no graph-only links added | Pass — final substantive-orphan count is 0 |
| CON-09 | map reachability | medium | named MOCs and Home | Validate after canonical link repair; add only curated missing entry points | Validator graph was reviewed after canonical link repair | Existing curated MOCs already reach substantive content; no indiscriminate links added | Pass — no substantive orphan remains |

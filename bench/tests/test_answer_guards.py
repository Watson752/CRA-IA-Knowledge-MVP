"""Unit tests for Phase 2 answer filters and policy checks (no API calls)."""

from __future__ import annotations

from types import SimpleNamespace

from rag.answer import (
    answer_has_correction,
    check_answer_policy,
    filter_evidence,
    is_evidence_allowed,
    looks_like_factual_assertion,
)
from rag.retrieve import RetrievalResult


def _result(note_id: str, title: str = "Note") -> RetrievalResult:
    return RetrievalResult(
        rank=1,
        chunk_id=f"{note_id}#0",
        note_id=note_id,
        title=title,
        note_path=f"{note_id}.md",
        chunk_heading=title,
        primary_domain="audit",
        semantic_score=1.0,
        lexical_score=0.0,
        graph_contribution=0.0,
        domain_score=0.0,
        authoritative_score=0.0,
        final_score=1.0,
        source_urls=["https://example.com/report"],
    )


def test_is_evidence_allowed_blocks_synthetic():
    note = SimpleNamespace(
        classification="synthetic",
        content_origin="synthetic-demonstration",
        approved_for_ai_retrieval=True,
    )
    assert is_evidence_allowed(note) is False


def test_is_evidence_allowed_keeps_disapproved_concept_notes():
    # Vault marks most concept notes approved_for_ai_retrieval=false; still usable
    # for inquiry answers (not a hard gate).
    note = SimpleNamespace(
        classification="public",
        content_origin="general-professional-knowledge",
        approved_for_ai_retrieval=False,
    )
    assert is_evidence_allowed(note) is True


def test_is_evidence_allowed_keeps_missing_approved_flag():
    note = SimpleNamespace(
        classification="public",
        content_origin="official-public-source",
        approved_for_ai_retrieval=None,
    )
    assert is_evidence_allowed(note) is True


def test_filter_evidence_drops_synthetic_and_prefers_official(tmp_path=None):
    corpus = SimpleNamespace(
        knowledge_notes={
            "concept": SimpleNamespace(
                classification="public",
                content_origin="general-professional-knowledge",
                approved_for_ai_retrieval=False,
                authoritative=False,
            ),
            "official": SimpleNamespace(
                classification="public",
                content_origin="official-public-source",
                approved_for_ai_retrieval=True,
                authoritative=True,
            ),
            "bad": SimpleNamespace(
                classification="synthetic",
                content_origin="synthetic-demonstration",
                approved_for_ai_retrieval=True,
                authoritative=False,
            ),
        },
        source_notes={},
    )
    kept, dropped = filter_evidence(
        [_result("concept", "Concept"), _result("official", "Official"), _result("bad", "Bad")],
        corpus,  # type: ignore[arg-type]
    )
    assert [r.note_id for r in kept] == ["official", "concept"]
    assert dropped == 1


def test_check_answer_policy_missing_citation():
    warnings = check_answer_policy(
        "Auditors should examine ownership and monitoring.",
        ["Missing Data", "Evidence Reliability"],
        [],
        evidence_empty=False,
    )
    assert any(w.startswith("missing_citation") for w in warnings)


def test_check_answer_policy_forbidden_pattern():
    warnings = check_answer_policy(
        "This proves CRA currently fails access certifications.",
        ["Privileged Access"],
        [],
        evidence_empty=False,
    )
    assert any(w.startswith("forbidden_pattern") for w in warnings)


def test_check_answer_policy_accepts_title_citation():
    warnings = check_answer_policy(
        "According to Missing Data, incomplete populations weaken assurance.",
        ["Missing Data"],
        [],
        evidence_empty=False,
    )
    assert not any(w.startswith("missing_citation") for w in warnings)
    assert not any(w.startswith("forbidden_pattern") for w in warnings)


def test_looks_like_factual_assertion():
    assert looks_like_factual_assertion("EFMS found failed access certifications.")
    assert looks_like_factual_assertion("Prove CRA currently has uncontrolled overrides.")
    assert not looks_like_factual_assertion(
        "How should Internal Audit assess privileged access?"
    )


def test_answer_has_correction_detects_refusal():
    assert answer_has_correction(
        "Public sources do not support the claim that EFMS found failed access certifications."
    )
    assert answer_has_correction(
        'The user statement "EFMS found failed access certifications" is not directly supported.'
    )
    assert not answer_has_correction(
        "Risk indicator → EFMS found failed access certifications → investigate remediation."
    )

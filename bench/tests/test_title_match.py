"""Unit tests for title/alias match scoring."""

from rag.retrieve import title_match_score


def test_exact_title_containment():
    assert title_match_score(
        "How does Missing Data weaken an audit conclusion?",
        "Missing Data",
    ) == 1.0


def test_token_overlap_technology_branch():
    score = title_match_score(
        "Which CRA branches are most relevant to technology and Internal Audit?",
        "Information Technology Branch",
    )
    assert score >= 0.3


def test_alias_match():
    score = title_match_score(
        "Tell me about Incomplete Data gaps",
        "Missing Data",
        aliases=["Incomplete Data", "Data Gaps"],
    )
    assert score == 1.0


def test_unrelated_near_zero():
    score = title_match_score(
        "How does selection bias distort analysis?",
        "CRA Corporate Secretariat",
    )
    assert score < 0.2

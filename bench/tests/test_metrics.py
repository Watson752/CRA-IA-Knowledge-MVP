"""Unit tests for shared retrieval metrics (no model downloads)."""

from __future__ import annotations

from eval.metrics import hit_at_k, match_expected, mrr, normalize, recall_at_k


def test_normalize_hyphens_and_case():
    assert normalize("CRA-Program-Branches.md") == "cra program branches"
    assert normalize("Evidence Reliability") == "evidence reliability"


def test_match_expected_title_and_stem():
    hits = match_expected(
        ["Missing Data"],
        ["06-Data-Statistics-Concepts/Missing Data"],
        ["Missing Data", "Population Completeness"],
    )
    assert hits == [True, False]


def test_hit_at_k_and_mrr():
    ranks = [1, 3, None, 2]
    assert hit_at_k(ranks, 1) == 0.25
    assert hit_at_k(ranks, 3) == 0.75
    # MRR: 1/1 + 1/3 + 0 + 1/2 = 1.833... / 4
    assert abs(mrr(ranks) - (1 + 1 / 3 + 0.5) / 4) < 1e-9


def test_recall_at_k():
    flags = [
        [True, False, True],  # 2/3
        [True, True],  # 2/2
    ]
    assert abs(recall_at_k(flags) - ((2 / 3) + 1.0) / 2) < 1e-9


def test_empty_inputs():
    assert hit_at_k([], 1) == 0.0
    assert mrr([]) == 0.0
    assert recall_at_k([]) == 0.0

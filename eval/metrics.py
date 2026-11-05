"""Shared retrieval metric helpers used by eval and bench runners."""

from __future__ import annotations

from pathlib import Path


def normalize(value: str) -> str:
    text = value.strip().casefold().removesuffix(".md")
    text = text.replace("–", "-").replace("—", "-")
    text = text.replace("_", " ").replace("-", " ")
    return " ".join(text.split())


def match_expected(
    retrieved_titles: list[str],
    retrieved_ids: list[str],
    expected: list[str],
) -> list[bool]:
    title_set = {normalize(t) for t in retrieved_titles}
    id_set = {normalize(i) for i in retrieved_ids}
    id_stems = {normalize(Path(i).name) for i in retrieved_ids}
    hits: list[bool] = []
    for exp in expected:
        key = normalize(exp)
        hits.append(key in title_set or key in id_set or key in id_stems)
    return hits


def hit_at_k(ranks: list[int | None], k: int) -> float:
    if not ranks:
        return 0.0
    return sum(1 for r in ranks if r is not None and r <= k) / len(ranks)


def recall_at_k(k_retrieved_flags: list[list[bool]]) -> float:
    """Mean recall@k where each question's expected set is the denominator."""
    scores: list[float] = []
    for expected_hits in k_retrieved_flags:
        if not expected_hits:
            continue
        scores.append(sum(1 for h in expected_hits if h) / len(expected_hits))
    return sum(scores) / len(scores) if scores else 0.0


def mrr(ranks: list[int | None]) -> float:
    if not ranks:
        return 0.0
    total = 0.0
    for rank in ranks:
        if rank is None:
            continue
        total += 1.0 / rank
    return total / len(ranks)


# Back-compat aliases used by older call sites.
_normalize = normalize
_match_expected = match_expected

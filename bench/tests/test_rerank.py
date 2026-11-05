"""Unit tests for reranker wiring (no Hub downloads)."""

from __future__ import annotations

from dataclasses import dataclass, field

from rag.rerank import CrossEncoderReranker, NoOpReranker, get_reranker


@dataclass
class FakeResult:
    rank: int
    chunk_id: str
    note_id: str = "n"
    title: str = "t"
    note_path: str = "p"
    chunk_heading: str = "h"
    primary_domain: str | None = None
    semantic_score: float = 0.0
    lexical_score: float = 0.0
    graph_contribution: float = 0.0
    domain_score: float = 0.0
    authoritative_score: float = 0.0
    final_score: float = 0.0
    why_included: list[str] = field(default_factory=list)
    graph_path: list[str] | None = None
    inclusion_origin: str = "direct"
    text_preview: str = "preview"
    related_sources: list[str] = field(default_factory=list)
    source_urls: list[str] = field(default_factory=list)


class FakeCE:
    def predict(self, pairs):
        # Higher index => higher score so last candidate wins.
        return list(range(len(pairs)))


def test_noop_preserves_order():
    cands = [FakeResult(rank=i, chunk_id=f"c{i}", final_score=10 - i) for i in range(1, 4)]
    out = NoOpReranker().rerank("q", cands, top_k=2)
    assert [c.chunk_id for c in out] == ["c1", "c2"]
    assert [c.rank for c in out] == [1, 2]


def test_get_reranker_none():
    assert isinstance(get_reranker(None), NoOpReranker)
    assert isinstance(get_reranker(""), NoOpReranker)


def test_cross_encoder_rerank_with_fake_model():
    rr = object.__new__(CrossEncoderReranker)
    rr.name = "fake-reranker"
    rr._model = FakeCE()
    cands = [
        FakeResult(rank=1, chunk_id="a", text_preview="A"),
        FakeResult(rank=2, chunk_id="b", text_preview="B"),
        FakeResult(rank=3, chunk_id="c", text_preview="C"),
    ]
    out = CrossEncoderReranker.rerank(rr, "query", cands, top_k=2)
    assert [c.chunk_id for c in out] == ["c", "b"]
    assert out[0].rank == 1
    assert "cross-encoder rerank" in out[0].why_included

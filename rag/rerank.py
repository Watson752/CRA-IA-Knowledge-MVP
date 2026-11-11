"""Optional post-hybrid rerankers. Default is a no-op (Phase 1 behaviour)."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from rag.retrieve import RetrievalResult


class Reranker(ABC):
    """Rank a candidate list for a query; return a new top-k list."""

    name: str

    @abstractmethod
    def rerank(
        self,
        query: str,
        candidates: Sequence[RetrievalResult],
        *,
        top_k: int,
        texts: dict[str, str] | None = None,
    ) -> list[RetrievalResult]:
        """Return up to top_k results, re-ranked. Preserve explainability fields."""


class NoOpReranker(Reranker):
    """Identity reranker — preserves hybrid ranking order."""

    name = "none"

    def rerank(
        self,
        query: str,
        candidates: Sequence[RetrievalResult],
        *,
        top_k: int,
        texts: dict[str, str] | None = None,
    ) -> list[RetrievalResult]:
        out = list(candidates)[:top_k]
        for idx, result in enumerate(out, start=1):
            result.rank = idx
        return out


class CrossEncoderReranker(Reranker):
    """sentence-transformers CrossEncoder reranker (e.g. BAAI/bge-reranker-v2-m3)."""

    def __init__(self, model_name: str = "BAAI/bge-reranker-v2-m3") -> None:
        from sentence_transformers import CrossEncoder

        self.name = model_name
        self._model = CrossEncoder(model_name)

    def rerank(
        self,
        query: str,
        candidates: Sequence[RetrievalResult],
        *,
        top_k: int,
        texts: dict[str, str] | None = None,
    ) -> list[RetrievalResult]:
        if not candidates:
            return []
        texts = texts or {}
        pairs: list[list[str]] = []
        for cand in candidates:
            body = texts.get(cand.chunk_id) or cand.text_preview or cand.title
            pairs.append([query, body])
        scores = self._model.predict(pairs)
        scored = list(zip(candidates, scores))
        scored.sort(key=lambda item: float(item[1]), reverse=True)
        out: list[RetrievalResult] = []
        for idx, (cand, score) in enumerate(scored[:top_k], start=1):
            cand.rank = idx
            cand.final_score = float(score)
            if "cross-encoder rerank" not in cand.why_included:
                cand.why_included = list(cand.why_included) + ["cross-encoder rerank"]
            out.append(cand)
        return out


def get_reranker(model_name: str | None) -> Reranker:
    if not model_name:
        return NoOpReranker()
    return CrossEncoderReranker(model_name=model_name)

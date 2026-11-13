"""Optional post-hybrid rerankers. Default is a no-op (Phase 1 behaviour)."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from rag.retrieve import RetrievalResult

DEFAULT_CE_BLEND_ALPHA = 0.35


def _minmax(values: list[float]) -> list[float]:
    if not values:
        return []
    lo, hi = min(values), max(values)
    if hi <= lo:
        return [1.0 for _ in values]
    return [(v - lo) / (hi - lo) for v in values]


def _pair_text(cand: RetrievalResult, texts: dict[str, str] | None) -> str:
    """Prefer title-heavy text for CE pairs to reduce generic-passage bias."""
    title = (cand.title or "").strip()
    heading = (cand.chunk_heading or "").strip()
    preview = (cand.text_preview or "").strip()
    # Optional override still allowed, but truncated and title-prefixed.
    body = ""
    if texts and cand.chunk_id in texts:
        body = texts[cand.chunk_id].strip()
    parts = [title]
    if heading and heading.casefold() != title.casefold():
        parts.append(heading)
    snippet = preview or body
    if snippet:
        parts.append(snippet[:400])
    return "\n".join(p for p in parts if p)


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
    """sentence-transformers CrossEncoder reranker with hybrid score blending."""

    def __init__(
        self,
        model_name: str = "BAAI/bge-reranker-v2-m3",
        *,
        alpha: float = DEFAULT_CE_BLEND_ALPHA,
    ) -> None:
        from sentence_transformers import CrossEncoder

        self.name = model_name
        self.alpha = max(0.0, min(1.0, float(alpha)))
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
        pairs: list[list[str]] = []
        hybrid_scores: list[float] = []
        for cand in candidates:
            pairs.append([query, _pair_text(cand, texts)])
            hybrid_scores.append(float(cand.final_score))
        raw_ce = [float(s) for s in self._model.predict(pairs)]
        ce_norm = _minmax(raw_ce)
        hybrid_norm = _minmax(hybrid_scores)
        alpha = self.alpha
        blended: list[tuple[RetrievalResult, float]] = []
        for cand, h, c in zip(candidates, hybrid_norm, ce_norm):
            score = (1.0 - alpha) * h + alpha * c
            blended.append((cand, score))
        blended.sort(key=lambda item: item[1], reverse=True)
        out: list[RetrievalResult] = []
        why = f"cross-encoder blend α={alpha:.2f}"
        for idx, (cand, score) in enumerate(blended[:top_k], start=1):
            cand.rank = idx
            cand.final_score = float(score)
            if why not in cand.why_included and "cross-encoder rerank" not in cand.why_included:
                cand.why_included = list(cand.why_included) + [why]
            out.append(cand)
        return out


def get_reranker(model_name: str | None, *, alpha: float = DEFAULT_CE_BLEND_ALPHA) -> Reranker:
    if not model_name:
        return NoOpReranker()
    return CrossEncoderReranker(model_name=model_name, alpha=alpha)

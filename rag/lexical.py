"""Simple BM25 lexical retrieval over chunks."""

from __future__ import annotations

import json
import pickle
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from rank_bm25 import BM25Okapi

from rag.chunking import Chunk
from rag.corpus import DEFAULT_RAG_DATA

TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9'_-]*", flags=re.IGNORECASE)


def tokenize(text: str) -> list[str]:
    return [tok.casefold() for tok in TOKEN_RE.findall(text or "")]


@dataclass
class LexicalIndex:
    """In-memory BM25 index with durable pickle cache."""

    chunk_ids: list[str]
    corpus_tokens: list[list[str]]
    bm25: BM25Okapi

    @classmethod
    def build(cls, chunks: Sequence[Chunk]) -> LexicalIndex:
        corpus_tokens = [tokenize(chunk.embed_text) for chunk in chunks]
        # BM25Okapi requires a non-empty corpus; guard empty vaults.
        if not corpus_tokens:
            corpus_tokens = [[]]
            chunk_ids: list[str] = []
        else:
            chunk_ids = [c.chunk_id for c in chunks]
        bm25 = BM25Okapi(corpus_tokens)
        return cls(chunk_ids=chunk_ids, corpus_tokens=corpus_tokens, bm25=bm25)

    def search(self, query: str, top_k: int = 20) -> list[tuple[str, float]]:
        if not self.chunk_ids:
            return []
        tokens = tokenize(query)
        if not tokens:
            return []
        scores = self.bm25.get_scores(tokens)
        top_k = min(top_k, len(scores))
        idxs = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
        return [(self.chunk_ids[i], float(scores[i])) for i in idxs if scores[i] > 0]

    def save(self, out_dir: Path | None = None) -> Path:
        out_dir = out_dir or DEFAULT_RAG_DATA
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / "lexical_bm25.pkl"
        payload = {
            "chunk_ids": self.chunk_ids,
            "corpus_tokens": self.corpus_tokens,
        }
        path.write_bytes(pickle.dumps(payload, protocol=pickle.HIGHEST_PROTOCOL))
        meta = out_dir / "lexical_meta.json"
        meta.write_text(
            json.dumps({"chunk_count": len(self.chunk_ids), "backend": "bm25"}, indent=2) + "\n",
            encoding="utf-8",
        )
        return path

    @classmethod
    def load(cls, out_dir: Path | None = None) -> LexicalIndex:
        out_dir = out_dir or DEFAULT_RAG_DATA
        path = out_dir / "lexical_bm25.pkl"
        payload = pickle.loads(path.read_bytes())
        corpus_tokens = payload["corpus_tokens"] or [[]]
        return cls(
            chunk_ids=list(payload["chunk_ids"]),
            corpus_tokens=corpus_tokens,
            bm25=BM25Okapi(corpus_tokens),
        )


def ensure_lexical_index(
    chunks: Sequence[Chunk],
    out_dir: Path | None = None,
    *,
    rebuild: bool = False,
) -> LexicalIndex:
    out_dir = out_dir or DEFAULT_RAG_DATA
    path = out_dir / "lexical_bm25.pkl"
    if not rebuild and path.exists():
        index = LexicalIndex.load(out_dir)
        if index.chunk_ids == [c.chunk_id for c in chunks]:
            return index
    index = LexicalIndex.build(chunks)
    index.save(out_dir)
    return index

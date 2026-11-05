"""Local embedding providers and NumPy vector store."""

from __future__ import annotations

import json
import os
import re
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Sequence

import numpy as np

from rag.chunking import Chunk
from rag.corpus import DEFAULT_RAG_DATA

DEFAULT_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def sanitize_model_id(model_name: str) -> str:
    """Filesystem-safe id for per-model cache directories."""
    cleaned = model_name.strip().replace("\\", "/")
    cleaned = cleaned.replace("/", "__")
    cleaned = re.sub(r"[^A-Za-z0-9._+-]+", "_", cleaned)
    return cleaned or "model"


def cache_dir_for_model(model_id: str, root: Path | None = None) -> Path:
    """Return rag_data/models/<sanitized_id>/ for embedding caches."""
    base = root or DEFAULT_RAG_DATA
    return base / "models" / sanitize_model_id(model_id)


class EmbeddingProvider(ABC):
    """Small replaceable interface for embedding backends."""

    name: str

    @abstractmethod
    def embed(self, texts: Sequence[str], *, batch_size: int = 32) -> np.ndarray:
        """Return L2-normalized float32 matrix of shape (n, d)."""

    def embed_query(self, text: str) -> np.ndarray:
        return self.embed([text])[0]


class SentenceTransformerProvider(EmbeddingProvider):
    """SentenceTransformers backend suitable for English semantic retrieval."""

    def __init__(
        self,
        model_name: str = DEFAULT_MODEL_NAME,
        *,
        local_files_only: bool = False,
        query_prompt_name: str | None = None,
    ) -> None:
        from sentence_transformers import SentenceTransformer

        self.name = model_name
        self.query_prompt_name = query_prompt_name
        self._model = SentenceTransformer(model_name, local_files_only=local_files_only)

    def embed(self, texts: Sequence[str], *, batch_size: int = 32) -> np.ndarray:
        if not texts:
            return np.zeros((0, 0), dtype=np.float32)
        vectors = self._model.encode(
            list(texts),
            batch_size=batch_size,
            show_progress_bar=False,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
        return np.asarray(vectors, dtype=np.float32)

    def embed_query(self, text: str) -> np.ndarray:
        if not self.query_prompt_name:
            return self.embed([text])[0]
        # Some models (e.g. Qwen3-Embedding) expose a dedicated query prompt.
        try:
            vectors = self._model.encode(
                [text],
                prompt_name=self.query_prompt_name,
                show_progress_bar=False,
                convert_to_numpy=True,
                normalize_embeddings=True,
            )
            return np.asarray(vectors, dtype=np.float32)[0]
        except Exception:
            return self.embed([text])[0]


class OpenAIEmbeddingProvider(EmbeddingProvider):
    """Hosted OpenAI embeddings (optional reference row)."""

    def __init__(self, model_name: str = "text-embedding-3-small") -> None:
        from openai import OpenAI

        if not os.environ.get("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY is not set")
        self.name = model_name
        self._client = OpenAI()

    def embed(self, texts: Sequence[str], *, batch_size: int = 32) -> np.ndarray:
        if not texts:
            return np.zeros((0, 0), dtype=np.float32)
        vectors: list[list[float]] = []
        batch: list[str] = []
        for text in texts:
            batch.append(text)
            if len(batch) >= batch_size:
                vectors.extend(self._embed_batch(batch))
                batch = []
        if batch:
            vectors.extend(self._embed_batch(batch))
        matrix = np.asarray(vectors, dtype=np.float32)
        # L2-normalize for cosine-via-dot search.
        norms = np.linalg.norm(matrix, axis=1, keepdims=True)
        norms = np.maximum(norms, 1e-12)
        return matrix / norms

    def _embed_batch(self, batch: list[str]) -> list[list[float]]:
        response = self._client.embeddings.create(model=self.name, input=batch)
        # API may not preserve order guarantees in all SDKs; sort by index.
        ordered = sorted(response.data, key=lambda row: row.index)
        return [list(row.embedding) for row in ordered]


def get_embedding_provider(
    model_name: str = DEFAULT_MODEL_NAME,
    *,
    provider_type: str = "sentence_transformers",
    local_files_only: bool | None = None,
    query_prompt_name: str | None = None,
) -> EmbeddingProvider:
    """Load provider; prefer local cache when available to avoid Hub round-trips."""
    provider_type = (provider_type or "sentence_transformers").lower()
    if provider_type in {"openai", "hosted"}:
        return OpenAIEmbeddingProvider(model_name=model_name)
    if local_files_only is None:
        try:
            return SentenceTransformerProvider(
                model_name=model_name,
                local_files_only=True,
                query_prompt_name=query_prompt_name,
            )
        except Exception:
            return SentenceTransformerProvider(
                model_name=model_name,
                local_files_only=False,
                query_prompt_name=query_prompt_name,
            )
    return SentenceTransformerProvider(
        model_name=model_name,
        local_files_only=local_files_only,
        query_prompt_name=query_prompt_name,
    )


def cosine_similarity(query: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    """Cosine similarity for L2-normalized vectors (equivalent to dot product)."""
    if matrix.size == 0:
        return np.zeros(0, dtype=np.float32)
    q = query.astype(np.float32)
    if q.ndim == 1:
        return matrix @ q
    return matrix @ q.T


class NumpyVectorStore:
    """Persist chunk embeddings as NumPy arrays under rag_data/."""

    def __init__(
        self,
        embeddings: np.ndarray,
        chunk_ids: list[str],
        model_name: str,
    ) -> None:
        self.embeddings = embeddings.astype(np.float32)
        self.chunk_ids = chunk_ids
        self.model_name = model_name
        self._id_to_row = {chunk_id: idx for idx, chunk_id in enumerate(chunk_ids)}

    @classmethod
    def build(
        cls,
        chunks: Sequence[Chunk],
        provider: EmbeddingProvider,
        *,
        batch_size: int = 32,
    ) -> NumpyVectorStore:
        texts = [chunk.embed_text for chunk in chunks]
        matrix = provider.embed(texts, batch_size=batch_size)
        return cls(
            embeddings=matrix,
            chunk_ids=[c.chunk_id for c in chunks],
            model_name=provider.name,
        )

    def search(self, query_vec: np.ndarray, top_k: int = 20) -> list[tuple[str, float]]:
        scores = cosine_similarity(query_vec, self.embeddings)
        if scores.size == 0:
            return []
        top_k = min(top_k, len(scores))
        idxs = np.argpartition(-scores, top_k - 1)[:top_k]
        idxs = idxs[np.argsort(-scores[idxs])]
        return [(self.chunk_ids[i], float(scores[i])) for i in idxs]

    def save(self, out_dir: Path | None = None) -> dict[str, Path]:
        out_dir = out_dir or DEFAULT_RAG_DATA
        out_dir.mkdir(parents=True, exist_ok=True)
        emb_path = out_dir / "embeddings.npy"
        meta_path = out_dir / "embeddings_meta.json"
        np.save(emb_path, self.embeddings)
        meta_path.write_text(
            json.dumps(
                {
                    "model_name": self.model_name,
                    "chunk_ids": self.chunk_ids,
                    "shape": list(self.embeddings.shape),
                    "dtype": str(self.embeddings.dtype),
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        return {"embeddings": emb_path, "meta": meta_path}

    @classmethod
    def load(cls, out_dir: Path | None = None) -> NumpyVectorStore:
        out_dir = out_dir or DEFAULT_RAG_DATA
        emb_path = out_dir / "embeddings.npy"
        meta_path = out_dir / "embeddings_meta.json"
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        matrix = np.load(emb_path)
        return cls(
            embeddings=matrix,
            chunk_ids=list(meta["chunk_ids"]),
            model_name=meta["model_name"],
        )


def ensure_vector_store(
    chunks: Sequence[Chunk],
    out_dir: Path | None = None,
    *,
    model_name: str = DEFAULT_MODEL_NAME,
    rebuild: bool = False,
    provider_type: str = "sentence_transformers",
    query_prompt_name: str | None = None,
    provider: EmbeddingProvider | None = None,
) -> NumpyVectorStore:
    out_dir = out_dir or DEFAULT_RAG_DATA
    emb_path = out_dir / "embeddings.npy"
    meta_path = out_dir / "embeddings_meta.json"
    if not rebuild and emb_path.exists() and meta_path.exists():
        store = NumpyVectorStore.load(out_dir)
        chunk_ids = [c.chunk_id for c in chunks]
        if store.chunk_ids == chunk_ids and store.model_name == model_name:
            return store
    if provider is None:
        provider = get_embedding_provider(
            model_name,
            provider_type=provider_type,
            query_prompt_name=query_prompt_name,
        )
    store = NumpyVectorStore.build(chunks, provider)
    store.save(out_dir)
    return store

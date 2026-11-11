"""Hybrid semantic + lexical + graph-expansion retrieval with explanations."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Literal

import numpy as np

from rag.chunking import Chunk, chunk_corpus, load_chunks, save_chunks
from rag.corpus import DEFAULT_RAG_DATA, Corpus, load_corpus, save_corpus_manifest
from rag.embeddings import (
    DEFAULT_MODEL_NAME,
    EmbeddingProvider,
    NumpyVectorStore,
    ensure_vector_store,
    get_embedding_provider,
)
from rag.graph import KnowledgeGraph, build_knowledge_graph, load_graph, save_graph
from rag.lexical import LexicalIndex, ensure_lexical_index
from rag.rerank import Reranker

Mode = Literal["semantic", "lexical", "hybrid", "hybrid_graph"]

# Generic tokens that should not alone justify graph-neighbour admission.
_QUERY_STOPWORDS = frozenset(
    {
        "a",
        "an",
        "and",
        "are",
        "as",
        "at",
        "be",
        "branch",
        "branches",
        "by",
        "can",
        "cra",
        "do",
        "does",
        "for",
        "from",
        "how",
        "in",
        "into",
        "is",
        "it",
        "most",
        "note",
        "notes",
        "of",
        "on",
        "or",
        "should",
        "the",
        "to",
        "what",
        "when",
        "which",
        "with",
    }
)


@dataclass
class RetrievalWeights:
    semantic: float = 0.45
    lexical: float = 0.35
    graph: float = 0.12
    domain: float = 0.05
    authoritative: float = 0.03

    def as_dict(self) -> dict[str, float]:
        return asdict(self)


@dataclass
class RetrievalResult:
    rank: int
    chunk_id: str
    note_id: str
    title: str
    note_path: str
    chunk_heading: str
    primary_domain: str | None
    semantic_score: float
    lexical_score: float
    graph_contribution: float
    domain_score: float
    authoritative_score: float
    final_score: float
    why_included: list[str] = field(default_factory=list)
    graph_path: list[str] | None = None
    inclusion_origin: str = "direct"  # direct | graph_expansion
    text_preview: str = ""
    related_sources: list[str] = field(default_factory=list)
    source_urls: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class RetrievalResponse:
    query: str
    mode: str
    results: list[RetrievalResult]
    direct_results: list[RetrievalResult]
    graph_expanded_results: list[RetrievalResult]
    source_notes: list[dict[str, Any]]
    seeds: list[str]
    stats: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "query": self.query,
            "mode": self.mode,
            "results": [r.to_dict() for r in self.results],
            "direct_results": [r.to_dict() for r in self.direct_results],
            "graph_expanded_results": [r.to_dict() for r in self.graph_expanded_results],
            "source_notes": self.source_notes,
            "seeds": self.seeds,
            "stats": self.stats,
        }


def _minmax(values: dict[str, float]) -> dict[str, float]:
    if not values:
        return {}
    xs = list(values.values())
    lo, hi = min(xs), max(xs)
    if hi <= lo:
        return {k: 1.0 for k in values}
    return {k: (v - lo) / (hi - lo) for k, v in values.items()}


class Retriever:
    """End-to-end Phase 1 retriever over vault indexes."""

    def __init__(
        self,
        corpus: Corpus,
        chunks: list[Chunk],
        graph: KnowledgeGraph,
        vector_store: NumpyVectorStore,
        lexical_index: LexicalIndex,
        embedding_provider: EmbeddingProvider | None = None,
        weights: RetrievalWeights | None = None,
        provider_type: str = "sentence_transformers",
        query_prompt_name: str | None = None,
    ) -> None:
        self.corpus = corpus
        self.chunks = chunks
        self.chunks_by_id = {c.chunk_id: c for c in chunks}
        self.chunks_by_note: dict[str, list[Chunk]] = {}
        for chunk in chunks:
            self.chunks_by_note.setdefault(chunk.note_id, []).append(chunk)
        self.graph = graph
        self.vector_store = vector_store
        self.lexical_index = lexical_index
        self.embedding_provider = embedding_provider
        self.weights = weights or RetrievalWeights()
        self.provider_type = provider_type
        self.query_prompt_name = query_prompt_name

    @classmethod
    def build(
        cls,
        root: Path | None = None,
        out_dir: Path | None = None,
        *,
        model_name: str = DEFAULT_MODEL_NAME,
        rebuild: bool = False,
        provider_type: str = "sentence_transformers",
        query_prompt_name: str | None = None,
        embedding_out_dir: Path | None = None,
        embedding_provider: EmbeddingProvider | None = None,
        shared_index_dir: Path | None = None,
    ) -> Retriever:
        """Build retriever indexes.

        Corpus/chunks/graph/lexical live under ``out_dir`` (or shared_index_dir).
        Embeddings may be stored separately under ``embedding_out_dir`` so each
        benchmark model keeps its own NumPy cache.
        """
        out_dir = out_dir or DEFAULT_RAG_DATA
        index_dir = shared_index_dir or out_dir
        index_dir.mkdir(parents=True, exist_ok=True)
        emb_dir = embedding_out_dir or out_dir
        emb_dir.mkdir(parents=True, exist_ok=True)

        corpus = load_corpus(root)
        save_corpus_manifest(corpus, index_dir)

        chunks_path = index_dir / "chunks.json"
        if rebuild or not chunks_path.exists():
            chunks = chunk_corpus(corpus)
            save_chunks(chunks, index_dir)
        else:
            chunks = load_chunks(chunks_path)
            # Rebuild chunks if corpus size drifted.
            if len({c.note_id for c in chunks}) != len(corpus.knowledge_notes):
                chunks = chunk_corpus(corpus)
                save_chunks(chunks, index_dir)

        graph_path = index_dir / "graph.json"
        if rebuild or not graph_path.exists():
            graph = build_knowledge_graph(corpus)
            save_graph(graph, index_dir)
        else:
            graph = load_graph(graph_path)

        vector_store = ensure_vector_store(
            chunks,
            emb_dir,
            model_name=model_name,
            rebuild=rebuild,
            provider_type=provider_type,
            query_prompt_name=query_prompt_name,
            provider=embedding_provider,
        )
        lexical_index = ensure_lexical_index(chunks, index_dir, rebuild=rebuild)
        # Lazy-load the embedding model on first semantic query unless provided.
        return cls(
            corpus=corpus,
            chunks=chunks,
            graph=graph,
            vector_store=vector_store,
            lexical_index=lexical_index,
            embedding_provider=embedding_provider,
            provider_type=provider_type,
            query_prompt_name=query_prompt_name,
        )

    def _ensure_provider(self) -> EmbeddingProvider:
        if self.embedding_provider is None:
            self.embedding_provider = get_embedding_provider(
                self.vector_store.model_name,
                provider_type=self.provider_type,
                query_prompt_name=self.query_prompt_name,
            )
        return self.embedding_provider

    def semantic_search(self, query: str, top_k: int = 20) -> list[tuple[str, float]]:
        provider = self._ensure_provider()
        q = provider.embed_query(query)
        return self.vector_store.search(q, top_k=top_k)

    def lexical_search(self, query: str, top_k: int = 20) -> list[tuple[str, float]]:
        return self.lexical_index.search(query, top_k=top_k)

    def _domain_bonus(self, chunk: Chunk, domain_filter: str | None) -> float:
        if not domain_filter:
            return 0.0
        return 1.0 if (chunk.primary_domain or "").lower() == domain_filter.lower() else 0.0

    def _authoritative_bonus(self, chunk: Chunk) -> float:
        score = 0.0
        if chunk.authoritative:
            score += 0.6
        origin = (chunk.content_origin or "").lower()
        if "official" in origin or "public-source" in origin:
            score += 0.4
        return min(score, 1.0)

    def _best_chunk_for_note(self, note_id: str, query: str) -> Chunk | None:
        chunks = self.chunks_by_note.get(note_id)
        if not chunks:
            return None
        # Prefer the first/heading-rich chunk; lexical overlap as light tie-break.
        q_tokens = set(query.casefold().split())
        best = chunks[0]
        best_score = -1
        for chunk in chunks:
            tokens = set(chunk.text.casefold().split())
            overlap = len(q_tokens & tokens)
            if overlap > best_score:
                best_score = overlap
                best = chunk
        return best

    def retrieve(
        self,
        query: str,
        *,
        top_k: int = 10,
        graph_hops: int = 1,
        domain: str | None = None,
        use_graph: bool = True,
        use_semantic: bool = True,
        use_lexical: bool = True,
        candidate_pool: int = 40,
        seed_count: int = 5,
        seed_score_threshold: float = 0.35,
        weights: RetrievalWeights | None = None,
        reranker: Reranker | None = None,
        rerank_pool: int = 30,
    ) -> RetrievalResponse:
        weights = weights or self.weights
        semantic_hits = self.semantic_search(query, top_k=candidate_pool) if use_semantic else []
        lexical_hits = self.lexical_search(query, top_k=candidate_pool) if use_lexical else []

        semantic_raw = {cid: score for cid, score in semantic_hits}
        lexical_raw = {cid: score for cid, score in lexical_hits}
        semantic_norm = _minmax(semantic_raw)
        lexical_norm = _minmax(lexical_raw)

        candidate_ids = set(semantic_raw) | set(lexical_raw)
        if domain:
            candidate_ids = {
                cid
                for cid in candidate_ids
                if (self.chunks_by_id[cid].primary_domain or "").lower() == domain.lower()
            }

        scored: dict[str, dict[str, Any]] = {}
        for chunk_id in candidate_ids:
            chunk = self.chunks_by_id[chunk_id]
            s = semantic_norm.get(chunk_id, 0.0)
            l = lexical_norm.get(chunk_id, 0.0)
            d = self._domain_bonus(chunk, domain)
            a = self._authoritative_bonus(chunk)
            base = (
                weights.semantic * s
                + weights.lexical * l
                + weights.domain * d
                + weights.authoritative * a
            )
            why = []
            if chunk_id in semantic_raw:
                why.append(f"semantic candidate (sim={semantic_raw[chunk_id]:.3f})")
            if chunk_id in lexical_raw:
                why.append(f"lexical candidate (bm25={lexical_raw[chunk_id]:.3f})")
            if d > 0:
                why.append(f"domain match ({chunk.primary_domain})")
            if a > 0:
                why.append("authoritative/source metadata bonus")
            scored[chunk_id] = {
                "chunk": chunk,
                "semantic": s,
                "semantic_raw": semantic_raw.get(chunk_id, 0.0),
                "lexical": l,
                "lexical_raw": lexical_raw.get(chunk_id, 0.0),
                "domain": d,
                "authoritative": a,
                "graph": 0.0,
                "graph_path": None,
                "base": base,
                "why": why,
                "origin": "direct",
            }

        # Seed notes from high-confidence direct hits (by note, not chunk).
        note_best: dict[str, float] = {}
        for chunk_id, info in scored.items():
            note_id = info["chunk"].note_id
            note_best[note_id] = max(note_best.get(note_id, 0.0), info["base"])
        seed_notes = [
            note_id
            for note_id, score in sorted(note_best.items(), key=lambda kv: kv[1], reverse=True)
            if score >= seed_score_threshold
        ][:seed_count]
        if not seed_notes and note_best:
            seed_notes = [
                note_id
                for note_id, _ in sorted(note_best.items(), key=lambda kv: kv[1], reverse=True)[:seed_count]
            ]

        graph_meta: dict[str, dict[str, Any]] = {}
        if use_graph and graph_hops > 0 and seed_notes:
            expanded = self.graph.n_hop_expansion(seed_notes, hops=graph_hops, undirected=True)
            graph_meta = expanded
            for note_id, meta in expanded.items():
                if meta["distance"] == 0:
                    continue
                # Skip notes outside the knowledge chunk set.
                chunk = self._best_chunk_for_note(note_id, query)
                if chunk is None:
                    continue
                if domain and (chunk.primary_domain or "").lower() != domain.lower():
                    continue
                distance = int(meta["distance"])
                proximity = max(0.0, 1.0 - 0.45 * (distance - 1))
                # Prefer neighbours already somewhat related via lexical/title overlap.
                title_overlap = 0.0
                q_tokens = {
                    t
                    for t in query.casefold().split()
                    if len(t) > 2 and t not in _QUERY_STOPWORDS
                }
                title_tokens = {
                    t
                    for t in chunk.note_title.casefold().replace("-", " ").split()
                    if len(t) > 2 and t not in _QUERY_STOPWORDS
                }
                if q_tokens and title_tokens:
                    title_overlap = len(q_tokens & title_tokens) / max(len(q_tokens), 1)
                # Light content overlap against the query tokens.
                text_tokens = {
                    t
                    for t in chunk.text.casefold().replace("-", " ").split()
                    if len(t) > 2 and t not in _QUERY_STOPWORDS
                }
                content_overlap = (
                    len(q_tokens & text_tokens) / max(len(q_tokens), 1) if q_tokens else 0.0
                )
                relevance = max(title_overlap, min(1.0, content_overlap))
                graph_score = 0.5 * proximity + 0.5 * relevance

                # Prefer best chunk already scored for this note, if any.
                existing_for_note = None
                for info in scored.values():
                    if info["chunk"].note_id == note_id:
                        existing_for_note = info
                        break

                if existing_for_note is not None:
                    # Keep direct ranking stable; attach path for explainability only.
                    if existing_for_note["graph_path"] is None:
                        existing_for_note["graph_path"] = meta["path"]
                        existing_for_note["why"].append(
                            f"also linked from seed via path {' -> '.join(meta['path'])}"
                        )
                    continue

                # Only admit graph-only neighbours with clear query relevance.
                if relevance < 0.25:
                    continue
                s = semantic_norm.get(chunk.chunk_id, 0.0)
                l = lexical_norm.get(chunk.chunk_id, 0.0)
                d = self._domain_bonus(chunk, domain)
                a = self._authoritative_bonus(chunk)
                base = (
                    weights.semantic * s
                    + weights.lexical * l
                    + weights.domain * d
                    + weights.authoritative * a
                )
                scored[chunk.chunk_id] = {
                    "chunk": chunk,
                    "semantic": s,
                    "semantic_raw": semantic_raw.get(chunk.chunk_id, 0.0),
                    "lexical": l,
                    "lexical_raw": lexical_raw.get(chunk.chunk_id, 0.0),
                    "domain": d,
                    "authoritative": a,
                    "graph": graph_score,
                    "graph_path": meta["path"],
                    "base": base,
                    "why": [
                        f"graph expansion from seed (distance={distance})",
                        f"path: {' -> '.join(meta['path'])}",
                    ],
                    "origin": "graph_expansion",
                }

        results: list[RetrievalResult] = []
        for chunk_id, info in scored.items():
            final = info["base"] + weights.graph * info["graph"]
            chunk: Chunk = info["chunk"]
            results.append(
                RetrievalResult(
                    rank=0,
                    chunk_id=chunk.chunk_id,
                    note_id=chunk.note_id,
                    title=chunk.note_title,
                    note_path=chunk.note_path,
                    chunk_heading=chunk.heading,
                    primary_domain=chunk.primary_domain,
                    semantic_score=round(info["semantic_raw"], 4),
                    lexical_score=round(info["lexical_raw"], 4),
                    graph_contribution=round(info["graph"], 4),
                    domain_score=round(info["domain"], 4),
                    authoritative_score=round(info["authoritative"], 4),
                    final_score=round(final, 4),
                    why_included=info["why"],
                    graph_path=info["graph_path"],
                    inclusion_origin=info["origin"],
                    text_preview=chunk.text[:280].replace("\n", " "),
                    related_sources=list(chunk.related_sources),
                    source_urls=list(chunk.source_urls),
                )
            )

        # Deduplicate by note: keep best-scoring chunk per note for ranking clarity.
        best_by_note: dict[str, RetrievalResult] = {}
        for result in results:
            prev = best_by_note.get(result.note_id)
            if prev is None or result.final_score > prev.final_score:
                best_by_note[result.note_id] = result
        ranked = sorted(best_by_note.values(), key=lambda r: r.final_score, reverse=True)
        for idx, result in enumerate(ranked, start=1):
            result.rank = idx

        pool = ranked[: max(top_k, rerank_pool if reranker is not None else top_k)]
        if reranker is not None:
            texts = {
                r.chunk_id: self.chunks_by_id[r.chunk_id].embed_text
                for r in pool
                if r.chunk_id in self.chunks_by_id
            }
            top = reranker.rerank(query, pool, top_k=top_k, texts=texts)
        else:
            top = pool[:top_k]

        direct = [r for r in top if r.inclusion_origin == "direct"]
        graph_expanded = [
            r
            for r in top
            if r.inclusion_origin == "graph_expansion"
            or (r.graph_path is not None and r.graph_contribution > 0)
        ]

        # Attach relevant source notes for top results.
        source_notes = self._collect_source_notes(top)

        mode = "hybrid_graph" if use_graph else ("hybrid" if use_semantic and use_lexical else (
            "semantic" if use_semantic else "lexical"
        ))
        return RetrievalResponse(
            query=query,
            mode=mode,
            results=top,
            direct_results=direct,
            graph_expanded_results=graph_expanded,
            source_notes=source_notes,
            seeds=seed_notes,
            stats={
                "semantic_candidates": len(semantic_hits),
                "lexical_candidates": len(lexical_hits),
                "merged_candidates": len(scored),
                "seed_notes": seed_notes,
                "graph_expanded_notes": [
                    nid for nid, meta in graph_meta.items() if meta.get("distance", 0) > 0
                ],
                "weights": weights.as_dict(),
                "knowledge_notes": len(self.corpus.knowledge_notes),
                "chunks": len(self.chunks),
                "graph_nodes": self.graph.node_count,
                "graph_edges": self.graph.edge_count,
                "reranker": getattr(reranker, "name", None),
                "rerank_pool": rerank_pool if reranker is not None else 0,
            },
        )

    def _collect_source_notes(self, results: list[RetrievalResult]) -> list[dict[str, Any]]:
        seen: set[str] = set()
        out: list[dict[str, Any]] = []
        for result in results:
            note = self.corpus.knowledge_notes.get(result.note_id)
            if not note:
                continue
            for raw in note.related_sources:
                resolved = self.corpus.alias_index.resolve(raw)
                source = None
                if resolved and resolved in self.corpus.source_notes:
                    source = self.corpus.source_notes[resolved]
                else:
                    # Try title match against source notes.
                    for snote in self.corpus.source_notes.values():
                        if snote.title.casefold() == raw.strip("[]").casefold():
                            source = snote
                            break
                if source is None or source.note_id in seen:
                    continue
                seen.add(source.note_id)
                out.append(
                    {
                        "note_id": source.note_id,
                        "title": source.title,
                        "path": source.path,
                        "source_url": source.source_url,
                        "publisher": source.publisher,
                        "related_from": result.note_id,
                    }
                )
        return out


def format_retrieval_report(response: RetrievalResponse) -> str:
    lines: list[str] = []
    lines.append(f"Query: {response.query}")
    lines.append(f"Mode: {response.mode}")
    lines.append(
        "Corpus: "
        f"{response.stats.get('knowledge_notes')} notes | "
        f"{response.stats.get('chunks')} chunks | "
        f"{response.stats.get('graph_nodes')} nodes | "
        f"{response.stats.get('graph_edges')} edges"
    )
    lines.append(f"Seeds: {', '.join(response.seeds) if response.seeds else '(none)'}")
    lines.append("")
    lines.append("=== Direct retrieval results ===")
    direct = response.direct_results or [r for r in response.results if r.inclusion_origin == "direct"]
    if not direct:
        lines.append("(none in top-k)")
    for result in direct:
        lines.extend(_format_result(result))
    lines.append("")
    lines.append("=== Graph-expanded results ===")
    graph_results = response.graph_expanded_results
    if not graph_results:
        lines.append("(none in top-k)")
    for result in graph_results:
        lines.extend(_format_result(result))
    if response.source_notes:
        lines.append("")
        lines.append("=== Related source notes ===")
        for src in response.source_notes:
            lines.append(
                f"- {src['title']} ({src['path']})"
                + (f" | {src['source_url']}" if src.get("source_url") else "")
                + f" [from {src['related_from']}]"
            )
    lines.append("")
    lines.append("=== Ranked top results ===")
    for result in response.results:
        lines.append(
            f"{result.rank}. {result.title} | final={result.final_score:.4f} | "
            f"sem={result.semantic_score:.4f} lex={result.lexical_score:.4f} "
            f"graph={result.graph_contribution:.4f} | {result.primary_domain} | "
            f"{result.inclusion_origin}"
        )
    return "\n".join(lines)


def _format_result(result: RetrievalResult) -> list[str]:
    lines = [
        f"#{result.rank} {result.title}",
        f"  path: {result.note_path}",
        f"  heading: {result.chunk_heading}",
        f"  domain: {result.primary_domain}",
        (
            "  scores: "
            f"semantic={result.semantic_score:.4f} "
            f"lexical={result.lexical_score:.4f} "
            f"graph={result.graph_contribution:.4f} "
            f"final={result.final_score:.4f}"
        ),
        f"  why: {'; '.join(result.why_included)}",
    ]
    if result.graph_path:
        lines.append(f"  graph_path: {' -> '.join(result.graph_path)}")
    lines.append(f"  preview: {result.text_preview[:220]}...")
    return lines

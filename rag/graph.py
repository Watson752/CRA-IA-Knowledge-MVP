"""In-memory directed knowledge graph built from Obsidian wikilinks."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

import networkx as nx

from rag.corpus import DEFAULT_RAG_DATA, Corpus
from rag.links import AliasIndex
from rag.metadata import NoteRecord


class KnowledgeGraph:
    """Directed NetworkX graph over canonical note IDs."""

    def __init__(self, graph: nx.DiGraph | None = None) -> None:
        self.graph = graph if graph is not None else nx.DiGraph()

    @property
    def node_count(self) -> int:
        return self.graph.number_of_nodes()

    @property
    def edge_count(self) -> int:
        return self.graph.number_of_edges()

    def neighbours(self, note_id: str) -> list[str]:
        if note_id not in self.graph:
            return []
        return sorted(self.graph.successors(note_id))

    def incoming_neighbours(self, note_id: str) -> list[str]:
        if note_id not in self.graph:
            return []
        return sorted(self.graph.predecessors(note_id))

    def degree(self, note_id: str) -> int:
        if note_id not in self.graph:
            return 0
        return int(self.graph.degree(note_id))

    def shortest_path(self, source: str, target: str) -> list[str] | None:
        if source not in self.graph or target not in self.graph:
            return None
        try:
            return list(nx.shortest_path(self.graph, source, target))
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return None

    def n_hop_expansion(
        self,
        seeds: Iterable[str],
        hops: int = 1,
        undirected: bool = True,
    ) -> dict[str, dict[str, Any]]:
        """Expand seeds by n hops. Returns note_id -> {distance, path, via}."""
        if hops < 0:
            hops = 0
        frontier = {seed for seed in seeds if seed in self.graph}
        reached: dict[str, dict[str, Any]] = {
            seed: {"distance": 0, "path": [seed], "via": "seed"} for seed in frontier
        }
        if hops == 0:
            return reached

        current = set(frontier)
        for distance in range(1, hops + 1):
            nxt: set[str] = set()
            for node in current:
                candidates = set(self.graph.successors(node))
                if undirected:
                    candidates |= set(self.graph.predecessors(node))
                for neigh in candidates:
                    if neigh in reached:
                        continue
                    parent_path = reached[node]["path"]
                    reached[neigh] = {
                        "distance": distance,
                        "path": parent_path + [neigh],
                        "via": "wikilink",
                    }
                    nxt.add(neigh)
            current = nxt
            if not current:
                break
        return reached

    def connected_components(self, weakly: bool = True) -> list[list[str]]:
        if weakly:
            comps = nx.weakly_connected_components(self.graph)
        else:
            comps = nx.strongly_connected_components(self.graph)
        return [sorted(comp) for comp in comps]

    def to_serializable(self) -> dict[str, Any]:
        nodes = []
        for node_id, attrs in self.graph.nodes(data=True):
            nodes.append({"id": node_id, **attrs})
        edges = []
        for source, target, attrs in self.graph.edges(data=True):
            edges.append({"source": source, "target": target, **attrs})
        return {
            "node_count": self.node_count,
            "edge_count": self.edge_count,
            "nodes": nodes,
            "edges": edges,
        }


def build_graph(
    notes: dict[str, NoteRecord],
    alias_index: AliasIndex,
    *,
    include_unresolved_as_nodes: bool = False,
) -> KnowledgeGraph:
    """Construct a directed graph. One node per canonical note; aliases collapse."""
    g = nx.DiGraph()
    for note_id, note in notes.items():
        g.add_node(
            note_id,
            title=note.title,
            path=note.path,
            aliases=list(note.aliases),
            note_type=note.note_type,
            primary_domain=note.primary_domain,
            domains=list(note.domains),
            classification=note.classification,
            content_origin=note.content_origin,
            authoritative=note.authoritative,
            review_status=note.review_status,
            corpus_role=note.corpus_role,
            source_urls=list(note.source_urls),
        )

    for note in notes.values():
        for target in note.wikilinks:
            resolved = alias_index.resolve(target)
            if resolved is None:
                if include_unresolved_as_nodes:
                    # Optional; Phase 1 default skips unresolved targets.
                    continue
                continue
            if resolved == note.note_id:
                continue
            if resolved not in g:
                # Target may be outside indexed set; skip rather than invent duplicates.
                continue
            if g.has_edge(note.note_id, resolved):
                continue
            g.add_edge(
                note.note_id,
                resolved,
                relationship_origin="wikilink",
                raw_target=target,
            )
    return KnowledgeGraph(g)


def build_knowledge_graph(corpus: Corpus) -> KnowledgeGraph:
    """Graph over knowledge notes; source notes are omitted from ordinary nodes."""
    return build_graph(corpus.knowledge_notes, corpus.alias_index)


def save_graph(graph: KnowledgeGraph, out_dir: Path | None = None) -> Path:
    out_dir = out_dir or DEFAULT_RAG_DATA
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "graph.json"
    path.write_text(
        json.dumps(graph.to_serializable(), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return path


def load_graph(path: Path | None = None) -> KnowledgeGraph:
    path = path or (DEFAULT_RAG_DATA / "graph.json")
    payload = json.loads(path.read_text(encoding="utf-8"))
    g = nx.DiGraph()
    for node in payload["nodes"]:
        node_id = node.pop("id")
        g.add_node(node_id, **node)
    for edge in payload["edges"]:
        source = edge.pop("source")
        target = edge.pop("target")
        g.add_edge(source, target, **edge)
    return KnowledgeGraph(g)

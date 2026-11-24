"""CLI for vault-native Phase 1 retrieval and Phase 2 grounded answers."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from rag.answer import DEFAULT_CHAT_MODEL, ask, format_answer_report
from rag.corpus import DEFAULT_RAG_DATA, ROOT
from rag.embeddings import DEFAULT_MODEL_NAME
from rag.retrieve import Retriever, format_retrieval_report


def _ensure_retriever(args: argparse.Namespace) -> Retriever:
    out_dir = Path(args.out_dir)
    if not (out_dir / "chunks.json").exists() or getattr(args, "rebuild", False):
        Retriever.build(
            root=Path(args.root),
            out_dir=out_dir,
            model_name=args.model,
            rebuild=True,
        )
    return Retriever.build(
        root=Path(args.root),
        out_dir=out_dir,
        model_name=args.model,
        rebuild=False,
    )


def cmd_index(args: argparse.Namespace) -> int:
    out_dir = Path(args.out_dir)
    retriever = Retriever.build(
        root=Path(args.root),
        out_dir=out_dir,
        model_name=args.model,
        rebuild=args.rebuild,
    )
    summary = retriever.corpus.summary()
    print("Indexed corpus")
    print(f"  knowledge notes: {summary['knowledge_notes']}")
    print(f"  source notes:    {summary['source_notes']}")
    print(f"  unresolved wikilinks (non-fatal): {summary['unresolved_wikilinks']}")
    print(f"  chunks:          {len(retriever.chunks)}")
    print(f"  graph nodes:     {retriever.graph.node_count}")
    print(f"  graph edges:     {retriever.graph.edge_count}")
    print(f"  artifacts:       {out_dir}")
    print("  primary_domain_counts:")
    for domain, count in summary["primary_domain_counts"].items():
        print(f"    {domain}: {count}")
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    retriever = _ensure_retriever(args)
    response = retriever.retrieve(
        args.query,
        top_k=args.top_k,
        graph_hops=0 if args.no_graph else args.graph_hops,
        domain=args.domain,
        use_graph=not args.no_graph and args.graph_hops > 0,
        use_semantic=not args.lexical_only,
        use_lexical=not args.semantic_only,
    )
    if args.json:
        print(json.dumps(response.to_dict(), indent=2, ensure_ascii=False))
    else:
        print(format_retrieval_report(response))
    return 0


def cmd_ask(args: argparse.Namespace) -> int:
    retriever = _ensure_retriever(args)
    try:
        result = ask(
            args.query,
            retriever,
            top_k=args.top_k,
            graph_hops=0 if args.no_graph else args.graph_hops,
            use_graph=not args.no_graph and args.graph_hops > 0,
            domain=args.domain,
            chat_model=args.chat_model,
            root=Path(args.root),
        )
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))
    else:
        print(format_answer_report(result))
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    out_dir = Path(args.out_dir)
    retriever = Retriever.build(
        root=Path(args.root),
        out_dir=out_dir,
        model_name=args.model,
        rebuild=False,
    )
    print(json.dumps(
        {
            "corpus": retriever.corpus.summary(),
            "chunks": len(retriever.chunks),
            "graph_nodes": retriever.graph.node_count,
            "graph_edges": retriever.graph.edge_count,
            "embedding_model": retriever.vector_store.model_name,
            "embedding_shape": list(retriever.vector_store.embeddings.shape),
        },
        indent=2,
    ))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m rag.cli",
        description="CRA IA vault-native hybrid retrieval (Phase 1) and grounded answers (Phase 2).",
    )
    parser.add_argument("--root", default=str(ROOT), help="Vault root directory")
    parser.add_argument("--out-dir", default=str(DEFAULT_RAG_DATA), help="Runtime artifact directory")
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL_NAME,
        help="SentenceTransformers embedding model (retrieval)",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    p_index = sub.add_parser("index", help="Build corpus, graph, chunk, and embedding indexes")
    p_index.add_argument("--rebuild", action="store_true", help="Force rebuild of all artifacts")
    p_index.set_defaults(func=cmd_index)

    p_search = sub.add_parser("search", help="Retrieve notes for a question (no answer generation)")
    p_search.add_argument("query", help="Natural-language retrieval query")
    p_search.add_argument("--top-k", type=int, default=10)
    p_search.add_argument("--graph-hops", type=int, default=1)
    p_search.add_argument("--domain", default=None, help="Filter by primary_domain")
    p_search.add_argument("--no-graph", action="store_true", help="Disable graph expansion")
    p_search.add_argument("--semantic-only", action="store_true")
    p_search.add_argument("--lexical-only", action="store_true")
    p_search.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    p_search.add_argument("--rebuild", action="store_true", help="Rebuild indexes before search")
    p_search.set_defaults(func=cmd_search)

    p_ask = sub.add_parser("ask", help="Retrieve then generate a grounded OpenAI answer")
    p_ask.add_argument("query", help="Natural-language audit inquiry")
    p_ask.add_argument("--top-k", type=int, default=10)
    p_ask.add_argument("--graph-hops", type=int, default=1)
    p_ask.add_argument("--domain", default=None, help="Filter by primary_domain")
    p_ask.add_argument("--no-graph", action="store_true", help="Disable graph expansion")
    p_ask.add_argument(
        "--chat-model",
        default=DEFAULT_CHAT_MODEL,
        help="OpenAI chat model (default gpt-4.1-mini or OPENAI_CHAT_MODEL)",
    )
    p_ask.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    p_ask.add_argument("--rebuild", action="store_true", help="Rebuild indexes before ask")
    p_ask.set_defaults(func=cmd_ask)

    p_stats = sub.add_parser("stats", help="Print index statistics")
    p_stats.set_defaults(func=cmd_stats)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

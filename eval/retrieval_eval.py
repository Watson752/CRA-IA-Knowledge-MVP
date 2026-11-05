#!/usr/bin/env python3
"""Phase 1 retrieval benchmark (terminal + optional JSON under runtime-results)."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

# Path kept for QUESTIONS_PATH / RESULTS_DIR.

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eval.metrics import hit_at_k, match_expected, mrr, recall_at_k
from rag.corpus import DEFAULT_RAG_DATA
from rag.retrieve import Retriever, RetrievalWeights

# Preserve previous private aliases for any external imports.
_match_expected = match_expected

QUESTIONS_PATH = ROOT / "eval" / "questions.json"
RESULTS_DIR = ROOT / "rag_data" / "runtime-results"


@dataclass
class ModeMetrics:
    mode: str
    hit_at_1: float
    hit_at_3: float
    hit_at_5: float
    recall_at_5: float
    recall_at_10: float
    mrr: float
    n_questions: int


def evaluate_mode(
    retriever: Retriever,
    questions: list[dict[str, Any]],
    *,
    mode: str,
    top_k: int = 10,
) -> tuple[ModeMetrics, list[dict[str, Any]]]:
    use_semantic = mode in {"semantic", "hybrid", "hybrid_graph"}
    use_lexical = mode in {"lexical", "hybrid", "hybrid_graph"}
    use_graph = mode == "hybrid_graph"

    first_hit_ranks: list[int | None] = []
    recall5_flags: list[list[bool]] = []
    recall10_flags: list[list[bool]] = []
    details: list[dict[str, Any]] = []

    for item in questions:
        query = item["query"]
        expected = list(item["expected_notes"])
        response = retriever.retrieve(
            query,
            top_k=top_k,
            graph_hops=1 if use_graph else 0,
            use_graph=use_graph,
            use_semantic=use_semantic,
            use_lexical=use_lexical,
            weights=RetrievalWeights(),
        )
        titles = [r.title for r in response.results]
        ids = [r.note_id for r in response.results]

        # Rank of first expected hit.
        first_rank = None
        for result in response.results:
            flags = match_expected([result.title], [result.note_id], expected)
            if any(flags):
                first_rank = result.rank
                break
        first_hit_ranks.append(first_rank)

        top5_titles = titles[:5]
        top5_ids = ids[:5]
        top10_titles = titles[:10]
        top10_ids = ids[:10]
        r5 = match_expected(top5_titles, top5_ids, expected)
        r10 = match_expected(top10_titles, top10_ids, expected)
        recall5_flags.append(r5)
        recall10_flags.append(r10)

        details.append(
            {
                "id": item["id"],
                "query": query,
                "expected_notes": expected,
                "first_hit_rank": first_rank,
                "retrieved": [
                    {
                        "rank": r.rank,
                        "title": r.title,
                        "note_id": r.note_id,
                        "final_score": r.final_score,
                        "origin": r.inclusion_origin,
                        "graph_path": r.graph_path,
                    }
                    for r in response.results
                ],
                "recall_at_5_hits": r5,
                "recall_at_10_hits": r10,
            }
        )

    metrics = ModeMetrics(
        mode=mode,
        hit_at_1=hit_at_k(first_hit_ranks, 1),
        hit_at_3=hit_at_k(first_hit_ranks, 3),
        hit_at_5=hit_at_k(first_hit_ranks, 5),
        recall_at_5=recall_at_k(recall5_flags),
        recall_at_10=recall_at_k(recall10_flags),
        mrr=mrr(first_hit_ranks),
        n_questions=len(questions),
    )
    return metrics, details


def print_metrics(metrics: ModeMetrics) -> None:
    print(f"\nMode: {metrics.mode}")
    print(f"  Hit@1     {metrics.hit_at_1:.3f}")
    print(f"  Hit@3     {metrics.hit_at_3:.3f}")
    print(f"  Hit@5     {metrics.hit_at_5:.3f}")
    print(f"  Recall@5  {metrics.recall_at_5:.3f}")
    print(f"  Recall@10 {metrics.recall_at_10:.3f}")
    print(f"  MRR       {metrics.mrr:.3f}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate Phase 1 retrieval modes.")
    parser.add_argument("--questions", default=str(QUESTIONS_PATH))
    parser.add_argument("--out-dir", default=str(DEFAULT_RAG_DATA))
    parser.add_argument("--rebuild", action="store_true")
    parser.add_argument("--top-k", type=int, default=10)
    args = parser.parse_args()

    payload = json.loads(Path(args.questions).read_text(encoding="utf-8"))
    questions = payload["questions"]

    print("Building / loading retriever indexes...")
    retriever = Retriever.build(out_dir=Path(args.out_dir), rebuild=args.rebuild)
    summary = retriever.corpus.summary()
    print(
        f"Indexed knowledge notes={summary['knowledge_notes']} "
        f"chunks={len(retriever.chunks)} "
        f"nodes={retriever.graph.node_count} "
        f"edges={retriever.graph.edge_count}"
    )

    modes = ["semantic", "lexical", "hybrid", "hybrid_graph"]
    all_metrics: list[ModeMetrics] = []
    all_details: dict[str, Any] = {"questions": questions, "modes": {}}

    for mode in modes:
        metrics, details = evaluate_mode(
            retriever, questions, mode=mode, top_k=args.top_k
        )
        all_metrics.append(metrics)
        all_details["modes"][mode] = {"metrics": asdict(metrics), "details": details}
        print_metrics(metrics)

    print("\n=== Comparison ===")
    header = f"{'mode':<14} {'Hit@1':>7} {'Hit@3':>7} {'Hit@5':>7} {'R@5':>7} {'R@10':>7} {'MRR':>7}"
    print(header)
    print("-" * len(header))
    for m in all_metrics:
        print(
            f"{m.mode:<14} {m.hit_at_1:7.3f} {m.hit_at_3:7.3f} {m.hit_at_5:7.3f} "
            f"{m.recall_at_5:7.3f} {m.recall_at_10:7.3f} {m.mrr:7.3f}"
        )

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RESULTS_DIR / "retrieval_eval.json"
    out_path.write_text(json.dumps(all_details, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nJSON results written to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

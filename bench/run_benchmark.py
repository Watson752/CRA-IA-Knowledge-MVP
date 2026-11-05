"""Run embedding/reranker benchmark configurations and publish results."""

from __future__ import annotations

import argparse
import json
import statistics
import subprocess
import sys
import time
import traceback
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from bench.config_loader import BenchConfig, load_configs, list_all_config_ids
from eval.metrics import hit_at_k, match_expected, mrr, recall_at_k
from rag.corpus import DEFAULT_RAG_DATA
from rag.embeddings import cache_dir_for_model
from rag.rerank import get_reranker
from rag.retrieve import Retriever, RetrievalWeights

QUESTIONS_PATH = ROOT / "eval" / "questions.json"
DRAFT_QUESTIONS_PATH = ROOT / "eval" / "questions_draft.json"
RESULTS_DIR = ROOT / "bench" / "results"
SHARED_INDEX_DIR = DEFAULT_RAG_DATA / "shared_index"

BASELINE_HIT1 = 0.9
BASELINE_MRR = 0.91
BASELINE_TOLERANCE = 0.005

HONESTY = (
    "Honesty note: the official eval set has only 10 questions. "
    "A Hit@1 difference of 0.10 (one question) is not statistically meaningful. "
    "Treat these rankings as directional signals for this MVP corpus, not as "
    "production model-selection proof."
)


@dataclass
class ConfigRunResult:
    config_id: str
    question_set: str
    status: str  # ok | failed | skipped
    embedding_model: str
    reranker: str | None
    provider: str
    hit_at_1: float | None = None
    hit_at_3: float | None = None
    hit_at_5: float | None = None
    recall_at_5: float | None = None
    recall_at_10: float | None = None
    mrr: float | None = None
    n_questions: int | None = None
    median_query_latency_ms: float | None = None
    index_build_seconds: float | None = None
    hardware: str | None = None
    error: str | None = None
    baseline_marked: bool = False
    per_question: list[dict[str, Any]] = field(default_factory=list)

    def to_row(self) -> dict[str, Any]:
        return {
            "config_id": self.config_id,
            "question_set": self.question_set,
            "status": self.status,
            "embedding_model": self.embedding_model,
            "reranker": self.reranker or "",
            "provider": self.provider,
            "hit_at_1": self.hit_at_1,
            "hit_at_3": self.hit_at_3,
            "hit_at_5": self.hit_at_5,
            "recall_at_5": self.recall_at_5,
            "recall_at_10": self.recall_at_10,
            "mrr": self.mrr,
            "n_questions": self.n_questions,
            "median_query_latency_ms": self.median_query_latency_ms,
            "index_build_seconds": self.index_build_seconds,
            "hardware": self.hardware,
            "error": self.error or "",
            "baseline_marked": self.baseline_marked,
        }


def detect_hardware() -> str:
    try:
        import torch

        return "cuda" if torch.cuda.is_available() else "cpu"
    except Exception:
        return "cpu"


def git_sha() -> str:
    try:
        return (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=ROOT, stderr=subprocess.DEVNULL
            )
            .decode()
            .strip()
        )
    except Exception:
        return "unknown"


def load_questions(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return list(payload.get("questions") or [])


def prepare_session(
    cfg: BenchConfig,
    *,
    rebuild: bool = False,
) -> tuple[Retriever | None, Any, float, str | None]:
    """Build shared retriever/reranker once per config. Returns (retriever, reranker, index_s, error)."""
    if not cfg.is_available():
        return None, None, 0.0, cfg.skip_reason()
    emb_dir = cache_dir_for_model(f"{cfg.id}__{cfg.embedding_model}")
    t0 = time.perf_counter()
    try:
        retriever = Retriever.build(
            root=ROOT,
            out_dir=SHARED_INDEX_DIR,
            shared_index_dir=SHARED_INDEX_DIR,
            embedding_out_dir=emb_dir,
            model_name=cfg.embedding_model,
            provider_type=cfg.provider,
            query_prompt_name=cfg.query_prompt_name,
            rebuild=rebuild,
        )
        reranker = get_reranker(cfg.reranker) if cfg.reranker else None
        _ = retriever._ensure_provider()
        return retriever, reranker, time.perf_counter() - t0, None
    except Exception as exc:
        return None, None, time.perf_counter() - t0, f"{type(exc).__name__}: {exc}"


def evaluate_config(
    cfg: BenchConfig,
    questions: list[dict[str, Any]],
    *,
    question_set: str,
    rebuild: bool = False,
    retriever: Retriever | None = None,
    reranker: Any = None,
    index_seconds: float | None = None,
) -> ConfigRunResult:
    hardware = detect_hardware()
    if not cfg.is_available():
        return ConfigRunResult(
            config_id=cfg.id,
            question_set=question_set,
            status="skipped",
            embedding_model=cfg.embedding_model,
            reranker=cfg.reranker,
            provider=cfg.provider,
            hardware=hardware,
            error=cfg.skip_reason(),
            baseline_marked=cfg.id == "baseline",
        )

    if retriever is None:
        retriever, reranker, built_s, err = prepare_session(cfg, rebuild=rebuild)
        index_seconds = built_s
        if err and retriever is None:
            status = "skipped" if cfg.optional and "env var" in (err or "") else "failed"
            return ConfigRunResult(
                config_id=cfg.id,
                question_set=question_set,
                status=status,
                embedding_model=cfg.embedding_model,
                reranker=cfg.reranker,
                provider=cfg.provider,
                hardware=hardware,
                index_build_seconds=round(built_s, 3),
                error=err,
                baseline_marked=cfg.id == "baseline",
            )
    assert retriever is not None
    index_seconds = float(index_seconds or 0.0)

    use_graph = cfg.mode == "hybrid_graph"
    first_hit_ranks: list[int | None] = []
    recall5_flags: list[list[bool]] = []
    recall10_flags: list[list[bool]] = []
    latencies_ms: list[float] = []
    per_question: list[dict[str, Any]] = []

    try:
        for item in questions:
            query = item["query"]
            expected = list(item["expected_notes"])
            q0 = time.perf_counter()
            response = retriever.retrieve(
                query,
                top_k=cfg.top_k,
                graph_hops=1 if use_graph else 0,
                use_graph=use_graph,
                use_semantic=True,
                use_lexical=True,
                weights=RetrievalWeights(),
                reranker=reranker,
                rerank_pool=cfg.rerank_pool,
            )
            latencies_ms.append((time.perf_counter() - q0) * 1000.0)

            titles = [r.title for r in response.results]
            ids = [r.note_id for r in response.results]
            first_rank = None
            for result in response.results:
                if any(match_expected([result.title], [result.note_id], expected)):
                    first_rank = result.rank
                    break
            first_hit_ranks.append(first_rank)
            r5 = match_expected(titles[:5], ids[:5], expected)
            r10 = match_expected(titles[:10], ids[:10], expected)
            recall5_flags.append(r5)
            recall10_flags.append(r10)
            hit1 = 1 if first_rank == 1 else 0
            per_question.append(
                {
                    "config_id": cfg.id,
                    "question_set": question_set,
                    "question_id": item.get("id"),
                    "first_hit_rank": first_rank,
                    "hit_at_1": hit1,
                    "missed_expected": "; ".join(expected) if hit1 == 0 else "",
                    "top1_title": titles[0] if titles else "",
                }
            )
    except Exception as exc:
        return ConfigRunResult(
            config_id=cfg.id,
            question_set=question_set,
            status="failed",
            embedding_model=cfg.embedding_model,
            reranker=cfg.reranker,
            provider=cfg.provider,
            hardware=hardware,
            index_build_seconds=round(index_seconds, 3),
            error=f"{type(exc).__name__}: {exc}\n{traceback.format_exc(limit=3)}",
            baseline_marked=cfg.id == "baseline",
        )

    return ConfigRunResult(
        config_id=cfg.id,
        question_set=question_set,
        status="ok",
        embedding_model=cfg.embedding_model,
        reranker=cfg.reranker,
        provider=cfg.provider,
        hit_at_1=round(hit_at_k(first_hit_ranks, 1), 4),
        hit_at_3=round(hit_at_k(first_hit_ranks, 3), 4),
        hit_at_5=round(hit_at_k(first_hit_ranks, 5), 4),
        recall_at_5=round(recall_at_k(recall5_flags), 4),
        recall_at_10=round(recall_at_k(recall10_flags), 4),
        mrr=round(mrr(first_hit_ranks), 4),
        n_questions=len(questions),
        median_query_latency_ms=round(statistics.median(latencies_ms), 2) if latencies_ms else None,
        index_build_seconds=round(index_seconds, 3),
        hardware=hardware,
        baseline_marked=cfg.id == "baseline",
        per_question=per_question,
    )


def check_baseline(result: ConfigRunResult) -> None:
    if result.status != "ok":
        raise SystemExit(
            f"Baseline reproduction failed: status={result.status} error={result.error}"
        )
    assert result.hit_at_1 is not None and result.mrr is not None
    if abs(result.hit_at_1 - BASELINE_HIT1) > BASELINE_TOLERANCE:
        raise SystemExit(
            f"Baseline Hit@1 mismatch: got {result.hit_at_1}, expected ~{BASELINE_HIT1}. "
            "Stopping without inventing metrics."
        )
    if abs(result.mrr - BASELINE_MRR) > BASELINE_TOLERANCE:
        raise SystemExit(
            f"Baseline MRR mismatch: got {result.mrr}, expected ~{BASELINE_MRR}. "
            "Stopping without inventing metrics."
        )


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    import pandas as pd

    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False)


def format_metric(value: float | None, status: str) -> str:
    if status != "ok" or value is None:
        return status if status != "ok" else "n/a"
    return f"{value:.3f}"


def write_results_md(path: Path, results: list[ConfigRunResult], meta: dict[str, Any]) -> None:
    original = [r for r in results if r.question_set == "original"]
    draft = [r for r in results if r.question_set == "draft"]
    combined = [r for r in results if r.question_set == "combined"]

    lines = [
        "# Embedding / Reranker Benchmark Results",
        "",
        HONESTY,
        "",
        f"- Generated: `{meta.get('generated_at')}`",
        f"- Git commit: `{meta.get('git_sha')}`",
        f"- Hardware: `{meta.get('hardware')}`",
        "",
        "## Official set (original 10 questions)",
        "",
    ]
    lines.extend(_markdown_table(original))
    if draft:
        lines.extend(["", "## Draft set (review before promotion)", ""])
        lines.extend(_markdown_table(draft))
    if combined:
        lines.extend(["", "## Combined (original + draft)", ""])
        lines.extend(_markdown_table(combined))
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def _markdown_table(rows: list[ConfigRunResult]) -> list[str]:
    ok_sorted = sorted(
        [r for r in rows if r.status == "ok"],
        key=lambda r: (r.mrr is None, -(r.mrr or 0.0), r.config_id),
    )
    other = [r for r in rows if r.status != "ok"]
    ordered = ok_sorted + other
    header = (
        "| config | embedding | reranker | status | Hit@1 | Hit@3 | Hit@5 | "
        "Recall@5 | Recall@10 | MRR | median_ms | index_s | hardware |"
    )
    sep = "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|"
    lines = [header, sep]
    for r in ordered:
        label = f"**{r.config_id} (baseline)**" if r.baseline_marked else r.config_id
        lines.append(
            "| "
            + " | ".join(
                [
                    label,
                    r.embedding_model,
                    r.reranker or "none",
                    r.status,
                    format_metric(r.hit_at_1, r.status),
                    format_metric(r.hit_at_3, r.status),
                    format_metric(r.hit_at_5, r.status),
                    format_metric(r.recall_at_5, r.status),
                    format_metric(r.recall_at_10, r.status),
                    format_metric(r.mrr, r.status),
                    format_metric(r.median_query_latency_ms, r.status)
                    if r.status == "ok"
                    else (r.status if r.status != "ok" else "n/a"),
                    format_metric(r.index_build_seconds, r.status)
                    if r.status == "ok"
                    else (r.error or r.status)[:40],
                    r.hardware or "",
                ]
            )
            + " |"
        )
    return lines


def resolve_question_sets(choice: str) -> list[tuple[str, list[dict[str, Any]]]]:
    original = load_questions(QUESTIONS_PATH)
    sets: list[tuple[str, list[dict[str, Any]]]] = []
    if choice in {"original", "both"}:
        sets.append(("original", original))
    draft: list[dict[str, Any]] = []
    if DRAFT_QUESTIONS_PATH.exists():
        draft = load_questions(DRAFT_QUESTIONS_PATH)
    if choice in {"draft", "both"} and draft:
        sets.append(("draft", draft))
    if choice == "both" and draft:
        sets.append(("combined", original + draft))
    if choice == "draft" and not draft:
        raise SystemExit("Draft question file missing: eval/questions_draft.json")
    return sets


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Embedding/reranker retrieval benchmark")
    parser.add_argument("--configs", default=None, help="Comma-separated config ids")
    parser.add_argument("--all", action="store_true", help="Run all configs from YAML")
    parser.add_argument(
        "--skip-optional",
        action="store_true",
        help="Skip optional configs (e.g. hosted_ref) even if env keys exist",
    )
    parser.add_argument(
        "--question-set",
        choices=("original", "draft", "both"),
        default="both",
        help="Which question files to evaluate",
    )
    parser.add_argument("--rebuild", action="store_true")
    parser.add_argument(
        "--no-baseline-check",
        action="store_true",
        help="Do not abort when baseline metrics diverge (debug only)",
    )
    args = parser.parse_args(argv)

    if args.all:
        ids = None
    elif args.configs:
        ids = [part.strip() for part in args.configs.split(",") if part.strip()]
    else:
        ids = ["baseline"]

    # Include unavailable optionals so we can record skipped rows when --all.
    configs = load_configs(
        ids=ids,
        skip_optional=args.skip_optional,
        include_unavailable=True,
    )
    if not configs:
        known = ", ".join(list_all_config_ids())
        raise SystemExit(f"No configs selected. Known ids: {known}")

    question_sets = resolve_question_sets(
        "original" if args.question_set == "both" and not DRAFT_QUESTIONS_PATH.exists() else args.question_set
    )

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    all_results: list[ConfigRunResult] = []
    hardware = detect_hardware()

    for cfg in configs:
        print(f"\n=== Config: {cfg.id} ({cfg.embedding_model}) ===")
        retriever, reranker, index_s, prep_err = prepare_session(
            cfg, rebuild=args.rebuild
        )
        if prep_err and retriever is None:
            for qset_name, questions in question_sets:
                status = "skipped" if cfg.optional and "env var" in prep_err else "failed"
                result = ConfigRunResult(
                    config_id=cfg.id,
                    question_set=qset_name,
                    status=status,
                    embedding_model=cfg.embedding_model,
                    reranker=cfg.reranker,
                    provider=cfg.provider,
                    hardware=hardware,
                    index_build_seconds=round(index_s, 3),
                    error=prep_err,
                    baseline_marked=cfg.id == "baseline",
                )
                all_results.append(result)
                print(f"  [{qset_name}] status={result.status} error={prep_err}")
            if cfg.id == "baseline" and not args.no_baseline_check:
                check_baseline(all_results[-1])
            continue

        for qset_name, questions in question_sets:
            result = evaluate_config(
                cfg,
                questions,
                question_set=qset_name,
                retriever=retriever,
                reranker=reranker,
                index_seconds=index_s,
            )
            all_results.append(result)
            print(
                f"  [{qset_name}] status={result.status} "
                f"Hit@1={result.hit_at_1} MRR={result.mrr} "
                f"error={result.error or ''}"
            )
            if (
                cfg.id == "baseline"
                and qset_name == "original"
                and not args.no_baseline_check
            ):
                check_baseline(result)

    meta = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "git_sha": git_sha(),
        "hardware": hardware,
        "configs": [asdict(c) if hasattr(c, "__dataclass_fields__") else c.__dict__ for c in configs],
    }
    # BenchConfig is a dataclass — serialize cleanly.
    meta["configs"] = [
        {
            "id": c.id,
            "embedding_model": c.embedding_model,
            "provider": c.provider,
            "reranker": c.reranker,
            "optional": c.optional,
        }
        for c in configs
    ]

    rows = [r.to_row() for r in all_results]
    write_csv(RESULTS_DIR / "latest.csv", rows)

    per_q_rows: list[dict[str, Any]] = []
    for r in all_results:
        per_q_rows.extend(r.per_question)
    write_csv(RESULTS_DIR / "per_question.csv", per_q_rows)

    payload = {
        "meta": meta,
        "results": [r.to_row() for r in all_results],
        "per_question": per_q_rows,
        "honesty": HONESTY,
        "package_versions": _package_versions(),
    }
    (RESULTS_DIR / "latest.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    write_results_md(RESULTS_DIR / "RESULTS.md", all_results, meta)
    print(f"\nWrote results under {RESULTS_DIR}")
    return 0


def _package_versions() -> dict[str, str]:
    versions: dict[str, str] = {}
    for name in ("sentence_transformers", "torch", "numpy", "networkx", "rank_bm25", "yaml", "pandas"):
        try:
            mod = __import__(name)
            versions[name] = getattr(mod, "__version__", "unknown")
        except Exception:
            versions[name] = "missing"
    return versions


if __name__ == "__main__":
    raise SystemExit(run())

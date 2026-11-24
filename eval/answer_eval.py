"""Structural Phase 2 answer evaluation (no LLM judge).

Runs grounded `ask` over eval/answer_questions.json and checks:
- answer text produced when OPENAI_API_KEY is set
- positive items cite at least one retrieved note title or source_url
- negative items do not match forbidden current-failure / finding patterns

Results are written under rag_data/runtime-results/ (gitignored).

Usage:
  python -m eval.answer_eval
  python -m eval.answer_eval --limit 2
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rag.answer import (  # noqa: E402
    answer_has_correction,
    ask,
    check_answer_policy,
    forbidden_pattern_hits,
    load_dotenv,
)
from rag.corpus import DEFAULT_RAG_DATA  # noqa: E402
from rag.retrieve import Retriever  # noqa: E402

QUESTIONS_PATH = ROOT / "eval" / "answer_questions.json"
OUT_DIR = DEFAULT_RAG_DATA / "runtime-results"


def load_questions(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return list(data.get("questions") or [])


def evaluate_item(
    item: dict[str, Any],
    retriever: Retriever,
    *,
    chat_model: str | None,
    top_k: int,
) -> dict[str, Any]:
    kind = str(item.get("kind") or "positive")
    expect_citation = bool(item.get("expect_citation", kind == "positive"))
    query = str(item["query"])
    result = ask(
        query,
        retriever,
        top_k=top_k,
        chat_model=chat_model,
        root=ROOT,
    )
    answer = result.answer or ""
    policy_warnings = check_answer_policy(
        answer,
        result.evidence_note_titles,
        result.citations,
        evidence_empty=len(result.evidence_note_titles) == 0,
    )
    forbidden_hits = forbidden_pattern_hits(answer)
    has_citation = not any(w.startswith("missing_citation") for w in policy_warnings)
    has_correction = answer_has_correction(answer)

    checks: dict[str, bool] = {
        "has_answer": bool(answer.strip()),
    }
    if expect_citation:
        checks["has_citation"] = has_citation
    if kind == "negative":
        # Must correct the unsupported claim and avoid affirming it as established fact.
        checks["has_correction"] = has_correction
        checks["no_forbidden_assertion"] = len(forbidden_hits) == 0

    passed = all(checks.values())
    return {
        "id": item.get("id"),
        "kind": kind,
        "query": query,
        "passed": passed,
        "checks": checks,
        "forbidden_hits": forbidden_hits,
        "has_correction": has_correction,
        "warnings": result.warnings + policy_warnings,
        "chat_model": result.chat_model,
        "citation_titles": [c.title for c in result.citations],
        "answer_preview": answer[:400],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Phase 2 structural answer eval")
    parser.add_argument("--questions", type=Path, default=QUESTIONS_PATH)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--chat-model", default=None)
    parser.add_argument("--limit", type=int, default=0, help="Evaluate only first N items")
    parser.add_argument("--rebuild", action="store_true")
    args = parser.parse_args(argv)

    load_dotenv(ROOT / ".env")
    if not os.environ.get("OPENAI_API_KEY"):
        print(
            "OPENAI_API_KEY is not set; add it to .env or export it in your shell.",
            file=sys.stderr,
        )
        return 2

    questions = load_questions(args.questions)
    if args.limit and args.limit > 0:
        questions = questions[: args.limit]

    retriever = Retriever.build(
        root=ROOT,
        out_dir=DEFAULT_RAG_DATA,
        rebuild=args.rebuild,
    )

    rows: list[dict[str, Any]] = []
    for item in questions:
        print(f"Evaluating {item.get('id')} ...")
        row = evaluate_item(
            item,
            retriever,
            chat_model=args.chat_model,
            top_k=args.top_k,
        )
        status = "PASS" if row["passed"] else "FAIL"
        print(f"  {status} checks={row['checks']}")
        rows.append(row)

    passed = sum(1 for r in rows if r["passed"])
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "n": len(rows),
        "passed": passed,
        "failed": len(rows) - passed,
        "results": rows,
    }
    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_path = args.out_dir / "answer_eval.json"
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"\n{passed}/{len(rows)} passed; wrote {out_path}")
    return 0 if passed == len(rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())

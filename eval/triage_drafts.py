"""Triage draft eval questions for promotion into questions.json.

Promotion criteria (all must pass):
1. Every expected_notes title resolves to a vault knowledge note title or alias.
2. On the dry-run per_question.csv row for the chosen config, first_hit_rank is
   present and <= 10 (Hit@10).

Usage:
  python -m eval.triage_drafts
  python -m eval.triage_drafts --config-id baseline --per-question bench/results/per_question.csv
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from eval.metrics import normalize
from rag.corpus import ROOT, load_corpus

DEFAULT_DRAFTS = ROOT / "eval" / "questions_draft.json"
DEFAULT_PER_QUESTION = ROOT / "bench" / "results" / "per_question.csv"


@dataclass
class TriageRow:
    question_id: str
    query: str
    expected_notes: list[str]
    multi_hop: bool
    missing_titles: list[str] = field(default_factory=list)
    first_hit_rank: int | None = None
    hit_at_10: bool = False
    promote: bool = False
    reasons: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "question_id": self.question_id,
            "query": self.query,
            "expected_notes": self.expected_notes,
            "multi_hop": self.multi_hop,
            "missing_titles": self.missing_titles,
            "first_hit_rank": self.first_hit_rank,
            "hit_at_10": self.hit_at_10,
            "promote": self.promote,
            "reasons": self.reasons,
        }


def build_title_alias_index(root: Path | None = None) -> set[str]:
    corpus = load_corpus(root)
    labels: set[str] = set()
    for note in corpus.knowledge_notes.values():
        labels.add(normalize(note.title))
        for alias in note.aliases or []:
            labels.add(normalize(alias))
    return labels


def load_drafts(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return list(data.get("questions") or [])


def load_hit_ranks(
    path: Path,
    *,
    config_id: str,
    question_set: str = "draft",
) -> dict[str, int | None]:
    if not path.exists():
        return {}
    ranks: dict[str, int | None] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row.get("config_id") != config_id:
                continue
            if row.get("question_set") != question_set:
                continue
            qid = row.get("question_id") or ""
            raw = (row.get("first_hit_rank") or "").strip()
            if raw == "" or raw.lower() in {"none", "nan"}:
                ranks[qid] = None
            else:
                ranks[qid] = int(float(raw))
    return ranks


def triage(
    drafts: list[dict[str, Any]],
    labels: set[str],
    hit_ranks: dict[str, int | None],
    *,
    require_hit_data: bool = True,
) -> list[TriageRow]:
    rows: list[TriageRow] = []
    for item in drafts:
        qid = str(item.get("id") or "")
        expected = [str(x) for x in (item.get("expected_notes") or [])]
        missing = [title for title in expected if normalize(title) not in labels]
        rank = hit_ranks.get(qid)
        has_rank_row = qid in hit_ranks
        hit10 = rank is not None and rank <= 10
        reasons: list[str] = []
        if missing:
            reasons.append(f"missing_titles:{len(missing)}")
        if require_hit_data and not has_rank_row:
            reasons.append("no_dry_run_row")
        elif not hit10:
            reasons.append("miss_at_10" if has_rank_row else "no_dry_run_row")
        promote = not missing and hit10
        if promote:
            reasons.append("ok")
        rows.append(
            TriageRow(
                question_id=qid,
                query=str(item.get("query") or ""),
                expected_notes=expected,
                multi_hop=bool(item.get("multi_hop")),
                missing_titles=missing,
                first_hit_rank=rank,
                hit_at_10=hit10,
                promote=promote,
                reasons=reasons,
            )
        )
    return rows


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Triage draft questions for promotion")
    parser.add_argument("--drafts", type=Path, default=DEFAULT_DRAFTS)
    parser.add_argument("--per-question", type=Path, default=DEFAULT_PER_QUESTION)
    parser.add_argument("--config-id", default="baseline")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--titles-only",
        action="store_true",
        help="Only check expected-note titles (ignore dry-run Hit@10)",
    )
    parser.add_argument(
        "--json-out",
        type=Path,
        default=None,
        help="Optional path to write full triage JSON",
    )
    args = parser.parse_args(argv)

    drafts = load_drafts(args.drafts)
    labels = build_title_alias_index(args.root)
    hit_ranks = {} if args.titles_only else load_hit_ranks(
        args.per_question, config_id=args.config_id
    )
    rows = triage(
        drafts,
        labels,
        hit_ranks,
        require_hit_data=not args.titles_only,
    )

    promote = [r for r in rows if r.promote]
    hold = [r for r in rows if not r.promote]
    missing_any = [r for r in rows if r.missing_titles]
    miss10 = [r for r in rows if not r.missing_titles and not r.hit_at_10]

    print(f"Drafts: {len(rows)}")
    print(f"Promote: {len(promote)}")
    print(f"Hold: {len(hold)} (missing_titles={len(missing_any)}, miss_at_10={len(miss10)})")
    print()
    print("## Promote")
    for row in promote:
        hop = "multi" if row.multi_hop else "single"
        print(f"  {row.question_id}\trank={row.first_hit_rank}\t[{hop}]\t{row.query}")
    print()
    print("## Hold")
    for row in hold:
        print(
            f"  {row.question_id}\trank={row.first_hit_rank}\t"
            f"{','.join(row.reasons)}\tmissing={row.missing_titles}"
        )

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "config_id": args.config_id,
            "promote_ids": [r.question_id for r in promote],
            "hold_ids": [r.question_id for r in hold],
            "rows": [r.to_dict() for r in rows],
        }
        args.json_out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"\nWrote {args.json_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

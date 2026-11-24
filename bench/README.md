# Embedding / Reranker Benchmark

Compares retrieval quality across embedding models and an optional cross-encoder
reranker, using the **same** hybrid pipeline each time:

`semantic + BM25 + wikilink graph + authority bonus` → optional rerank(top-30 → top-10)

## Honesty note

The official eval set currently has **67 questions** (10 golden Phase 1 items plus
promoted drafts). Treat rankings as directional signals for this MVP corpus, not
as production model selection proof. The baseline regression gate still uses the
original Phase 1 ten questions.

Remaining draft questions live in `eval/questions_draft.json`. Promote candidates
with `python -m eval.triage_drafts` after a draft dry-run.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r bench/requirements.txt
# Or reuse the repo root requirements + bench extras
```

Embeddings and HF weights are cached under gitignored `rag_data/` and
`~/.cache/huggingface`. Never commit them.

## Run

```bash
# Reproduce Phase 1 baseline (Qwen3) on the official eval set
python -m bench.run_benchmark --configs baseline

# All local configs (skips hosted_ref unless OPENAI_API_KEY is set)
python -m bench.run_benchmark --all

# Explicit question set
python -m bench.run_benchmark --all --question-set original
python -m bench.run_benchmark --all --question-set both

# Sync README markers from RESULTS.md
python -m bench.update_readme
```

Default runtime embedder (`rag.embeddings.DEFAULT_MODEL_NAME` / `rag` CLI):
`Qwen/Qwen3-Embedding-0.6B`.

Outputs (committed when refreshed on purpose):

- `bench/results/latest.csv`
- `bench/results/latest.json`
- `bench/results/RESULTS.md`
- `bench/results/per_question.csv`

## Configs

See [`configs.yaml`](configs.yaml). Add a model by appending one entry.

| id | embedding | reranker |
|----|-----------|----------|
| baseline | Qwen3-Embedding-0.6B | none |
| minilm | all-MiniLM-L6-v2 | none |
| minilm_rr | all-MiniLM-L6-v2 | bge-reranker-v2-m3 |
| bge_m3 | BAAI/bge-m3 (dense) | none |
| bge_m3_rr | BAAI/bge-m3 | bge-reranker-v2-m3 |
| qwen3_rr | Qwen3-Embedding-0.6B | bge-reranker-v2-m3 |
| hosted_ref | text-embedding-3-small | none (needs `OPENAI_API_KEY`) |

## CI

`.github/workflows/bench.yml` runs unit tests on PRs touching `rag/`, `eval/`,
or `bench/`, and can run the CPU benchmark via `workflow_dispatch`. Results are
uploaded as artifacts. Committing results to the branch requires
`commit_results=true` on a manual dispatch—never on pull requests.

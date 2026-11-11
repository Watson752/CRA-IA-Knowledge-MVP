# Embedding / Reranker Benchmark

Compares retrieval quality across embedding models and an optional cross-encoder
reranker, using the **same** hybrid pipeline each time:

`semantic + BM25 + wikilink graph + authority bonus` → optional rerank(top-30 → top-10)

## Honesty note

The official eval set has **only 10 questions**. A Hit@1 difference of `0.10`
(one question) is **not statistically meaningful**. Treat rankings as directional
signals for this MVP corpus, not as production model selection proof.

Draft questions live in `eval/questions_draft.json` (`source: draft`) for review
before promotion into `eval/questions.json`.

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
# Reproduce Phase 1 baseline on the original 10 questions
python -m bench.run_benchmark --configs baseline

# All local configs (skips hosted_ref unless OPENAI_API_KEY is set)
python -m bench.run_benchmark --all

# Explicit question set
python -m bench.run_benchmark --all --question-set original
python -m bench.run_benchmark --all --question-set both

# Sync README markers from RESULTS.md
python -m bench.update_readme
```

Outputs (committed when refreshed on purpose):

- `bench/results/latest.csv`
- `bench/results/latest.json`
- `bench/results/RESULTS.md`
- `bench/results/per_question.csv`

## Configs

See [`configs.yaml`](configs.yaml). Add a model by appending one entry.

| id | embedding | reranker |
|----|-----------|----------|
| baseline | all-MiniLM-L6-v2 | none |
| minilm_rr | all-MiniLM-L6-v2 | bge-reranker-v2-m3 |
| bge_m3 | BAAI/bge-m3 (dense) | none |
| bge_m3_rr | BAAI/bge-m3 | bge-reranker-v2-m3 |
| qwen3 | Qwen3-Embedding-0.6B | none |
| qwen3_rr | Qwen3-Embedding-0.6B | bge-reranker-v2-m3 |
| hosted_ref | text-embedding-3-small | none (needs `OPENAI_API_KEY`) |

## CI

`.github/workflows/bench.yml` runs unit tests on PRs touching `rag/`, `eval/`,
or `bench/`, and can run the CPU benchmark via `workflow_dispatch`. Results are
uploaded as artifacts. Committing results to the branch requires
`commit_results=true` on a manual dispatch—never on pull requests.

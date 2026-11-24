# Embedding / Reranker Benchmark Results

Honesty note: the official eval set has 67 questions. Rankings are directional signals for this MVP corpus, not production model-selection proof. The baseline regression gate still uses the original Phase 1 ten questions.

- Generated: `2026-11-23T06:44:42.541491+00:00`
- Git commit: `0279fd86b8f0f10386e8ca4044cc8f2c01cc0fde`
- Hardware: `cpu`

## Official set (67 questions)

| config | embedding | reranker | status | Hit@1 | Hit@3 | Hit@5 | Recall@5 | Recall@10 | MRR | median_ms | index_s | hardware |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| bge_m3 | BAAI/bge-m3 | none | ok | 0.940 | 0.985 | 1.000 | 0.679 | 0.763 | 0.963 | 165.930 | 1.791 | cpu |
| **baseline (baseline)** | Qwen/Qwen3-Embedding-0.6B | none | ok | 0.925 | 0.985 | 0.985 | 0.687 | 0.785 | 0.958 | 172.980 | 4.183 | cpu |
| qwen3_rr | Qwen/Qwen3-Embedding-0.6B | BAAI/bge-reranker-v2-m3 | ok | 0.910 | 0.985 | 0.985 | 0.690 | 0.802 | 0.950 | 6021.960 | 3.958 | cpu |
| bge_m3_rr | BAAI/bge-m3 | BAAI/bge-reranker-v2-m3 | ok | 0.895 | 1.000 | 1.000 | 0.677 | 0.764 | 0.945 | 5219.540 | 5.434 | cpu |
| minilm | sentence-transformers/all-MiniLM-L6-v2 | none | ok | 0.895 | 0.985 | 0.985 | 0.667 | 0.775 | 0.940 | 14.800 | 11.205 | cpu |
| minilm_rr | sentence-transformers/all-MiniLM-L6-v2 | BAAI/bge-reranker-v2-m3 | ok | 0.866 | 0.985 | 0.985 | 0.665 | 0.776 | 0.928 | 5168.590 | 4.943 | cpu |

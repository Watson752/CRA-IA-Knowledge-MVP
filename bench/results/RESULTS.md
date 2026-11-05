# Embedding / Reranker Benchmark Results

Honesty note: the official eval set has only 10 questions. A Hit@1 difference of 0.10 (one question) is not statistically meaningful. Treat these rankings as directional signals for this MVP corpus, not as production model-selection proof.

- Generated: `2026-11-05T04:12:07.698548+00:00`
- Git commit: `2f9d10fd575ac9f49dd93c828ec33c33d878bbd1`
- Hardware: `cpu`

## Official set (original 10 questions)

| config | embedding | reranker | status | Hit@1 | Hit@3 | Hit@5 | Recall@5 | Recall@10 | MRR | median_ms | index_s | hardware |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| qwen3 | Qwen/Qwen3-Embedding-0.6B | none | ok | 0.900 | 0.900 | 0.900 | 0.590 | 0.820 | 0.911 | 146.030 | 239.398 | cpu |
| **baseline (baseline)** | sentence-transformers/all-MiniLM-L6-v2 | none | ok | 0.900 | 0.900 | 0.900 | 0.490 | 0.715 | 0.910 | 11.260 | 2.327 | cpu |
| bge_m3_rr | BAAI/bge-m3 | BAAI/bge-reranker-v2-m3 | ok | 0.700 | 0.900 | 1.000 | 0.440 | 0.670 | 0.825 | 26012.620 | 298.228 | cpu |
| bge_m3 | BAAI/bge-m3 | none | ok | 0.700 | 0.900 | 0.900 | 0.525 | 0.780 | 0.814 | 157.900 | 358.876 | cpu |
| minilm_rr | sentence-transformers/all-MiniLM-L6-v2 | BAAI/bge-reranker-v2-m3 | ok | 0.500 | 0.800 | 0.900 | 0.335 | 0.610 | 0.669 | 21128.850 | 3.263 | cpu |
| qwen3_rr | Qwen/Qwen3-Embedding-0.6B | BAAI/bge-reranker-v2-m3 | ok | 0.300 | 0.800 | 0.900 | 0.360 | 0.655 | 0.568 | 22852.550 | 201.844 | cpu |

# Embedding / Reranker Benchmark Results

Honesty note: the official eval set has only 10 questions. A Hit@1 difference of 0.10 (one question) is not statistically meaningful. Treat these rankings as directional signals for this MVP corpus, not as production model-selection proof.

- Generated: `2026-11-13T16:49:20.264198+00:00`
- Git commit: `75155bbe02a4b62a3d08b417017e9fe2e1214e98`
- Hardware: `cpu`

## Official set (original 10 questions)

| config | embedding | reranker | status | Hit@1 | Hit@3 | Hit@5 | Recall@5 | Recall@10 | MRR | median_ms | index_s | hardware |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| bge_m3 | BAAI/bge-m3 | none | ok | 0.900 | 0.900 | 1.000 | 0.610 | 0.780 | 0.920 | 270.340 | 1.503 | cpu |
| **baseline (baseline)** | sentence-transformers/all-MiniLM-L6-v2 | none | ok | 0.900 | 0.900 | 0.900 | 0.525 | 0.695 | 0.917 | 13.860 | 2.142 | cpu |
| qwen3 | Qwen/Qwen3-Embedding-0.6B | none | ok | 0.900 | 0.900 | 0.900 | 0.570 | 0.800 | 0.917 | 132.170 | 0.528 | cpu |
| bge_m3_rr | BAAI/bge-m3 | BAAI/bge-reranker-v2-m3 | ok | 0.800 | 1.000 | 1.000 | 0.610 | 0.760 | 0.900 | 12862.420 | 8.702 | cpu |
| minilm_rr | sentence-transformers/all-MiniLM-L6-v2 | BAAI/bge-reranker-v2-m3 | ok | 0.800 | 0.900 | 0.900 | 0.550 | 0.700 | 0.867 | 8734.530 | 7.291 | cpu |
| qwen3_rr | Qwen/Qwen3-Embedding-0.6B | BAAI/bge-reranker-v2-m3 | ok | 0.800 | 0.900 | 0.900 | 0.590 | 0.840 | 0.867 | 13388.000 | 7.663 | cpu |

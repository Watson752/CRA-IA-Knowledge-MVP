"""Load and filter benchmark configurations from configs.yaml."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from rag.embeddings import sanitize_model_id

BENCH_DIR = Path(__file__).resolve().parent
DEFAULT_CONFIG_PATH = BENCH_DIR / "configs.yaml"


@dataclass
class BenchConfig:
    id: str
    embedding_model: str
    provider: str = "sentence_transformers"
    reranker: str | None = None
    optional: bool = False
    env_key: str | None = None
    query_prompt_name: str | None = None
    mode: str = "hybrid_graph"
    top_k: int = 10
    rerank_pool: int = 30

    @property
    def cache_key(self) -> str:
        return sanitize_model_id(f"{self.id}__{self.embedding_model}")

    def is_available(self) -> bool:
        if not self.optional:
            return True
        if not self.env_key:
            return True
        return bool(os.environ.get(self.env_key))

    def skip_reason(self) -> str | None:
        if self.is_available():
            return None
        return f"optional config skipped: env var {self.env_key} not set"


def load_raw_config(path: Path | None = None) -> dict[str, Any]:
    path = path or DEFAULT_CONFIG_PATH
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or "configs" not in data:
        raise ValueError(f"Invalid bench config file: {path}")
    return data


def load_configs(
    path: Path | None = None,
    *,
    ids: list[str] | None = None,
    skip_optional: bool = False,
    include_unavailable: bool = False,
) -> list[BenchConfig]:
    data = load_raw_config(path)
    defaults = data.get("defaults") or {}
    configs: list[BenchConfig] = []
    for item in data["configs"]:
        cfg = BenchConfig(
            id=str(item["id"]),
            embedding_model=str(item["embedding_model"]),
            provider=str(item.get("provider") or "sentence_transformers"),
            reranker=item.get("reranker"),
            optional=bool(item.get("optional", False)),
            env_key=item.get("env_key"),
            query_prompt_name=item.get("query_prompt_name"),
            mode=str(item.get("mode") or defaults.get("mode") or "hybrid_graph"),
            top_k=int(item.get("top_k") or defaults.get("top_k") or 10),
            rerank_pool=int(item.get("rerank_pool") or defaults.get("rerank_pool") or 30),
        )
        if ids is not None and cfg.id not in ids:
            continue
        if skip_optional and cfg.optional:
            continue
        if not include_unavailable and not cfg.is_available():
            continue
        configs.append(cfg)
    return configs


def list_all_config_ids(path: Path | None = None) -> list[str]:
    data = load_raw_config(path)
    return [str(item["id"]) for item in data["configs"]]

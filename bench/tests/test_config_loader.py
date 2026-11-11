"""Unit tests for bench config loading (no model downloads)."""

from __future__ import annotations

import os
from pathlib import Path

import yaml

from bench.config_loader import load_configs, load_raw_config
from rag.embeddings import sanitize_model_id


def test_sanitize_model_id():
    assert sanitize_model_id("sentence-transformers/all-MiniLM-L6-v2") == (
        "sentence-transformers__all-MiniLM-L6-v2"
    )
    assert "/" not in sanitize_model_id("BAAI/bge-m3")


def test_load_configs_includes_baseline(tmp_path: Path):
    path = tmp_path / "configs.yaml"
    path.write_text(
        yaml.safe_dump(
            {
                "defaults": {"mode": "hybrid_graph", "top_k": 10, "rerank_pool": 30},
                "configs": [
                    {
                        "id": "baseline",
                        "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
                        "provider": "sentence_transformers",
                        "reranker": None,
                        "optional": False,
                    },
                    {
                        "id": "hosted_ref",
                        "embedding_model": "text-embedding-3-small",
                        "provider": "openai",
                        "optional": True,
                        "env_key": "OPENAI_API_KEY",
                    },
                ],
            }
        ),
        encoding="utf-8",
    )
    raw = load_raw_config(path)
    assert "configs" in raw
    # Without API key, optional unavailable configs are filtered by default.
    os.environ.pop("OPENAI_API_KEY", None)
    available = load_configs(path)
    assert [c.id for c in available] == ["baseline"]
    # include_unavailable keeps the optional row for skip recording.
    all_cfgs = load_configs(path, include_unavailable=True)
    assert [c.id for c in all_cfgs] == ["baseline", "hosted_ref"]
    assert all_cfgs[1].skip_reason() is not None
    # skip_optional drops hosted even if key present
    os.environ["OPENAI_API_KEY"] = "sk-test"
    try:
        skipped = load_configs(path, skip_optional=True)
        assert [c.id for c in skipped] == ["baseline"]
    finally:
        os.environ.pop("OPENAI_API_KEY", None)


def test_repo_configs_yaml_parses():
    cfgs = load_configs(include_unavailable=True)
    ids = [c.id for c in cfgs]
    assert "baseline" in ids
    assert "qwen3" in ids
    assert "hosted_ref" in ids

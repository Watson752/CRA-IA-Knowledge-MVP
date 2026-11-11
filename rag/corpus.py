"""Markdown corpus discovery and loading for Phase 1 retrieval."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from rag.links import AliasIndex, build_alias_index
from rag.metadata import (
    NoteRecord,
    is_excluded_path,
    is_knowledge_candidate,
    is_source_path,
    note_from_path,
)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RAG_DATA = ROOT / "rag_data"


@dataclass
class Corpus:
    """Loaded knowledge notes plus separately tracked source notes."""

    root: Path
    knowledge_notes: dict[str, NoteRecord] = field(default_factory=dict)
    source_notes: dict[str, NoteRecord] = field(default_factory=dict)
    alias_index: AliasIndex = field(default_factory=AliasIndex)
    unresolved_wikilinks: list[dict[str, str]] = field(default_factory=list)

    @property
    def notes(self) -> dict[str, NoteRecord]:
        """All notes available for graph resolution (knowledge + sources)."""
        merged = dict(self.knowledge_notes)
        merged.update(self.source_notes)
        return merged

    def summary(self) -> dict[str, Any]:
        by_domain: dict[str, int] = {}
        for note in self.knowledge_notes.values():
            key = note.primary_domain or "missing"
            by_domain[key] = by_domain.get(key, 0) + 1
        return {
            "knowledge_notes": len(self.knowledge_notes),
            "source_notes": len(self.source_notes),
            "unresolved_wikilinks": len(self.unresolved_wikilinks),
            "primary_domain_counts": dict(sorted(by_domain.items())),
        }


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.parts and ".venv" not in path.parts
    )


def load_corpus(root: Path | None = None) -> Corpus:
    """Parse included knowledge notes and separate source notes."""
    root = (root or ROOT).resolve()
    corpus = Corpus(root=root)

    parsed: list[NoteRecord] = []
    for path in iter_markdown_files(root):
        rel = str(path.relative_to(root)).replace("\\", "/")
        if is_excluded_path(rel):
            continue
        try:
            note = note_from_path(path, root)
        except Exception as exc:  # noqa: BLE001 - keep indexing resilient
            # Unreadable notes are skipped; indexing must not crash.
            corpus.unresolved_wikilinks.append(
                {"source": rel, "target": "", "classification": f"parse-error:{exc}"}
            )
            continue
        if is_source_path(rel):
            corpus.source_notes[note.note_id] = note
            parsed.append(note)
        elif is_knowledge_candidate(rel, note.primary_domain):
            corpus.knowledge_notes[note.note_id] = note
            parsed.append(note)

    # Alias index covers knowledge + sources so provenance links can resolve.
    corpus.alias_index = build_alias_index(parsed)

    for note in corpus.knowledge_notes.values():
        for target in note.wikilinks:
            resolved = corpus.alias_index.resolve(target)
            if resolved is None:
                corpus.unresolved_wikilinks.append(
                    {
                        "source": note.note_id,
                        "target": target,
                        "classification": "unresolved",
                    }
                )
    return corpus


def save_corpus_manifest(corpus: Corpus, out_dir: Path | None = None) -> Path:
    out_dir = out_dir or DEFAULT_RAG_DATA
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "corpus_manifest.json"
    payload = {
        "summary": corpus.summary(),
        "knowledge_notes": [n.to_dict() for n in corpus.knowledge_notes.values()],
        "source_notes": [n.to_dict() for n in corpus.source_notes.values()],
        "unresolved_wikilinks": corpus.unresolved_wikilinks,
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def load_corpus_manifest(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def note_records_from_manifest(payload: dict[str, Any]) -> tuple[dict[str, NoteRecord], dict[str, NoteRecord]]:
    def revive(items: list[dict[str, Any]]) -> dict[str, NoteRecord]:
        out: dict[str, NoteRecord] = {}
        for item in items:
            note = NoteRecord(**item)
            out[note.note_id] = note
        return out

    return revive(payload.get("knowledge_notes", [])), revive(payload.get("source_notes", []))

"""Heading-based Markdown chunking with local context preservation."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from rag.corpus import DEFAULT_RAG_DATA, Corpus
from rag.metadata import NoteRecord

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", flags=re.MULTILINE)
MIN_CHUNK_CHARS = 220
MAX_CHUNK_CHARS = 2800


@dataclass
class Chunk:
    chunk_id: str
    note_id: str
    note_title: str
    note_path: str
    heading: str
    heading_path: list[str] = field(default_factory=list)
    text: str = ""
    primary_domain: str | None = None
    note_type: str | None = None
    content_origin: str | None = None
    authoritative: bool | None = None
    source_urls: list[str] = field(default_factory=list)
    related_sources: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @property
    def embed_text(self) -> str:
        heading = self.heading or self.note_title
        return f"{self.note_title}\n{heading}\n{self.text}".strip()


def _chunk_id(note_id: str, heading: str, ordinal: int) -> str:
    raw = f"{note_id}::{ordinal}::{heading}"
    digest = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:12]
    return f"{note_id}#{ordinal}-{digest}"


def _split_sections(body: str) -> list[tuple[str, list[str], str]]:
    """Return (heading, heading_path, section_text) segments."""
    matches = list(HEADING_RE.finditer(body))
    if not matches:
        text = body.strip()
        return [("", [], text)] if text else []

    sections: list[tuple[str, list[str], str]] = []
    stack: list[tuple[int, str]] = []

    # Preamble before first heading.
    preamble = body[: matches[0].start()].strip()
    if preamble:
        sections.append(("", [], preamble))

    for idx, match in enumerate(matches):
        level = len(match.group(1))
        heading = match.group(2).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        text = body[start:end].strip()

        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, heading))
        heading_path = [h for _, h in stack]
        sections.append((heading, heading_path, text))
    return sections


def _merge_small_sections(
    sections: list[tuple[str, list[str], str]],
) -> list[tuple[str, list[str], str]]:
    if not sections:
        return []
    merged: list[tuple[str, list[str], str]] = []
    for heading, path, text in sections:
        if not text:
            continue
        if merged and len(text) < MIN_CHUNK_CHARS:
            prev_h, prev_path, prev_text = merged[-1]
            combined = f"{prev_text}\n\n## {heading}\n{text}".strip() if heading else f"{prev_text}\n\n{text}".strip()
            if len(combined) <= MAX_CHUNK_CHARS:
                label = prev_h if prev_h else heading
                merged[-1] = (label, prev_path or path, combined)
                continue
        merged.append((heading, path, text))

    # If still tiny after merge, fold into previous when possible.
    final: list[tuple[str, list[str], str]] = []
    for heading, path, text in merged:
        if final and len(text) < MIN_CHUNK_CHARS // 2:
            prev_h, prev_path, prev_text = final[-1]
            combined = f"{prev_text}\n\n{text}".strip()
            if len(combined) <= MAX_CHUNK_CHARS:
                final[-1] = (prev_h or heading, prev_path or path, combined)
                continue
        final.append((heading, path, text))
    return final


def chunk_note(note: NoteRecord) -> list[Chunk]:
    sections = _merge_small_sections(_split_sections(note.body_text))
    if not sections:
        text = note.body_text.strip() or note.title
        sections = [("", [], text)]

    chunks: list[Chunk] = []
    for ordinal, (heading, path, text) in enumerate(sections):
        # Keep a short title breadcrumb for context.
        if heading and note.title not in text[:120]:
            context = f"{note.title} — {heading}\n\n{text}"
        elif not heading:
            context = text
        else:
            context = f"{heading}\n\n{text}"
        chunks.append(
            Chunk(
                chunk_id=_chunk_id(note.note_id, heading or note.title, ordinal),
                note_id=note.note_id,
                note_title=note.title,
                note_path=note.path,
                heading=heading or note.title,
                heading_path=path or ([note.title] if not heading else path),
                text=context.strip(),
                primary_domain=note.primary_domain,
                note_type=note.note_type,
                content_origin=note.content_origin,
                authoritative=note.authoritative,
                source_urls=list(note.source_urls),
                related_sources=list(note.related_sources),
            )
        )
    return chunks


def chunk_corpus(corpus: Corpus) -> list[Chunk]:
    chunks: list[Chunk] = []
    for note in sorted(corpus.knowledge_notes.values(), key=lambda n: n.note_id):
        chunks.extend(chunk_note(note))
    return chunks


def save_chunks(chunks: list[Chunk], out_dir: Path | None = None) -> Path:
    out_dir = out_dir or DEFAULT_RAG_DATA
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "chunks.json"
    payload = {
        "chunk_count": len(chunks),
        "chunks": [c.to_dict() for c in chunks],
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def load_chunks(path: Path | None = None) -> list[Chunk]:
    path = path or (DEFAULT_RAG_DATA / "chunks.json")
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [Chunk(**item) for item in payload["chunks"]]

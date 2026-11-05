"""Wikilink extraction and alias → canonical note resolution."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rag.metadata import NoteRecord

# Obsidian wikilinks; ignore images (![[...]]) and do not match Markdown links.
WIKILINK_RE = re.compile(r"(?<!\!)\[\[([^\]]+)\]\]")
CODE_FENCE_RE = re.compile(r"```.*?```", flags=re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")


def strip_code_regions(text: str) -> str:
    """Remove fenced and inline code so link extraction ignores examples."""
    without_fences = CODE_FENCE_RE.sub(" ", text)
    return INLINE_CODE_RE.sub(" ", without_fences)


def normalize_link_target(raw: str) -> str:
    """Normalize a wikilink target to a lookup key (no alias display, no heading)."""
    raw = raw.replace("\\|", "|").strip()
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    if target.endswith(".md"):
        target = target[:-3]
    return target


def extract_wikilinks(body: str) -> list[str]:
    """Extract unique Obsidian wikilink targets from note body text."""
    cleaned = strip_code_regions(body)
    seen: set[str] = set()
    out: list[str] = []
    for match in WIKILINK_RE.findall(cleaned):
        target = normalize_link_target(match)
        if not target:
            continue
        key = target.casefold()
        if key in seen:
            continue
        seen.add(key)
        out.append(target)
    return out


@dataclass
class AliasIndex:
    """Maps titles, aliases, and path stems to a single canonical note_id."""

    title_to_ids: dict[str, list[str]] = field(default_factory=dict)
    alias_to_ids: dict[str, list[str]] = field(default_factory=dict)
    stem_to_ids: dict[str, list[str]] = field(default_factory=dict)
    path_to_id: dict[str, str] = field(default_factory=dict)

    def add(self, note: NoteRecord) -> None:
        self.path_to_id[note.path.casefold()] = note.note_id
        self.path_to_id[note.note_id.casefold()] = note.note_id
        self._append(self.title_to_ids, note.title.casefold(), note.note_id)
        stem = note.filename.removesuffix(".md")
        self._append(self.stem_to_ids, stem.casefold(), note.note_id)
        for alias in note.aliases:
            self._append(self.alias_to_ids, alias.casefold(), note.note_id)

    @staticmethod
    def _append(index: dict[str, list[str]], key: str, note_id: str) -> None:
        if not key:
            return
        bucket = index.setdefault(key, [])
        if note_id not in bucket:
            bucket.append(note_id)

    def resolve(self, target: str) -> str | None:
        """Resolve a wikilink/alias/path to a canonical note_id, or None if unresolved."""
        if not target:
            return None
        normalized = normalize_link_target(target)
        key = normalized.casefold()

        if key in self.path_to_id:
            return self.path_to_id[key]

        # Path-style links: folder/Note
        if "/" in normalized:
            path_key = normalized.casefold()
            if path_key in self.path_to_id:
                return self.path_to_id[path_key]
            with_md = f"{path_key}.md"
            if with_md in self.path_to_id:
                return self.path_to_id[with_md]

        candidates: list[str] = []
        for index in (self.title_to_ids, self.alias_to_ids, self.stem_to_ids):
            for note_id in index.get(key, []):
                if note_id not in candidates:
                    candidates.append(note_id)

        if len(candidates) == 1:
            return candidates[0]
        # Ambiguous or missing: leave unresolved rather than guessing.
        return None


def build_alias_index(notes: list[NoteRecord]) -> AliasIndex:
    index = AliasIndex()
    for note in notes:
        index.add(note)
    return index

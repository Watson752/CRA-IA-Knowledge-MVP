"""YAML frontmatter and note metadata helpers for the Obsidian vault."""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

URL_RE = re.compile(r"https?://[^\s<>)\]]+")

KNOWLEDGE_DOMAINS = frozenset(
    {
        "audit",
        "bridge",
        "case",
        "organization-business",
        "risk-control",
        "software-data",
        "statistics-analytics",
    }
)

EXCLUDED_DIR_PREFIXES = (
    "00-Start/",
    "14-Templates/",
    "15-Governance/",
    "16-Testing/",
)

ROOT_EXCLUDED_NAMES = frozenset(
    {
        "README.md",
        "MVP_REPORT.md",
        "PROJECT_PLAN.md",
        "RESEARCH_LOG.md",
        "VALIDATION_REPORT.md",
        "METADATA_VALIDATION_REPORT.md",
        "ORGANIZATION_VALIDATION_REPORT.md",
    }
)


def scalar(value: str) -> Any:
    value = value.strip()
    if not value or value in {"null", "Null", "NULL", "~"}:
        return None
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        return [scalar(item) for item in value[1:-1].split(",") if item.strip()]
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Parse the simple YAML subset used by this vault."""
    if not text.startswith("---\n"):
        return {}, text
    match = re.search(r"^---\s*$", text[4:], re.MULTILINE)
    if not match:
        return {}, text
    end = 4 + match.start()
    raw = text[4:end]
    body = text[4 + match.end() :]
    data: dict[str, Any] = {}
    key: str | None = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        item = re.match(r"^\s*-\s+(.*)$", line)
        if item and key:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(scalar(item.group(1)))
            continue
        if re.match(r"^\s*\[\]\s*$", line) and key:
            data[key] = []
            continue
        match_key = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if not match_key:
            continue
        key, raw_value = match_key.groups()
        data[key] = [] if raw_value is None or not raw_value.strip() else scalar(raw_value)
    return data, body


def as_str_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value] if value.strip() else []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [str(value).strip()]


def extract_source_urls(meta: dict[str, Any], body: str) -> list[str]:
    values: list[str] = []
    for field_name in ("source_url", "official_url", "url"):
        value = meta.get(field_name)
        if isinstance(value, str) and value.strip():
            values.append(value.strip())
    values.extend(URL_RE.findall(body))
    # Preserve order, drop duplicates.
    seen: set[str] = set()
    out: list[str] = []
    for url in values:
        if url not in seen:
            seen.add(url)
            out.append(url)
    return out


def extract_headings(body: str) -> list[dict[str, Any]]:
    headings: list[dict[str, Any]] = []
    for match in re.finditer(r"^(#{1,6})\s+(.+?)\s*$", body, flags=re.MULTILINE):
        headings.append(
            {
                "level": len(match.group(1)),
                "text": match.group(2).strip(),
                "offset": match.start(),
            }
        )
    return headings


@dataclass
class NoteRecord:
    """Canonical parsed note used by indexing and retrieval."""

    note_id: str
    path: str
    filename: str
    title: str
    aliases: list[str] = field(default_factory=list)
    note_type: str | None = None
    primary_domain: str | None = None
    domains: list[str] = field(default_factory=list)
    classification: str | None = None
    content_origin: str | None = None
    authoritative: bool | None = None
    review_status: str | None = None
    official_source: Any = None
    official_government_source: Any = None
    publisher: str | None = None
    publication_date: Any = None
    source_url: str | None = None
    source_status: str | None = None
    related_sources: list[str] = field(default_factory=list)
    wikilinks: list[str] = field(default_factory=list)
    headings: list[dict[str, Any]] = field(default_factory=list)
    body_text: str = ""
    source_urls: list[str] = field(default_factory=list)
    corpus_role: str = "knowledge"  # knowledge | source

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def is_excluded_path(rel: str) -> bool:
    if rel in ROOT_EXCLUDED_NAMES:
        return True
    if any(part.endswith("REPORT.md") for part in [Path(rel).name]) and "/" not in rel:
        return True
    if any(rel.startswith(prefix) for prefix in EXCLUDED_DIR_PREFIXES):
        return True
    return False


def is_source_path(rel: str) -> bool:
    return rel.startswith("99-Sources/")


def is_knowledge_candidate(rel: str, primary_domain: str | None) -> bool:
    if is_excluded_path(rel) or is_source_path(rel):
        return False
    return (primary_domain or "").lower() in KNOWLEDGE_DOMAINS


def note_from_path(path: Path, root: Path) -> NoteRecord:
    from rag.links import extract_wikilinks

    rel = str(path.relative_to(root)).replace("\\", "/")
    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    title = str(meta.get("title") or path.stem).strip()
    aliases = as_str_list(meta.get("aliases"))
    domains = as_str_list(meta.get("domains"))
    related_sources = as_str_list(meta.get("related_sources"))
    primary = meta.get("primary_domain")
    primary_s = str(primary).strip() if primary is not None else None
    role = "source" if is_source_path(rel) else "knowledge"
    return NoteRecord(
        note_id=rel.removesuffix(".md"),
        path=rel,
        filename=path.name,
        title=title,
        aliases=aliases,
        note_type=str(meta.get("note_type")) if meta.get("note_type") is not None else None,
        primary_domain=primary_s,
        domains=domains,
        classification=(
            str(meta.get("classification")) if meta.get("classification") is not None else None
        ),
        content_origin=(
            str(meta.get("content_origin")) if meta.get("content_origin") is not None else None
        ),
        authoritative=meta.get("authoritative") if isinstance(meta.get("authoritative"), bool) else None,
        review_status=(
            str(meta.get("review_status")) if meta.get("review_status") is not None else None
        ),
        official_source=meta.get("official_source"),
        official_government_source=meta.get("official_government_source"),
        publisher=str(meta.get("publisher")) if meta.get("publisher") is not None else None,
        publication_date=meta.get("publication_date"),
        source_url=str(meta.get("source_url")) if meta.get("source_url") is not None else None,
        source_status=str(meta.get("source_status")) if meta.get("source_status") is not None else None,
        related_sources=related_sources,
        wikilinks=extract_wikilinks(body),
        headings=extract_headings(body),
        body_text=body.strip(),
        source_urls=extract_source_urls(meta, body),
        corpus_role=role,
    )

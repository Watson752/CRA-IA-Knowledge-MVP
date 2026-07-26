#!/usr/bin/env python3
"""Read-only validator for the CRA IA Obsidian vault.

It never alters vault notes.  Its only writes are the generated diagnostic
artifacts under 16-Testing/Consistency/Reports/, as requested by this MVP.
Run: python scripts/validate_vault.py [--label baseline|final]
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "16-Testing" / "Consistency" / "Reports"
ALLOWED_PRIMARY = {
    "case", "bridge", "audit", "risk-control", "software-data",
    "statistics-analytics", "organization-business", "source", "governance",
    "navigation", "template",
}
ALLOWED_DOMAINS = {
    "audit", "organization", "business", "software", "data", "statistics",
    "risk", "control", "governance", "case", "source", "ai",
}
INFRA_TYPES = {"navigation", "governance", "source", "template", "testing", "report"}
LINK_RE = re.compile(r"(?<!\!)\[\[([^\]]+)\]\]")
URL_RE = re.compile(r"https?://[^\s<>)\]]+")


def vault_files() -> list[Path]:
    return sorted(
        path for path in ROOT.rglob("*.md")
        if not any(part == ".git" for part in path.parts)
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
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str, list[str]]:
    """Parse the simple YAML subset used by this vault and detect duplicate keys."""
    if not text.startswith("---\n"):
        return {}, text, ["missing-frontmatter"]
    match = re.search(r"^---\s*$", text[4:], re.MULTILINE)
    if not match:
        return {}, text, ["unclosed-frontmatter"]
    end = 4 + match.start()
    raw = text[4:end]
    body = text[4 + match.end():]
    data: dict[str, Any] = {}
    errors: list[str] = []
    key: str | None = None
    for lineno, line in enumerate(raw.splitlines(), 2):
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
            errors.append(f"malformed-yaml-line:{lineno}")
            continue
        key, raw_value = match_key.groups()
        if key in data:
            errors.append(f"duplicate-yaml-key:{key}")
        data[key] = [] if raw_value is None or not raw_value.strip() else scalar(raw_value)
    return data, body, errors


def title_for(path: Path, meta: dict[str, Any]) -> str:
    return str(meta.get("title") or path.stem).strip()


def link_target(raw: str) -> str:
    raw = raw.replace("\\|", "|").strip()
    raw = raw.split("|", 1)[0].split("#", 1)[0].strip()
    return raw


def classify(path: Path, meta: dict[str, Any]) -> str:
    note_type = str(meta.get("note_type", "")).lower()
    primary = str(meta.get("primary_domain", "")).lower()
    content_role = str(meta.get("content_role", "")).lower()
    rel = str(path.relative_to(ROOT))
    if rel == "README.md":
        return "project-documentation"
    if meta.get("include_in_graph") is False or content_role in {"report", "backup", "testing"}:
        return "report" if content_role == "report" or note_type == "report" else "testing"
    if rel.startswith("16-Testing/") or note_type == "testing":
        return "testing"
    if note_type == "report" or rel.endswith("REPORT.md"):
        return "report"
    if primary == "source" or note_type == "source":
        return "source"
    if primary == "governance" or note_type == "governance":
        return "governance"
    if primary == "navigation" or note_type in {"navigation", "learning-path"}:
        return "navigation"
    if primary == "template" or note_type == "template":
        return "template"
    return "substantive-knowledge"


def source_links(meta: dict[str, Any], body: str) -> list[str]:
    values: list[str] = []
    for field in ("source_url", "official_url", "url"):
        value = meta.get(field)
        if isinstance(value, str) and value:
            values.append(value)
    return sorted(set(values + URL_RE.findall(body)))


def compact(value: Any) -> str:
    if isinstance(value, list):
        return "; ".join(str(x) for x in value)
    return "" if value is None else str(value)


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    return "| " + " | ".join(headers) + " |\n|" + "|".join("---" for _ in headers) + "|\n" + "\n".join(
        "| " + " | ".join(value.replace("|", "\\|").replace("\n", " ") for value in row) + " |" for row in rows
    ) + "\n"


def run(label: str) -> dict[str, Any]:
    files = vault_files()
    notes: dict[str, dict[str, Any]] = {}
    title_index: dict[str, list[str]] = collections.defaultdict(list)
    alias_index: dict[str, list[str]] = collections.defaultdict(list)
    stem_index: dict[str, list[str]] = collections.defaultdict(list)

    for path in files:
        rel = str(path.relative_to(ROOT))
        text = path.read_text(encoding="utf-8")
        meta, body, yaml_errors = parse_frontmatter(text)
        title = title_for(path, meta)
        aliases = meta.get("aliases", [])
        if isinstance(aliases, str):
            aliases = [aliases]
        if not isinstance(aliases, list):
            aliases = []
            yaml_errors.append("aliases-not-list")
        domains = meta.get("domains")
        if not isinstance(domains, list):
            domains = []
        links = [link_target(item) for item in LINK_RE.findall(text)]
        record = {
            "path": rel, "title": title, "aliases": aliases, "note_type": meta.get("note_type"),
            "primary_domain": meta.get("primary_domain"), "domains": domains,
            "classification": meta.get("classification"), "content_origin": meta.get("content_origin"),
            "review_status": meta.get("review_status"), "outgoing_links": sorted(set(links)),
            "source_links": source_links(meta, body), "word_count": len(re.findall(r"\b[\w'-]+\b", body)),
            "classification_type": classify(path, meta), "yaml_errors": yaml_errors,
            "has_frontmatter": not ("missing-frontmatter" in yaml_errors),
            "body": body, "meta": meta,
        }
        notes[rel] = record
        title_index[title.casefold()].append(rel)
        stem_index[path.stem.casefold()].append(rel)
        for alias in dict.fromkeys(aliases):
            if isinstance(alias, str) and alias.strip():
                alias_index[alias.strip().casefold()].append(rel)

    incoming: dict[str, list[str]] = collections.defaultdict(list)
    unresolved: list[dict[str, str]] = []
    all_names = {**title_index, **stem_index}
    for rel, record in notes.items():
        for target in record["outgoing_links"]:
            key = target.casefold()
            candidates = set(title_index.get(key, []) + alias_index.get(key, []) + stem_index.get(key, []))
            if "/" in target:
                normalized = target.removesuffix(".md").casefold()
                candidates.update(
                    note_rel for note_rel in notes
                    if note_rel.removesuffix(".md").casefold() == normalized
                )
            if len(candidates) == 1:
                incoming[next(iter(candidates))].append(rel)
            elif not candidates:
                kind = "filename mismatch" if "/" in target else "substantive missing concept"
                unresolved.append({"source": rel, "target": target, "classification": kind})
            else:
                unresolved.append({"source": rel, "target": target, "classification": "ambiguous and requires review"})

    for rel, record in notes.items():
        record["incoming_links"] = sorted(set(incoming.get(rel, [])))
        record["orphan"] = (
            record["classification_type"] == "substantive-knowledge"
            and not record["incoming_links"] and not record["outgoing_links"]
        )
        record["one_way"] = (
            record["classification_type"] == "substantive-knowledge"
            and (not record["incoming_links"] or not record["outgoing_links"])
        )
        record["invalid_primary_domain"] = (
            record["classification_type"] == "substantive-knowledge"
            and record["primary_domain"] not in ALLOWED_PRIMARY - {"source", "governance", "navigation", "template"}
        )
        record["missing_domains"] = record["classification_type"] == "substantive-knowledge" and not record["domains"]
        record["invalid_domains"] = (
            sorted(set(record["domains"]) - ALLOWED_DOMAINS)
            if record["classification_type"] == "substantive-knowledge" else []
        )
        record["quality"] = (
            "placeholder" if record["classification_type"] == "substantive-knowledge" and record["word_count"] < 35
            else "weak" if record["classification_type"] == "substantive-knowledge" and record["word_count"] < 90
            else "adequate"
        )

    duplicate_titles = {key: paths for key, paths in title_index.items() if len(paths) > 1}
    alias_conflicts = {key: paths for key, paths in alias_index.items() if len(paths) > 1}
    note_type_counts = collections.Counter(str(r["note_type"] or "missing") for r in notes.values())
    domain_counts = collections.Counter(str(r["primary_domain"] or "missing") for r in notes.values())
    folder_counts = collections.Counter(rel.split("/", 1)[0] for rel in notes)
    summary = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "label": label, "total_markdown_files": len(notes),
        "substantive_knowledge_notes": sum(r["classification_type"] == "substantive-knowledge" for r in notes.values()),
        "infrastructure_files": sum(r["classification_type"] != "substantive-knowledge" for r in notes.values()),
        "missing_frontmatter": sorted(rel for rel, r in notes.items() if not r["has_frontmatter"]),
        "malformed_yaml": {rel: r["yaml_errors"] for rel, r in notes.items() if r["yaml_errors"] and r["yaml_errors"] != ["missing-frontmatter"]},
        "invalid_primary_domains": sorted(rel for rel, r in notes.items() if r["invalid_primary_domain"]),
        "missing_domains": sorted(rel for rel, r in notes.items() if r["missing_domains"]),
        "invalid_domains": {rel: r["invalid_domains"] for rel, r in notes.items() if r["invalid_domains"]},
        "unresolved_links": unresolved, "orphan_substantive_notes": sorted(rel for rel, r in notes.items() if r["orphan"]),
        "one_way_substantive_notes": sorted(rel for rel, r in notes.items() if r["one_way"]),
        "duplicate_titles": duplicate_titles, "alias_conflicts": alias_conflicts,
        "weak_or_placeholder": {rel: r["quality"] for rel, r in notes.items() if r["quality"] in {"weak", "placeholder"}},
        "folder_counts": dict(sorted(folder_counts.items())), "note_type_counts": dict(sorted(note_type_counts.items())),
        "primary_domain_counts": dict(sorted(domain_counts.items())),
    }

    REPORTS.mkdir(parents=True, exist_ok=True)
    suffix = "" if label == "final" else f"_{label.upper()}"
    (REPORTS / f"AUTOMATED_VALIDATION{suffix}.json").write_text(
        json.dumps({"summary": summary, "notes": notes}, indent=2, default=str) + "\n", encoding="utf-8"
    )
    report_lines = [
        "---", f'title: "Automated Vault Validation ({label.title()})"', "note_type: report", "primary_domain: governance",
        "domains:", "  - governance", "  - source", "classification: public", "content_origin: derived-analysis",
        "authoritative: false", "official_source: false", "review_status: analytical-draft", "---", "",
        "# Automated Vault Validation", "",
        f"Generated locally without network access on {summary['generated_at']}. Label: **{label}**.", "",
        "## Summary", "",
        markdown_table(["Metric", "Count"], [
            ["Markdown files", str(summary["total_markdown_files"])],
            ["Substantive knowledge notes", str(summary["substantive_knowledge_notes"])],
            ["Infrastructure files", str(summary["infrastructure_files"])],
            ["Missing YAML", str(len(summary["missing_frontmatter"]))],
            ["Malformed YAML", str(len(summary["malformed_yaml"]))],
            ["Invalid primary domains", str(len(summary["invalid_primary_domains"]))],
            ["Missing domains arrays", str(len(summary["missing_domains"]))],
            ["Invalid domains values", str(len(summary["invalid_domains"]))],
            ["Unresolved or ambiguous wikilinks", str(len(summary["unresolved_links"]))],
            ["Substantive orphans", str(len(summary["orphan_substantive_notes"]))],
            ["Duplicate titles", str(len(summary["duplicate_titles"]))],
            ["Alias conflicts", str(len(summary["alias_conflicts"]))],
        ]),
        "## Counts by folder", "", markdown_table(["Folder", "Files"], [[k, str(v)] for k, v in summary["folder_counts"].items()]),
        "## Counts by note type", "", markdown_table(["Note type", "Files"], [[k, str(v)] for k, v in summary["note_type_counts"].items()]),
        "## Counts by primary domain", "", markdown_table(["Primary domain", "Files"], [[k, str(v)] for k, v in summary["primary_domain_counts"].items()]),
        "## Unresolved links", "",
        markdown_table(["Source", "Target", "Classification"], [[x["source"], x["target"], x["classification"]] for x in unresolved] or [["None", "", ""]]),
        "## Notes requiring review", "",
        markdown_table(["Category", "Paths"], [
            ["Missing YAML", "; ".join(summary["missing_frontmatter"]) or "None"],
            ["Invalid primary domain", "; ".join(summary["invalid_primary_domains"]) or "None"],
            ["Missing domains", "; ".join(summary["missing_domains"]) or "None"],
            ["Substantive orphans", "; ".join(summary["orphan_substantive_notes"]) or "None"],
        ]),
    ]
    (REPORTS / f"AUTOMATED_VALIDATION{suffix}.md").write_text("\n".join(report_lines), encoding="utf-8")
    inventory_rows = [
        [
            r["path"], r["title"], compact(r["aliases"]), compact(r["note_type"]),
            compact(r["primary_domain"]), compact(r["domains"]), compact(r["classification"]),
            compact(r["content_origin"]), compact(r["review_status"]),
            "; ".join(r["outgoing_links"]), "; ".join(r["incoming_links"]),
            "; ".join(r["source_links"]), str(r["word_count"]), r["classification_type"],
            "yes" if r["orphan"] else "no", "; ".join(r["yaml_errors"]) or "no",
        ]
        for r in notes.values()
    ]
    inventory = [
        "---", f'title: "Vault Inventory ({label.title()})"', "note_type: report", "primary_domain: governance",
        "domains:", "  - governance", "  - source", "classification: public",
        "content_origin: derived-analysis", "authoritative: false", "official_source: false",
        "review_status: analytical-draft", "---", "", "# Vault Inventory", "",
        f"Generated from the local validator ({label}); backup copies are excluded from inventory.", "",
        markdown_table(
            ["Path", "Title", "Aliases", "Note type", "Primary domain", "Domains", "Classification",
             "Content origin", "Review status", "Outgoing Wikilinks", "Incoming Wikilinks",
             "Source links", "Words", "Class", "Orphan", "Malformed metadata"],
            inventory_rows,
        ),
    ]
    (REPORTS / f"VAULT_INVENTORY{suffix}.md").write_text("\n".join(inventory), encoding="utf-8")
    unresolved_report = [
        "---", f'title: "Unresolved Link Report ({label.title()})"', "note_type: report", "primary_domain: governance",
        "domains:", "  - governance", "classification: public", "content_origin: derived-analysis",
        "authoritative: false", "official_source: false", "review_status: analytical-draft", "---", "",
        "# Unresolved Link Report", "",
        f"Baseline/final validator label: **{label}**. Count: **{len(unresolved)}**.", "",
        markdown_table(["Source", "Target", "Classification"], [[x["source"], x["target"], x["classification"]] for x in unresolved] or [["None", "", ""]]),
        "## Interpretation", "", "Targets classified as ambiguous require canonical-path review; this report does not treat every duplicate title as a missing concept.",
    ]
    (REPORTS / f"UNRESOLVED_LINK_REPORT{suffix}.md").write_text("\n".join(unresolved_report), encoding="utf-8")
    orphan_rows = [
        [rel, notes[rel]["title"], "zero incoming and outgoing", "Substantive; repair or explicitly exclude"]
        for rel in summary["orphan_substantive_notes"]
    ] + [
        [rel, notes[rel]["title"], "one-way graph connection", "Review for meaningful map/backlink"]
        for rel in summary["one_way_substantive_notes"] if rel not in summary["orphan_substantive_notes"]
    ]
    orphan_report = [
        "---", f'title: "Orphan Report ({label.title()})"', "note_type: report", "primary_domain: governance",
        "domains:", "  - governance", "classification: public", "content_origin: derived-analysis",
        "authoritative: false", "official_source: false", "review_status: analytical-draft", "---", "",
        "# Orphan Report", "", f"Baseline/final validator label: **{label}**.", "",
        markdown_table(["Path", "Title", "Condition", "Disposition"], orphan_rows or [["None", "", "", ""]]),
    ]
    (REPORTS / f"ORPHAN_REPORT{suffix}.md").write_text("\n".join(orphan_report), encoding="utf-8")
    if label == "final":
        (REPORTS / "AUTOMATED_VALIDATION.json").write_text(
            json.dumps({"summary": summary, "notes": notes}, indent=2, default=str) + "\n", encoding="utf-8"
        )
        (REPORTS / "AUTOMATED_VALIDATION.md").write_text("\n".join(report_lines), encoding="utf-8")
        (REPORTS / "VAULT_INVENTORY.md").write_text("\n".join(inventory), encoding="utf-8")
        (REPORTS / "UNRESOLVED_LINK_REPORT.md").write_text("\n".join(unresolved_report), encoding="utf-8")
        (REPORTS / "ORPHAN_REPORT.md").write_text("\n".join(orphan_report), encoding="utf-8")
    return {"summary": summary, "notes": notes}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate the Obsidian vault without modifying vault notes.")
    parser.add_argument("--label", choices=("baseline", "final"), default="final")
    args = parser.parse_args()
    result = run(args.label)
    print(json.dumps({
        "markdown_files": result["summary"]["total_markdown_files"],
        "unresolved_links": len(result["summary"]["unresolved_links"]),
        "substantive_orphans": len(result["summary"]["orphan_substantive_notes"]),
    }))

"""Phase 2 grounded answer generation over Phase 1 retrieval."""

from __future__ import annotations

import os
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from rag.corpus import ROOT, Corpus
from rag.retrieve import RetrievalResponse, RetrievalResult, Retriever

DEFAULT_CHAT_MODEL = os.environ.get("OPENAI_CHAT_MODEL", "gpt-4.1-mini")
MAX_CONTEXT_CHARS = 12_000
MAX_CHUNK_CHARS = 1_200

GOVERNANCE_FILES = (
    "15-Governance/Grounded-Audit-Inquiry-Guidelines.md",
    "15-Governance/Public-Source-RAG-Grounding.md",
)

FORBIDDEN_PATTERNS = (
    re.compile(r"\bcra currently fails\b", re.I),
    re.compile(r"\bproves?\s+(?:that\s+)?(?:cra\s+)?non[- ]compliance\b", re.I),
    re.compile(r"\bprove(?:s|d)?\s+cra currently\b", re.I),
    re.compile(r"\bdeclares?\s+(?:a\s+)?finding\b", re.I),
    re.compile(r"\bthis (?:is|constitutes) (?:a )?finding of non[- ]compliance\b", re.I),
    # Affirm unsupported EFMS access-cert claim as established fact (not mere quotation).
    re.compile(
        r"\b(?:the\s+)?efms\s+(?:report\s+)?(?:found|identified|showed|confirmed)\s+"
        r"failed\s+access\s+certifications\b",
        re.I,
    ),
)

# Negative-eval / refusal quality: answer should explicitly correct unsupported claims.
CORRECTION_PATTERNS = (
    re.compile(
        r"\b(?:does not|do not|don't|cannot|can't|did not|didn't|is not|are not|was not|were not)\b"
        r".{0,100}\b(?:support|supported|state|say|show|prove|confirm|mention|contain)\b",
        re.I | re.S,
    ),
    re.compile(
        r"\bnot(?:\s+\w+){0,3}\s+"
        r"(?:what|stated|supported|found|accurate|correct|true)\b",
        re.I,
    ),
    re.compile(
        r"\b(?:no (?:evidence|public (?:source|evidence|report)|such finding)|"
        r"unsupported|incorrect|inaccurate|false claim|misstates?|"
        r"user statement|not directly supported)\b",
        re.I,
    ),
)

SYSTEM_PREFIX = """You are a grounded Internal Audit assistant over a public-only CRA knowledge vault.

Mandatory behaviour (also detailed in the governance excerpts below):
1. Retrieve-first: use ONLY the provided evidence blocks. Do not invent CRA facts, URLs, systems, or findings.
2. Propose lines of inquiry, not findings. Risk indicators ≠ findings.
3. Historical public audit reports are precedents for a past audit period — never proof of current CRA conditions.
4. Distinguish content classes: official-public-source vs derived analysis vs general professional concepts. Never treat synthetic demos as evidence.
5. Cite supporting vault note titles and, for CRA-specific claims, include public source_url values from the evidence blocks.
6. If evidence is insufficient, say so and state what internal evidence would be required.
7. Prefer this shape for inquiry questions:
   Risk indicator → line of inquiry → evidence request → audit procedure → analysis → possible observation (not finding).
8. If the user asserts a CRA finding or current condition, verify it against the evidence blocks first.
   If unsupported, open with an explicit correction (e.g. public sources do not support that claim).
   Do NOT restate unsupported claims as established facts or as confirmed risk indicators.

"""


@dataclass
class Citation:
    title: str
    note_path: str
    source_urls: list[str] = field(default_factory=list)
    content_origin: str | None = None
    authoritative: bool | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class AnswerResult:
    query: str
    answer: str
    chat_model: str
    citations: list[Citation]
    warnings: list[str]
    retrieval: RetrievalResponse
    filtered_count: int
    evidence_note_titles: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "query": self.query,
            "answer": self.answer,
            "chat_model": self.chat_model,
            "citations": [c.to_dict() for c in self.citations],
            "warnings": self.warnings,
            "filtered_count": self.filtered_count,
            "evidence_note_titles": self.evidence_note_titles,
            "retrieval": self.retrieval.to_dict(),
        }


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text.strip()
    match = re.search(r"^---\s*$", text[4:], re.MULTILINE)
    if not match:
        return text.strip()
    return text[4 + match.end() :].strip()


def load_governance_prompt(root: Path | None = None) -> str:
    root = root or ROOT
    parts = [SYSTEM_PREFIX, "## Governance excerpts (authoritative for this assistant)\n"]
    for rel in GOVERNANCE_FILES:
        path = root / rel
        if not path.exists():
            parts.append(f"\n### Missing file: {rel}\n")
            continue
        body = strip_frontmatter(path.read_text(encoding="utf-8"))
        # Keep prompt bounded.
        if len(body) > 6_000:
            body = body[:6_000] + "\n\n[truncated]"
        parts.append(f"\n### {rel}\n{body}\n")
    return "\n".join(parts)


def _is_synthetic(classification: str | None, content_origin: str | None) -> bool:
    cls = (classification or "").casefold()
    origin = (content_origin or "").casefold()
    return (
        cls == "synthetic"
        or "synthetic" in origin
        or origin.startswith("synthetic")
    )


def is_evidence_allowed(note: Any | None, chunk_origin: str | None = None) -> bool:
    """Hard-exclude synthetic evidence only.

    In this vault, most concept/bridge/case notes are marked
    ``approved_for_ai_retrieval: false`` while only a small Class A set is
    ``true``. Hard-requiring approval empties inquiry evidence, so approval is
    used as a soft preference in ``prefer_official_evidence``, not a gate.
    """
    classification = getattr(note, "classification", None) if note is not None else None
    content_origin = (
        getattr(note, "content_origin", None) if note is not None else None
    ) or chunk_origin
    if _is_synthetic(classification, content_origin):
        return False
    return True


def _evidence_priority(note: Any | None) -> tuple[int, int, int]:
    """Sort key: approved/official/authoritative first."""
    if note is None:
        return (0, 0, 0)
    approved = 1 if getattr(note, "approved_for_ai_retrieval", None) is True else 0
    origin = (getattr(note, "content_origin", None) or "").casefold()
    official = 1 if "official-public-source" in origin else 0
    authoritative = 1 if getattr(note, "authoritative", None) is True else 0
    return (approved, official, authoritative)


def filter_evidence(
    results: list[RetrievalResult],
    corpus: Corpus,
) -> tuple[list[RetrievalResult], int]:
    kept: list[RetrievalResult] = []
    dropped = 0
    for result in results:
        note = corpus.knowledge_notes.get(result.note_id) or corpus.source_notes.get(
            result.note_id
        )
        origin = getattr(note, "content_origin", None) if note is not None else None
        if not is_evidence_allowed(note, origin):
            dropped += 1
            continue
        kept.append(result)
    # Prefer official/approved chunks earlier in the packed context without
    # discarding concept notes needed for inquiry answers.
    kept.sort(
        key=lambda r: _evidence_priority(
            corpus.knowledge_notes.get(r.note_id) or corpus.source_notes.get(r.note_id)
        ),
        reverse=True,
    )
    return kept, dropped


def pack_context(
    results: list[RetrievalResult],
    retriever: Retriever,
    *,
    max_chars: int = MAX_CONTEXT_CHARS,
) -> tuple[str, list[Citation], list[str]]:
    blocks: list[str] = []
    citations: list[Citation] = []
    titles: list[str] = []
    seen_notes: set[str] = set()
    total = 0

    for idx, result in enumerate(results, start=1):
        chunk = retriever.chunks_by_id.get(result.chunk_id)
        note = retriever.corpus.knowledge_notes.get(result.note_id)
        text = (chunk.text if chunk else result.text_preview) or ""
        if len(text) > MAX_CHUNK_CHARS:
            text = text[:MAX_CHUNK_CHARS] + "…"
        origin = (
            (chunk.content_origin if chunk else None)
            or (note.content_origin if note else None)
        )
        authoritative = (
            chunk.authoritative if chunk and chunk.authoritative is not None else None
        )
        if authoritative is None and note is not None:
            authoritative = note.authoritative
        urls = list(result.source_urls)
        if not urls and chunk:
            urls = list(chunk.source_urls)
        graph = " → ".join(result.graph_path) if result.graph_path else ""
        block = (
            f"[E{idx}] title={result.title}\n"
            f"path={result.note_path}\n"
            f"heading={result.chunk_heading}\n"
            f"content_origin={origin or 'unknown'}\n"
            f"authoritative={authoritative}\n"
            f"source_urls={urls or []}\n"
            f"graph_path={graph or 'n/a'}\n"
            f"text:\n{text}\n"
        )
        if total + len(block) > max_chars and blocks:
            break
        blocks.append(block)
        total += len(block)
        titles.append(result.title)
        if result.note_id not in seen_notes:
            seen_notes.add(result.note_id)
            citations.append(
                Citation(
                    title=result.title,
                    note_path=result.note_path,
                    source_urls=urls,
                    content_origin=origin,
                    authoritative=authoritative,
                )
            )
    return "\n---\n".join(blocks), citations, titles


def _has_class_a(citations: list[Citation]) -> bool:
    for cite in citations:
        origin = (cite.content_origin or "").casefold()
        if cite.authoritative or "official-public-source" in origin or origin == "official":
            return True
        if cite.source_urls:
            return True
    return False


def looks_like_factual_assertion(query: str) -> bool:
    """Heuristic: short declarative user claims that need verify-or-correct handling."""
    text = query.strip()
    if not text:
        return False
    if "?" in text:
        return False
    words = text.split()
    if len(words) > 24:
        return False
    return bool(re.search(r"\b(prove|found|failed|currently|declare|non[- ]compliance)\b", text, re.I))


def build_user_prompt(
    query: str,
    context: str,
    *,
    evidence_empty: bool,
    has_class_a: bool,
) -> str:
    guidance: list[str] = []
    if evidence_empty:
        guidance.append(
            "No eligible evidence blocks were retrieved. State that public vault evidence "
            "is insufficient and do not invent CRA-specific facts."
        )
    elif not has_class_a:
        guidance.append(
            "Retrieved evidence appears concept/derived-heavy without strong Class A "
            "official-public-source support. For CRA-specific factual claims, say evidence "
            "is limited and avoid asserting current CRA conditions."
        )
    if looks_like_factual_assertion(query):
        guidance.append(
            "The user statement looks like a factual assertion about CRA. First check whether "
            "the evidence blocks support it. If not, explicitly correct it (do not adopt it as "
            "a confirmed risk indicator or finding)."
        )
    guide = "\n".join(f"- {g}" for g in guidance) if guidance else "- Use the evidence blocks below."
    return (
        f"User question:\n{query}\n\n"
        f"Answering constraints:\n{guide}\n\n"
        f"Evidence blocks:\n{context or '(none)'}\n\n"
        "Write the answer now. Include vault note titles used and public URLs when present."
    )


def load_dotenv(path: Path | None = None) -> None:
    """Load KEY=VALUE pairs from .env into os.environ if not already set."""
    env_path = path or (ROOT / ".env")
    if not env_path.exists():
        return
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if not key:
            continue
        os.environ.setdefault(key, value)


def run_openai_chat(
    *,
    system: str,
    user: str,
    model: str,
) -> str:
    load_dotenv()
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Add it to .env or export it in your shell."
        )
    if key.endswith("HERE") or "NEW_KEY" in key or "OPENAI_API_KEY" in key[8:]:
        raise RuntimeError(
            "OPENAI_API_KEY looks invalid/corrupted (placeholder or mangled value). "
            "Edit .env to a single line: OPENAI_API_KEY=sk-proj-... with your real key, no spaces."
        )
    from openai import AuthenticationError, OpenAI

    client = OpenAI(api_key=key)
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=0.2,
        )
    except AuthenticationError as exc:
        raise RuntimeError(
            "OpenAI rejected the API key (401). Create a new key at "
            "https://platform.openai.com/api-keys and put it in .env as "
            "OPENAI_API_KEY=sk-proj-... (no spaces)."
        ) from exc
    content = response.choices[0].message.content
    return (content or "").strip()


def answer_has_correction(answer: str) -> bool:
    """True when the answer explicitly corrects or rejects an unsupported claim."""
    return any(pattern.search(answer) for pattern in CORRECTION_PATTERNS)


def _match_is_corrective(answer: str, start: int, end: int) -> bool:
    """Skip forbidden matches that appear inside a corrective/quoted denial."""
    window = answer[max(0, start - 100) : min(len(answer), end + 60)]
    if answer_has_correction(window):
        return True
    return bool(
        re.search(
            r"\b(?:claim that|allegation that|assertion that|statement that|"
            r"user statement|misstates? that|incorrect that|not (?:true|accurate) that|"
            r"is not(?:\s+\w+){0,3}\s+supported|not supported by)\b",
            window,
            re.I,
        )
    )


def forbidden_pattern_hits(answer: str) -> list[str]:
    """Return forbidden patterns that affirm bad claims (ignoring corrective mentions)."""
    hits: list[str] = []
    for pattern in FORBIDDEN_PATTERNS:
        for match in pattern.finditer(answer):
            if _match_is_corrective(answer, match.start(), match.end()):
                continue
            hits.append(pattern.pattern)
            break
    return hits


def check_answer_policy(
    answer: str,
    evidence_titles: list[str],
    citations: list[Citation],
    *,
    evidence_empty: bool,
) -> list[str]:
    warnings: list[str] = []
    for pattern in forbidden_pattern_hits(answer):
        warnings.append(f"forbidden_pattern:{pattern}")

    if evidence_empty:
        return warnings

    answer_cf = answer.casefold()
    title_hit = any(title and title.casefold() in answer_cf for title in evidence_titles)
    url_values = [u for c in citations for u in c.source_urls]
    url_hit = any(u and u.casefold() in answer_cf for u in url_values)
    if not title_hit and not url_hit:
        warnings.append(
            "missing_citation: answer does not mention any retrieved note title or source_url"
        )
    return warnings


def format_answer_report(result: AnswerResult) -> str:
    lines = [
        f"Query: {result.query}",
        f"Chat model: {result.chat_model}",
        f"Evidence notes: {len(result.evidence_note_titles)} (filtered out {result.filtered_count})",
        "",
        "## Answer",
        result.answer,
        "",
        "## Citations",
    ]
    if not result.citations:
        lines.append("(none)")
    for cite in result.citations:
        urls = ", ".join(cite.source_urls) if cite.source_urls else "n/a"
        lines.append(
            f"- {cite.title} ({cite.note_path}); origin={cite.content_origin or 'unknown'}; urls={urls}"
        )
    if result.warnings:
        lines.extend(["", "## Warnings"])
        for warning in result.warnings:
            lines.append(f"- {warning}")
    lines.extend(["", "## Top retrieval"])
    for item in result.retrieval.results[:5]:
        lines.append(f"{item.rank}. {item.title} [{item.final_score:.3f}]")
    return "\n".join(lines)


def ask(
    query: str,
    retriever: Retriever,
    *,
    top_k: int = 10,
    graph_hops: int = 1,
    use_graph: bool = True,
    domain: str | None = None,
    chat_model: str | None = None,
    root: Path | None = None,
) -> AnswerResult:
    """Retrieve, filter, generate a grounded answer, and run policy checks."""
    model = chat_model or DEFAULT_CHAT_MODEL
    retrieval = retriever.retrieve(
        query,
        top_k=top_k,
        graph_hops=graph_hops if use_graph else 0,
        domain=domain,
        use_graph=use_graph and graph_hops > 0,
        use_semantic=True,
        use_lexical=True,
    )
    filtered, dropped = filter_evidence(retrieval.results, retriever.corpus)
    context, citations, titles = pack_context(filtered, retriever)
    evidence_empty = len(filtered) == 0
    has_class_a = _has_class_a(citations)
    warnings: list[str] = []
    if dropped:
        warnings.append(f"filtered_synthetic:{dropped}")
    if evidence_empty:
        warnings.append("no_eligible_evidence")
    elif not has_class_a:
        warnings.append("limited_official_source_support")

    system = load_governance_prompt(root or retriever.corpus.root)
    user = build_user_prompt(
        query,
        context,
        evidence_empty=evidence_empty,
        has_class_a=has_class_a,
    )
    answer = run_openai_chat(system=system, user=user, model=model)
    warnings.extend(
        check_answer_policy(
            answer,
            titles,
            citations,
            evidence_empty=evidence_empty,
        )
    )
    return AnswerResult(
        query=query,
        answer=answer,
        chat_model=model,
        citations=citations,
        warnings=warnings,
        retrieval=retrieval,
        filtered_count=dropped,
        evidence_note_titles=titles,
    )

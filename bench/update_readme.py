"""Replace the README.md <!-- BENCH:START --> … <!-- BENCH:END --> block."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
RESULTS_MD = ROOT / "bench" / "results" / "RESULTS.md"

START = "<!-- BENCH:START -->"
END = "<!-- BENCH:END -->"

PLACEHOLDER = f"""{START}
### Retrieval embedding / reranker benchmark

Honesty note: the official eval set has only **10 questions**. A Hit@1 difference
of `0.10` (one question) is **not statistically meaningful**.

Run `python -m bench.run_benchmark --all` then `python -m bench.update_readme`
to refresh this table from `bench/results/RESULTS.md`.
{END}
"""


def build_block(results_md: Path) -> str:
    if not results_md.exists():
        return PLACEHOLDER
    text = results_md.read_text(encoding="utf-8")
    # Prefer the official (original 10) section for the README summary.
    section = text
    if "## Official set" in text:
        section = text.split("## Official set", 1)[1]
        if "## Draft set" in section:
            section = section.split("## Draft set", 1)[0]
        if "## Combined" in section:
            section = section.split("## Combined", 1)[0]
        section = "## Official set" + section
    # Keep honesty + table compact.
    honesty = ""
    for line in text.splitlines():
        if line.startswith("Honesty note:"):
            honesty = line
            break
    table_lines: list[str] = []
    in_table = False
    for line in section.splitlines():
        if line.startswith("|"):
            in_table = True
            table_lines.append(line)
        elif in_table:
            break
    body = [
        START,
        "### Retrieval embedding / reranker benchmark",
        "",
        honesty
        or (
            "Honesty note: the official eval set has only 10 questions. "
            "A Hit@1 difference of 0.10 is not statistically meaningful."
        ),
        "",
        "Source: [`bench/results/RESULTS.md`](bench/results/RESULTS.md).",
        "",
    ]
    body.extend(table_lines or ["_(no results table yet)_"])
    body.append(END)
    return "\n".join(body) + "\n"


def update_readme(readme_path: Path, results_md: Path) -> bool:
    block = build_block(results_md)
    if not readme_path.exists():
        raise SystemExit(f"Missing README: {readme_path}")
    text = readme_path.read_text(encoding="utf-8")
    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END),
        flags=re.DOTALL,
    )
    if pattern.search(text):
        new_text = pattern.sub(block.rstrip("\n"), text)
    else:
        # Insert before "## Current limitations" if present, else append.
        anchor = "## Current limitations and future direction"
        if anchor in text:
            new_text = text.replace(anchor, block + "\n" + anchor)
        else:
            new_text = text.rstrip() + "\n\n" + block
    if new_text == text:
        return False
    readme_path.write_text(new_text, encoding="utf-8")
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Sync README BENCH markers from RESULTS.md")
    parser.add_argument("--readme", default=str(README_PATH))
    parser.add_argument("--results", default=str(RESULTS_MD))
    args = parser.parse_args(argv)
    changed = update_readme(Path(args.readme), Path(args.results))
    print("README updated" if changed else "README already up to date")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

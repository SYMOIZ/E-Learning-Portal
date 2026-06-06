#!/usr/bin/env python3
"""Generate scripts/topic_snippets.py — single entry point."""

from __future__ import annotations

import ast
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "topic_snippets.py"

# Re-use emitter utilities
emit = runpy.run_path(str(ROOT / "emit_topic_snippets.py"))
py_repr = emit["py_repr"]
validate_snippet = emit["validate_snippet"]
ALL_TOPICS = emit["ALL_TOPICS"]

# Load merged snippet dict built in make_full_catalog.py
catalog = runpy.run_path(str(ROOT / "make_full_catalog.py"))
ALL_SNIPPETS: dict = catalog["ALL_SNIPPETS"]


def main() -> None:
    missing = [t for t in ALL_TOPICS if t not in ALL_SNIPPETS]
    extra = [t for t in ALL_SNIPPETS if t not in ALL_TOPICS]
    if missing:
        raise SystemExit(f"Missing {len(missing)} topics: {missing}")
    if extra:
        raise SystemExit(f"Extra topics: {extra}")

    for title in ALL_TOPICS:
        validate_snippet(title, ALL_SNIPPETS[title])

    lines = [
        '"""Curated topic snippets for the Python Mastery knowledge base."""',
        "",
        "from textwrap import dedent",
        "",
        "TOPIC_SNIPPETS: dict[str, dict] = {",
    ]
    for title in ALL_TOPICS:
        lines.append(f"    {title!r}: {py_repr(ALL_SNIPPETS[title], 4)},")
    lines.append("}")
    lines.append("")
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size:,} bytes, {len(ALL_SNIPPETS)} topics)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Validate curriculum coverage, structure, examples, diagrams, and links."""

from __future__ import annotations

import ast
import re
from pathlib import Path
from urllib.parse import unquote

from curriculum_manifest import DESTINATION, LEVELS, REQUIRED_SECTIONS, ROOT, SOURCE


EXAMPLE_SECTIONS = ("Beginner Example", "Intermediate Example", "Advanced Example")
INFOGRAPHIC_BLOCKS = (
    "📌 Concept",
    "⚡ Purpose",
    "🔥 Benefits",
    "🎯 Use Cases",
    "🚀 Best Practices",
    "❌ Common Mistakes",
)
CAREER_ROADMAPS = (
    "Complete Python Roadmap",
    "Python Career Paths",
    "Python Developer Roadmap",
    "Backend Engineer Roadmap",
    "Data Engineer Roadmap",
    "AI Engineer Roadmap",
    "DevOps Engineer Roadmap",
    "Cybersecurity Engineer Roadmap",
)


def markdown_links(document: str) -> list[str]:
    return re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", document)


def validate_relative_links(markdown_file: Path, errors: list[str]) -> None:
    document = markdown_file.read_text(encoding="utf-8")
    for raw_target in markdown_links(document):
        target = raw_target.split("#", maxsplit=1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        resolved = (markdown_file.parent / unquote(target)).resolve()
        if not resolved.exists():
            errors.append(
                f"{markdown_file.relative_to(ROOT)}: broken link to {raw_target}"
            )


def validate_topic_files(errors: list[str]) -> int:
    expected_count = sum(len(topics) for topics in LEVELS.values())
    root_document = SOURCE.read_text(encoding="utf-8")
    topic_files = [
        path
        for level in LEVELS
        for path in sorted((DESTINATION / level).glob("*.md"))
    ]
    if len(topic_files) != expected_count:
        errors.append(
            f"Expected {expected_count} topic files, found {len(topic_files)}"
        )

    for path in topic_files:
        document = path.read_text(encoding="utf-8")
        topic_heading = next(
            (line for line in document.splitlines() if line.startswith("# ")),
            None,
        )
        if topic_heading is None:
            errors.append(f"{path.relative_to(ROOT)}: missing topic heading")
        else:
            footer = document.rfind("\n---\n")
            lesson = document[document.find(topic_heading) : footer].rstrip()
            if root_document.count(f"\n{topic_heading}\n") != 1:
                errors.append(
                    f"README.md: expected exactly one synchronized {topic_heading}"
                )
            elif lesson not in root_document:
                errors.append(
                    f"{path.relative_to(ROOT)}: lesson differs from root README"
                )
        for heading in REQUIRED_SECTIONS:
            if document.count(f"## {heading}") != 1:
                errors.append(f"{path.relative_to(ROOT)}: invalid {heading!r} count")
        for heading in EXAMPLE_SECTIONS:
            if document.count(f"### {heading}") != 1:
                errors.append(f"{path.relative_to(ROOT)}: missing {heading}")
        for block in INFOGRAPHIC_BLOCKS:
            if document.count(block) != 1:
                errors.append(f"{path.relative_to(ROOT)}: missing {block}")
        if document.count("```mermaid") != 1:
            errors.append(f"{path.relative_to(ROOT)}: expected one Mermaid diagram")
        if document.count("```python") < 3:
            errors.append(f"{path.relative_to(ROOT)}: expected at least three examples")
        if document.count("```") % 2:
            errors.append(f"{path.relative_to(ROOT)}: unbalanced code fences")
        validate_relative_links(path, errors)
    return len(topic_files)


def validate_python_examples(errors: list[str]) -> int:
    source = SOURCE.read_text(encoding="utf-8")
    snippets = re.findall(r"```python\n(.*?)```", source, flags=re.DOTALL)
    for index, snippet in enumerate(snippets, start=1):
        try:
            ast.parse(snippet)
        except SyntaxError as error:
            errors.append(
                "README.md: Python snippet "
                f"{index} has invalid syntax at line {error.lineno}: {error.msg}"
            )
    return len(snippets)


def validate_indexes(errors: list[str]) -> None:
    index = (DESTINATION / "README.md").read_text(encoding="utf-8")
    for level, topics in LEVELS.items():
        if f"## Level {list(LEVELS).index(level) + 1}: {level}" not in index:
            errors.append(f"Python-Mastery/README.md: missing {level} index")
        for topic in topics:
            if f"| {topic} |" not in index:
                errors.append(f"Python-Mastery/README.md: missing topic {topic}")

    roadmaps = (DESTINATION / "Roadmaps" / "README.md").read_text(encoding="utf-8")
    for roadmap in CAREER_ROADMAPS:
        if f"## {roadmap}" not in roadmaps:
            errors.append(f"Roadmaps/README.md: missing {roadmap}")

    for path in DESTINATION.rglob("*.md"):
        validate_relative_links(path, errors)


def main() -> None:
    errors: list[str] = []
    topic_count = validate_topic_files(errors)
    snippet_count = validate_python_examples(errors)
    validate_indexes(errors)

    pdf = ROOT / "A Smarter Way to Learn Python .pdf"
    if not pdf.is_file() or pdf.stat().st_size == 0:
        errors.append("Supplemental PDF is missing or empty")

    if errors:
        print("Knowledge-base validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print(
        "Knowledge-base validation passed: "
        f"{topic_count} topic files, {snippet_count} Python examples, "
        "8 final roadmaps, valid relative links."
    )


if __name__ == "__main__":
    main()

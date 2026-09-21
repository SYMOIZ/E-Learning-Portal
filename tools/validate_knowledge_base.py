#!/usr/bin/env python3
"""Validate curriculum coverage, structure, examples, diagrams, and links."""

from __future__ import annotations

import ast
import contextlib
import io
import re
from pathlib import Path
from urllib.parse import unquote

from curriculum_manifest import (
    DESTINATION,
    LEVELS,
    REQUIRED_SECTIONS,
    ROOT,
    SOURCE,
    topic_filename,
)


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

SPLIT_ROADMAPS = (
    "01-complete-python-roadmap.md",
    "02-python-career-paths.md",
    "03-python-developer-roadmap.md",
    "04-backend-engineer-roadmap.md",
    "05-data-engineer-roadmap.md",
    "06-ai-engineer-roadmap.md",
    "07-devops-engineer-roadmap.md",
    "08-cybersecurity-engineer-roadmap.md",
)

STUDY_GUIDES = (
    "README.md",
    "notebooklm-obsidian-notion.md",
    "12-week-plan.md",
    "24-week-plan.md",
    "deep-dive-crosswalk.md",
)

CHEAT_SHEETS = (
    "README.md",
    "01-beginner.md",
    "02-intermediate.md",
    "03-advanced.md",
)

INFOGRAPHIC_MAPS = (
    "README.md",
    "01-beginner-map.md",
    "02-intermediate-map.md",
    "03-advanced-map.md",
    "04-career-path-map.md",
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


THIRD_PARTY_IMPORTS = {
    "pandas",
    "numpy",
    "pyspark",
    "django",
    "flask",
    "fastapi",
    "sklearn",
    "torch",
    "tensorflow",
    "cv2",
    "nltk",
    "spacy",
    "boto3",
    "azure",
    "google",
    "kubernetes",
    "docker",
    "sqlalchemy",
    "pymysql",
    "psycopg",
    "psycopg2",
    "requests",
    "bs4",
    "scrapy",
    "selenium",
    "httpx",
    "pytest",
}


def imported_modules(tree: ast.AST) -> set[str]:
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name.split(".", maxsplit=1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module.split(".", maxsplit=1)[0])
    return names


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


def validate_self_contained_examples(errors: list[str]) -> None:
    """Require beginner/intermediate/advanced examples to run without NameError."""
    skip_tokens = (
        "input(",
        "pdb.set_trace",
        "breakpoint(",
        "Process(",
        "Pool(",
        "multiprocessing",
        "ProcessPoolExecutor",
    )
    for level, topics in LEVELS.items():
        for number, topic in enumerate(topics, start=1):
            path = DESTINATION / level / topic_filename(number, topic)
            document = path.read_text(encoding="utf-8")
            for heading in EXAMPLE_SECTIONS:
                match = re.search(
                    rf"### {re.escape(heading)}\n+```python\n(.*?)```",
                    document,
                    flags=re.DOTALL,
                )
                if match is None:
                    continue
                snippet = match.group(1)
                try:
                    tree = ast.parse(snippet)
                except SyntaxError:
                    continue
                if imported_modules(tree) & THIRD_PARTY_IMPORTS:
                    continue
                if any(token in snippet for token in skip_tokens):
                    continue
                captured = io.StringIO()
                try:
                    with contextlib.redirect_stdout(captured), contextlib.redirect_stderr(
                        captured
                    ):
                        exec(compile(tree, str(path), "exec"), {"__name__": "__main__"})
                except NameError as error:
                    errors.append(f"{path.relative_to(ROOT)} {heading}: {error}")
                except (Exception, SystemExit):
                    continue


def validate_indexes(errors: list[str]) -> None:
    root_document = SOURCE.read_text(encoding="utf-8")
    root_index_start = root_document.find("## Complete Topic Index")
    root_index_end = root_document.find("## Level 1: Beginner")
    if root_index_start < 0 or root_index_end <= root_index_start:
        errors.append("README.md: missing Complete Topic Index")
    else:
        root_index = root_document[root_index_start:root_index_end]
        if re.search(r"^#\s*$", root_index, flags=re.MULTILINE):
            errors.append("README.md: empty heading in Complete Topic Index")
        for topics in LEVELS.values():
            for topic in topics:
                if f"| [{topic}](" not in root_index:
                    errors.append(f"README.md: Complete Topic Index missing {topic}")

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

    for filename in SPLIT_ROADMAPS:
        path = DESTINATION / "Roadmaps" / filename
        if not path.is_file():
            errors.append(f"Roadmaps/{filename}: missing split roadmap")
        else:
            heading = path.read_text(encoding="utf-8").lstrip().splitlines()[0]
            if not heading.startswith("# "):
                errors.append(f"Roadmaps/{filename}: missing title heading")

    for filename in STUDY_GUIDES:
        path = DESTINATION / "Study-Guides" / filename
        if not path.is_file():
            errors.append(f"Study-Guides/{filename}: missing study guide")

    for filename in CHEAT_SHEETS:
        path = DESTINATION / "CheatSheets" / filename
        if not path.is_file():
            errors.append(f"CheatSheets/{filename}: missing cheat sheet")

    for filename in INFOGRAPHIC_MAPS:
        path = DESTINATION / "Infographics" / filename
        if not path.is_file():
            errors.append(f"Infographics/{filename}: missing infographic map")

    companion = ROOT / "python-learning-roadmap" / "README.md"
    if companion.is_file():
        text = companion.read_text(encoding="utf-8")
        if "Python-Mastery/" not in text:
            errors.append(
                "python-learning-roadmap/README.md: missing canonical Python-Mastery link"
            )

    for path in DESTINATION.rglob("*.md"):
        validate_relative_links(path, errors)


def main() -> None:
    errors: list[str] = []
    topic_count = validate_topic_files(errors)
    snippet_count = validate_python_examples(errors)
    validate_self_contained_examples(errors)
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
        "8 final roadmaps, 8 split roadmaps, study guides, valid relative links."
    )


if __name__ == "__main__":
    main()

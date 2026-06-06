#!/usr/bin/env python3
"""Emit scripts/topic_snippets.py from curated snippet parts."""

from __future__ import annotations

import ast
import importlib.util
import sys
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent
PARTS_DIR = ROOT / "snippet_parts"
OUTPUT = ROOT / "topic_snippets.py"

BEGINNER = [
    "Introduction to Python", "Installing Python", "IDE Setup", "Python Syntax", "Variables",
    "Data Types", "Type Casting", "Input and Output", "Operators", "Conditional Statements",
    "Loops", "Nested Loops", "Break Continue Pass", "Strings", "String Methods",
    "Lists", "List Methods", "Tuples", "Sets", "Dictionaries",
    "Functions", "Arguments and Parameters", "Return Statements", "Scope", "Lambda Functions",
    "Modules", "Packages", "Date and Time", "Math Module", "Random Module",
    "File Handling", "Exception Handling", "Debugging Basics", "Virtual Environments",
    "Basic Project Structure",
]
INTERMEDIATE = [
    "Object Oriented Programming", "Classes", "Objects", "Constructors", "Encapsulation",
    "Inheritance", "Polymorphism", "Abstraction", "Magic Methods", "Iterators",
    "Generators", "Decorators", "Context Managers", "Regular Expressions", "JSON Processing",
    "CSV Processing", "XML Processing", "Logging", "Configuration Management", "Multithreading",
    "Multiprocessing", "Async Programming", "API Development", "API Consumption", "Requests Library",
    "Database Fundamentals", "SQLite", "MySQL Integration", "PostgreSQL Integration", "SQLAlchemy ORM",
    "Unit Testing", "Pytest", "Mocking", "Packaging Python Projects", "CLI Applications",
]
ADVANCED = [
    "Data Structures Internals", "Algorithms in Python", "Design Patterns", "SOLID Principles",
    "Memory Management", "Garbage Collection", "Python Internals", "Metaclasses", "Descriptors",
    "Concurrency", "Parallel Computing", "Distributed Systems", "Network Programming", "Socket Programming",
    "Cybersecurity Automation", "Web Scraping", "Automation Frameworks", "ETL Development", "Data Engineering",
    "Pandas", "NumPy", "PySpark", "Machine Learning", "Deep Learning", "NLP", "Computer Vision",
    "FastAPI", "Django", "Flask", "Microservices", "Docker with Python", "Kubernetes Integration",
    "Cloud Development", "AWS with Python", "Azure with Python", "GCP with Python", "DevOps Automation",
    "CI/CD Pipelines", "Performance Optimization", "System Design with Python",
]
ALL_TOPICS = BEGINNER + INTERMEDIATE + ADVANCED


def load_part(name: str) -> dict:
    if str(PARTS_DIR) not in sys.path:
        sys.path.insert(0, str(PARTS_DIR))
    path = PARTS_DIR / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.SNIPPETS


def py_repr(value, indent: int = 0) -> str:
    """Render Python literals with dedent() calls for multiline strings."""
    pad = " " * indent
    if isinstance(value, dict):
        if not value:
            return "{}"
        lines = ["{"]
        for k, v in value.items():
            key = repr(k)
            lines.append(f"{pad}    {key}: {py_repr(v, indent + 4)},")
        lines.append(f"{pad}}}")
        return "\n".join(lines)
    if isinstance(value, list):
        if not value:
            return "[]"
        lines = ["["]
        for item in value:
            lines.append(f"{pad}    {py_repr(item, indent + 4)},")
        lines.append(f"{pad}]")
        return "\n".join(lines)
    if isinstance(value, tuple):
        if not value:
            return "()"
        inner = ",\n".join(f"{pad}    {py_repr(item, indent + 4)}" for item in value)
        if len(value) == 1:
            return f"(\n{inner},\n{pad})"
        return f"(\n{inner},\n{pad})"
    if isinstance(value, str):
        if "\n" in value:
            return f"dedent({repr(value)})"
        return repr(value)
    return repr(value)


def validate_snippet(title: str, data: dict) -> None:
    required = {
        "what", "why", "where", "objectives", "outcome", "industry", "concepts",
        "concept", "purpose", "benefits", "use_cases", "best_practices", "mistakes",
        "basic_syntax", "structure", "pattern", "beginner", "intermediate", "advanced", "mermaid",
    }
    missing = required - data.keys()
    if missing:
        raise ValueError(f"{title} missing keys: {missing}")
    if len(data["objectives"]) != 3:
        raise ValueError(f"{title} objectives must have 3 items")
    if len(data["industry"]) != 4:
        raise ValueError(f"{title} industry must have 4 items")
    if len(data["concepts"]) != 3:
        raise ValueError(f"{title} concepts must have 3 tuples")
    for field in ("basic_syntax", "structure", "pattern", "beginner", "intermediate", "advanced"):
        text = data[field].strip()
        if text in {"pass", "# example", "# Example usage"}:
            raise ValueError(f"{title}.{field} contains placeholder")
        if field != "basic_syntax" and "..." in text and "Protocol" not in text:
            # allow Protocol ellipsis only in advanced patterns sparingly
            if "..." in text and not text.strip().startswith("class"):
                raise ValueError(f"{title}.{field} contains ellipsis placeholder")
    for name, _defn, code in data["concepts"]:
        if not code.strip() or code.strip().startswith("# Example"):
            raise ValueError(f"{title} concept {name!r} has invalid example_code")
    # syntax-check python code fields (skip bash/dockerfile blocks)
    for field in ("basic_syntax", "pattern", "beginner", "intermediate", "advanced"):
        text = dedent(data[field]).strip()
        if text.lstrip().startswith("#") and "FROM " in text:
            continue
        if "apt " in text or text.strip().startswith("# Linux"):
            continue
        if field in {"structure", "pattern"} and "->" in text and not any(
            kw in text for kw in ("def ", "import ", "print(", "for ", "if ", "class ")
        ):
            continue
        try:
            ast.parse(text)
        except SyntaxError:
            if field in {"structure", "pattern"} and not any(
                kw in text for kw in ("def ", "import ", "print(", "for ", "if ", "class ")
            ):
                continue
            raise ValueError(f"{title}.{field} is not valid Python: {text[:80]!r}") from None


def main() -> None:
    merged: dict[str, dict] = {}
    for part in ("beginner", "intermediate", "advanced"):
        merged.update(load_part(part))

    missing = [t for t in ALL_TOPICS if t not in merged]
    extra = [t for t in merged if t not in ALL_TOPICS]
    if missing:
        raise SystemExit(f"Missing topics ({len(missing)}): {missing[:5]} ...")
    if extra:
        raise SystemExit(f"Unexpected extra topics: {extra}")

    for title in ALL_TOPICS:
        validate_snippet(title, merged[title])

    body_lines = [
        '"""Curated topic snippets for the Python Mastery knowledge base."""',
        "",
        "from textwrap import dedent",
        "",
        "TOPIC_SNIPPETS: dict[str, dict] = {",
    ]
    for title in ALL_TOPICS:
        body_lines.append(f"    {repr(title)}: {py_repr(merged[title], 4)},")
    body_lines.append("}")
    body_lines.append("")

    OUTPUT.write_text("\n".join(body_lines), encoding="utf-8")
    print(f"Wrote {OUTPUT} with {len(merged)} topics ({OUTPUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()

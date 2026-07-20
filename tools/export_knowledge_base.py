#!/usr/bin/env python3
"""Export the canonical README into a NotebookLM-friendly knowledge base.

The repository root README is the source of truth. This script creates
topic-level Markdown documents and the companion indexes requested by the
curriculum's recommended ``Python-Mastery`` layout.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "README.md"
DESTINATION = ROOT / "Python-Mastery"

LEVELS: dict[str, list[str]] = {
    "Beginner": [
        "Introduction to Python",
        "Installing Python",
        "IDE Setup",
        "Python Syntax",
        "Variables",
        "Data Types",
        "Type Casting",
        "Input and Output",
        "Operators",
        "Conditional Statements",
        "Loops",
        "Nested Loops",
        "Break Continue Pass",
        "Strings",
        "String Methods",
        "Lists",
        "List Methods",
        "Tuples",
        "Sets",
        "Dictionaries",
        "Functions",
        "Arguments and Parameters",
        "Return Statements",
        "Scope",
        "Lambda Functions",
        "Modules",
        "Packages",
        "Date and Time",
        "Math Module",
        "Random Module",
        "File Handling",
        "Exception Handling",
        "Debugging Basics",
        "Virtual Environments",
        "Basic Project Structure",
    ],
    "Intermediate": [
        "Object Oriented Programming",
        "Classes",
        "Objects",
        "Constructors",
        "Encapsulation",
        "Inheritance",
        "Polymorphism",
        "Abstraction",
        "Magic Methods",
        "Iterators",
        "Generators",
        "Decorators",
        "Context Managers",
        "Regular Expressions",
        "JSON Processing",
        "CSV Processing",
        "XML Processing",
        "Logging",
        "Configuration Management",
        "Multithreading",
        "Multiprocessing",
        "Async Programming",
        "API Development",
        "API Consumption",
        "Requests Library",
        "Database Fundamentals",
        "SQLite",
        "MySQL Integration",
        "PostgreSQL Integration",
        "SQLAlchemy ORM",
        "Unit Testing",
        "Pytest",
        "Mocking",
        "Packaging Python Projects",
        "CLI Applications",
    ],
    "Advanced": [
        "Data Structures Internals",
        "Algorithms in Python",
        "Design Patterns",
        "SOLID Principles",
        "Memory Management",
        "Garbage Collection",
        "Python Internals",
        "Metaclasses",
        "Descriptors",
        "Concurrency",
        "Parallel Computing",
        "Distributed Systems",
        "Network Programming",
        "Socket Programming",
        "Cybersecurity Automation",
        "Web Scraping",
        "Automation Frameworks",
        "ETL Development",
        "Data Engineering",
        "Pandas",
        "NumPy",
        "PySpark",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "Computer Vision",
        "FastAPI",
        "Django",
        "Flask",
        "Microservices",
        "Docker with Python",
        "Kubernetes Integration",
        "Cloud Development",
        "AWS with Python",
        "Azure with Python",
        "GCP with Python",
        "DevOps Automation",
        "CI/CD Pipelines",
        "Performance Optimization",
        "System Design with Python",
    ],
}

REQUIRED_SECTIONS = (
    "Overview",
    "Learning Objectives",
    "Real World Applications",
    "Core Concepts",
    "Infographic Summary",
    "Syntax Guide",
    "Examples",
    "Workflow Diagram",
)


def slugify(value: str) -> str:
    """Return a filesystem-safe, readable topic slug."""
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def topic_filename(number: int, topic: str) -> str:
    return f"{number:02d}-{slugify(topic)}.md"


def extract_topic(source: str, topic: str, next_heading: str) -> str:
    start_marker = f"# {topic}\n"
    end_marker = f"\n# {next_heading}\n"
    start = source.find(start_marker)
    if start < 0:
        raise ValueError(f"Missing topic heading: {topic}")
    end = source.find(end_marker, start + len(start_marker))
    if end < 0:
        raise ValueError(f"Missing heading after {topic}: {next_heading}")

    lesson = source[start:end].rstrip()
    lesson = re.sub(
        rf"\n\[Back to topic index\]\(#{re.escape(slugify(topic))}\)\n?",
        "",
        lesson,
    )
    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in lesson:
            raise ValueError(f"{topic} is missing required section: {section}")
    return lesson


def navigation(level: str, number: int, topic: str) -> str:
    topics = LEVELS[level]
    links = ["[↑ Level index](../README.md)"]
    if number > 1:
        links.insert(
            0,
            f"[← {topics[number - 2]}](./{topic_filename(number - 1, topics[number - 2])})",
        )
    if number < len(topics):
        links.append(
            f"[{topics[number]} →](./{topic_filename(number + 1, topics[number])})"
        )
    return " · ".join(links)


def build_topic_documents(source: str) -> None:
    all_topics = [topic for topics in LEVELS.values() for topic in topics]
    next_topics = all_topics[1:] + ["FINAL SECTION"]

    for level, topics in LEVELS.items():
        level_directory = DESTINATION / level
        level_directory.mkdir(parents=True, exist_ok=True)
        for number, topic in enumerate(topics, start=1):
            global_index = all_topics.index(topic)
            lesson = extract_topic(source, topic, next_topics[global_index])
            nav = navigation(level, number, topic)
            document = (
                f"> **Level {list(LEVELS).index(level) + 1}: {level}** · "
                f"Topic {number} of {len(topics)}\n\n"
                f"{nav}\n\n"
                f"{lesson}\n\n"
                "---\n\n"
                f"{nav}\n"
            )
            (level_directory / topic_filename(number, topic)).write_text(
                document,
                encoding="utf-8",
            )


def topic_table(level: str) -> str:
    rows = [
        "| # | Topic | Learning document |",
        "| ---: | --- | --- |",
    ]
    for number, topic in enumerate(LEVELS[level], start=1):
        path = f"./{level}/{topic_filename(number, topic)}"
        rows.append(f"| {number:02d} | {topic} | [Open lesson]({path}) |")
    return "\n".join(rows)


def build_main_index() -> None:
    total = sum(len(topics) for topics in LEVELS.values())
    sections = []
    for level_number, level in enumerate(LEVELS, start=1):
        sections.append(
            f"## Level {level_number}: {level}\n\n"
            f"{topic_table(level)}"
        )

    content = f"""# Python Mastery Knowledge Base

> A portable, topic-by-topic edition of the [canonical Python Learning Roadmap](../README.md), designed for GitHub, NotebookLM, Obsidian, Notion, and documentation portals.

## Knowledge Base at a Glance

| Metric | Coverage |
| --- | ---: |
| Learning levels | {len(LEVELS)} |
| Beginner lessons | {len(LEVELS["Beginner"])} |
| Intermediate lessons | {len(LEVELS["Intermediate"])} |
| Advanced lessons | {len(LEVELS["Advanced"])} |
| Total topic documents | {total} |
| Examples per topic | 3 progressive examples |
| Visual learning | Infographic table and Mermaid workflow per topic |

## How to Study

1. Read the **Overview** and **Learning Objectives** to set a goal.
2. Recreate each **Core Concepts** example instead of copying it.
3. Move through the beginner, intermediate, and advanced examples.
4. Explain the **Workflow Diagram** aloud in your own words.
5. Build one project from the [Projects](./Projects/) catalog.
6. Use the [career roadmaps](./Roadmaps/) to select deeper topics.

```mermaid
flowchart LR
    A[Beginner Foundations] --> B[Intermediate Engineering]
    B --> C[Advanced Systems]
    C --> D{{Choose Career Path}}
    D --> E[Backend]
    D --> F[Data and AI]
    D --> G[DevOps and Cloud]
    D --> H[Cybersecurity]
    E --> I[Portfolio Evidence]
    F --> I
    G --> I
    H --> I
```

{"\n\n".join(sections)}

## Companion Learning Resources

| Resource | Purpose |
| --- | --- |
| [Infographics](./Infographics/) | Visual mental models and symbol legend |
| [Cheat Sheets](./CheatSheets/) | Fast syntax and standard-library reference |
| [Interview Questions](./Interview-Questions/) | Recall, discussion, and system-design prompts |
| [Projects](./Projects/) | Progressive portfolio briefs and acceptance criteria |
| [Roadmaps](./Roadmaps/) | Complete and role-specific learning sequences |
| [Supplemental book](../A%20Smarter%20Way%20to%20Learn%20Python%20.pdf) | Additional practice reading (241-page PDF) |

## Directory Map

```text
Python-Mastery/
├── Beginner/              # 35 topic documents
├── Intermediate/          # 35 topic documents
├── Advanced/              # 40 topic documents
├── Infographics/
├── CheatSheets/
├── Interview-Questions/
├── Projects/
├── Roadmaps/
└── README.md
```

## Publishing Notes

- Markdown headings and relative links work directly on GitHub and Obsidian.
- Each topic is self-contained for NotebookLM source selection.
- Mermaid-enabled portals render the workflow blocks as diagrams.
- Notion users can import the folders or individual Markdown files.
- The repository root `README.md` remains the canonical single-page edition.
"""
    DESTINATION.mkdir(parents=True, exist_ok=True)
    (DESTINATION / "README.md").write_text(content, encoding="utf-8")


def build_infographics() -> None:
    content = """# Python Learning Infographics

[← Knowledge base](../README.md)

## Three-Level Mental Model

```mermaid
flowchart TB
    subgraph L1[Level 1 · Beginner]
        A[Values and Types] --> B[Control Flow]
        B --> C[Functions and Files]
    end
    subgraph L2[Level 2 · Intermediate]
        D[Objects and Protocols] --> E[Integration and Data]
        E --> F[Testing and Packaging]
    end
    subgraph L3[Level 3 · Advanced]
        G[Internals and Architecture] --> H[Scale and Distribution]
        H --> I[Specialization]
    end
    C --> D
    F --> G
```

## Infographic Block Legend

| Block | Question it answers | Study action |
| --- | --- | --- |
| 📌 Concept | What is the essential mental model? | Explain it in one sentence. |
| ⚡ Purpose | Why does this capability exist? | Name the problem it solves. |
| 🔥 Benefits | What improves when it is applied well? | Identify a measurable benefit. |
| 🎯 Use Cases | Where does it create value? | Connect it to a real system. |
| 🚀 Best Practices | How should professionals apply it? | Add the practice to your code review. |
| ❌ Common Mistakes | What failure modes should you avoid? | Write a failing example, then fix it. |

## Program Execution Model

```mermaid
flowchart LR
    S[Source Code] --> P[Parse]
    P --> B[Compile to Bytecode]
    B --> V[Python Virtual Machine]
    V --> O[Observable Result]
    O --> T[Tests and Feedback]
    T --> S
```

Every topic document contains a focused infographic table and workflow diagram. Use this directory as the visual entry point, then open the relevant lesson for code and detail.
"""
    directory = DESTINATION / "Infographics"
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "README.md").write_text(content, encoding="utf-8")


def build_cheat_sheets() -> None:
    content = """# Python Cheat Sheets

[← Knowledge base](../README.md)

## Core Syntax

| Goal | Pattern | Note |
| --- | --- | --- |
| Assign a value | `name = "Ada"` | Names reference objects. |
| Branch | `if condition: ... elif other: ... else: ...` | Indentation defines each block. |
| Iterate | `for item in iterable: ...` | Prefer direct iteration to indexes. |
| Define behavior | `def function(arg: str) -> str: ...` | Keep one clear responsibility. |
| Handle failure | `try: ... except ValueError as error: ...` | Catch the narrowest useful exception. |
| Manage a resource | `with open(path) as stream: ...` | Context managers guarantee cleanup. |
| Transform values | `[f(x) for x in values if valid(x)]` | Use a loop when logic becomes dense. |
| Model data | `@dataclass class Item: ...` | Add types and explicit invariants. |

## Collection Selection

| Type | Ordered | Mutable | Unique | Best fit |
| --- | --- | --- | --- | --- |
| `list` | Yes | Yes | No | Sequence that changes |
| `tuple` | Yes | No | No | Fixed record or return group |
| `set` | No | Yes | Yes | Membership and deduplication |
| `dict` | Yes | Yes | Keys | Keyed records and lookup |

## Complexity Quick Reference

| Operation | Typical cost | Caveat |
| --- | --- | --- |
| List index | O(1) | Insert near the front is O(n). |
| Dictionary lookup | O(1) average | Hash collisions affect worst cases. |
| Set membership | O(1) average | Members must be hashable. |
| Sort | O(n log n) | Key functions run once per item. |
| Linear scan | O(n) | Stop early when possible. |

## Standard Library Starter Kit

| Need | Module |
| --- | --- |
| Paths and files | `pathlib`, `shutil` |
| Dates and time zones | `datetime`, `zoneinfo` |
| Structured data | `json`, `csv`, `sqlite3` |
| CLI parsing | `argparse` |
| Testing | `unittest`, `unittest.mock` |
| Concurrency | `threading`, `multiprocessing`, `asyncio` |
| Diagnostics | `logging`, `traceback`, `cProfile` |
| Iteration tools | `itertools`, `functools`, `collections` |

> Treat cheat sheets as retrieval aids, not substitutes for the topic lessons or hands-on practice.
"""
    directory = DESTINATION / "CheatSheets"
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "README.md").write_text(content, encoding="utf-8")


def build_interview_questions() -> None:
    content = """# Python Interview Questions

[← Knowledge base](../README.md)

Use these prompts for active recall, mock interviews, or instructor-led reviews. Strong answers explain tradeoffs and include a small example.

## Beginner

1. What is the difference between an object, a variable, and a type?
2. When would you choose a tuple instead of a list?
3. How do truthiness, `and`, and `or` affect conditional execution?
4. What is the difference between `break`, `continue`, and `pass`?
5. Why are mutable default arguments dangerous?
6. How does local scope differ from global and nonlocal scope?
7. What guarantees does a `with open(...)` block provide?
8. How would you isolate a project’s dependencies?

## Intermediate

1. Compare composition and inheritance. When does each reduce coupling?
2. Explain the iterator protocol and how a generator implements it.
3. What does a decorator replace, and how do you preserve metadata?
4. When should an application log an exception versus raise it?
5. Compare threads, processes, and async tasks for I/O- and CPU-bound work.
6. How do parameterized SQL queries prevent injection?
7. Where should API validation, business logic, and persistence live?
8. What distinguishes a unit test from an integration test?
9. How do mocks help, and how can excessive mocking make tests misleading?
10. What files are required to package and publish a modern Python project?

## Advanced

1. How do descriptors participate in attribute lookup?
2. What problem can a metaclass solve that a class decorator cannot?
3. Explain reference counting and cyclic garbage collection in CPython.
4. How does the GIL affect concurrency choices?
5. What consistency, availability, and failure tradeoffs arise in distributed systems?
6. How would you design an idempotent ETL pipeline?
7. Which metrics reveal that Python code needs optimization?
8. How do you prevent cascading failures between microservices?
9. What belongs in a container image versus runtime configuration?
10. How would you secure, observe, and scale a Python API?

## Answer Framework

```mermaid
flowchart LR
    A[Define] --> B[Show a Minimal Example]
    B --> C[Name Tradeoffs]
    C --> D[Describe Failure Modes]
    D --> E[Connect to Production]
```

For each answer, aim to provide: a precise definition, one concrete example, alternatives, edge cases, and a production decision rule.
"""
    directory = DESTINATION / "Interview-Questions"
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "README.md").write_text(content, encoding="utf-8")


def build_projects() -> None:
    content = """# Python Portfolio Projects

[← Knowledge base](../README.md)

## Progressive Project Catalog

| Level | Project | Core capabilities | Acceptance evidence |
| --- | --- | --- | --- |
| Beginner | Expense tracker CLI | Input, types, functions, files, exceptions | Validated entries persist and reload |
| Beginner | Text analytics tool | Strings, dictionaries, sorting | Frequency report handles empty input |
| Beginner | Quiz engine | Control flow, collections, modules | Score and missed-answer review |
| Intermediate | Installable task CLI | Packaging, argparse, logging, tests | Clean install plus automated tests |
| Intermediate | API data synchronizer | Requests, JSON, config, retries | Idempotent sync and failure logs |
| Intermediate | Inventory service | OOP, SQLite, SQLAlchemy, pytest | CRUD flow with isolated test database |
| Intermediate | Concurrent URL checker | Threads or asyncio, timeouts | Bounded concurrency and summary report |
| Advanced | FastAPI order service | API design, validation, persistence | OpenAPI docs, tests, container image |
| Advanced | Resilient ETL pipeline | Pandas/PySpark, quality checks | Restart-safe stages and lineage notes |
| Advanced | ML inference service | NumPy/ML, FastAPI, monitoring | Versioned model and latency metrics |
| Advanced | Cloud automation controller | SDK, security, CI/CD | Dry-run mode and least-privilege policy |
| Advanced | Distributed job platform | Queues, workers, idempotency | Retry strategy and architecture diagram |

## Definition of Done

- A concise problem statement and explicit non-goals.
- Reproducible setup with pinned or constrained dependencies.
- Tests for important behavior and failure paths.
- Structured logging without secrets or personal data.
- Configuration outside source code.
- Security assumptions and threat notes.
- Architecture or workflow diagram.
- A README that explains operation, tradeoffs, and limitations.

```mermaid
flowchart TD
    A[Select a Real Problem] --> B[Write Acceptance Criteria]
    B --> C[Build the Smallest Vertical Slice]
    C --> D[Test Happy and Failure Paths]
    D --> E[Add Observability and Security]
    E --> F[Package or Deploy]
    F --> G[Document Evidence]
    G --> H{Criteria Met?}
    H -- No --> C
    H -- Yes --> I[Portfolio Ready]
```
"""
    directory = DESTINATION / "Projects"
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "README.md").write_text(content, encoding="utf-8")


def build_roadmaps(source: str) -> None:
    start = source.find("## Complete Python Roadmap")
    end = source.find("## Recommended Folder Structure for NotebookLM", start)
    if start < 0 or end < 0:
        raise ValueError("Could not locate the final career roadmaps")
    roadmaps = source[start:end].rstrip()
    content = (
        "# Python Career Roadmaps\n\n"
        "[← Knowledge base](../README.md)\n\n"
        "Use the complete roadmap for shared foundations, then choose one role path. "
        "The “Demonstrate” column is a portfolio requirement, not an optional reading task.\n\n"
        f"{roadmaps}\n"
    )
    directory = DESTINATION / "Roadmaps"
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "README.md").write_text(content, encoding="utf-8")


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    if DESTINATION.exists():
        shutil.rmtree(DESTINATION)
    DESTINATION.mkdir()

    build_topic_documents(source)
    build_main_index()
    build_infographics()
    build_cheat_sheets()
    build_interview_questions()
    build_projects()
    build_roadmaps(source)

    total = sum(len(topics) for topics in LEVELS.values())
    print(f"Exported {total} topic documents to {DESTINATION.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

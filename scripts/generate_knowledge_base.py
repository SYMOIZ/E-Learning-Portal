#!/usr/bin/env python3
"""Generate the complete Python Knowledge Base README and topic files."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from textwrap import dedent

sys.path.insert(0, str(Path(__file__).resolve().parent))
from topic_snippets import TOPIC_SNIPPETS

ROOT = Path(__file__).resolve().parents[1]
MASTERY = ROOT / "Python-Mastery"

BEGINNER = [
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
]

INTERMEDIATE = [
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
]

ADVANCED = [
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
]

def slugify(title: str) -> str:
    s = title.lower().replace(" ", "-")
    return re.sub(r"[^a-z0-9-]", "", s)


def default_topic_data(title: str, level: str) -> dict:
    level_context = {
        "Beginner": ("foundational Python skill", "scripts and small programs", "learning and automation"),
        "Intermediate": ("production-oriented Python capability", "applications and integrations", "backend and data workflows"),
        "Advanced": ("expert-level Python engineering topic", "large-scale systems", "cloud, ML, and platform engineering"),
    }
    ctx, use, career = level_context[level]
    short = title.lower()
    return {
        "what": f"{title} is a {ctx} that helps you write reliable Python software.",
        "why": f"Mastering {title} unlocks faster development, fewer bugs, and stronger career options.",
        "where": f"Used in {use} across startups and enterprises.",
        "objectives": [
            f"Explain the purpose of {title}.",
            f"Apply {title} in practical examples.",
            f"Recognize common pitfalls and best practices.",
        ],
        "outcome": f"You can use {title} confidently in real projects.",
        "industry": ["Software engineering", "Data platforms", "DevOps", "Security automation"],
        "concepts": [
            (f"{title} Basics", f"Core idea behind {short}.", f"# Example usage of {short}"),
            ("Workflow Integration", f"How {short} fits a Python project.", "import -> configure -> execute"),
            ("Error Handling", "Anticipate failures and recover gracefully.", "try/except with logging"),
        ],
        "concept": f"{title} extends your Python toolkit.",
        "purpose": f"Solve problems related to {short} efficiently.",
        "benefits": "Cleaner code, better performance, easier maintenance.",
        "use_cases": f"Projects requiring {short} in web, data, or ops stacks.",
        "best_practices": "Read docs, write tests, prefer standard library when sufficient.",
        "mistakes": "Skipping documentation, over-engineering, ignoring edge cases.",
        "basic_syntax": f"# {title} basic usage\npass",
        "structure": f"# setup {short}\n# apply {short}\n# validate results",
        "pattern": f"prepare -> apply {short} -> verify output",
        "beginner": f"# Beginner: {title}\nresult = 'example'\nprint(result)",
        "intermediate": dedent(
            f'''\
            # Intermediate: {title}
            def apply_{slugify(title).replace("-", "_")}(data):
                processed = data
                return processed


            print(apply_{slugify(title).replace("-", "_")}([1, 2, 3]))'''
        ),
        "advanced": dedent(
            f'''\
            # Advanced: {title}
            from typing import Protocol


            class {re.sub(r"[^A-Za-z0-9]", "", title)}Handler(Protocol):
                def run(self) -> None: ...


            class ProductionHandler:
                def run(self) -> None:
                    print("Executing {title} pipeline")'''
        ),
        "mermaid": dedent(
            f'''\
            flowchart LR
                A[Input] --> B[{title}]
                B --> C[Processing]
                C --> D[Output]'''
        ),
    }


def get_topic_data(title: str, level: str) -> dict:
    if title in TOPIC_SNIPPETS:
        return TOPIC_SNIPPETS[title]
    return default_topic_data(title, level)


def render_topic(title: str, level: str, index: int) -> str:
    d = get_topic_data(title, level)
    concepts_md = ""
    for name, definition, example in d["concepts"]:
        concepts_md += f"\n### {name}\n\n"
        concepts_md += f"- **Definition:** {definition}\n"
        concepts_md += f"- **Visual explanation:** `{name}` → process → result\n"
        concepts_md += f"- **Practical example:**\n\n```python\n{example}\n```\n"

    objectives = "\n".join(f"- {o}" for o in d["objectives"])
    industry = "\n".join(f"- {i}" for i in d["industry"])

    return (
        f"# {title}\n\n"
        f"## Overview\n\n"
        f"- **What is it?** {d['what']}\n"
        f"- **Why is it important?** {d['why']}\n"
        f"- **Where is it used?** {d['where']}\n\n"
        f"## Learning Objectives\n\n"
        f"- **Skills gained:** Practical command of {title}.\n"
        f"- **Concepts covered:**\n\n"
        f"{objectives}\n\n"
        f"- **Expected outcome:** {d['outcome']}\n\n"
        f"## Real World Applications\n\n"
        f"{industry}\n\n"
        f"- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.\n"
        f"- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.\n\n"
        f"## Core Concepts\n"
        f"{concepts_md}\n"
        f"## Infographic Summary\n\n"
        f"| Block | Summary |\n"
        f"| --- | --- |\n"
        f"| 📌 Concept | {d['concept']} |\n"
        f"| ⚡ Purpose | {d['purpose']} |\n"
        f"| 🔥 Benefits | {d['benefits']} |\n"
        f"| 🎯 Use Cases | {d['use_cases']} |\n"
        f"| 🚀 Best Practices | {d['best_practices']} |\n"
        f"| ❌ Common Mistakes | {d['mistakes']} |\n\n"
        f"## Syntax Guide\n\n"
        f"### Basic Syntax\n\n"
        f"```python\n{d['basic_syntax']}\n```\n\n"
        f"### Standard Structure\n\n"
        f"```python\n{d['structure']}\n```\n\n"
        f"### Code Pattern\n\n"
        f"```python\n{d['pattern']}\n```\n\n"
        f"## Examples\n\n"
        f"### Beginner Example\n\n"
        f"```python\n{d['beginner']}\n```\n\n"
        f"### Intermediate Example\n\n"
        f"```python\n{d['intermediate']}\n```\n\n"
        f"### Advanced Example\n\n"
        f"```python\n{d['advanced']}\n```\n\n"
        f"## Workflow Diagram\n\n"
        f"```mermaid\n{d['mermaid']}\n```\n\n"
        f"---\n"
    )


def render_toc(level_name: str, topics: list[str], level_slug: str) -> str:
    lines = [f"### {level_name}\n"]
    for i, topic in enumerate(topics, 1):
        anchor = slugify(topic)
        lines.append(f"{i}. [{topic}](#{anchor})")
    lines.append("")
    lines.append("")
    return "\n".join(lines)


def render_career_section() -> str:
    return dedent(
        """\
        # Complete Python Roadmap

        ```mermaid
        flowchart TB
            subgraph L1[Level 1: Beginner]
                B1[Syntax & Types]
                B2[Control Flow]
                B3[Functions & Files]
            end
            subgraph L2[Level 2: Intermediate]
                I1[OOP & Patterns]
                I2[APIs & Databases]
                I3[Testing & Packaging]
            end
            subgraph L3[Level 3: Advanced]
                A1[Internals & Performance]
                A2[Cloud & DevOps]
                A3[Data & AI]
            end
            L1 --> L2 --> L3
        ```

        ## Python Career Paths

        | Path | Focus | Key Skills | Typical Titles |
        | --- | --- | --- | --- |
        | Backend Engineer | APIs, databases, services | FastAPI/Django, SQL, caching, auth | Backend Dev, API Engineer |
        | Data Engineer | Pipelines, warehousing, ETL | Pandas, PySpark, SQL, Airflow | Data Engineer, Analytics Engineer |
        | AI Engineer | Models, MLOps, inference | NumPy, ML/DL, FastAPI serving | ML Engineer, AI Engineer |
        | DevOps Engineer | CI/CD, infra, automation | Docker, K8s, Terraform, pytest | DevOps, Platform Engineer |
        | Security Engineer | Automation, scanning, SOAR | scripting, sockets, APIs | AppSec, Detection Engineer |

        ## Python Developer Roadmap

        1. **Months 1–2:** Syntax, collections, functions, files, exceptions.
        2. **Months 3–4:** OOP, modules, venv, testing basics, CLI tools.
        3. **Months 5–6:** Web or data specialization, Git, REST APIs, SQL.
        4. **Months 7–12:** Framework depth, cloud deployment, performance, system design.

        ## Backend Engineer Roadmap

        | Stage | Topics | Deliverable |
        | --- | --- | --- |
        | Foundation | Python, HTTP, JSON, SQL | CRUD CLI or script |
        | Framework | FastAPI/Flask/Django, auth, ORM | REST API with tests |
        | Production | Docker, logging, migrations, caching | Deployed microservice |
        | Scale | async, queues, observability, CI/CD | High-traffic API design |

        ## Data Engineer Roadmap

        | Stage | Topics | Deliverable |
        | --- | --- | --- |
        | Foundation | Python, pandas, SQL, CSV/JSON | Data cleaning notebook |
        | Pipelines | ETL, scheduling, logging | Batch ingestion job |
        | Big Data | PySpark, partitioning, Parquet | Distributed transform |
        | Platform | cloud storage, orchestration, data quality | Production pipeline |

        ## AI Engineer Roadmap

        | Stage | Topics | Deliverable |
        | --- | --- | --- |
        | Math & Python | NumPy, linear algebra basics | Vector operations script |
        | ML | scikit-learn, evaluation, features | Classification project |
        | Deep Learning | PyTorch/TF, NLP/CV basics | Model training pipeline |
        | MLOps | FastAPI serving, monitoring, CI | Deployed inference API |

        ## DevOps Engineer Roadmap

        | Stage | Topics | Deliverable |
        | --- | --- | --- |
        | Scripting | Python automation, argparse, logging | Ops automation script |
        | Containers | Docker, compose, health checks | Containerized Python app |
        | Orchestration | Kubernetes, Helm, secrets | K8s deployment manifest |
        | CI/CD | GitHub Actions, tests, lint, deploy | Full pipeline |

        ## Cybersecurity Engineer Roadmap

        | Stage | Topics | Deliverable |
        | --- | --- | --- |
        | Scripting | sockets, regex, file parsing | Log parser |
        | Automation | API consumption, scheduling | Vuln scan orchestrator |
        | Integration | SIEM/API hooks, async jobs | Alert enrichment tool |
        | Hardening | secure coding, secrets, testing | Audited automation framework |

        ---

        ## Recommended Folder Structure for NotebookLM

        ```text
        Python-Mastery/
        │
        ├── Beginner/
        │   ├── 01-Introduction-to-Python.md
        │   ├── 02-Installing-Python.md
        │   └── ...
        │
        ├── Intermediate/
        │   ├── 01-Object-Oriented-Programming.md
        │   └── ...
        │
        ├── Advanced/
        │   ├── 01-Data-Structures-Internals.md
        │   └── ...
        │
        ├── Infographics/
        ├── CheatSheets/
        ├── Interview-Questions/
        ├── Projects/
        ├── Roadmaps/
        └── README.md
        ```

        ## Quick Reference Cheat Sheet

        | Category | Must-Know |
        | --- | --- |
        | Syntax | indent blocks, `:` endings, `#` comments |
        | Collections | list `[]`, tuple `()`, set `{}`, dict `{k:v}` |
        | Functions | `def`, `*args`, `**kwargs`, `return` |
        | OOP | `class`, `__init__`, inheritance, `@property` |
        | Async | `async def`, `await`, `asyncio.run()` |
        | Testing | `pytest`, fixtures, mocking |
        | Web | FastAPI/Flask routes, Pydantic, middleware |
        | Data | pandas DataFrame, groupby, merge |
        | DevOps | Docker, `requirements.txt`, GitHub Actions |

        ---

        *Generated for GitHub, NotebookLM, Obsidian, Notion, and documentation portals.*
        """
    )


def write_topic_files(level: str, topics: list[str]) -> None:
    folder = MASTERY / level
    folder.mkdir(parents=True, exist_ok=True)
    for i, topic in enumerate(topics, 1):
        content = render_topic(topic, level, i)
        filename = f"{i:02d}-{slugify(topic)}.md"
        (folder / filename).write_text(content, encoding="utf-8")


def build_readme() -> str:
    header = dedent(
        """\
        # PYTHON LEARNING ROADMAP

        > **E-Learning Portal** — Complete Python Knowledge Base for GitHub, NotebookLM, Obsidian, Notion, and documentation portals.

        ## How to Use This Knowledge Base

        1. Start at **Level 1: Beginner** if you are new to programming.
        2. Progress to **Level 2: Intermediate** when you can build small apps independently.
        3. Study **Level 3: Advanced** for production engineering, cloud, data, and AI roles.
        4. Import individual topic files from [`Python-Mastery/`](Python-Mastery/) into NotebookLM or Obsidian.

        ## Table of Contents

        """
    )
    toc = (
        render_toc("Level 1: Beginner", BEGINNER, "beginner")
        + render_toc("Level 2: Intermediate", INTERMEDIATE, "intermediate")
        + render_toc("Level 3: Advanced", ADVANCED, "advanced")
        + "\n### Final Sections\n\n"
        + "- [Complete Python Roadmap](#complete-python-roadmap)\n"
        + "- [Python Career Paths](#python-career-paths)\n"
        + "- [Recommended Folder Structure](#recommended-folder-structure-for-notebooklm)\n\n"
        + "---\n\n"
    )

    body_parts = ["## Level 1: Beginner\n"]
    for i, t in enumerate(BEGINNER, 1):
        body_parts.append(render_topic(t, "Beginner", i))

    body_parts.append("## Level 2: Intermediate\n")
    for i, t in enumerate(INTERMEDIATE, 1):
        body_parts.append(render_topic(t, "Intermediate", i))

    body_parts.append("## Level 3: Advanced\n")
    for i, t in enumerate(ADVANCED, 1):
        body_parts.append(render_topic(t, "Advanced", i))

    body_parts.append(render_career_section())
    return header + toc + "\n".join(body_parts)


def main() -> None:
    for sub in ["Infographics", "CheatSheets", "Interview-Questions", "Projects", "Roadmaps"]:
        (MASTERY / sub).mkdir(parents=True, exist_ok=True)
        placeholder = MASTERY / sub / "README.md"
        placeholder.write_text(f"# {sub.replace('-', ' ')}\n\nAdd resources here.\n", encoding="utf-8")

    write_topic_files("Beginner", BEGINNER)
    write_topic_files("Intermediate", INTERMEDIATE)
    write_topic_files("Advanced", ADVANCED)

    readme = build_readme()
    (ROOT / "README.md").write_text(readme, encoding="utf-8")

    mastery_readme = dedent(
        """\
        # Python Mastery — Topic Library

        This folder mirrors the main [README](../README.md) as individual topic files for NotebookLM, Obsidian, and Notion imports.

        | Level | Topics | Folder |
        | --- | --- | --- |
        | Beginner | 35 | [Beginner/](Beginner/) |
        | Intermediate | 36 | [Intermediate/](Intermediate/) |
        | Advanced | 40 | [Advanced/](Advanced/) |

        ## Import Tips

        - **NotebookLM:** Upload an entire level folder as a source set.
        - **Obsidian:** Symlink or copy `Python-Mastery/` into your vault.
        - **Notion:** Import markdown files per level or per topic.
        """
    )
    (MASTERY / "README.md").write_text(mastery_readme, encoding="utf-8")

    print(f"Generated README.md ({len(readme):,} chars)")
    print(f"Topic files: {len(BEGINNER) + len(INTERMEDIATE) + len(ADVANCED)}")


if __name__ == "__main__":
    main()

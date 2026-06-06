#!/usr/bin/env python3
"""Build scripts/topic_snippets.py with all topic entries."""

from __future__ import annotations

import ast
import re
from pathlib import Path
from textwrap import dedent

OUTPUT = Path(__file__).resolve().parent / "topic_snippets.py"

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

ALL_TOPICS = [(t, "Beginner") for t in BEGINNER] + [(t, "Intermediate") for t in INTERMEDIATE] + [(t, "Advanced") for t in ADVANCED]


def slug(title: str) -> str:
    return re.sub(r"[^a-z0-9_]", "_", title.lower())


def S(
    title: str,
    *,
    what: str,
    why: str,
    where: str,
    objectives: list[str],
    outcome: str,
    industry: list[str],
    concepts: list[tuple[str, str, str]],
    concept: str,
    purpose: str,
    benefits: str,
    use_cases: str,
    best_practices: str,
    mistakes: str,
    basic_syntax: str,
    structure: str,
    pattern: str,
    beginner: str,
    intermediate: str,
    advanced: str,
    mermaid: str,
) -> dict:
    assert len(objectives) == 3, title
    assert len(industry) == 4, title
    assert len(concepts) == 3, title
    return {
        "what": what,
        "why": why,
        "where": where,
        "objectives": objectives,
        "outcome": outcome,
        "industry": industry,
        "concepts": concepts,
        "concept": concept,
        "purpose": purpose,
        "benefits": benefits,
        "use_cases": use_cases,
        "best_practices": best_practices,
        "mistakes": mistakes,
        "basic_syntax": basic_syntax,
        "structure": structure,
        "pattern": pattern,
        "beginner": beginner,
        "intermediate": intermediate,
        "advanced": advanced,
        "mermaid": mermaid,
    }


# ---------------------------------------------------------------------------
# Curated topic snippets (keyed by exact title)
# ---------------------------------------------------------------------------

SNIPPETS: dict[str, dict] = {}

def add(title: str, data: dict) -> None:
    SNIPPETS[title] = data


add("Introduction to Python", S(
    "Introduction to Python",
    what="Python is a high-level, interpreted language prized for readable syntax and a vast ecosystem.",
    why="It powers web backends, data science, automation, AI, and DevOps with one of the largest communities.",
    where="Startups, enterprises, research labs, fintech, healthcare analytics, and cloud platforms.",
    objectives=[
        "Explain Python's design philosophy and ecosystem.",
        "Compare Python to other languages for common workloads.",
        "Identify domains where Python excels.",
    ],
    outcome="You can explain why Python fits a project and where it belongs in a tech stack.",
    industry=["Web services", "Data pipelines", "ML platforms", "Security automation"],
    concepts=[
        ("Interpreted Execution", "Source code runs via the interpreter without a separate compile step.", "print('Hello, Python!')"),
        ("Standard Library", "Batteries-included modules ship with Python.", "import json\nprint(json.dumps({'ok': True}))"),
        ("Dynamic Typing", "Names bind to objects; types are checked at runtime.", "x = 10\nx = 'ten'\nprint(x)"),
    ],
    concept="Python is interpreted, dynamically typed, and multi-paradigm.",
    purpose="Ship solutions quickly with readable code and strong libraries.",
    benefits="Fast prototyping, huge community, cross-platform, excellent for teams.",
    use_cases="APIs, ETL, notebooks, scripting, AI/ML, test automation.",
    best_practices="Follow PEP 8, use virtual environments, prefer clarity over cleverness.",
    mistakes="Assuming Python is slow for every task, ignoring version pins, skipping tests.",
    basic_syntax='print("Hello, Python!")',
    structure=dedent("""\
        def main():
            print("Learning Python")


        if __name__ == "__main__":
            main()"""),
    pattern=dedent("""\
        import module
        result = module.do_work()
        print(result)"""),
    beginner='print("Python is fun!")',
    intermediate=dedent("""\
        domains = ["web", "data", "automation", "ai"]
        for domain in domains:
            print(f"Python powers {domain}")"""),
    advanced=dedent("""\
        from dataclasses import dataclass


        @dataclass(frozen=True)
        class LanguageProfile:
            name: str
            paradigms: tuple[str, ...]
            typing: str


        python = LanguageProfile("Python", ("multi-paradigm",), "dynamic")
        print(python)"""),
    mermaid=dedent("""\
        flowchart TD
            A[Write Python Code] --> B[Interpreter]
            B --> C[Standard Library]
            B --> D[Third-Party Packages]
            C --> E[Application Output]
            D --> E"""),
))

add("Installing Python", S(
    "Installing Python",
    what="Installing Python means obtaining the interpreter, pip, and tooling on your system.",
    why="A correct install prevents version conflicts and broken dependencies across projects.",
    where="Developer laptops, CI runners, Docker images, and cloud VMs.",
    objectives=[
        "Install a supported Python 3.x release safely.",
        "Verify python and pip from the terminal.",
        "Choose between system Python, pyenv, or conda.",
    ],
    outcome="You can install Python and confirm a working environment from the shell.",
    industry=["Developer onboarding", "CI/CD images", "Container builds", "Education platforms"],
    concepts=[
        ("Interpreter", "The python binary executes .py files.", "python3 --version"),
        ("pip", "Package installer bundled with Python.", "python3 -m pip --version"),
        ("Virtual Environments", "Isolated installs per project.", "python3 -m venv .venv"),
    ],
    concept="Installation delivers interpreter + pip + optional version managers.",
    purpose="Run Python code reliably on any machine.",
    benefits="Reproducible environments, easier collaboration, safer upgrades.",
    use_cases="Local dev, servers, notebooks, automation agents.",
    best_practices="Pin versions, use venv, document setup in README.",
    mistakes="Mixing Python 2 and 3, global pip installs, ignoring PATH.",
    basic_syntax="python3 --version",
    structure="# download -> install -> verify -> create venv",
    pattern="python3 -m venv .venv && source .venv/bin/activate",
    beginner=dedent("""\
        # Linux (Debian/Ubuntu)
        sudo apt update && sudo apt install -y python3 python3-venv python3-pip"""),
    intermediate=dedent("""\
        import sys
        print(sys.version)
        print(sys.executable)"""),
    advanced=dedent("""\
        # Dockerfile
        FROM python:3.12-slim
        WORKDIR /app
        COPY requirements.txt .
        RUN pip install --no-cache-dir -r requirements.txt"""),
    mermaid="flowchart LR\n    A[Download] --> B[Install]\n    B --> C[Verify]\n    C --> D[venv]\n    D --> E[Dependencies]",
))

add("IDE Setup", S(
    "IDE Setup",
    what="IDE setup configures an editor with Python interpreter, linting, debugging, and formatting.",
    why="Good tooling catches errors early and speeds up navigation in growing codebases.",
    where="Daily development in VS Code, PyCharm, Vim/Neovim, and cloud IDEs.",
    objectives=[
        "Select and configure a Python-capable editor.",
        "Attach the correct interpreter and extensions.",
        "Enable format-on-save, linting, and debugging.",
    ],
    outcome="You have a productive Python workspace with run and debug shortcuts.",
    industry=["Software teams", "Remote development", "Bootcamps", "Open-source contributors"],
    concepts=[
        ("Interpreter Path", "Editor must point at project venv Python.", 'which python  # e.g. .venv/bin/python'),
        ("LSP / Pylance", "Language server powers autocomplete and types.", "# VS Code: Python extension + Pylance"),
        ("Debugger", "Breakpoints inspect live program state.", "import pdb; pdb.set_trace()"),
    ],
    concept="IDE = editor + language server + debugger + formatter.",
    purpose="Reduce friction while writing and testing Python.",
    benefits="Autocomplete, refactor tools, integrated tests, faster onboarding.",
    use_cases="Feature development, code review prep, teaching, pair programming.",
    best_practices="One venv per repo, commit editorconfig, share launch.json for teams.",
    mistakes="Using global Python, disabling type checking, no formatter config.",
    basic_syntax="# Open folder, select interpreter, run current file",
    structure="# install editor -> select venv -> configure linter/formatter -> debug",
    pattern="edit -> lint -> format -> run tests",
    beginner=dedent("""\
        # settings.json snippet (VS Code)
        # "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python"
        print("Ready to code")"""),
    intermediate=dedent("""\
        import sys
        print("Interpreter:", sys.executable)
        print("Version:", sys.version.split()[0])"""),
    advanced=dedent("""\
        # pyproject.toml tool config
        # [tool.ruff]
        # line-length = 88
        # select = ["E", "F", "I"]
        def greet(name: str) -> str:
            return f"Hello, {name}"


        print(greet("Dev"))"""),
    mermaid="flowchart LR\n    A[Project Folder] --> B[Select venv]\n    B --> C[LSP]\n    C --> D[Lint/Format]\n    D --> E[Run/Debug]",
))

add("Python Syntax", S(
    "Python Syntax",
    what="Python syntax defines how statements, blocks, and expressions are written.",
    why="Correct syntax is required before logic, libraries, or frameworks matter.",
    where="Every script, notebook cell, test file, and module.",
    objectives=[
        "Use indentation, colons, and statement structure correctly.",
        "Write valid expressions and comments.",
        "Read tracebacks caused by syntax errors.",
    ],
    outcome="You write syntactically valid Python without constant SyntaxError failures.",
    industry=["Application code", "Data notebooks", "Infrastructure scripts", "Test suites"],
    concepts=[
        ("Indentation", "Blocks are defined by consistent leading spaces.", "if True:\n    print('indented')"),
        ("Colon Blocks", "Compound statements end with a colon.", "for i in range(3):\n    print(i)"),
        ("Comments", "Lines starting with # are ignored.", "# this is a comment\nx = 1"),
    ],
    concept="Python uses significant whitespace and readable English keywords.",
    purpose="Express program structure clearly without braces.",
    benefits="Less boilerplate, enforced readability, quick to learn.",
    use_cases="Scripts, functions, classes, config loaders.",
    best_practices="4 spaces per level, PEP 8 naming, one statement style per project.",
    mistakes="Mixing tabs and spaces, missing colons, trailing commas confusion.",
    basic_syntax='name = "Ada"\nprint(name)',
    structure="imports -> definitions -> main guard -> execution",
    pattern="prepare data -> process -> output",
    beginner=dedent("""\
        message = "Syntax matters"
        print(message)"""),
    intermediate=dedent("""\
        values = [1, 2, 3]
        squared = [v * v for v in values]
        print(squared)"""),
    advanced=dedent("""\
        from typing import Iterator


        def fibonacci(n: int) -> Iterator[int]:
            a, b = 0, 1
            for _ in range(n):
                yield a
                a, b = b, a + b


        print(list(fibonacci(6)))"""),
    mermaid="flowchart TD\n    A[Source File] --> B[Parser]\n    B --> C{Valid Syntax?}\n    C -->|yes| D[Execute]\n    C -->|no| E[SyntaxError]",
))

add("Variables", S(
    "Variables",
    what="Variables are names that reference objects stored in memory.",
    why="They let programs remember state and transform data over time.",
    where="Every Python program from scripts to ML pipelines.",
    objectives=[
        "Assign and reassign variables correctly.",
        "Follow PEP 8 naming conventions.",
        "Distinguish names from object identity.",
    ],
    outcome="You model program state with clear, consistent variable names.",
    industry=["Business logic", "ETL transforms", "Game state", "Financial models"],
    concepts=[
        ("Assignment", "Binds a name to an object.", "score = 100\nprint(score)"),
        ("Rebinding", "A name can refer to a new object.", "score = score + 10\nprint(score)"),
        ("snake_case", "Standard style for variable names.", "user_email = 'a@b.com'\nprint(user_email)"),
    ],
    concept="Variables label objects; they are not typed boxes.",
    purpose="Store and update program data.",
    benefits="Readable code, reusable values, easier debugging.",
    use_cases="Counters, configs, user input, API payloads.",
    best_practices="Descriptive names, avoid shadowing builtins, init before use.",
    mistakes="Reusing names for different concepts, mutating shared references unexpectedly.",
    basic_syntax="name = 'Ada'\nage = 36",
    structure="# declare -> use -> update",
    pattern="total = price * quantity\nprint(total)",
    beginner="x = 5\ny = 3\nprint(x + y)",
    intermediate="first, second, *rest = [1, 2, 3, 4, 5]\nprint(first, second, rest)",
    advanced=dedent("""\
        from typing import Final

        MAX_RETRIES: Final = 3
        attempts = 0
        while attempts < MAX_RETRIES:
            attempts += 1
        print(attempts)"""),
    mermaid="flowchart LR\n    A[Assign Name] --> B[Reference Object]\n    B --> C[Read/Update]",
))

# Remaining topics filled by build_snippet() below using curated templates
TOPIC_TEMPLATES: dict[str, dict] = {}

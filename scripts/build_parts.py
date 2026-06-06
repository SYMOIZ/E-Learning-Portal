#!/usr/bin/env python3
"""Generate snippet_parts/*.py with all curated topic entries."""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent

PARTS = Path(__file__).resolve().parent / "snippet_parts"


def S(
    what, why, where, objectives, outcome, industry, concepts,
    concept, purpose, benefits, use_cases, best_practices, mistakes,
    basic_syntax, structure, pattern, beginner, intermediate, advanced, mermaid,
):
    return {
        "what": what, "why": why, "where": where,
        "objectives": list(objectives), "outcome": outcome, "industry": list(industry),
        "concepts": list(concepts), "concept": concept, "purpose": purpose,
        "benefits": benefits, "use_cases": use_cases, "best_practices": best_practices,
        "mistakes": mistakes, "basic_syntax": basic_syntax, "structure": structure,
        "pattern": pattern, "beginner": beginner, "intermediate": intermediate,
        "advanced": advanced, "mermaid": mermaid,
    }


def beginner_snippets() -> dict:
    d = {}
    d["Introduction to Python"] = S(
        "Python is a high-level, interpreted language prized for readable syntax and a vast ecosystem.",
        "It powers web backends, data science, automation, AI, and DevOps with one of the largest communities.",
        "Startups, enterprises, research labs, fintech, healthcare analytics, and cloud platforms.",
        ("Explain Python's design philosophy and ecosystem.", "Compare Python to other languages for common workloads.", "Identify domains where Python excels."),
        "You can explain why Python fits a project and where it belongs in a tech stack.",
        ("Web services", "Data pipelines", "ML platforms", "Security automation"),
        (("Interpreted Execution", "Source runs via the interpreter without a separate compile step.", "print('Hello, Python!')"),
         ("Standard Library", "Batteries-included modules ship with Python.", "import json\nprint(json.dumps({'ok': True}))"),
         ("Dynamic Typing", "Names bind to objects; types are checked at runtime.", "x = 10\nx = 'ten'\nprint(x)")),
        "Python is interpreted, dynamically typed, and multi-paradigm.",
        "Ship solutions quickly with readable code and strong libraries.",
        "Fast prototyping, huge community, cross-platform, excellent for teams.",
        "APIs, ETL, notebooks, scripting, AI/ML, test automation.",
        "Follow PEP 8, use virtual environments, prefer clarity over cleverness.",
        "Assuming Python is slow for every task, ignoring version pins, skipping tests.",
        'print("Hello, Python!")',
        dedent("""def main():\n    print("Learning Python")\n\n\nif __name__ == "__main__":\n    main()"""),
        dedent("""import module\nresult = module.do_work()\nprint(result)"""),
        'print("Python is fun!")',
        dedent("""domains = ["web", "data", "automation", "ai"]\nfor domain in domains:\n    print(f"Python powers {domain}")"""),
        dedent("""from dataclasses import dataclass\n\n\n@dataclass(frozen=True)\nclass LanguageProfile:\n    name: str\n    paradigms: tuple[str, ...]\n    typing: str\n\n\npython = LanguageProfile("Python", ("multi-paradigm",), "dynamic")\nprint(python)"""),
        dedent("""flowchart TD\n    A[Write Python Code] --> B[Interpreter]\n    B --> C[Standard Library]\n    B --> D[Third-Party Packages]\n    C --> E[Application Output]\n    D --> E"""),
    )
    d["Installing Python"] = S(
        "Installing Python means obtaining the interpreter, pip, and tooling on your system.",
        "A correct install prevents version conflicts and broken dependencies across projects.",
        "Developer laptops, CI runners, Docker images, and cloud VMs.",
        ("Install a supported Python 3.x release safely.", "Verify python and pip from the terminal.", "Choose between system Python, pyenv, or conda."),
        "You can install Python and confirm a working environment from the shell.",
        ("Developer onboarding", "CI/CD images", "Container builds", "Education platforms"),
        (("Interpreter", "The python binary executes .py files.", "import sys\nprint(sys.version_info.major)"),
         ("pip", "Package installer bundled with Python.", "import ensurepip\nprint('pip available')"),
         ("Virtual Environments", "Isolated installs per project.", "import venv\nvenv.EnvBuilder().create('demo_venv')")),
        "Installation delivers interpreter + pip + optional version managers.",
        "Run Python code reliably on any machine.",
        "Reproducible environments, easier collaboration, safer upgrades.",
        "Local dev, servers, notebooks, automation agents.",
        "Pin versions, use venv, document setup in README.",
        "Mixing Python 2 and 3, global pip installs, ignoring PATH.",
        "import sys\nprint(sys.executable)",
        "# download -> install -> verify -> create venv",
        "import sys\nprint(f'Python {sys.version_info.major}.{sys.version_info.minor}')",
        dedent("""# Linux package install (run in shell)\n# sudo apt update && sudo apt install -y python3 python3-venv python3-pip\nimport platform\nprint(platform.python_version())"""),
        dedent("""import sys\nprint(sys.version)\nprint(sys.executable)"""),
        dedent("""import subprocess\nresult = subprocess.run([sys.executable, '-m', 'pip', '--version'], capture_output=True, text=True)\nprint(result.stdout.strip())"""),
        "flowchart LR\n    A[Download] --> B[Install]\n    B --> C[Verify]\n    C --> D[venv]\n    D --> E[Dependencies]",
    )
    return d


def write_part(name: str, snippets: dict) -> None:
    lines = [
        '"""Curated topic snippets ({} level)."""'.format(name),
        "from textwrap import dedent",
        "from _helpers import S",
        "",
        "SNIPPETS = {",
    ]
    for title, data in snippets.items():
        lines.append(f"    {title!r}: {data!r},")
    lines.append("}")
    lines.append("")
    # Use repr loses dedent - need proper serialization
    raise NotImplementedError("use pprint custom")


if __name__ == "__main__":
    print(len(beginner_snippets()))

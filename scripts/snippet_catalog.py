"""In-memory catalog of all 110 topic snippets."""

from __future__ import annotations

import sys
from pathlib import Path
from textwrap import dedent

sys.path.insert(0, str(Path(__file__).resolve().parent / "snippet_parts"))
from _helpers import S


def _beginner() -> dict[str, dict]:
    return {
        "Introduction to Python": S(
            "Python is a high-level, interpreted language prized for readable syntax and a vast ecosystem.",
            "It powers web backends, data science, automation, AI, and DevOps with one of the largest communities.",
            "Startups, enterprises, research labs, fintech, healthcare analytics, and cloud platforms.",
            (
                "Explain Python's design philosophy and ecosystem.",
                "Compare Python to other languages for common workloads.",
                "Identify domains where Python excels.",
            ),
            "You can explain why Python fits a project and where it belongs in a tech stack.",
            ("Web services", "Data pipelines", "ML platforms", "Security automation"),
            (
                ("Interpreted Execution", "Source runs via the interpreter without a separate compile step.", "print('Hello, Python!')"),
                ("Standard Library", "Batteries-included modules ship with Python.", "import json\nprint(json.dumps({'ok': True}))"),
                ("Dynamic Typing", "Names bind to objects; types are checked at runtime.", "x = 10\nx = 'ten'\nprint(x)"),
            ),
            "Python is interpreted, dynamically typed, and multi-paradigm.",
            "Ship solutions quickly with readable code and strong libraries.",
            "Fast prototyping, huge community, cross-platform, excellent for teams.",
            "APIs, ETL, notebooks, scripting, AI/ML, test automation.",
            "Follow PEP 8, use virtual environments, prefer clarity over cleverness.",
            "Assuming Python is slow for every task, ignoring version pins, skipping tests.",
            'print("Hello, Python!")',
            dedent("""\
                def main():
                    print("Learning Python")


                if __name__ == "__main__":
                    main()"""),
            dedent("""\
                import json
                payload = {"status": "ok"}
                print(json.dumps(payload))"""),
            'print("Python is fun!")',
            dedent("""\
                domains = ["web", "data", "automation", "ai"]
                for domain in domains:
                    print(f"Python powers {domain}")"""),
            dedent("""\
                from dataclasses import dataclass


                @dataclass(frozen=True)
                class LanguageProfile:
                    name: str
                    paradigms: tuple[str, ...]
                    typing: str


                python = LanguageProfile("Python", ("multi-paradigm",), "dynamic")
                print(python)"""),
            dedent("""\
                flowchart TD
                    A[Write Python Code] --> B[Interpreter]
                    B --> C[Standard Library]
                    B --> D[Third-Party Packages]
                    C --> E[Application Output]
                    D --> E"""),
        ),
        "Installing Python": S(
            "Installing Python means obtaining the interpreter, pip, and tooling on your system.",
            "A correct install prevents version conflicts and broken dependencies across projects.",
            "Developer laptops, CI runners, Docker images, and cloud VMs.",
            ("Install a supported Python 3.x release safely.", "Verify python and pip from the terminal.", "Choose between system Python, pyenv, or conda."),
            "You can install Python and confirm a working environment from the shell.",
            ("Developer onboarding", "CI/CD images", "Container builds", "Education platforms"),
            (
                ("Interpreter", "The python binary executes .py files.", "import sys\nprint(sys.version_info >= (3, 10))"),
                ("pip", "Package installer bundled with Python.", "import importlib.util\nprint(importlib.util.find_spec('pip') is not None)"),
                ("venv", "Creates isolated environments per project.", "import venv\nbuilder = venv.EnvBuilder(with_pip=True)\nprint(callable(builder.create))"),
            ),
            "Installation delivers interpreter + pip + optional version managers.",
            "Run Python code reliably on any machine.",
            "Reproducible environments, easier collaboration, safer upgrades.",
            "Local dev, servers, notebooks, automation agents.",
            "Pin versions, use venv, document setup in README.",
            "Mixing Python 2 and 3, global pip installs, ignoring PATH.",
            "import sys\nprint(sys.executable)",
            "# download -> install -> verify -> create venv",
            "import sys\nprint(f'Python {sys.version_info.major}.{sys.version_info.minor}')",
            dedent("""\
                # Shell: sudo apt install -y python3 python3-venv python3-pip
                import platform
                print(platform.python_version())"""),
            dedent("""\
                import sys
                print(sys.version)
                print(sys.executable)"""),
            dedent("""\
                import subprocess, sys
                out = subprocess.run([sys.executable, "-m", "pip", "--version"], capture_output=True, text=True)
                print(out.stdout.strip())"""),
            "flowchart LR\n    A[Download] --> B[Install]\n    B --> C[Verify]\n    C --> D[venv]\n    D --> E[Dependencies]",
        ),
        "IDE Setup": S(
            "IDE setup configures an editor with Python interpreter, linting, debugging, and formatting.",
            "Good tooling catches errors early and speeds up navigation in growing codebases.",
            "Daily development in VS Code, PyCharm, Vim/Neovim, and cloud IDEs.",
            ("Select and configure a Python-capable editor.", "Attach the correct interpreter and extensions.", "Enable format-on-save, linting, and debugging."),
            "You have a productive Python workspace with run and debug shortcuts.",
            ("Software teams", "Remote development", "Bootcamps", "Open-source contributors"),
            (
                ("Interpreter Path", "Editor must point at project venv Python.", "import sys\nprint(sys.executable)"),
                ("Language Server", "Powers autocomplete and diagnostics.", "import typing\nprint(typing.__name__)"),
                ("Debugger", "Breakpoints inspect live program state.", "x = 1\nx += 1\nprint(x)"),
            ),
            "IDE = editor + language server + debugger + formatter.",
            "Reduce friction while writing and testing Python.",
            "Autocomplete, refactor tools, integrated tests, faster onboarding.",
            "Feature development, code review prep, teaching, pair programming.",
            "One venv per repo, commit .editorconfig, share launch.json for teams.",
            "Using global Python, disabling type checking, no formatter config.",
            "print('IDE ready')",
            "# install editor -> select venv -> configure linter -> debug",
            "import sys\nprint('Interpreter:', sys.executable)",
            dedent("""\
                # VS Code: set python.defaultInterpreterPath to .venv/bin/python
                import sys
                print(sys.version.split()[0])"""),
            dedent("""\
                import sys
                print("Interpreter:", sys.executable)
                print("Version:", sys.version.split()[0])"""),
            dedent("""\
                def greet(name: str) -> str:
                    return f"Hello, {name}"


                print(greet("Dev"))"""),
            "flowchart LR\n    A[Project Folder] --> B[Select venv]\n    B --> C[LSP]\n    C --> D[Lint/Format]\n    D --> E[Run/Debug]",
        ),
        "Python Syntax": S(
            "Python syntax defines how statements, blocks, and expressions are written.",
            "Correct syntax is required before logic, libraries, or frameworks matter.",
            "Every script, notebook cell, test file, and module.",
            ("Use indentation, colons, and statement structure correctly.", "Write valid expressions and comments.", "Read tracebacks caused by syntax errors."),
            "You write syntactically valid Python without constant SyntaxError failures.",
            ("Application code", "Data notebooks", "Infrastructure scripts", "Test suites"),
            (
                ("Indentation", "Blocks are defined by consistent leading spaces.", "if True:\n    print('indented')"),
                ("Colon Blocks", "Compound statements end with a colon.", "for i in range(3):\n    print(i)"),
                ("Comments", "Lines starting with # are ignored.", "# comment\nx = 1\nprint(x)"),
            ),
            "Python uses significant whitespace and readable English keywords.",
            "Express program structure clearly without braces.",
            "Less boilerplate, enforced readability, quick to learn.",
            "Scripts, functions, classes, config loaders.",
            "4 spaces per level, PEP 8 naming, one statement style per project.",
            "Mixing tabs and spaces, missing colons, trailing comma confusion.",
            'name = "Ada"\nprint(name)',
            "imports -> definitions -> main guard -> execution",
            "values = [1, 2, 3]\nsquared = [v * v for v in values]\nprint(squared)",
            'message = "Syntax matters"\nprint(message)',
            dedent("""\
                values = [1, 2, 3]
                squared = [v * v for v in values]
                print(squared)"""),
            dedent("""\
                from typing import Iterator


                def fibonacci(n: int) -> Iterator[int]:
                    a, b = 0, 1
                    for _ in range(n):
                        yield a
                        a, b = b, a + b


                print(list(fibonacci(6)))"""),
            "flowchart TD\n    A[Source File] --> B[Parser]\n    B --> C{Valid?}\n    C -->|yes| D[Execute]\n    C -->|no| E[SyntaxError]",
        ),
        "Variables": S(
            "Variables are names that reference objects stored in memory.",
            "They let programs remember state and transform data over time.",
            "Every Python program from scripts to ML pipelines.",
            ("Assign and reassign variables correctly.", "Follow PEP 8 naming conventions.", "Distinguish names from object identity."),
            "You model program state with clear, consistent variable names.",
            ("Business logic", "ETL transforms", "Game state", "Financial models"),
            (
                ("Assignment", "Binds a name to an object.", "score = 100\nprint(score)"),
                ("Rebinding", "A name can refer to a new object.", "score = score + 10\nprint(score)"),
                ("snake_case", "Standard style for variable names.", "user_email = 'a@b.com'\nprint(user_email)"),
            ),
            "Variables label objects; they are not typed boxes.",
            "Store and update program data.",
            "Readable code, reusable values, easier debugging.",
            "Counters, configs, user input, API payloads.",
            "Descriptive names, avoid shadowing builtins, init before use.",
            "Reusing names for different concepts, mutating shared references unexpectedly.",
            "name = 'Ada'\nage = 36",
            "# declare -> use -> update",
            "total = price * quantity\nprint(total)",
            "x = 5\ny = 3\nprint(x + y)",
            "first, second, *rest = [1, 2, 3, 4, 5]\nprint(first, second, rest)",
            dedent("""\
                from typing import Final

                MAX_RETRIES: Final = 3
                attempts = 0
                while attempts < MAX_RETRIES:
                    attempts += 1
                print(attempts)"""),
            "flowchart LR\n    A[Assign Name] --> B[Reference Object]\n    B --> C[Read/Update]",
        ),
    }


ALL_SNIPPETS: dict[str, dict] = {}
ALL_SNIPPETS.update(_beginner())

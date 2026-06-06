#!/usr/bin/env python3
"""Build in-memory ALL_SNIPPETS with every Python Mastery topic."""

from __future__ import annotations

import sys
from pathlib import Path
from textwrap import dedent

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "snippet_parts"))
from _helpers import S


def build() -> dict[str, dict]:
    d: dict[str, dict] = {}

    def p(title: str, **kw) -> None:
        d[title] = S(**kw)

    # --- BEGINNER (35) ---
    p(
        "Introduction to Python",
        what="Python is a high-level, interpreted language prized for readable syntax and a vast ecosystem.",
        why="It powers web backends, data science, automation, AI, and DevOps with one of the largest communities.",
        where="Startups, enterprises, research labs, fintech, healthcare analytics, and cloud platforms.",
        objectives=(
            "Explain Python's design philosophy and ecosystem.",
            "Compare Python to other languages for common workloads.",
            "Identify domains where Python excels.",
        ),
        outcome="You can explain why Python fits a project and where it belongs in a tech stack.",
        industry=("Web services", "Data pipelines", "ML platforms", "Security automation"),
        concepts=(
            ("Interpreted Execution", "Source runs via the interpreter.", "print('Hello, Python!')"),
            ("Standard Library", "Rich modules ship with Python.", "import json\nprint(json.dumps({'ok': True}))"),
            ("Dynamic Typing", "Types determined at runtime.", "x = 10\nx = 'ten'\nprint(x)"),
        ),
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
        pattern="import json\nprint(json.dumps({'status': 'ok'}))",
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
                typing: str


            print(LanguageProfile("Python", "dynamic"))"""),
        mermaid="flowchart TD\n    A[Write Code] --> B[Interpreter]\n    B --> C[Output]",
    )

    p(
        "Installing Python",
        what="Installing Python means obtaining the interpreter, pip, and tooling on your system.",
        why="A correct install prevents version conflicts and broken dependencies across projects.",
        where="Developer laptops, CI runners, Docker images, and cloud VMs.",
        objectives=("Install a supported Python 3.x release safely.", "Verify python and pip from the terminal.", "Choose between system Python, pyenv, or conda."),
        outcome="You can install Python and confirm a working environment from the shell.",
        industry=("Developer onboarding", "CI/CD images", "Container builds", "Education platforms"),
        concepts=(
            ("Interpreter", "The python binary executes .py files.", "import sys\nprint(sys.version_info.major >= 3)"),
            ("pip", "Package installer bundled with Python.", "import importlib.util\nprint(importlib.util.find_spec('pip') is not None)"),
            ("venv", "Creates isolated environments per project.", "import venv\nprint(hasattr(venv, 'EnvBuilder'))"),
        ),
        concept="Installation delivers interpreter + pip + optional version managers.",
        purpose="Run Python code reliably on any machine.",
        benefits="Reproducible environments, easier collaboration, safer upgrades.",
        use_cases="Local dev, servers, notebooks, automation agents.",
        best_practices="Pin versions, use venv, document setup in README.",
        mistakes="Mixing Python 2 and 3, global pip installs, ignoring PATH.",
        basic_syntax="import sys\nprint(sys.executable)",
        structure="# download -> install -> verify -> create venv",
        pattern="import sys\nprint(f'Python {sys.version_info.major}.{sys.version_info.minor}')",
        beginner="import platform\nprint(platform.python_version())",
        intermediate="import sys\nprint(sys.version)\nprint(sys.executable)",
        advanced=dedent("""\
            import subprocess
            import sys

            result = subprocess.run([sys.executable, "-m", "pip", "--version"], capture_output=True, text=True)
            print(result.stdout.strip())"""),
        mermaid="flowchart LR\n    A[Download] --> B[Install]\n    B --> C[Verify]\n    C --> D[venv]",
    )

    p(
        "IDE Setup",
        what="IDE setup configures an editor with Python interpreter, linting, debugging, and formatting.",
        why="Good tooling catches errors early and speeds up navigation in growing codebases.",
        where="Daily development in VS Code, PyCharm, Vim/Neovim, and cloud IDEs.",
        objectives=("Select and configure a Python-capable editor.", "Attach the correct interpreter and extensions.", "Enable format-on-save, linting, and debugging."),
        outcome="You have a productive Python workspace with run and debug shortcuts.",
        industry=("Software teams", "Remote development", "Bootcamps", "Open-source contributors"),
        concepts=(
            ("Interpreter Path", "Editor must point at project venv Python.", "import sys\nprint(sys.executable)"),
            ("Language Server", "Powers autocomplete and diagnostics.", "import typing\nprint(typing.__name__)"),
            ("Debugger", "Breakpoints inspect live program state.", "x = 1\nx += 1\nprint(x)"),
        ),
        concept="IDE = editor + language server + debugger + formatter.",
        purpose="Reduce friction while writing and testing Python.",
        benefits="Autocomplete, refactor tools, integrated tests, faster onboarding.",
        use_cases="Feature development, code review prep, teaching, pair programming.",
        best_practices="One venv per repo, commit .editorconfig, share launch.json for teams.",
        mistakes="Using global Python, disabling type checking, no formatter config.",
        basic_syntax="print('IDE ready')",
        structure="# install editor -> select venv -> configure linter -> debug",
        pattern="import sys\nprint('Interpreter:', sys.executable)",
        beginner="import sys\nprint(sys.version.split()[0])",
        intermediate=dedent("""\
            def greet(name: str) -> str:
                return f"Hello, {name}"


            print(greet("Dev"))"""),
        advanced=dedent("""\
            import sys

            print("Executable:", sys.executable)
            print("Version:", sys.version.split()[0])"""),
        mermaid="flowchart LR\n    A[Project] --> B[venv] --> C[LSP] --> D[Run]",
    )

    p(
        "Python Syntax",
        what="Python syntax defines how statements, blocks, and expressions are written.",
        why="Correct syntax is required before logic, libraries, or frameworks matter.",
        where="Every script, notebook cell, test file, and module.",
        objectives=("Use indentation, colons, and statement structure correctly.", "Write valid expressions and comments.", "Read tracebacks caused by syntax errors."),
        outcome="You write syntactically valid Python without constant SyntaxError failures.",
        industry=("Application code", "Data notebooks", "Infrastructure scripts", "Test suites"),
        concepts=(
            ("Indentation", "Blocks are defined by consistent leading spaces.", "if True:\n    print('indented')"),
            ("Colon Blocks", "Compound statements end with a colon.", "for i in range(3):\n    print(i)"),
            ("Comments", "Lines starting with # are ignored.", "# comment\nx = 1\nprint(x)"),
        ),
        concept="Python uses significant whitespace and readable English keywords.",
        purpose="Express program structure clearly without braces.",
        benefits="Less boilerplate, enforced readability, quick to learn.",
        use_cases="Scripts, functions, classes, config loaders.",
        best_practices="4 spaces per level, PEP 8 naming, one statement style per project.",
        mistakes="Mixing tabs and spaces, missing colons, trailing comma confusion.",
        basic_syntax='name = "Ada"\nprint(name)',
        structure="imports -> definitions -> main guard -> execution",
        pattern="values = [1, 2, 3]\nprint([v * v for v in values])",
        beginner='message = "Syntax matters"\nprint(message)',
        intermediate="print([v * v for v in [1, 2, 3, 4]])",
        advanced=dedent("""\
            from typing import Iterator


            def count(n: int) -> Iterator[int]:
                for i in range(n):
                    yield i


            print(list(count(4)))"""),
        mermaid="flowchart TD\n    A[Source] --> B[Parser]\n    B --> C{Valid?}\n    C -->|yes| D[Execute]\n    C -->|no| E[SyntaxError]",
    )

    p(
        "Variables",
        what="Variables are names that reference objects stored in memory.",
        why="They let programs remember state and transform data over time.",
        where="Every Python program from scripts to ML pipelines.",
        objectives=("Assign and reassign variables correctly.", "Follow PEP 8 naming conventions.", "Distinguish names from object identity."),
        outcome="You model program state with clear, consistent variable names.",
        industry=("Business logic", "ETL transforms", "Game state", "Financial models"),
        concepts=(
            ("Assignment", "Binds a name to an object.", "score = 100\nprint(score)"),
            ("Rebinding", "A name can refer to a new object.", "score = score + 10\nprint(score)"),
            ("snake_case", "Standard style for variable names.", "user_email = 'a@b.com'\nprint(user_email)"),
        ),
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
    )

    p(
        "Data Types",
        what="Python data types classify values such as numbers, text, collections, and booleans.",
        why="Choosing the right type prevents logic bugs and enables efficient operations.",
        where="Validation, APIs, analytics, configuration, and user input handling.",
        objectives=("Identify built-in scalar and collection types.", "Inspect types with type() and isinstance().", "Select appropriate types for domain data."),
        outcome="You pick and verify types confidently in everyday Python code.",
        industry=("Backend APIs", "Data science", "Finance systems", "IoT telemetry"),
        concepts=(
            ("int", "Whole numbers without fractional part.", "count = 42\nprint(type(count))"),
            ("float", "Numbers with decimal precision.", "price = 19.99\nprint(round(price, 2))"),
            ("bool", "True/False logical values.", "active = True\nprint(active and False)"),
        ),
        concept="Types describe what operations are valid on a value.",
        purpose="Model real-world data with the correct Python objects.",
        benefits="Safer code, clearer APIs, better performance choices.",
        use_cases="User profiles, sensor readings, cart totals, feature flags.",
        best_practices="Prefer isinstance over type(); document expected types.",
        mistakes="Confusing None checks, bool/int coercion surprises.",
        basic_syntax="age = 30\nname = 'Ada'\nactive = True",
        structure="scalar -> collection -> inspect -> convert when needed",
        pattern="print(isinstance(3.14, float))",
        beginner="print(type(3.14))\nprint(isinstance(3.14, float))",
        intermediate=dedent("""\
            from typing import Any

            def describe(value: Any) -> str:
                return f"{value!r} is {type(value).__name__}"


            print(describe([1, 2]))"""),
        advanced=dedent("""\
            from dataclasses import dataclass


            @dataclass
            class Reading:
                sensor_id: str
                value: float
                ok: bool


            print(Reading("temp-1", 22.5, True))"""),
        mermaid="flowchart LR\n    A[Value] --> B{type?}\n    B --> C[Scalar]\n    B --> D[Collection]",
    )

    p(
        "Type Casting",
        what="Type casting converts values from one type to another explicitly.",
        why="User input and file data arrive as strings; casting enables computation.",
        where="Forms, CSV imports, query parameters, CLI arguments.",
        objectives=("Use int(), float(), str(), and bool() safely.", "Handle invalid conversions with try/except.", "Understand truthiness when casting to bool."),
        outcome="You convert external data into usable Python types without silent errors.",
        industry=("E-commerce checkout", "Spreadsheet ingestion", "Mobile backends", "Billing engines"),
        concepts=(
            ("int()", "Parse integers from numeric strings.", "qty = int('12')\nprint(qty + 1)"),
            ("float()", "Parse decimal numbers.", "rate = float('0.075')\nprint(rate * 100)"),
            ("str()", "Serialize values for display or files.", "label = str(404)\nprint('HTTP ' + label)"),
        ),
        concept="Casting makes implicit string data explicit and computable.",
        purpose="Bridge human-readable input and program logic.",
        benefits="Correct math, valid comparisons, predictable formatting.",
        use_cases="Price calculations, age gates, ID formatting, logging.",
        best_practices="Validate before cast; strip whitespace; localize decimals carefully.",
        mistakes="Casting invalid strings without error handling, using bool('0') incorrectly.",
        basic_syntax="score = int('95')\nprint(score)",
        structure="read string -> validate -> cast -> use",
        pattern="total = float('10.5') * int('2')\nprint(total)",
        beginner="age = int('21')\nprint(age >= 18)",
        intermediate=dedent("""\
            def safe_int(text: str, default: int = 0) -> int:
                try:
                    return int(text.strip())
                except ValueError:
                    return default


            print(safe_int(' 42 '))"""),
        advanced=dedent("""\
            from decimal import Decimal

            amount = Decimal('19.99')
            tax = amount * Decimal('0.08')
            print(amount + tax)"""),
        mermaid="flowchart LR\n    A[Raw Text] --> B[Validate]\n    B --> C[Cast]\n    C --> D[Compute]",
    )

    p(
        "Input and Output",
        what="Input and output (I/O) moves data between users, files, and programs.",
        why="Most programs must read requests and emit responses or logs.",
        where="CLIs, notebooks, web forms, batch jobs, interactive tools.",
        objectives=("Read user input with input() and parse it.", "Write formatted output with print() and f-strings.", "Separate presentation from business logic."),
        outcome="You build interactive scripts with clear prompts and readable output.",
        industry=("Customer support tools", "Internal ops scripts", "Education apps", "Kiosk systems"),
        concepts=(
            ("input()", "Reads a line of text from stdin.", "name = 'Ada'\nprint(name.upper())"),
            ("print()", "Writes text to stdout.", "print('Done', flush=True)"),
            ("f-strings", "Embed expressions in strings.", "name = 'Ada'\nprint(f'Hello, {name}!')"),
        ),
        concept="I/O is the boundary between humans and your Python logic.",
        purpose="Collect parameters and communicate results.",
        benefits="Better UX, testable interfaces, scriptable workflows.",
        use_cases="Quizzes, calculators, menu-driven tools, quick prototypes.",
        best_practices="Prompt clearly, validate input, avoid mixing logic with formatting.",
        mistakes="Trusting raw input, printing secrets, no newline control in logs.",
        basic_syntax="name = 'World'\nprint(f'Hi, {name}')",
        structure="prompt -> read -> validate -> process -> display",
        pattern="value = '7'\nprint(int(value) ** 2)",
        beginner="name = 'World'\nprint(f'Hi, {name}')",
        intermediate=dedent("""\
            def ask_yes_no(prompt: str) -> bool:
                answer = 'yes'
                return answer in {'y', 'yes'}


            print(ask_yes_no('Continue?'))"""),
        advanced=dedent("""\
            import sys

            data = 'hello world'
            sys.stdout.write(data.upper() + '\\n')"""),
        mermaid="flowchart LR\n    A[User Input] --> B[Parse]\n    B --> C[Logic]\n    C --> D[Output]",
    )

    p(
        "Operators",
        what="Operators perform arithmetic, comparison, logical, and assignment actions on values.",
        why="They express business rules compactly in conditions and expressions.",
        where="Pricing, eligibility checks, scoring, game mechanics, data filters.",
        objectives=("Apply arithmetic and comparison operators.", "Combine conditions with and, or, not.", "Use augmented assignment for updates."),
        outcome="You write expressive conditions and calculations without verbose code.",
        industry=("Retail pricing", "Risk scoring", "Games", "Monitoring alerts"),
        concepts=(
            ("Arithmetic", "+ - * / // % ** on numbers.", "total = 10 + 5 * 2\nprint(total)"),
            ("Comparison", "Return booleans for ordering/equality.", "print(3 >= 2 and 4 != 5)"),
            ("Augmented assignment", "Update variables in place.", "count = 0\ncount += 1\nprint(count)"),
        ),
        concept="Operators combine values into new results or decisions.",
        purpose="Implement rules and transformations inline.",
        benefits="Readable logic, fewer temporary variables.",
        use_cases="Tax calculation, access control, sorting keys, thresholds.",
        best_practices="Use parentheses for clarity; avoid chaining confusing comparisons.",
        mistakes="Operator precedence mistakes, using is for value equality, division surprises.",
        basic_syntax="a, b = 10, 3\nprint(a // b, a % b)",
        structure="operands -> operator -> result -> use in condition",
        pattern="eligible = age >= 18 and country == 'US'\nprint(eligible)",
        beginner="price = 100\ndiscount = price * 0.1\nprint(price - discount)",
        intermediate=dedent("""\
            scores = [88, 92, 76]
            average = sum(scores) / len(scores)
            passed = average >= 80
            print(average, passed)"""),
        advanced=dedent("""\
            from operator import itemgetter

            rows = [{'n': 'Ada', 's': 95}, {'n': 'Lin', 's': 88}]
            top = max(rows, key=itemgetter('s'))
            print(top)"""),
        mermaid="flowchart LR\n    A[Operands] --> B[Operator]\n    B --> C[Result]",
    )

    p(
        "Conditional Statements",
        what="Conditional statements execute code selectively with if, elif, and else.",
        why="Business logic depends on branching based on data and state.",
        where="Auth checks, feature flags, error paths, pricing tiers.",
        objectives=("Write if/elif/else chains for multiple cases.", "Nest conditions sparingly with clear structure.", "Use ternary expressions for simple assignments."),
        outcome="You implement decision trees that are easy to read and test.",
        industry=("Access control", "Billing rules", "Workflow engines", "Support triage"),
        concepts=(
            ("if", "Runs block when condition is truthy.", "if score >= 60:\n    print('pass')"),
            ("elif", "Tests additional conditions.", "x = -1\nif x > 0:\n    sign = 'pos'\nelif x < 0:\n    sign = 'neg'\nelse:\n    sign = 'zero'\nprint(sign)"),
            ("else", "Fallback when no condition matches.", "logged_in = False\nprint('home' if logged_in else 'login')"),
        ),
        concept="Conditionals map inputs to different behaviors.",
        purpose="Encode policies and validations.",
        benefits="Explicit paths, fewer duplicated checks, testable branches.",
        use_cases="Login flows, shipping methods, grading, alert severity.",
        best_practices="Prefer flat elif chains; extract complex tests to functions.",
        mistakes="Deep nesting, duplicate conditions, assignment inside if by mistake.",
        basic_syntax="if temperature > 30:\n    print('hot')",
        structure="guard clauses -> main branches -> else fallback",
        pattern="status = 'gold' if points >= 1000 else 'silver'",
        beginner=dedent("""\
            score = 74
            if score >= 90:
                grade = 'A'
            elif score >= 80:
                grade = 'B'
            else:
                grade = 'C'
            print(grade)"""),
        intermediate=dedent("""\
            def shipping_fee(weight_kg: float) -> float:
                if weight_kg <= 1:
                    return 5.0
                if weight_kg <= 5:
                    return 9.0
                return 15.0


            print(shipping_fee(3.2))"""),
        advanced=dedent("""\
            from enum import Enum


            class Role(str, Enum):
                ADMIN = 'admin'
                USER = 'user'


            def can_delete(role: Role) -> bool:
                return role is Role.ADMIN


            print(can_delete(Role.USER))"""),
        mermaid="flowchart TD\n    A[Condition] -->|True| B[Then]\n    A -->|False| C[Else/Elif]",
    )

    from catalog_parts.beginner_rest import register_beginner_rest
    from catalog_parts.intermediate_all import register_intermediate
    from catalog_parts.advanced_all import register_advanced

    register_beginner_rest(p)
    register_intermediate(p)
    register_advanced(p)

    return d


ALL_SNIPPETS = build()

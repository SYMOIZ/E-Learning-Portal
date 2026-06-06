#!/usr/bin/env python3
"""Curated topic snippet specifications for all Python Mastery topics."""

from __future__ import annotations

from textwrap import dedent


def _s(
    what: str,
    why: str,
    where: str,
    objectives: tuple[str, str, str],
    outcome: str,
    industry: tuple[str, str, str, str],
    concepts: tuple[tuple[str, str, str], tuple[str, str, str], tuple[str, str, str]],
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
    return {
        "what": what,
        "why": why,
        "where": where,
        "objectives": list(objectives),
        "outcome": outcome,
        "industry": list(industry),
        "concepts": list(concepts),
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


SPECS: dict[str, dict] = {
    "Data Types": _s(
        "Python data types classify values such as numbers, text, collections, and booleans.",
        "Choosing the right type prevents logic bugs and enables efficient operations.",
        "Validation, APIs, analytics, configuration, and user input handling.",
        (
            "Identify built-in scalar and collection types.",
            "Inspect types at runtime with type() and isinstance().",
            "Select appropriate types for domain data.",
        ),
        "You pick and verify types confidently in everyday Python code.",
        ("Backend APIs", "Data science", "Finance systems", "IoT telemetry"),
        (
            ("int", "Whole numbers without fractional part.", "count = 42\nprint(type(count))"),
            ("float", "Numbers with decimal precision.", "price = 19.99\nprint(round(price, 2))"),
            ("bool", "True/False logical values.", "active = True\nprint(active and False)"),
        ),
        "Types describe what operations are valid on a value.",
        "Model real-world data with the correct Python objects.",
        "Safer code, clearer APIs, better performance choices.",
        "User profiles, sensor readings, cart totals, feature flags.",
        "Prefer isinstance over type comparisons; document expected types.",
        "Using mutable defaults, confusing None checks, ignoring bool/int distinction.",
        "age = 30\nname = 'Ada'\nactive = True",
        "scalar -> collection -> inspect -> convert when needed",
        "if isinstance(value, str):\n    value = value.strip()",
        "print(type(3.14))\nprint(isinstance(3.14, float))",
        dedent("""\
            from typing import Any

            def describe(value: Any) -> str:
                return f"{value!r} is {type(value).__name__}"


            print(describe([1, 2]))"""),
        dedent("""\
            from dataclasses import dataclass


            @dataclass
            class Reading:
                sensor_id: str
                value: float
                ok: bool


            print(Reading("temp-1", 22.5, True))"""),
        "flowchart LR\n    A[Value] --> B{type?}\n    B --> C[Scalar]\n    B --> D[Collection]\n    C --> E[Operations]\n    D --> E",
    ),
    "Type Casting": _s(
        "Type casting converts values from one type to another explicitly.",
        "User input and file data arrive as strings; casting enables computation.",
        "Forms, CSV imports, query parameters, CLI arguments.",
        (
            "Use int(), float(), str(), and bool() safely.",
            "Handle invalid conversions with try/except.",
            "Understand truthiness when casting to bool.",
        ),
        "You convert external data into usable Python types without silent errors.",
        ("E-commerce checkout", "Spreadsheet ingestion", "Mobile backends", "Billing engines"),
        (
            ("int()", "Parse integers from numeric strings.", "qty = int('12')\nprint(qty + 1)"),
            ("float()", "Parse decimal numbers.", "rate = float('0.075')\nprint(rate * 100)"),
            ("str()", "Serialize values for display or files.", "label = str(404)\nprint('HTTP ' + label)"),
        ),
        "Casting makes implicit string data explicit and computable.",
        "Bridge human-readable input and program logic.",
        "Correct math, valid comparisons, predictable formatting.",
        "Price calculations, age gates, ID formatting, logging.",
        "Validate before cast; strip whitespace; localize decimals carefully.",
        "Casting invalid strings without error handling, using bool('0') incorrectly.",
        "score = int('95')\nprint(score)",
        "read string -> validate -> cast -> use",
        "total = float(price) * int(quantity)",
        "age = int(input('Age: ') or '0')\nprint(age >= 18)",
        dedent("""\
            def safe_int(text: str, default: int = 0) -> int:
                try:
                    return int(text.strip())
                except ValueError:
                    return default


            print(safe_int(' 42 '))"""),
        dedent("""\
            from decimal import Decimal

            amount = Decimal(str('19.99'))
            tax = amount * Decimal('0.08')
            print(amount + tax)"""),
        "flowchart LR\n    A[Raw Text] --> B[Validate]\n    B --> C[Cast]\n    C --> D[Compute]",
    ),
    "Input and Output": _s(
        "Input and output (I/O) moves data between users, files, and programs.",
        "Most programs must read requests and emit responses or logs.",
        "CLIs, notebooks, web forms, batch jobs, interactive tools.",
        (
            "Read user input with input() and parse it.",
            "Write formatted output with print() and f-strings.",
            "Separate presentation from business logic.",
        ),
        "You build interactive scripts with clear prompts and readable output.",
        ("Customer support tools", "Internal ops scripts", "Education apps", "Kiosk systems"),
        (
            ("input()", "Reads a line of text from stdin.", "name = input('Name: ')\nprint(name.upper())"),
            ("print()", "Writes text to stdout.", "print('Done', flush=True)"),
            ("f-strings", "Embed expressions in strings.", "print(f'Hello, {name}!')"),
        ),
        "I/O is the boundary between humans and your Python logic.",
        "Collect parameters and communicate results.",
        "Better UX, testable interfaces, scriptable workflows.",
        "Quizzes, calculators, menu-driven tools, quick prototypes.",
        "Prompt clearly, validate input, avoid mixing logic with formatting.",
        "Trusting raw input, printing secrets, no newline control in logs.",
        "name = input('Your name: ')\nprint(f'Hi, {name}')",
        "prompt -> read -> validate -> process -> display",
        "value = input('Enter a number: ')\nprint(int(value) ** 2)",
        "name = input('Name: ')\nprint('Welcome', name)",
        dedent("""\
            def ask_yes_no(prompt: str) -> bool:
                answer = input(f"{prompt} [y/n]: ").strip().lower()
                return answer in {"y", "yes"}


            print(ask_yes_no('Continue?'))"""),
        dedent("""\
            import sys

            for line in sys.stdin:
                cleaned = line.strip()
                if cleaned:
                    print(cleaned.upper())"""),
        "flowchart LR\n    A[User Input] --> B[Parse]\n    B --> C[Logic]\n    C --> D[Formatted Output]",
    ),
    "Operators": _s(
        "Operators perform arithmetic, comparison, logical, and assignment actions on values.",
        "They express business rules compactly in conditions and expressions.",
        "Pricing, eligibility checks, scoring, game mechanics, data filters.",
        (
            "Apply arithmetic and comparison operators.",
            "Combine conditions with and, or, not.",
            "Use augmented assignment for updates.",
        ),
        "You write expressive conditions and calculations without verbose code.",
        ("Retail pricing", "Risk scoring", "Games", "Monitoring alerts"),
        (
            ("Arithmetic", "+ - * / // % ** on numbers.", "total = 10 + 5 * 2\nprint(total)"),
            ("Comparison", "Return booleans for ordering/equality.", "print(3 >= 2 and 4 != 5)"),
            ("Augmented assignment", "Update variables in place.", "count = 0\ncount += 1\nprint(count)"),
        ),
        "Operators combine values into new results or decisions.",
        "Implement rules and transformations inline.",
        "Readable logic, fewer temporary variables.",
        "Tax calculation, access control, sorting keys, thresholds.",
        "Use parentheses for clarity; avoid chaining confusing comparisons.",
        "Operator precedence mistakes, using is for value equality, division surprises.",
        "a, b = 10, 3\nprint(a // b, a % b)",
        "operands -> operator -> result -> use in condition",
        "eligible = age >= 18 and country == 'US'\nprint(eligible)",
        "price = 100\ndiscount = price * 0.1\nprint(price - discount)",
        dedent("""\
            scores = [88, 92, 76]
            average = sum(scores) / len(scores)
            passed = average >= 80
            print(average, passed)"""),
        dedent("""\
            from operator import itemgetter

            rows = [{'n': 'Ada', 's': 95}, {'n': 'Lin', 's': 88}]
            top = max(rows, key=itemgetter('s'))
            print(top)"""),
        "flowchart LR\n    A[Operands] --> B[Operator]\n    B --> C[Result]\n    C --> D[Branch/Store]",
    ),
    "Conditional Statements": _s(
        "Conditional statements execute code selectively with if, elif, and else.",
        "Business logic depends on branching based on data and state.",
        "Auth checks, feature flags, error paths, pricing tiers.",
        (
            "Write if/elif/else chains for multiple cases.",
            "Nest conditions sparingly with clear structure.",
            "Use ternary expressions for simple assignments.",
        ),
        "You implement decision trees that are easy to read and test.",
        ("Access control", "Billing rules", "Workflow engines", "Support triage"),
        (
            ("if", "Runs block when condition is truthy.", "if score >= 60:\n    print('pass')"),
            ("elif", "Tests additional conditions.", "if x > 0:\n    sign = 'pos'\nelif x < 0:\n    sign = 'neg'"),
            ("else", "Fallback when no condition matches.", "if logged_in:\n    view = 'home'\nelse:\n    view = 'login'"),
        ),
        "Conditionals map inputs to different behaviors.",
        "Encode policies and validations.",
        "Explicit paths, fewer duplicated checks, testable branches.",
        "Login flows, shipping methods, grading, alert severity.",
        "Prefer flat elif chains; extract complex tests to functions.",
        "Deep nesting, duplicate conditions, assignment inside if by mistake.",
        "if temperature > 30:\n    print('hot')",
        "guard clauses -> main branches -> else fallback",
        "status = 'gold' if points >= 1000 else 'silver'",
        "score = 74\nif score >= 90:\n    grade = 'A'\nelif score >= 80:\n    grade = 'B'\nelse:\n    grade = 'C'\nprint(grade)",
        dedent("""\
            def shipping_fee(weight_kg: float) -> float:
                if weight_kg <= 1:
                    return 5.0
                if weight_kg <= 5:
                    return 9.0
                return 15.0


            print(shipping_fee(3.2))"""),
        dedent("""\
            from enum import Enum


            class Role(str, Enum):
                ADMIN = 'admin'
                USER = 'user'


            def can_delete(role: Role) -> bool:
                return role is Role.ADMIN


            print(can_delete(Role.USER))"""),
        "flowchart TD\n    A[Condition] -->|True| B[Then Block]\n    A -->|False| C{elif?}\n    C -->|match| D[Elif Block]\n    C -->|none| E[Else Block]",
    ),
}

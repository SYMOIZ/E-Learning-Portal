# PYTHON LEARNING ROADMAP

> **E-Learning Portal** — Complete Python Knowledge Base for GitHub, NotebookLM, Obsidian, Notion, and documentation portals.

## How to Use This Knowledge Base

1. Start at **Level 1: Beginner** if you are new to programming.
2. Progress to **Level 2: Intermediate** when you can build small apps independently.
3. Study **Level 3: Advanced** for production engineering, cloud, data, and AI roles.
4. Import individual topic files from [`Python-Mastery/`](Python-Mastery/) into NotebookLM or Obsidian.

## Table of Contents

### Level 1: Beginner

1. [Introduction to Python](#introduction-to-python)
2. [Installing Python](#installing-python)
3. [IDE Setup](#ide-setup)
4. [Python Syntax](#python-syntax)
5. [Variables](#variables)
6. [Data Types](#data-types)
7. [Type Casting](#type-casting)
8. [Input and Output](#input-and-output)
9. [Operators](#operators)
10. [Conditional Statements](#conditional-statements)
11. [Loops](#loops)
12. [Nested Loops](#nested-loops)
13. [Break Continue Pass](#break-continue-pass)
14. [Strings](#strings)
15. [String Methods](#string-methods)
16. [Lists](#lists)
17. [List Methods](#list-methods)
18. [Tuples](#tuples)
19. [Sets](#sets)
20. [Dictionaries](#dictionaries)
21. [Functions](#functions)
22. [Arguments and Parameters](#arguments-and-parameters)
23. [Return Statements](#return-statements)
24. [Scope](#scope)
25. [Lambda Functions](#lambda-functions)
26. [Modules](#modules)
27. [Packages](#packages)
28. [Date and Time](#date-and-time)
29. [Math Module](#math-module)
30. [Random Module](#random-module)
31. [File Handling](#file-handling)
32. [Exception Handling](#exception-handling)
33. [Debugging Basics](#debugging-basics)
34. [Virtual Environments](#virtual-environments)
35. [Basic Project Structure](#basic-project-structure)

### Level 2: Intermediate

1. [Object Oriented Programming](#object-oriented-programming)
2. [Classes](#classes)
3. [Objects](#objects)
4. [Constructors](#constructors)
5. [Encapsulation](#encapsulation)
6. [Inheritance](#inheritance)
7. [Polymorphism](#polymorphism)
8. [Abstraction](#abstraction)
9. [Magic Methods](#magic-methods)
10. [Iterators](#iterators)
11. [Generators](#generators)
12. [Decorators](#decorators)
13. [Context Managers](#context-managers)
14. [Regular Expressions](#regular-expressions)
15. [JSON Processing](#json-processing)
16. [CSV Processing](#csv-processing)
17. [XML Processing](#xml-processing)
18. [Logging](#logging)
19. [Configuration Management](#configuration-management)
20. [Multithreading](#multithreading)
21. [Multiprocessing](#multiprocessing)
22. [Async Programming](#async-programming)
23. [API Development](#api-development)
24. [API Consumption](#api-consumption)
25. [Requests Library](#requests-library)
26. [Database Fundamentals](#database-fundamentals)
27. [SQLite](#sqlite)
28. [MySQL Integration](#mysql-integration)
29. [PostgreSQL Integration](#postgresql-integration)
30. [SQLAlchemy ORM](#sqlalchemy-orm)
31. [Unit Testing](#unit-testing)
32. [Pytest](#pytest)
33. [Mocking](#mocking)
34. [Packaging Python Projects](#packaging-python-projects)
35. [CLI Applications](#cli-applications)

### Level 3: Advanced

1. [Data Structures Internals](#data-structures-internals)
2. [Algorithms in Python](#algorithms-in-python)
3. [Design Patterns](#design-patterns)
4. [SOLID Principles](#solid-principles)
5. [Memory Management](#memory-management)
6. [Garbage Collection](#garbage-collection)
7. [Python Internals](#python-internals)
8. [Metaclasses](#metaclasses)
9. [Descriptors](#descriptors)
10. [Concurrency](#concurrency)
11. [Parallel Computing](#parallel-computing)
12. [Distributed Systems](#distributed-systems)
13. [Network Programming](#network-programming)
14. [Socket Programming](#socket-programming)
15. [Cybersecurity Automation](#cybersecurity-automation)
16. [Web Scraping](#web-scraping)
17. [Automation Frameworks](#automation-frameworks)
18. [ETL Development](#etl-development)
19. [Data Engineering](#data-engineering)
20. [Pandas](#pandas)
21. [NumPy](#numpy)
22. [PySpark](#pyspark)
23. [Machine Learning](#machine-learning)
24. [Deep Learning](#deep-learning)
25. [NLP](#nlp)
26. [Computer Vision](#computer-vision)
27. [FastAPI](#fastapi)
28. [Django](#django)
29. [Flask](#flask)
30. [Microservices](#microservices)
31. [Docker with Python](#docker-with-python)
32. [Kubernetes Integration](#kubernetes-integration)
33. [Cloud Development](#cloud-development)
34. [AWS with Python](#aws-with-python)
35. [Azure with Python](#azure-with-python)
36. [GCP with Python](#gcp-with-python)
37. [DevOps Automation](#devops-automation)
38. [CI/CD Pipelines](#cicd-pipelines)
39. [Performance Optimization](#performance-optimization)
40. [System Design with Python](#system-design-with-python)


### Final Sections

- [Complete Python Roadmap](#complete-python-roadmap)
- [Python Career Paths](#python-career-paths)
- [Recommended Folder Structure](#recommended-folder-structure-for-notebooklm)

---

## Level 1: Beginner

# Introduction to Python

## Overview

- **What is it?** Python is a high-level, interpreted language prized for readable syntax and a vast ecosystem.
- **Why is it important?** It powers web backends, data science, automation, AI, and DevOps with one of the largest communities.
- **Where is it used?** Startups, enterprises, research labs, fintech, healthcare analytics, and cloud platforms.

## Learning Objectives

- **Skills gained:** Practical command of Introduction to Python.
- **Concepts covered:**

- Explain Python's design philosophy and ecosystem.
- Compare Python to other languages for common workloads.
- Identify domains where Python excels.

- **Expected outcome:** You can explain why Python fits a project and where it belongs in a tech stack.

## Real World Applications

- Web services
- Data pipelines
- ML platforms
- Security automation

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Interpreted Execution

- **Definition:** Source runs via the interpreter.
- **Visual explanation:** `Interpreted Execution` → process → result
- **Practical example:**

```python
print('Hello, Python!')
```

### Standard Library

- **Definition:** Rich modules ship with Python.
- **Visual explanation:** `Standard Library` → process → result
- **Practical example:**

```python
import json
print(json.dumps({'ok': True}))
```

### Dynamic Typing

- **Definition:** Types determined at runtime.
- **Visual explanation:** `Dynamic Typing` → process → result
- **Practical example:**

```python
x = 10
x = 'ten'
print(x)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Python is interpreted, dynamically typed, and multi-paradigm. |
| ⚡ Purpose | Ship solutions quickly with readable code and strong libraries. |
| 🔥 Benefits | Fast prototyping, huge community, cross-platform, excellent for teams. |
| 🎯 Use Cases | APIs, ETL, notebooks, scripting, AI/ML, test automation. |
| 🚀 Best Practices | Follow PEP 8, use virtual environments, prefer clarity over cleverness. |
| ❌ Common Mistakes | Assuming Python is slow for every task, ignoring version pins, skipping tests. |

## Syntax Guide

### Basic Syntax

```python
print("Hello, Python!")
```

### Standard Structure

```python
def main():
    print("Learning Python")


if __name__ == "__main__":
    main()
```

### Code Pattern

```python
import json
print(json.dumps({'status': 'ok'}))
```

## Examples

### Beginner Example

```python
print("Python is fun!")
```

### Intermediate Example

```python
domains = ["web", "data", "automation", "ai"]
for domain in domains:
    print(f"Python powers {domain}")
```

### Advanced Example

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class LanguageProfile:
    name: str
    typing: str


print(LanguageProfile("Python", "dynamic"))
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Write Code] --> B[Interpreter]
    B --> C[Output]
```

---

# Installing Python

## Overview

- **What is it?** Installing Python means obtaining the interpreter, pip, and tooling on your system.
- **Why is it important?** A correct install prevents version conflicts and broken dependencies across projects.
- **Where is it used?** Developer laptops, CI runners, Docker images, and cloud VMs.

## Learning Objectives

- **Skills gained:** Practical command of Installing Python.
- **Concepts covered:**

- Install a supported Python 3.x release safely.
- Verify python and pip from the terminal.
- Choose between system Python, pyenv, or conda.

- **Expected outcome:** You can install Python and confirm a working environment from the shell.

## Real World Applications

- Developer onboarding
- CI/CD images
- Container builds
- Education platforms

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Interpreter

- **Definition:** The python binary executes .py files.
- **Visual explanation:** `Interpreter` → process → result
- **Practical example:**

```python
import sys
print(sys.version_info.major >= 3)
```

### pip

- **Definition:** Package installer bundled with Python.
- **Visual explanation:** `pip` → process → result
- **Practical example:**

```python
import importlib.util
print(importlib.util.find_spec('pip') is not None)
```

### venv

- **Definition:** Creates isolated environments per project.
- **Visual explanation:** `venv` → process → result
- **Practical example:**

```python
import venv
print(hasattr(venv, 'EnvBuilder'))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Installation delivers interpreter + pip + optional version managers. |
| ⚡ Purpose | Run Python code reliably on any machine. |
| 🔥 Benefits | Reproducible environments, easier collaboration, safer upgrades. |
| 🎯 Use Cases | Local dev, servers, notebooks, automation agents. |
| 🚀 Best Practices | Pin versions, use venv, document setup in README. |
| ❌ Common Mistakes | Mixing Python 2 and 3, global pip installs, ignoring PATH. |

## Syntax Guide

### Basic Syntax

```python
import sys
print(sys.executable)
```

### Standard Structure

```python
# download -> install -> verify -> create venv
```

### Code Pattern

```python
import sys
print(f'Python {sys.version_info.major}.{sys.version_info.minor}')
```

## Examples

### Beginner Example

```python
import platform
print(platform.python_version())
```

### Intermediate Example

```python
import sys
print(sys.version)
print(sys.executable)
```

### Advanced Example

```python
import subprocess
import sys

result = subprocess.run([sys.executable, "-m", "pip", "--version"], capture_output=True, text=True)
print(result.stdout.strip())
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Download] --> B[Install]
    B --> C[Verify]
    C --> D[venv]
```

---

# IDE Setup

## Overview

- **What is it?** IDE setup configures an editor with Python interpreter, linting, debugging, and formatting.
- **Why is it important?** Good tooling catches errors early and speeds up navigation in growing codebases.
- **Where is it used?** Daily development in VS Code, PyCharm, Vim/Neovim, and cloud IDEs.

## Learning Objectives

- **Skills gained:** Practical command of IDE Setup.
- **Concepts covered:**

- Select and configure a Python-capable editor.
- Attach the correct interpreter and extensions.
- Enable format-on-save, linting, and debugging.

- **Expected outcome:** You have a productive Python workspace with run and debug shortcuts.

## Real World Applications

- Software teams
- Remote development
- Bootcamps
- Open-source contributors

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Interpreter Path

- **Definition:** Editor must point at project venv Python.
- **Visual explanation:** `Interpreter Path` → process → result
- **Practical example:**

```python
import sys
print(sys.executable)
```

### Language Server

- **Definition:** Powers autocomplete and diagnostics.
- **Visual explanation:** `Language Server` → process → result
- **Practical example:**

```python
import typing
print(typing.__name__)
```

### Debugger

- **Definition:** Breakpoints inspect live program state.
- **Visual explanation:** `Debugger` → process → result
- **Practical example:**

```python
x = 1
x += 1
print(x)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | IDE = editor + language server + debugger + formatter. |
| ⚡ Purpose | Reduce friction while writing and testing Python. |
| 🔥 Benefits | Autocomplete, refactor tools, integrated tests, faster onboarding. |
| 🎯 Use Cases | Feature development, code review prep, teaching, pair programming. |
| 🚀 Best Practices | One venv per repo, commit .editorconfig, share launch.json for teams. |
| ❌ Common Mistakes | Using global Python, disabling type checking, no formatter config. |

## Syntax Guide

### Basic Syntax

```python
print('IDE ready')
```

### Standard Structure

```python
# install editor -> select venv -> configure linter -> debug
```

### Code Pattern

```python
import sys
print('Interpreter:', sys.executable)
```

## Examples

### Beginner Example

```python
import sys
print(sys.version.split()[0])
```

### Intermediate Example

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


print(greet("Dev"))
```

### Advanced Example

```python
import sys

print("Executable:", sys.executable)
print("Version:", sys.version.split()[0])
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Project] --> B[venv] --> C[LSP] --> D[Run]
```

---

# Python Syntax

## Overview

- **What is it?** Python syntax defines how statements, blocks, and expressions are written.
- **Why is it important?** Correct syntax is required before logic, libraries, or frameworks matter.
- **Where is it used?** Every script, notebook cell, test file, and module.

## Learning Objectives

- **Skills gained:** Practical command of Python Syntax.
- **Concepts covered:**

- Use indentation, colons, and statement structure correctly.
- Write valid expressions and comments.
- Read tracebacks caused by syntax errors.

- **Expected outcome:** You write syntactically valid Python without constant SyntaxError failures.

## Real World Applications

- Application code
- Data notebooks
- Infrastructure scripts
- Test suites

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Indentation

- **Definition:** Blocks are defined by consistent leading spaces.
- **Visual explanation:** `Indentation` → process → result
- **Practical example:**

```python
if True:
    print('indented')
```

### Colon Blocks

- **Definition:** Compound statements end with a colon.
- **Visual explanation:** `Colon Blocks` → process → result
- **Practical example:**

```python
for i in range(3):
    print(i)
```

### Comments

- **Definition:** Lines starting with # are ignored.
- **Visual explanation:** `Comments` → process → result
- **Practical example:**

```python
# comment
x = 1
print(x)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Python uses significant whitespace and readable English keywords. |
| ⚡ Purpose | Express program structure clearly without braces. |
| 🔥 Benefits | Less boilerplate, enforced readability, quick to learn. |
| 🎯 Use Cases | Scripts, functions, classes, config loaders. |
| 🚀 Best Practices | 4 spaces per level, PEP 8 naming, one statement style per project. |
| ❌ Common Mistakes | Mixing tabs and spaces, missing colons, trailing comma confusion. |

## Syntax Guide

### Basic Syntax

```python
name = "Ada"
print(name)
```

### Standard Structure

```python
imports -> definitions -> main guard -> execution
```

### Code Pattern

```python
values = [1, 2, 3]
print([v * v for v in values])
```

## Examples

### Beginner Example

```python
message = "Syntax matters"
print(message)
```

### Intermediate Example

```python
print([v * v for v in [1, 2, 3, 4]])
```

### Advanced Example

```python
from typing import Iterator


def count(n: int) -> Iterator[int]:
    for i in range(n):
        yield i


print(list(count(4)))
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Source] --> B[Parser]
    B --> C{Valid?}
    C -->|yes| D[Execute]
    C -->|no| E[SyntaxError]
```

---

# Variables

## Overview

- **What is it?** Variables are names that reference objects stored in memory.
- **Why is it important?** They let programs remember state and transform data over time.
- **Where is it used?** Every Python program from scripts to ML pipelines.

## Learning Objectives

- **Skills gained:** Practical command of Variables.
- **Concepts covered:**

- Assign and reassign variables correctly.
- Follow PEP 8 naming conventions.
- Distinguish names from object identity.

- **Expected outcome:** You model program state with clear, consistent variable names.

## Real World Applications

- Business logic
- ETL transforms
- Game state
- Financial models

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Assignment

- **Definition:** Binds a name to an object.
- **Visual explanation:** `Assignment` → process → result
- **Practical example:**

```python
score = 100
print(score)
```

### Rebinding

- **Definition:** A name can refer to a new object.
- **Visual explanation:** `Rebinding` → process → result
- **Practical example:**

```python
score = score + 10
print(score)
```

### snake_case

- **Definition:** Standard style for variable names.
- **Visual explanation:** `snake_case` → process → result
- **Practical example:**

```python
user_email = 'a@b.com'
print(user_email)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Variables label objects; they are not typed boxes. |
| ⚡ Purpose | Store and update program data. |
| 🔥 Benefits | Readable code, reusable values, easier debugging. |
| 🎯 Use Cases | Counters, configs, user input, API payloads. |
| 🚀 Best Practices | Descriptive names, avoid shadowing builtins, init before use. |
| ❌ Common Mistakes | Reusing names for different concepts, mutating shared references unexpectedly. |

## Syntax Guide

### Basic Syntax

```python
name = 'Ada'
age = 36
```

### Standard Structure

```python
# declare -> use -> update
```

### Code Pattern

```python
total = price * quantity
print(total)
```

## Examples

### Beginner Example

```python
x = 5
y = 3
print(x + y)
```

### Intermediate Example

```python
first, second, *rest = [1, 2, 3, 4, 5]
print(first, second, rest)
```

### Advanced Example

```python
from typing import Final

MAX_RETRIES: Final = 3
attempts = 0
while attempts < MAX_RETRIES:
    attempts += 1
print(attempts)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Assign Name] --> B[Reference Object]
    B --> C[Read/Update]
```

---

# Data Types

## Overview

- **What is it?** Python data types classify values such as numbers, text, collections, and booleans.
- **Why is it important?** Choosing the right type prevents logic bugs and enables efficient operations.
- **Where is it used?** Validation, APIs, analytics, configuration, and user input handling.

## Learning Objectives

- **Skills gained:** Practical command of Data Types.
- **Concepts covered:**

- Identify built-in scalar and collection types.
- Inspect types with type() and isinstance().
- Select appropriate types for domain data.

- **Expected outcome:** You pick and verify types confidently in everyday Python code.

## Real World Applications

- Backend APIs
- Data science
- Finance systems
- IoT telemetry

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### int

- **Definition:** Whole numbers without fractional part.
- **Visual explanation:** `int` → process → result
- **Practical example:**

```python
count = 42
print(type(count))
```

### float

- **Definition:** Numbers with decimal precision.
- **Visual explanation:** `float` → process → result
- **Practical example:**

```python
price = 19.99
print(round(price, 2))
```

### bool

- **Definition:** True/False logical values.
- **Visual explanation:** `bool` → process → result
- **Practical example:**

```python
active = True
print(active and False)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Types describe what operations are valid on a value. |
| ⚡ Purpose | Model real-world data with the correct Python objects. |
| 🔥 Benefits | Safer code, clearer APIs, better performance choices. |
| 🎯 Use Cases | User profiles, sensor readings, cart totals, feature flags. |
| 🚀 Best Practices | Prefer isinstance over type(); document expected types. |
| ❌ Common Mistakes | Confusing None checks, bool/int coercion surprises. |

## Syntax Guide

### Basic Syntax

```python
age = 30
name = 'Ada'
active = True
```

### Standard Structure

```python
scalar -> collection -> inspect -> convert when needed
```

### Code Pattern

```python
print(isinstance(3.14, float))
```

## Examples

### Beginner Example

```python
print(type(3.14))
print(isinstance(3.14, float))
```

### Intermediate Example

```python
from typing import Any

def describe(value: Any) -> str:
    return f"{value!r} is {type(value).__name__}"


print(describe([1, 2]))
```

### Advanced Example

```python
from dataclasses import dataclass


@dataclass
class Reading:
    sensor_id: str
    value: float
    ok: bool


print(Reading("temp-1", 22.5, True))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Value] --> B{type?}
    B --> C[Scalar]
    B --> D[Collection]
```

---

# Type Casting

## Overview

- **What is it?** Type casting converts values from one type to another explicitly.
- **Why is it important?** User input and file data arrive as strings; casting enables computation.
- **Where is it used?** Forms, CSV imports, query parameters, CLI arguments.

## Learning Objectives

- **Skills gained:** Practical command of Type Casting.
- **Concepts covered:**

- Use int(), float(), str(), and bool() safely.
- Handle invalid conversions with try/except.
- Understand truthiness when casting to bool.

- **Expected outcome:** You convert external data into usable Python types without silent errors.

## Real World Applications

- E-commerce checkout
- Spreadsheet ingestion
- Mobile backends
- Billing engines

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### int()

- **Definition:** Parse integers from numeric strings.
- **Visual explanation:** `int()` → process → result
- **Practical example:**

```python
qty = int('12')
print(qty + 1)
```

### float()

- **Definition:** Parse decimal numbers.
- **Visual explanation:** `float()` → process → result
- **Practical example:**

```python
rate = float('0.075')
print(rate * 100)
```

### str()

- **Definition:** Serialize values for display or files.
- **Visual explanation:** `str()` → process → result
- **Practical example:**

```python
label = str(404)
print('HTTP ' + label)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Casting makes implicit string data explicit and computable. |
| ⚡ Purpose | Bridge human-readable input and program logic. |
| 🔥 Benefits | Correct math, valid comparisons, predictable formatting. |
| 🎯 Use Cases | Price calculations, age gates, ID formatting, logging. |
| 🚀 Best Practices | Validate before cast; strip whitespace; localize decimals carefully. |
| ❌ Common Mistakes | Casting invalid strings without error handling, using bool('0') incorrectly. |

## Syntax Guide

### Basic Syntax

```python
score = int('95')
print(score)
```

### Standard Structure

```python
read string -> validate -> cast -> use
```

### Code Pattern

```python
total = float('10.5') * int('2')
print(total)
```

## Examples

### Beginner Example

```python
age = int('21')
print(age >= 18)
```

### Intermediate Example

```python
def safe_int(text: str, default: int = 0) -> int:
    try:
        return int(text.strip())
    except ValueError:
        return default


print(safe_int(' 42 '))
```

### Advanced Example

```python
from decimal import Decimal

amount = Decimal('19.99')
tax = amount * Decimal('0.08')
print(amount + tax)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Raw Text] --> B[Validate]
    B --> C[Cast]
    C --> D[Compute]
```

---

# Input and Output

## Overview

- **What is it?** Input and output (I/O) moves data between users, files, and programs.
- **Why is it important?** Most programs must read requests and emit responses or logs.
- **Where is it used?** CLIs, notebooks, web forms, batch jobs, interactive tools.

## Learning Objectives

- **Skills gained:** Practical command of Input and Output.
- **Concepts covered:**

- Read user input with input() and parse it.
- Write formatted output with print() and f-strings.
- Separate presentation from business logic.

- **Expected outcome:** You build interactive scripts with clear prompts and readable output.

## Real World Applications

- Customer support tools
- Internal ops scripts
- Education apps
- Kiosk systems

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### input()

- **Definition:** Reads a line of text from stdin.
- **Visual explanation:** `input()` → process → result
- **Practical example:**

```python
name = 'Ada'
print(name.upper())
```

### print()

- **Definition:** Writes text to stdout.
- **Visual explanation:** `print()` → process → result
- **Practical example:**

```python
print('Done', flush=True)
```

### f-strings

- **Definition:** Embed expressions in strings.
- **Visual explanation:** `f-strings` → process → result
- **Practical example:**

```python
name = 'Ada'
print(f'Hello, {name}!')
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | I/O is the boundary between humans and your Python logic. |
| ⚡ Purpose | Collect parameters and communicate results. |
| 🔥 Benefits | Better UX, testable interfaces, scriptable workflows. |
| 🎯 Use Cases | Quizzes, calculators, menu-driven tools, quick prototypes. |
| 🚀 Best Practices | Prompt clearly, validate input, avoid mixing logic with formatting. |
| ❌ Common Mistakes | Trusting raw input, printing secrets, no newline control in logs. |

## Syntax Guide

### Basic Syntax

```python
name = 'World'
print(f'Hi, {name}')
```

### Standard Structure

```python
prompt -> read -> validate -> process -> display
```

### Code Pattern

```python
value = '7'
print(int(value) ** 2)
```

## Examples

### Beginner Example

```python
name = 'World'
print(f'Hi, {name}')
```

### Intermediate Example

```python
def ask_yes_no(prompt: str) -> bool:
    answer = 'yes'
    return answer in {'y', 'yes'}


print(ask_yes_no('Continue?'))
```

### Advanced Example

```python
import sys

data = 'hello world'
sys.stdout.write(data.upper() + '\n')
```

## Workflow Diagram

```mermaid
flowchart LR
    A[User Input] --> B[Parse]
    B --> C[Logic]
    C --> D[Output]
```

---

# Operators

## Overview

- **What is it?** Operators perform arithmetic, comparison, logical, and assignment actions on values.
- **Why is it important?** They express business rules compactly in conditions and expressions.
- **Where is it used?** Pricing, eligibility checks, scoring, game mechanics, data filters.

## Learning Objectives

- **Skills gained:** Practical command of Operators.
- **Concepts covered:**

- Apply arithmetic and comparison operators.
- Combine conditions with and, or, not.
- Use augmented assignment for updates.

- **Expected outcome:** You write expressive conditions and calculations without verbose code.

## Real World Applications

- Retail pricing
- Risk scoring
- Games
- Monitoring alerts

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Arithmetic

- **Definition:** + - * / // % ** on numbers.
- **Visual explanation:** `Arithmetic` → process → result
- **Practical example:**

```python
total = 10 + 5 * 2
print(total)
```

### Comparison

- **Definition:** Return booleans for ordering/equality.
- **Visual explanation:** `Comparison` → process → result
- **Practical example:**

```python
print(3 >= 2 and 4 != 5)
```

### Augmented assignment

- **Definition:** Update variables in place.
- **Visual explanation:** `Augmented assignment` → process → result
- **Practical example:**

```python
count = 0
count += 1
print(count)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Operators combine values into new results or decisions. |
| ⚡ Purpose | Implement rules and transformations inline. |
| 🔥 Benefits | Readable logic, fewer temporary variables. |
| 🎯 Use Cases | Tax calculation, access control, sorting keys, thresholds. |
| 🚀 Best Practices | Use parentheses for clarity; avoid chaining confusing comparisons. |
| ❌ Common Mistakes | Operator precedence mistakes, using is for value equality, division surprises. |

## Syntax Guide

### Basic Syntax

```python
a, b = 10, 3
print(a // b, a % b)
```

### Standard Structure

```python
operands -> operator -> result -> use in condition
```

### Code Pattern

```python
eligible = age >= 18 and country == 'US'
print(eligible)
```

## Examples

### Beginner Example

```python
price = 100
discount = price * 0.1
print(price - discount)
```

### Intermediate Example

```python
scores = [88, 92, 76]
average = sum(scores) / len(scores)
passed = average >= 80
print(average, passed)
```

### Advanced Example

```python
from operator import itemgetter

rows = [{'n': 'Ada', 's': 95}, {'n': 'Lin', 's': 88}]
top = max(rows, key=itemgetter('s'))
print(top)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Operands] --> B[Operator]
    B --> C[Result]
```

---

# Conditional Statements

## Overview

- **What is it?** Conditional statements execute code selectively with if, elif, and else.
- **Why is it important?** Business logic depends on branching based on data and state.
- **Where is it used?** Auth checks, feature flags, error paths, pricing tiers.

## Learning Objectives

- **Skills gained:** Practical command of Conditional Statements.
- **Concepts covered:**

- Write if/elif/else chains for multiple cases.
- Nest conditions sparingly with clear structure.
- Use ternary expressions for simple assignments.

- **Expected outcome:** You implement decision trees that are easy to read and test.

## Real World Applications

- Access control
- Billing rules
- Workflow engines
- Support triage

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### if

- **Definition:** Runs block when condition is truthy.
- **Visual explanation:** `if` → process → result
- **Practical example:**

```python
if score >= 60:
    print('pass')
```

### elif

- **Definition:** Tests additional conditions.
- **Visual explanation:** `elif` → process → result
- **Practical example:**

```python
x = -1
if x > 0:
    sign = 'pos'
elif x < 0:
    sign = 'neg'
else:
    sign = 'zero'
print(sign)
```

### else

- **Definition:** Fallback when no condition matches.
- **Visual explanation:** `else` → process → result
- **Practical example:**

```python
logged_in = False
print('home' if logged_in else 'login')
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Conditionals map inputs to different behaviors. |
| ⚡ Purpose | Encode policies and validations. |
| 🔥 Benefits | Explicit paths, fewer duplicated checks, testable branches. |
| 🎯 Use Cases | Login flows, shipping methods, grading, alert severity. |
| 🚀 Best Practices | Prefer flat elif chains; extract complex tests to functions. |
| ❌ Common Mistakes | Deep nesting, duplicate conditions, assignment inside if by mistake. |

## Syntax Guide

### Basic Syntax

```python
if temperature > 30:
    print('hot')
```

### Standard Structure

```python
guard clauses -> main branches -> else fallback
```

### Code Pattern

```python
status = 'gold' if points >= 1000 else 'silver'
```

## Examples

### Beginner Example

```python
score = 74
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'
print(grade)
```

### Intermediate Example

```python
def shipping_fee(weight_kg: float) -> float:
    if weight_kg <= 1:
        return 5.0
    if weight_kg <= 5:
        return 9.0
    return 15.0


print(shipping_fee(3.2))
```

### Advanced Example

```python
from enum import Enum


class Role(str, Enum):
    ADMIN = 'admin'
    USER = 'user'


def can_delete(role: Role) -> bool:
    return role is Role.ADMIN


print(can_delete(Role.USER))
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Condition] -->|True| B[Then]
    A -->|False| C[Else/Elif]
```

---

# Loops

## Overview

- **What is it?** Loops repeat blocks of code while a condition holds or over a sequence.
- **Why is it important?** Iteration processes collections and repeated tasks without duplication.
- **Where is it used?** Batch processing, reports, games, polling, data pipelines.

## Learning Objectives

- **Skills gained:** Practical command of Loops.
- **Concepts covered:**

- Use for and while loops appropriately.
- Iterate sequences and ranges.
- Avoid infinite loops.

- **Expected outcome:** You process collections and repeated work with clear loop constructs.

## Real World Applications

- Report generation
- Game loops
- IoT sampling
- Finance batch jobs

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### for

- **Definition:** Iterate over iterable objects.
- **Visual explanation:** `for` → process → result
- **Practical example:**

```python
for ch in 'abc':
    print(ch)
```

### while

- **Definition:** Repeat while condition is true.
- **Visual explanation:** `while` → process → result
- **Practical example:**

```python
n = 3
while n:
    n -= 1
    print(n)
```

### range

- **Definition:** Generate arithmetic progressions.
- **Visual explanation:** `range` → process → result
- **Practical example:**

```python
for i in range(3):
    print(i)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Loops automate repetition with controlled exit conditions. |
| ⚡ Purpose | Traverse data and repeat operations efficiently. |
| 🔥 Benefits | Less duplication, scalable processing, idiomatic Python. |
| 🎯 Use Cases | Summing lists, retry logic, parsing lines, animations. |
| 🚀 Best Practices | Prefer for over while when iterating sequences; use enumerate when needed. |
| ❌ Common Mistakes | Off-by-one errors, modifying list while iterating, unbounded while True without break. |

## Syntax Guide

### Basic Syntax

```python
for item in items:
    print(item)
```

### Standard Structure

```python
init -> loop header -> body -> next item
```

### Code Pattern

```python
for row in rows:
    print(row)
```

## Examples

### Beginner Example

```python
for i in range(5):
    print(i * i)
```

### Intermediate Example

```python
total = 0
for value in [1, 2, 3, 4]:
    total += value
print(total)
```

### Advanced Example

```python
for index, name in enumerate(['Ada', 'Grace'], start=1):
    print(index, name)
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Start Loop] --> B{More?}
    B -->|yes| C[Body]
    C --> B
    B -->|no| D[Exit]
```

---

# Nested Loops

## Overview

- **What is it?** Nested loops place one loop inside another to handle multi-dimensional iteration.
- **Why is it important?** Matrices, grids, combinations, and nested records require nested iteration.
- **Where is it used?** Image pixels, seat maps, cartesian products, nested JSON.

## Learning Objectives

- **Skills gained:** Practical command of Nested Loops.
- **Concepts covered:**

- Write nested for loops for 2D data.
- Control complexity with helper functions.
- Break early when possible.

- **Expected outcome:** You traverse nested structures without losing readability.

## Real World Applications

- Graphics
- Scheduling
- E-commerce bundles
- Simulation

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Outer loop

- **Definition:** Controls major dimension.
- **Visual explanation:** `Outer loop` → process → result
- **Practical example:**

```python
for row in [[1, 2], [3]]:
    print(row)
```

### Inner loop

- **Definition:** Processes each element in a row.
- **Visual explanation:** `Inner loop` → process → result
- **Practical example:**

```python
for row in [[1, 2], [3]]:
    for x in row:
        print(x)
```

### Cartesian product

- **Definition:** Nested loops generate pairs.
- **Visual explanation:** `Cartesian product` → process → result
- **Practical example:**

```python
pairs = [(a, b) for a in range(2) for b in range(2)]
print(len(pairs))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Nested loops walk structures with more than one dimension. |
| ⚡ Purpose | Visit every combination or nested element systematically. |
| 🔥 Benefits | Straightforward for small data, easy to reason about. |
| 🎯 Use Cases | Multiplication tables, board games, nested categories. |
| 🚀 Best Practices | Extract inner body to functions; consider itertools.product. |
| ❌ Common Mistakes | O(n^3) surprises, deep nesting without bounds, reusing loop variable names. |

## Syntax Guide

### Basic Syntax

```python
for i in range(2):
    for j in range(2):
        print(i, j)
```

### Standard Structure

```python
outer init -> inner init -> body -> inner next -> outer next
```

### Code Pattern

```python
for y in rows:
    for x in y:
        print(x)
```

## Examples

### Beginner Example

```python
for r in range(2):
    for c in range(2):
        print(r, c)
```

### Intermediate Example

```python
matrix = [[1, 2], [3, 4]]
flat = [x for row in matrix for x in row]
print(flat)
```

### Advanced Example

```python
from itertools import product

for a, b in product(['A', 'B'], [1, 2]):
    print(a, b)
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Outer] --> B[Inner]
    B --> C[Process]
    C --> B
```

---

# Break Continue Pass

## Overview

- **What is it?** break, continue, and pass alter loop flow or serve as placeholders.
- **Why is it important?** They express early exit, skip iteration, or stub incomplete code cleanly.
- **Where is it used?** Search loops, validation pipelines, protocol stubs, parsers.

## Learning Objectives

- **Skills gained:** Practical command of Break Continue Pass.
- **Concepts covered:**

- Use break to exit loops early.
- Use continue to skip iterations.
- Use pass for empty blocks.

- **Expected outcome:** You control loop flow precisely without awkward flags.

## Real World Applications

- Log parsing
- Search features
- Games
- Network clients

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### break

- **Definition:** Exit the nearest enclosing loop.
- **Visual explanation:** `break` → process → result
- **Practical example:**

```python
for n in range(10):
    if n == 3:
        break
print('done')
```

### continue

- **Definition:** Skip to next iteration.
- **Visual explanation:** `continue` → process → result
- **Practical example:**

```python
for n in range(5):
    if n % 2 == 0:
        continue
    print(n)
```

### pass

- **Definition:** Null statement preserving syntax.
- **Visual explanation:** `pass` → process → result
- **Practical example:**

```python
def todo():
    pass
print(callable(todo))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Flow keywords fine-tune iteration without extra state variables. |
| ⚡ Purpose | Express skip, stop, or stub directly in loops and classes. |
| 🔥 Benefits | Clearer loops, less boilerplate, valid empty blocks. |
| 🎯 Use Cases | Find first match, filter invalid rows, TDD stubs. |
| 🚀 Best Practices | Prefer functions over deeply broken loops; document pass usage. |
| ❌ Common Mistakes | break only breaks one level, continue in wrong place, pass hiding missing logic. |

## Syntax Guide

### Basic Syntax

```python
for x in xs:
    if x < 0:
        continue
    print(x)
```

### Standard Structure

```python
loop -> test -> break/continue/pass -> body
```

### Code Pattern

```python
for item in items:
    if item is None:
        continue
    print(item)
```

## Examples

### Beginner Example

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

### Intermediate Example

```python
evens = []
for n in range(6):
    if n % 2:
        continue
    evens.append(n)
print(evens)
```

### Advanced Example

```python
class Parser:
    def feed(self, chunk: bytes) -> None:
        pass


print(hasattr(Parser(), 'feed'))
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Loop] --> B{break?}
    B -->|yes| C[Exit]
    B -->|no| D{continue?}
```

---

# Strings

## Overview

- **What is it?** Strings are immutable sequences of Unicode characters.
- **Why is it important?** Text processing is central to APIs, logs, and user interfaces.
- **Where is it used?** Web apps, document tools, NLP preprocessing, log parsers.

## Learning Objectives

- **Skills gained:** Practical command of Strings.
- **Concepts covered:**

- Create and slice strings.
- Use common string methods.
- Format output with f-strings.

- **Expected outcome:** You manipulate and format text confidently in Python.

## Real World Applications

- Web frontends
- Log analysis
- Chatbots
- Document automation

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Literals

- **Definition:** Quoted text creates str objects.
- **Visual explanation:** `Literals` → process → result
- **Practical example:**

```python
msg = 'hello'
print(msg.upper())
```

### Slicing

- **Definition:** Extract subsequences by index.
- **Visual explanation:** `Slicing` → process → result
- **Practical example:**

```python
print('Python'[0:2])
```

### f-strings

- **Definition:** Embed expressions in strings.
- **Visual explanation:** `f-strings` → process → result
- **Practical example:**

```python
name = 'Ada'
print(f'Hi {name}')
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Strings are immutable Unicode text. |
| ⚡ Purpose | Represent and transform textual data. |
| 🔥 Benefits | Rich methods, easy formatting, UTF-8 by default. |
| 🎯 Use Cases | User names, templates, CSV fields, HTTP bodies. |
| 🚀 Best Practices | Prefer f-strings; avoid concatenating in tight loops. |
| ❌ Common Mistakes | Mutating strings, poor encoding handling, O(n^2) concat. |

## Syntax Guide

### Basic Syntax

```python
greeting = 'Hello'
print(greeting + ' World')
```

### Standard Structure

```python
create -> transform -> format -> output
```

### Code Pattern

```python
label = f'item: {name}'
print(label)
```

## Examples

### Beginner Example

```python
text = '  Python  '
print(text.strip().lower())
```

### Intermediate Example

```python
words = 'a,b,c'.split(',')
print('-'.join(words))
```

### Advanced Example

```python
import re

print(re.sub(r'\d+', '#', 'Room 42'))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Text Input] --> B[Normalize]
    B --> C[Transform]
    C --> D[Output]
```

---

# String Methods

## Overview

- **What is it?** String methods provide built-in operations for searching, splitting, and formatting text.
- **Why is it important?** Method calls replace hand-written parsing for common text tasks.
- **Where is it used?** Data cleaning, URL handling, validation, templating.

## Learning Objectives

- **Skills gained:** Practical command of String Methods.
- **Concepts covered:**

- Apply strip, split, join, replace, and find.
- Choose methods vs regex appropriately.
- Chain operations readably.

- **Expected outcome:** You clean and transform strings using the str API efficiently.

## Real World Applications

- Marketing analytics
- Support tickets
- SEO tools
- Compliance redaction

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### strip

- **Definition:** Remove leading/trailing whitespace.
- **Visual explanation:** `strip` → process → result
- **Practical example:**

```python
print('  hi  '.strip())
```

### split/join

- **Definition:** Tokenize and reassemble strings.
- **Visual explanation:** `split/join` → process → result
- **Practical example:**

```python
print('-'.join('a b c'.split()))
```

### replace

- **Definition:** Substitute substrings.
- **Visual explanation:** `replace` → process → result
- **Practical example:**

```python
print('foo-bar'.replace('-', '_'))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | str methods operate on immutable copies. |
| ⚡ Purpose | Standardize text transformations. |
| 🔥 Benefits | Readable, fast C implementations, fewer bugs. |
| 🎯 Use Cases | Normalizing emails, parsing tags, masking PII. |
| 🚀 Best Practices | Normalize once; store canonical form; handle None before calling. |
| ❌ Common Mistakes | Calling methods on None, locale-unaware case folding, excessive regex. |

## Syntax Guide

### Basic Syntax

```python
email = ' Ada@Example.COM '
print(email.strip().lower())
```

### Standard Structure

```python
normalize -> tokenize -> transform -> join
```

### Code Pattern

```python
parts = line.strip().split(',')
print(parts)
```

## Examples

### Beginner Example

```python
print('hello world'.title())
```

### Intermediate Example

```python
slug = 'Hello World'.lower().replace(' ', '-')
print(slug)
```

### Advanced Example

```python
from textwrap import dedent as d

block = d('''                line one
    line two
''')
print(block.splitlines())
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Raw str] --> B[Methods]
    B --> C[Clean str]
```

---

# Lists

## Overview

- **What is it?** Lists are ordered, mutable sequences of arbitrary objects.
- **Why is it important?** They are the default workhorse collection for ordered data.
- **Where is it used?** Queues, result sets, UI lists, algorithm inputs.

## Learning Objectives

- **Skills gained:** Practical command of Lists.
- **Concepts covered:**

- Create, index, slice, and mutate lists.
- Use list comprehensions.
- Copy lists safely.

- **Expected outcome:** You store and transform ordered collections fluently.

## Real World Applications

- Inventory systems
- Analytics
- Media playlists
- Task queues

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Literals

- **Definition:** Square brackets build lists.
- **Visual explanation:** `Literals` → process → result
- **Practical example:**

```python
nums = [1, 2, 3]
print(nums[0])
```

### append

- **Definition:** Add element at end.
- **Visual explanation:** `append` → process → result
- **Practical example:**

```python
items = []
items.append('a')
print(items)
```

### Comprehension

- **Definition:** Build lists from iterables.
- **Visual explanation:** `Comprehension` → process → result
- **Practical example:**

```python
squares = [n * n for n in range(4)]
print(squares)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Lists are dynamic arrays of references. |
| ⚡ Purpose | Hold ordered, changeable sequences. |
| 🔥 Benefits | Versatile, fast append/pop at end, rich API. |
| 🎯 Use Cases | Shopping carts, timelines, batch results. |
| 🚀 Best Practices | Avoid using as default args; copy before mutate shared data. |
| ❌ Common Mistakes | Shallow copy surprises, O(n) inserts at front, aliasing bugs. |

## Syntax Guide

### Basic Syntax

```python
fruits = ['apple', 'banana']
print(len(fruits))
```

### Standard Structure

```python
create -> access -> mutate -> iterate
```

### Code Pattern

```python
results = [transform(x) for x in data]
```

## Examples

### Beginner Example

```python
colors = ['red', 'green']
colors.append('blue')
print(colors)
```

### Intermediate Example

```python
matrix = [[1, 2], [3, 4]]
print([row[0] for row in matrix])
```

### Advanced Example

```python
from copy import deepcopy

original = [[1], [2]]
cloned = deepcopy(original)
cloned[0].append(9)
print(original, cloned)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[List] --> B[Index/Slice]
    B --> C[Mutate]
    C --> D[Iterate]
```

---

# List Methods

## Overview

- **What is it?** List methods mutate or query lists in place: sort, extend, pop, remove, and more.
- **Why is it important?** In-place operations save memory and express intent clearly.
- **Where is it used?** Sorting results, stack behavior, deduplication workflows.

## Learning Objectives

- **Skills gained:** Practical command of List Methods.
- **Concepts covered:**

- Use sort, reverse, extend, insert, pop, remove.
- Know which methods return None.
- Pick list vs set for uniqueness.

- **Expected outcome:** You update lists efficiently using the list API.

## Real World Applications

- Ranking dashboards
- Undo stacks
- Batch ETL
- Leaderboards

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### sort

- **Definition:** Order list in place.
- **Visual explanation:** `sort` → process → result
- **Practical example:**

```python
nums = [3, 1, 2]
nums.sort()
print(nums)
```

### pop

- **Definition:** Remove and return item.
- **Visual explanation:** `pop` → process → result
- **Practical example:**

```python
stack = [1, 2]
print(stack.pop())
```

### extend

- **Definition:** Add multiple items.
- **Visual explanation:** `extend` → process → result
- **Practical example:**

```python
a = [1]
a.extend([2, 3])
print(a)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Mutating methods update the same list object. |
| ⚡ Purpose | Modify ordered collections without reassigning names. |
| 🔥 Benefits | Performance, clarity, idiomatic Python. |
| 🎯 Use Cases | Priority queues, rolling windows, in-memory buffers. |
| 🚀 Best Practices | sorted() for new list; key= for custom ordering. |
| ❌ Common Mistakes | Assigning sort result, modifying while iterating, pop empty list. |

## Syntax Guide

### Basic Syntax

```python
values = [3, 1, 2]
values.sort()
print(values)
```

### Standard Structure

```python
prepare list -> call method -> verify state
```

### Code Pattern

```python
items.extend(new_batch)
items.sort(key=len)
```

## Examples

### Beginner Example

```python
pets = ['cat', 'dog']
pets.append('bird')
print(pets)
```

### Intermediate Example

```python
data = ['b', 'a', 'c']
print(sorted(data))
print(data)
```

### Advanced Example

```python
from bisect import insort

scores = [10, 20, 40]
insort(scores, 25)
print(scores)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[List] --> B[Method]
    B --> C[Updated List]
```

---

# Tuples

## Overview

- **What is it?** Tuples are ordered, immutable sequences often used for fixed records.
- **Why is it important?** Immutability makes tuples safe dictionary keys and return values.
- **Where is it used?** Coordinates, DB rows, function returns, config constants.

## Learning Objectives

- **Skills gained:** Practical command of Tuples.
- **Concepts covered:**

- Create tuples and unpack them.
- Use tuples as dict keys.
- Choose tuple vs list.

- **Expected outcome:** You model fixed-size records with tuples appropriately.

## Real World Applications

- GIS
- Finance ticks
- ORM rows
- Robotics state

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Literals

- **Definition:** Parentheses or commas create tuples.
- **Visual explanation:** `Literals` → process → result
- **Practical example:**

```python
point = (10, 20)
print(point[0])
```

### Unpacking

- **Definition:** Assign elements to names.
- **Visual explanation:** `Unpacking` → process → result
- **Practical example:**

```python
x, y = (3, 4)
print(x + y)
```

### Immutability

- **Definition:** Cannot change length or items.
- **Visual explanation:** `Immutability` → process → result
- **Practical example:**

```python
t = (1, 2)
print(len(t))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Tuples protect data from accidental mutation. |
| ⚡ Purpose | Represent small fixed structures. |
| 🔥 Benefits | Hashable, memory efficient, clear intent. |
| 🎯 Use Cases | RGB triples, lat/long, multi-return values. |
| 🚀 Best Practices | Use namedtuple or dataclass for many fields. |
| ❌ Common Mistakes | Trying to append, confusing single-element syntax, huge tuples. |

## Syntax Guide

### Basic Syntax

```python
rgb = (255, 128, 0)
print(rgb)
```

### Standard Structure

```python
pack values -> pass/store -> unpack/use
```

### Code Pattern

```python
name, score = get_result()
```

## Examples

### Beginner Example

```python
dims = (1920, 1080)
print(dims[0] * dims[1])
```

### Intermediate Example

```python
record = ('Ada', 36)
print(f'{record[0]} is {record[1]}')
```

### Advanced Example

```python
from collections import namedtuple

Point = namedtuple('Point', 'x y')
print(Point(1, 2)._asdict())
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Values] --> B[Tuple]
    B --> C[Unpack/Key]
```

---

# Sets

## Overview

- **What is it?** Sets are unordered collections of unique hashable elements.
- **Why is it important?** They provide fast membership tests and set algebra.
- **Where is it used?** Tag systems, deduplication, permission unions, graph nodes.

## Learning Objectives

- **Skills gained:** Practical command of Sets.
- **Concepts covered:**

- Create sets and test membership.
- Apply union, intersection, difference.
- Use set comprehensions.

- **Expected outcome:** You deduplicate and compare collections with sets.

## Real World Applications

- Ad targeting
- Security IOC lists
- Catalog tags
- Graph analytics

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Literals

- **Definition:** Curly braces or set() constructor.
- **Visual explanation:** `Literals` → process → result
- **Practical example:**

```python
tags = {'python', 'web'}
print('python' in tags)
```

### Uniqueness

- **Definition:** Duplicates are ignored.
- **Visual explanation:** `Uniqueness` → process → result
- **Practical example:**

```python
print(set([1, 1, 2]))
```

### Algebra

- **Definition:** Union and intersection ops.
- **Visual explanation:** `Algebra` → process → result
- **Practical example:**

```python
a = {1, 2}
b = {2, 3}
print(a & b)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Sets enforce uniqueness with hash-based lookup. |
| ⚡ Purpose | Track distinct items and relationships. |
| 🔥 Benefits | O(1) average membership, expressive operators. |
| 🎯 Use Cases | Unique visitors, skill tags, anomaly detection. |
| 🚀 Best Practices | Use frozenset for immutable sets; beware unhashable elements. |
| ❌ Common Mistakes | Using {} for empty set, relying on order, set of lists. |

## Syntax Guide

### Basic Syntax

```python
seen = set()
seen.add('a')
print(seen)
```

### Standard Structure

```python
build set -> membership/ops -> consume
```

### Code Pattern

```python
unique = set(items)
print(len(unique))
```

## Examples

### Beginner Example

```python
print(set('hello'))
```

### Intermediate Example

```python
required = {'read', 'write'}
granted = {'read'}
print(required <= granted)
```

### Advanced Example

```python
def jaccard(a: set[str], b: set[str]) -> float:
    return len(a & b) / len(a | b)


print(jaccard({'a', 'b'}, {'b', 'c'}))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Items] --> B[Set]
    B --> C[Unique/Membership]
```

---

# Dictionaries

## Overview

- **What is it?** Dictionaries map hashable keys to values for fast lookup.
- **Why is it important?** Key-value storage models records, caches, and indexes naturally.
- **Where is it used?** JSON-like data, configs, memoization, frequency counts.

## Learning Objectives

- **Skills gained:** Practical command of Dictionaries.
- **Concepts covered:**

- Create, access, and update dicts.
- Iterate keys, values, items.
- Use get and setdefault safely.

- **Expected outcome:** You structure associative data with dictionaries.

## Real World Applications

- API payloads
- Session stores
- Feature flags
- Word counts

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Literals

- **Definition:** Key:value pairs in braces.
- **Visual explanation:** `Literals` → process → result
- **Practical example:**

```python
user = {'name': 'Ada'}
print(user['name'])
```

### get

- **Definition:** Safe lookup with default.
- **Visual explanation:** `get` → process → result
- **Practical example:**

```python
print({'a': 1}.get('b', 0))
```

### items

- **Definition:** Iterate key-value pairs.
- **Visual explanation:** `items` → process → result
- **Practical example:**

```python
for k, v in {'x': 1}.items():
    print(k, v)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Dicts are hash tables mapping keys to values. |
| ⚡ Purpose | Associate labels with data for O(1) lookup. |
| 🔥 Benefits | Flexible schema, fast access, JSON-like. |
| 🎯 Use Cases | HTTP headers, tallies, object caches. |
| 🚀 Best Practices | Use dict comprehensions; avoid mutating while iterating. |
| ❌ Common Mistakes | KeyError on missing keys, unhashable keys, relying on order before 3.7 mentally. |

## Syntax Guide

### Basic Syntax

```python
scores = {'Ada': 98, 'Lin': 87}
print(scores['Ada'])
```

### Standard Structure

```python
build -> lookup/update -> iterate
```

### Code Pattern

```python
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
```

## Examples

### Beginner Example

```python
capitals = {'FR': 'Paris'}
print(capitals.get('FR'))
```

### Intermediate Example

```python
rows = [{'id': 1, 'name': 'Ada'}, {'id': 2, 'name': 'Lin'}]
by_id = {r['id']: r for r in rows}
print(by_id[2])
```

### Advanced Example

```python
from collections import defaultdict

dd = defaultdict(list)
for dept, name in [('eng', 'Ada'), ('eng', 'Lin')]:
    dd[dept].append(name)
print(dict(dd))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Key] --> B[Hash]
    B --> C[Value]
```

---

# Functions

## Overview

- **What is it?** Functions are reusable blocks of code that perform a task and optionally return a value.
- **Why is it important?** They reduce duplication and organize logic into testable units.
- **Where is it used?** API handlers, data transforms, CLI tools, ML training loops.

## Learning Objectives

- **Skills gained:** Practical command of Functions.
- **Concepts covered:**

- Define and call functions.
- Use parameters and return values.
- Apply default and keyword arguments.

- **Expected outcome:** You structure programs into composable functions.

## Real World Applications

- Backend services
- Data engineering
- Test automation
- Quant libraries

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### def

- **Definition:** Keyword to define a function.
- **Visual explanation:** `def` → process → result
- **Practical example:**

```python
def greet(name):
    return f'Hi {name}'
print(greet('Ada'))
```

### Parameters

- **Definition:** Inputs declared in the definition.
- **Visual explanation:** `Parameters` → process → result
- **Practical example:**

```python
def add(a, b):
    return a + b
print(add(2, 3))
```

### Return

- **Definition:** Sends a result back to the caller.
- **Visual explanation:** `Return` → process → result
- **Practical example:**

```python
def double(n):
    return n * 2
print(double(4))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Functions encapsulate behavior with a clear interface. |
| ⚡ Purpose | Reuse logic and improve maintainability. |
| 🔥 Benefits | Testability, readability, modularity. |
| 🎯 Use Cases | Validation, formatting, API clients, business rules. |
| 🚀 Best Practices | Single responsibility, type hints, docstrings. |
| ❌ Common Mistakes | Side effects in pure helpers, too many parameters. |

## Syntax Guide

### Basic Syntax

```python
def double(n):
    return n * 2
```

### Standard Structure

```python
def name(params):
    body
    return result
```

### Code Pattern

```python
def process(data):
    return transform(clean(data))
```

## Examples

### Beginner Example

```python
def greet(name):
    print(f'Hello, {name}')

greet('World')
```

### Intermediate Example

```python
def summarize(numbers: list[float]) -> dict[str, float]:
    return {"count": len(numbers), "total": sum(numbers)}


print(summarize([1.5, 2.5, 3.0]))
```

### Advanced Example

```python
from functools import wraps


def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__, 'called')
        return result

    return wrapper


@log_calls
def add(a, b):
    return a + b


print(add(1, 2))
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Call] --> B[Bind Args]
    B --> C[Body]
    C --> D[Return]
```

---

# Arguments and Parameters

## Overview

- **What is it?** Parameters define what a function accepts; arguments are the values passed in.
- **Why is it important?** Flexible signatures support optional config, variadic input, and readable call sites.
- **Where is it used?** Library APIs, frameworks, decorators, CLI wrappers.

## Learning Objectives

- **Skills gained:** Practical command of Arguments and Parameters.
- **Concepts covered:**

- Use positional and keyword parameters.
- Apply *args and **kwargs.
- Avoid mutable default arguments.

- **Expected outcome:** You design function signatures that are safe and expressive.

## Real World Applications

- SDK design
- Web frameworks
- Plugin systems
- Testing utilities

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Defaults

- **Definition:** Parameters with fallback values.
- **Visual explanation:** `Defaults` → process → result
- **Practical example:**

```python
def connect(timeout=30):
    return timeout
print(connect())
```

### Keyword args

- **Definition:** Call by name for clarity.
- **Visual explanation:** `Keyword args` → process → result
- **Practical example:**

```python
def plot(x, y, color='blue'):
    return (x, y, color)
print(plot(1, 2, color='red'))
```

### *args/**kwargs

- **Definition:** Collect extra positional/keyword args.
- **Visual explanation:** `*args/**kwargs` → process → result
- **Practical example:**

```python
def wrap(*args, **kwargs):
    return (args, kwargs)
print(wrap(1, z=2))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Binding maps arguments to parameters at call time. |
| ⚡ Purpose | Let functions accept varying inputs cleanly. |
| 🔥 Benefits | Readable calls, extensibility, wrapper-friendly. |
| 🎯 Use Cases | Decorators, logging wrappers, optional flags. |
| 🚀 Best Practices | Keyword-only for bool flags; immutable defaults; type hints. |
| ❌ Common Mistakes | Mutable defaults, overusing **kwargs, unclear parameter order. |

## Syntax Guide

### Basic Syntax

```python
def power(base, exp=2):
    return base ** exp
```

### Standard Structure

```python
define params -> bind at call -> execute
```

### Code Pattern

```python
def create_user(name, *, active=True):
    return {'name': name, 'active': active}
```

## Examples

### Beginner Example

```python
def greet(name, punctuation='!'):
    print(f'Hello, {name}{punctuation}')

greet('Ada')
```

### Intermediate Example

```python
def tag(*labels, **meta):
    return {'labels': labels, 'meta': meta}


print(tag('py', 'web', year=2026))
```

### Advanced Example

```python
from typing import Callable


def twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))


print(twice(lambda x: x + 1, 3))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Call Site] --> B[Bind Params]
    B --> C[Function Body]
```

---

# Return Statements

## Overview

- **What is it?** return sends a value back to the caller and exits the function.
- **Why is it important?** Callers need results; early returns simplify control flow.
- **Where is it used?** Calculations, parsers, validators, service methods.

## Learning Objectives

- **Skills gained:** Practical command of Return Statements.
- **Concepts covered:**

- Return single and multiple values.
- Use early return for guards.
- Distinguish return vs print.

- **Expected outcome:** You write functions that communicate results clearly.

## Real World Applications

- Financial calculators
- Compilers
- Auth services
- Games

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Single value

- **Definition:** Most common return form.
- **Visual explanation:** `Single value` → process → result
- **Practical example:**

```python
def sq(n):
    return n * n
print(sq(4))
```

### Tuple return

- **Definition:** Multiple values as one object.
- **Visual explanation:** `Tuple return` → process → result
- **Practical example:**

```python
def minmax(nums):
    return min(nums), max(nums)
print(minmax([3, 1, 2]))
```

### Early return

- **Definition:** Exit when precondition fails.
- **Visual explanation:** `Early return` → process → result
- **Practical example:**

```python
def safe_div(a, b):
    if b == 0:
        return None
    return a / b
print(safe_div(4, 2))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | return completes the function call expression. |
| ⚡ Purpose | Deliver outputs and stop execution when done. |
| 🔥 Benefits | Composable functions, clearer flow, testable outputs. |
| 🎯 Use Cases | Validation results, parsed tokens, status codes. |
| 🚀 Best Practices | Keep return types consistent; document None cases. |
| ❌ Common Mistakes | Returning print result, inconsistent types, missing return. |

## Syntax Guide

### Basic Syntax

```python
def add(a, b):
    return a + b
```

### Standard Structure

```python
compute -> optionally early exit -> return
```

### Code Pattern

```python
if not valid(x):
    return None
return transform(x)
```

## Examples

### Beginner Example

```python
def is_even(n):
    return n % 2 == 0
print(is_even(4))
```

### Intermediate Example

```python
def partition(nums, pivot):
    low = [n for n in nums if n < pivot]
    high = [n for n in nums if n >= pivot]
    return low, high
print(partition([3, 1, 4, 2], 3))
```

### Advanced Example

```python
from typing import Optional


def find_user(users: list[dict], user_id: int) -> Optional[dict]:
    for user in users:
        if user.get('id') == user_id:
            return user
    return None


print(find_user([{'id': 1}], 1))
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Function] --> B{Guard?}
    B -->|fail| C[Early Return]
    B -->|ok| D[Return Result]
```

---

# Scope

## Overview

- **What is it?** Scope determines where names are visible: local, enclosing, global, or builtin (LEGB).
- **Why is it important?** Understanding scope prevents accidental shadowing and mutation bugs.
- **Where is it used?** Closures, modules, nested functions, configuration.

## Learning Objectives

- **Skills gained:** Practical command of Scope.
- **Concepts covered:**

- Trace LEGB name lookup.
- Use global/nonlocal intentionally.
- Avoid shadowing builtins.

- **Expected outcome:** You predict where assignments bind and how nested functions capture state.

## Real World Applications

- Plugin hosts
- GUI callbacks
- Financial models
- Game engines

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Local

- **Definition:** Names inside a function.
- **Visual explanation:** `Local` → process → result
- **Practical example:**

```python
def f():
    x = 1
    return x
print(f())
```

### Global

- **Definition:** Module-level names.
- **Visual explanation:** `Global` → process → result
- **Practical example:**

```python
count = 0
def inc():
    global count
    count += 1
inc()
print(count)
```

### nonlocal

- **Definition:** Modify enclosing function variables.
- **Visual explanation:** `nonlocal` → process → result
- **Practical example:**

```python
def outer():
    total = 0
    def inner():
        nonlocal total
        total += 1
        return total
    return inner()
print(outer())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Python resolves names outward through LEGB. |
| ⚡ Purpose | Control visibility and lifetime of variables. |
| 🔥 Benefits | Modularity, encapsulation, predictable bindings. |
| 🎯 Use Cases | Counters, factories, decorators, cached state. |
| 🚀 Best Practices | Minimize global state; prefer parameters and return values. |
| ❌ Common Mistakes | UnboundLocalError, accidental global mutation, shadowing list/str. |

## Syntax Guide

### Basic Syntax

```python
x = 'global'
def demo():
    x = 'local'
    return x
print(demo(), x)
```

### Standard Structure

```python
define scope -> assign -> lookup
```

### Code Pattern

```python
def make_adder(n):
    def add(x):
        return x + n
    return add
```

## Examples

### Beginner Example

```python
message = 'hi'
def show():
    return message
print(show())
```

### Intermediate Example

```python
def counter():
    n = 0
    def step():
        nonlocal n
        n += 1
        return n
    return step
c = counter()
print(c(), c())
```

### Advanced Example

```python
def multiplier(factor):
    def wrap(value):
        return value * factor
    return wrap


double = multiplier(2)
print(double(5))
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Name Lookup] --> B[Local]
    B --> C[Enclosing]
    C --> D[Global]
    D --> E[Builtins]
```

---

# Lambda Functions

## Overview

- **What is it?** Lambda functions are anonymous one-expression functions.
- **Why is it important?** They shine as short callbacks for sort keys and functional helpers.
- **Where is it used?** sorted/key=, map/filter, pandas apply, event handlers.

## Learning Objectives

- **Skills gained:** Practical command of Lambda Functions.
- **Concepts covered:**

- Write simple lambda expressions.
- Use with sorted, map, filter.
- Know when def is clearer.

- **Expected outcome:** You apply lambdas appropriately without harming readability.

## Real World Applications

- Data wrangling
- UI tooling
- Competitive programming
- Config DSLs

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Syntax

- **Definition:** lambda params: expression.
- **Visual explanation:** `Syntax` → process → result
- **Practical example:**

```python
double = lambda x: x * 2
print(double(3))
```

### sorted key

- **Definition:** Customize ordering.
- **Visual explanation:** `sorted key` → process → result
- **Practical example:**

```python
pairs = [(1, 'b'), (2, 'a')]
print(sorted(pairs, key=lambda p: p[1]))
```

### map/filter

- **Definition:** Functional transforms.
- **Visual explanation:** `map/filter` → process → result
- **Practical example:**

```python
print(list(map(lambda x: x * 2, [1, 2, 3])))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Lambdas are expressions that create function objects. |
| ⚡ Purpose | Inline tiny functions at point of use. |
| 🔥 Benefits | Concise sort keys, quick transforms. |
| 🎯 Use Cases | Sorting records, simple predicates, callback slots. |
| 🚀 Best Practices | Use def for multi-line or complex logic; add types at boundaries. |
| ❌ Common Mistakes | Over nesting lambdas, side effects inside, unreadable one-liners. |

## Syntax Guide

### Basic Syntax

```python
square = lambda n: n * n
print(square(5))
```

### Standard Structure

```python
lambda params: expr -> pass to higher-order func
```

### Code Pattern

```python
sorted(items, key=lambda x: x['score'], reverse=True)
```

## Examples

### Beginner Example

```python
nums = [1, 2, 3]
print(list(map(lambda x: x ** 2, nums)))
```

### Intermediate Example

```python
employees = [{'name': 'Ada', 'age': 36}, {'name': 'Lin', 'age': 30}]
print(sorted(employees, key=lambda e: e['age']))
```

### Advanced Example

```python
from functools import reduce

print(reduce(lambda acc, x: acc + x, [1, 2, 3, 4], 0))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Lambda] --> B[Higher-Order Func]
    B --> C[Result]
```

---

# Modules

## Overview

- **What is it?** Modules are Python files that group related code and expose a namespace.
- **Why is it important?** Modules organize code, enable reuse, and control what is public.
- **Where is it used?** Standard library, internal packages, shared utilities.

## Learning Objectives

- **Skills gained:** Practical command of Modules.
- **Concepts covered:**

- Import modules and names correctly.
- Understand __name__ and __main__.
- Structure module-level code.

- **Expected outcome:** You split programs into importable modules cleanly.

## Real World Applications

- Monoliths
- Shared libs
- Notebooks
- Microservices

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### import

- **Definition:** Load module namespace.
- **Visual explanation:** `import` → process → result
- **Practical example:**

```python
import math
print(math.sqrt(9))
```

### from import

- **Definition:** Bind specific names.
- **Visual explanation:** `from import` → process → result
- **Practical example:**

```python
from math import pi
print(round(pi, 2))
```

### __name__

- **Definition:** Tells if module is run or imported.
- **Visual explanation:** `__name__` → process → result
- **Practical example:**

```python
print(__name__)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Modules are the unit of reuse in Python. |
| ⚡ Purpose | Encapsulate related functions, classes, constants. |
| 🔥 Benefits | Namespace control, testability, lazy loading. |
| 🎯 Use Cases | Utils, models, clients, constants. |
| 🚀 Best Practices | Explicit __all__; guard main with if __name__. |
| ❌ Common Mistakes | Circular imports, star imports, heavy work at import time. |

## Syntax Guide

### Basic Syntax

```python
import json
print(json.dumps({'a': 1}))
```

### Standard Structure

```python
imports -> constants -> defs -> main guard
```

### Code Pattern

```python
if __name__ == '__main__':
    main()
```

## Examples

### Beginner Example

```python
import datetime
print(datetime.date.today())
```

### Intermediate Example

```python
import importlib.util
spec = importlib.util.find_spec('pathlib')
print(spec is not None)
```

### Advanced Example

```python
import importlib
math = importlib.import_module('math')
print(math.hypot(3, 4))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[module.py] --> B[import]
    B --> C[Namespace]
```

---

# Packages

## Overview

- **What is it?** Packages are directories of modules with an __init__.py (or namespace package).
- **Why is it important?** Packages scale codebases beyond single files and define public APIs.
- **Where is it used?** Libraries, services, frameworks, internal platforms.

## Learning Objectives

- **Skills gained:** Practical command of Packages.
- **Concepts covered:**

- Create package layout with submodules.
- Import from packages correctly.
- Expose stable __all__ or submodules.

- **Expected outcome:** You organize multi-module projects into installable packages.

## Real World Applications

- PyPI libraries
- Enterprise apps
- ML repos
- Platform SDKs

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Package dir

- **Definition:** Folder with __init__.py.
- **Visual explanation:** `Package dir` → process → result
- **Practical example:**

```python
from pathlib import Path
print(Path('snippet_parts/_helpers.py').exists())
```

### Relative import

- **Definition:** Import within package.
- **Visual explanation:** `Relative import` → process → result
- **Practical example:**

```python
from snippet_parts._helpers import S
print(callable(S))
```

### __init__

- **Definition:** Runs when package imported.
- **Visual explanation:** `__init__` → process → result
- **Practical example:**

```python
import snippet_parts
print(snippet_parts.__file__)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Packages group modules under a shared name. |
| ⚡ Purpose | Scale structure and distribution. |
| 🔥 Benefits | Clear boundaries, versioning, reuse. |
| 🎯 Use Cases | Web apps, SDKs, data platforms. |
| 🚀 Best Practices | Flat is better than nested; document public API. |
| ❌ Common Mistakes | Deep circular imports, bloated __init__, missing pyproject. |

## Syntax Guide

### Basic Syntax

```python
from snippet_parts._helpers import S
```

### Standard Structure

```python
package/ -> submodules -> __init__ exports
```

### Code Pattern

```python
from mypkg.services import billing
```

## Examples

### Beginner Example

```python
import snippet_parts
print(snippet_parts.__name__)
```

### Intermediate Example

```python
import pkgutil
print(any(m.name == '_helpers' for m in pkgutil.iter_modules(['snippet_parts'])))
```

### Advanced Example

```python
import importlib.metadata as md
print(md.version('pip'))
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Package] --> B[Submodule]
    B --> C[Public API]
```

---

# Date and Time

## Overview

- **What is it?** Python's datetime module models dates, times, timestamps, and timedeltas.
- **Why is it important?** Scheduling, logging, billing, and analytics require correct temporal logic.
- **Where is it used?** Cron jobs, audit trails, SLAs, reporting windows.

## Learning Objectives

- **Skills gained:** Practical command of Date and Time.
- **Concepts covered:**

- Create datetime and timedelta objects.
- Format and parse ISO timestamps.
- Handle time zones with zoneinfo.

- **Expected outcome:** You perform reliable date/time calculations and formatting.

## Real World Applications

- Fintech settlement
- SaaS billing
- Log aggregation
- Travel booking

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### datetime

- **Definition:** Calendar date and clock time.
- **Visual explanation:** `datetime` → process → result
- **Practical example:**

```python
from datetime import datetime
print(datetime(2026, 6, 6).isoformat())
```

### timedelta

- **Definition:** Differences and durations.
- **Visual explanation:** `timedelta` → process → result
- **Practical example:**

```python
from datetime import timedelta
print(timedelta(days=7).days)
```

### timezone

- **Definition:** Aware UTC timestamps.
- **Visual explanation:** `timezone` → process → result
- **Practical example:**

```python
from datetime import datetime, timezone
print(datetime.now(timezone.utc).year)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Use aware datetimes for distributed systems. |
| ⚡ Purpose | Measure, compare, and display time correctly. |
| 🔥 Benefits | Standard library support, ISO interoperability. |
| 🎯 Use Cases | Token expiry, report ranges, retry backoff. |
| 🚀 Best Practices | Store UTC; convert at display; use zoneinfo. |
| ❌ Common Mistakes | Naive vs aware mixing, DST bugs, parsing locale dates loosely. |

## Syntax Guide

### Basic Syntax

```python
from datetime import date
print(date.today())
```

### Standard Structure

```python
parse -> normalize TZ -> compute -> format
```

### Code Pattern

```python
deadline = start + timedelta(hours=24)
```

## Examples

### Beginner Example

```python
from datetime import datetime
print(datetime.now().year)
```

### Intermediate Example

```python
from datetime import datetime, timedelta
start = datetime(2026, 1, 1)
print((start + timedelta(days=30)).date())
```

### Advanced Example

```python
from datetime import datetime
from zoneinfo import ZoneInfo

utc = datetime(2026, 6, 6, 12, tzinfo=ZoneInfo('UTC'))
print(utc.astimezone(ZoneInfo('America/New_York')).hour)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Parse Time] --> B[UTC Store]
    B --> C[Compute]
    C --> D[Display TZ]
```

---

# Math Module

## Overview

- **What is it?** The math module provides standard mathematical functions and constants.
- **Why is it important?** It supplements built-in operators with trig, logs, rounding, and constants.
- **Where is it used?** Graphics, statistics, engineering, games, ML feature prep.

## Learning Objectives

- **Skills gained:** Practical command of Math Module.
- **Concepts covered:**

- Import and use math functions.
- Apply ceil, floor, sqrt, log.
- Know math vs numpy boundaries.

- **Expected outcome:** You perform common numeric operations with the math module.

## Real World Applications

- Simulation
- CAD tooling
- Quant finance
- Robotics

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Constants

- **Definition:** pi and e.
- **Visual explanation:** `Constants` → process → result
- **Practical example:**

```python
import math
print(round(math.pi, 3))
```

### sqrt/log

- **Definition:** Roots and logarithms.
- **Visual explanation:** `sqrt/log` → process → result
- **Practical example:**

```python
import math
print(math.sqrt(16), math.log2(8))
```

### hypot

- **Definition:** Distance calculations.
- **Visual explanation:** `hypot` → process → result
- **Practical example:**

```python
import math
print(math.hypot(3, 4))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | math operates on scalars (not vectorized). |
| ⚡ Purpose | Accurate numeric primitives for algorithms. |
| 🔥 Benefits | Fast, standard, no extra dependency. |
| 🎯 Use Cases | Distance metrics, probability, geometry. |
| 🚀 Best Practices | Use math.isclose for floats; prefer decimal for money. |
| ❌ Common Mistakes | Using math on lists, domain errors on log/sqrt, float equality. |

## Syntax Guide

### Basic Syntax

```python
import math
print(math.pow(2, 3))
```

### Standard Structure

```python
import math -> compute scalar -> combine
```

### Code Pattern

```python
hyp = math.hypot(dx, dy)
```

## Examples

### Beginner Example

```python
import math
print(math.ceil(4.2))
```

### Intermediate Example

```python
import math
angles = [0, math.pi/2]
print([math.sin(a) for a in angles])
```

### Advanced Example

```python
import math

def sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x))


print(round(sigmoid(0), 4))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Scalars] --> B[math func]
    B --> C[Result]
```

---

# Random Module

## Overview

- **What is it?** The random module generates pseudo-random numbers and samples for simulations.
- **Why is it important?** Games, sampling, shuffling, and Monte Carlo methods need controlled randomness.
- **Where is it used?** A/B tests, load balancing, procedural content, QA fuzzing.

## Learning Objectives

- **Skills gained:** Practical command of Random Module.
- **Concepts covered:**

- Use random, randint, choice, shuffle.
- Seed RNG for reproducibility.
- Choose secrets vs random correctly.

- **Expected outcome:** You generate randomness safely for simulations and sampling.

## Real World Applications

- Gaming
- ML data splits
- Security training
- Load testing

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### randint

- **Definition:** Random integer in range.
- **Visual explanation:** `randint` → process → result
- **Practical example:**

```python
import random
print(random.randint(1, 6))
```

### choice

- **Definition:** Pick random element.
- **Visual explanation:** `choice` → process → result
- **Practical example:**

```python
import random
print(random.choice(['red', 'blue']))
```

### seed

- **Definition:** Reproducible sequences.
- **Visual explanation:** `seed` → process → result
- **Practical example:**

```python
import random
random.seed(0)
print(random.random())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | random is deterministic given a seed. |
| ⚡ Purpose | Simulate uncertainty and shuffle data. |
| 🔥 Benefits | Simple API, reproducible tests with seed. |
| 🎯 Use Cases | Dice rolls, train/test split, lottery draws. |
| 🚀 Best Practices | Use secrets module for crypto; seed in tests only. |
| ❌ Common Mistakes | Using random for passwords, biased sampling, forgetting seed in tests. |

## Syntax Guide

### Basic Syntax

```python
import random
print(random.random())
```

### Standard Structure

```python
seed (optional) -> draw -> use
```

### Code Pattern

```python
sample = random.sample(population, k=3)
```

## Examples

### Beginner Example

```python
import random
print(random.choice(['A', 'B', 'C']))
```

### Intermediate Example

```python
import random
items = [1, 2, 3, 4]
random.shuffle(items)
print(items)
```

### Advanced Example

```python
import random

def bootstrap(data: list[float], n: int) -> list[float]:
    return [random.choice(data) for _ in range(n)]


print(bootstrap([1.0, 2.0, 3.0], 5))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Seed] --> B[RNG]
    B --> C[Sample]
```

---

# File Handling

## Overview

- **What is it?** File handling reads and writes persistent data using paths and file objects.
- **Why is it important?** Programs must load configs, export reports, and process uploads.
- **Where is it used?** ETL, logging, document pipelines, local tools.

## Learning Objectives

- **Skills gained:** Practical command of File Handling.
- **Concepts covered:**

- Open files with context managers.
- Read/write text and binary safely.
- Use pathlib for paths.

- **Expected outcome:** You read and write files reliably with proper encoding and cleanup.

## Real World Applications

- Reporting
- Media processing
- Backup tools
- Compliance archives

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### open

- **Definition:** Returns file object.
- **Visual explanation:** `open` → process → result
- **Practical example:**

```python
from io import StringIO
f = StringIO('hi')
print(f.read())
```

### with

- **Definition:** Ensures files close.
- **Visual explanation:** `with` → process → result
- **Practical example:**

```python
from tempfile import NamedTemporaryFile
with NamedTemporaryFile('w+', delete=False) as tmp:
    tmp.write('data')
    name = tmp.name
print(name.endswith('tmp') or len(name) > 0)
```

### pathlib

- **Definition:** OO paths.
- **Visual explanation:** `pathlib` → process → result
- **Practical example:**

```python
from pathlib import Path
p = Path('README.md')
print(p.suffix)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Files are streams; paths are pathlib.Path objects. |
| ⚡ Purpose | Persist and exchange data on disk. |
| 🔥 Benefits | Context managers, pathlib clarity, binary support. |
| 🎯 Use Cases | Config load, CSV export, image bytes, log rotation. |
| 🚀 Best Practices | Specify encoding=utf-8; use Path; handle missing files. |
| ❌ Common Mistakes | Forgetting close, wrong newline mode, loading huge files fully. |

## Syntax Guide

### Basic Syntax

```python
from pathlib import Path
print(Path('.').resolve())
```

### Standard Structure

```python
open path -> read/write -> atomic replace optional
```

### Code Pattern

```python
text = Path('file.txt').read_text(encoding='utf-8')
```

## Examples

### Beginner Example

```python
from pathlib import Path
p = Path('README.md')
print(p.exists())
```

### Intermediate Example

```python
from pathlib import Path
lines = Path('README.md').read_text(encoding='utf-8').splitlines()
print(len(lines))
```

### Advanced Example

```python
from pathlib import Path

def write_atomic(path: Path, content: str) -> None:
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(content, encoding='utf-8')
    tmp.replace(path)


p = Path('demo_out.txt')
write_atomic(p, 'hello')
print(p.read_text(encoding='utf-8'))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Path] --> B[Open]
    B --> C[Read/Write]
    C --> D[Close]
```

---

# Exception Handling

## Overview

- **What is it?** Exception handling manages errors with try, except, else, and finally.
- **Why is it important?** Robust programs recover from failures and preserve resources.
- **Where is it used?** Network I/O, parsing, databases, user input.

## Learning Objectives

- **Skills gained:** Practical command of Exception Handling.
- **Concepts covered:**

- Catch specific exceptions.
- Raise meaningful errors.
- Use finally for cleanup.

- **Expected outcome:** You write fault-tolerant code with clear error paths.

## Real World Applications

- Payment processing
- API gateways
- Data ingestion
- Desktop apps

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### try/except

- **Definition:** Handle expected failures.
- **Visual explanation:** `try/except` → process → result
- **Practical example:**

```python
try:
    int('x')
except ValueError as e:
    print(type(e).__name__)
```

### raise

- **Definition:** Signal errors upstream.
- **Visual explanation:** `raise` → process → result
- **Practical example:**

```python
def require_positive(n):
    if n <= 0:
        raise ValueError('must be positive')
require_positive(1)
```

### finally

- **Definition:** Always-run cleanup.
- **Visual explanation:** `finally` → process → result
- **Practical example:**

```python
f = None
try:
    f = open(__file__)
    data = f.read(10)
finally:
    if f:
        f.close()
print(len(data))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Exceptions unwind the stack until a matching handler runs. |
| ⚡ Purpose | Separate happy path from error recovery. |
| 🔥 Benefits | Resource safety, clearer control flow, rich tracebacks. |
| 🎯 Use Cases | Retry wrappers, validation, transaction rollback. |
| 🚀 Best Practices | Catch specific types; chain exceptions; log context. |
| ❌ Common Mistakes | Bare except, swallowing errors, using exceptions for flow control. |

## Syntax Guide

### Basic Syntax

```python
try:
    risky()
except Exception:
    handle()
```

### Standard Structure

```python
try -> except specific -> else -> finally
```

### Code Pattern

```python
try:
    return parse(data)
except ParseError:
    return default
```

## Examples

### Beginner Example

```python
try:
    print(1 / 0)
except ZeroDivisionError:
    print('cannot divide by zero')
```

### Intermediate Example

```python
class AppError(Exception):
    pass


def load(value: str) -> int:
    try:
        return int(value)
    except ValueError as exc:
        raise AppError('bad input') from exc


print(load('10'))
```

### Advanced Example

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    open('missing.txt').read()
print('continued')
```

## Workflow Diagram

```mermaid
flowchart TD
    A[try] --> B{Error?}
    B -->|yes| C[except]
    B -->|no| D[else]
    C --> E[finally]
    D --> E
```

---

# Debugging Basics

## Overview

- **What is it?** Debugging basics include reading tracebacks, using print/logging, and breakpoints.
- **Why is it important?** Finding root cause quickly saves hours in development and incidents.
- **Where is it used?** Local dev, staging reproduction, postmortems.

## Learning Objectives

- **Skills gained:** Practical command of Debugging Basics.
- **Concepts covered:**

- Read stack traces bottom-up.
- Use pdb/breakpoint().
- Form hypotheses and isolate bugs.

- **Expected outcome:** You systematically narrow down and fix defects.

## Real World Applications

- SRE
- QA automation
- Game dev
- Enterprise apps

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Traceback

- **Definition:** Shows call stack at error.
- **Visual explanation:** `Traceback` → process → result
- **Practical example:**

```python
import traceback
try:
    1/0
except ZeroDivisionError:
    traceback.print_exc()
```

### breakpoint

- **Definition:** Interactive debugger entry.
- **Visual explanation:** `breakpoint` → process → result
- **Practical example:**

```python
x = 1
x += 1
print(x)
```

### logging

- **Definition:** Better than print in prod.
- **Visual explanation:** `logging` → process → result
- **Practical example:**

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info('check')
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Debug loop: reproduce -> isolate -> fix -> verify. |
| ⚡ Purpose | Restore correct program behavior. |
| 🔥 Benefits | Faster fixes, fewer regressions, shared techniques. |
| 🎯 Use Cases | Failing tests, prod incidents, flaky jobs. |
| 🚀 Best Practices | Minimal repro, binary search commits, watch variables. |
| ❌ Common Mistakes | Random changes, ignoring traceback, debugging without tests. |

## Syntax Guide

### Basic Syntax

```python
import logging
logging.debug('state=%s', value)
```

### Standard Structure

```python
reproduce -> inspect -> hypothesize -> fix -> test
```

### Code Pattern

```python
assert expected == actual, (expected, actual)
```

## Examples

### Beginner Example

```python
def add(a, b):
    return a + b
assert add(2, 3) == 5
```

### Intermediate Example

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')


print(divide(1, 0))
```

### Advanced Example

```python
import logging

logger = logging.getLogger(__name__)


def compute(values):
    logger.debug('inputs=%r', values)
    return sum(values)


print(compute([1, 2, 3]))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Bug Report] --> B[Repro]
    B --> C[Inspect]
    C --> D[Fix]
    D --> E[Test]
```

---

# Virtual Environments

## Overview

- **What is it?** Virtual environments isolate project dependencies from the system Python.
- **Why is it important?** Isolation prevents version conflicts and makes projects reproducible.
- **Where is it used?** Every professional Python project locally and in CI.

## Learning Objectives

- **Skills gained:** Practical command of Virtual Environments.
- **Concepts covered:**

- Create and activate venv.
- Install packages into venv only.
- Export requirements or lockfiles.

- **Expected outcome:** You manage per-project dependencies safely.

## Real World Applications

- Web teams
- ML labs
- CI pipelines
- Consulting deliverables

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### venv module

- **Definition:** Creates env directory.
- **Visual explanation:** `venv module` → process → result
- **Practical example:**

```python
import venv
print(hasattr(venv, 'EnvBuilder'))
```

### pip in venv

- **Definition:** Installs into env site-packages.
- **Visual explanation:** `pip in venv` → process → result
- **Practical example:**

```python
import site
print(len(site.getsitepackages()) >= 1)
```

### requirements.txt

- **Definition:** Pinned dependency list.
- **Visual explanation:** `requirements.txt` → process → result
- **Practical example:**

```python
from pathlib import Path
print(Path('README.md').exists())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Each venv has its own interpreter symlink and site-packages. |
| ⚡ Purpose | Reproducible dependency graphs per project. |
| 🔥 Benefits | No global pollution, easier onboarding, safer upgrades. |
| 🎯 Use Cases | App dev, notebooks, test matrices. |
| 🚀 Best Practices | Commit requirements; never pip install globally; use python -m pip. |
| ❌ Common Mistakes | Forgetting activate, mixing conda/pip blindly, no pin files. |

## Syntax Guide

### Basic Syntax

```python
import sys
print(sys.prefix)
```

### Standard Structure

```python
python -m venv -> activate -> pip install -r requirements
```

### Code Pattern

```python
import sys
print('venv active' if sys.prefix != sys.base_prefix else 'system')
```

## Examples

### Beginner Example

```python
import sys
print(sys.prefix != sys.base_prefix)
```

### Intermediate Example

```python
import sys
print('executable:', sys.executable)
print('prefix:', sys.prefix)
```

### Advanced Example

```python
import subprocess
import sys

cmd = [sys.executable, '-m', 'pip', 'list', '--format=freeze']
out = subprocess.run(cmd, capture_output=True, text=True, check=True)
print(len(out.stdout.splitlines()))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Project] --> B[venv]
    B --> C[pip install]
    C --> D[Isolated deps]
```

---

# Basic Project Structure

## Overview

- **What is it?** Basic project structure organizes source, tests, config, and docs for maintainability.
- **Why is it important?** Consistent layout helps teams navigate, test, and package code.
- **Where is it used?** Every repo from tutorials to production services.

## Learning Objectives

- **Skills gained:** Practical command of Basic Project Structure.
- **Concepts covered:**

- Lay out src/ or package root with tests.
- Add README, requirements, and .gitignore.
- Use pyproject.toml for modern tooling.

- **Expected outcome:** You bootstrap Python projects that scale beyond one file.

## Real World Applications

- Open source
- Agencies
- Product engineering
- Research labs

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### src layout

- **Definition:** Package under src/ avoids import confusion.
- **Visual explanation:** `src layout` → process → result
- **Practical example:**

```python
from pathlib import Path
print(Path('scripts').is_dir())
```

### tests/

- **Definition:** Automated verification.
- **Visual explanation:** `tests/` → process → result
- **Practical example:**

```python
import pathlib
print(pathlib.Path('scripts').exists())
```

### pyproject.toml

- **Definition:** Project metadata and tools.
- **Visual explanation:** `pyproject.toml` → process → result
- **Practical example:**

```python
print('pyproject'[:3])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Structure communicates boundaries and entry points. |
| ⚡ Purpose | Enable testing, packaging, and collaboration. |
| 🔥 Benefits | Onboarding speed, CI clarity, fewer import hacks. |
| 🎯 Use Cases | CLI tools, libraries, microservices. |
| 🚀 Best Practices | One obvious README; Makefile/task runner optional; pin Python version. |
| ❌ Common Mistakes | Flat script pile, tests not runnable, secrets in repo. |

## Syntax Guide

### Basic Syntax

```python
from pathlib import Path
print(list(Path('.').glob('scripts/*.py'))[:1])
```

### Standard Structure

```python
README + pyproject + package + tests + scripts
```

### Code Pattern

```python
layout = {'src': 'pkg', 'tests': 'tests', 'config': 'pyproject.toml'}
print(layout['src'])
```

## Examples

### Beginner Example

```python
from pathlib import Path
print([p.name for p in Path('scripts').glob('*.py')][:3])
```

### Intermediate Example

```python
from pathlib import Path
root = Path('.')
print('has scripts:', (root / 'scripts').exists())
print('has README:', (root / 'README.md').exists())
```

### Advanced Example

```python
from pathlib import Path

def tree(path: Path, prefix: str = '') -> None:
    entries = sorted(path.iterdir(), key=lambda p: p.name)
    for entry in entries[:5]:
        print(prefix + entry.name)


tree(Path('scripts'))
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Repo Root] --> B[src/package]
    A --> C[tests]
    A --> D[pyproject.toml]
    A --> E[README]
```

---

## Level 2: Intermediate

# Object Oriented Programming

## Overview

- **What is it?** OOP organizes code around objects that combine data and behavior.
- **Why is it important?** It models real-world entities and scales large codebases.
- **Where is it used?** Web frameworks, game engines, enterprise apps, SDK design.

## Learning Objectives

- **Skills gained:** Practical command of Object Oriented Programming.
- **Concepts covered:**

- Design classes and objects.
- Apply encapsulation, inheritance, polymorphism.
- Choose OOP vs functional patterns.

- **Expected outcome:** You design maintainable class hierarchies.

## Real World Applications

- Django models
- Fintech domains
- Simulation software
- Game engines

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Class

- **Definition:** Blueprint for objects.
- **Visual explanation:** `Class` → process → result
- **Practical example:**

```python
class User:
    pass
print(User)
```

### Object

- **Definition:** Instance of a class.
- **Visual explanation:** `Object` → process → result
- **Practical example:**

```python
class Box:
    pass
b = Box()
print(type(b).__name__)
```

### Method

- **Definition:** Function bound to an object.
- **Visual explanation:** `Method` → process → result
- **Practical example:**

```python
class Greeter:
    def hi(self):
        return 'hello'
print(Greeter().hi())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Objects bundle state and behavior. |
| ⚡ Purpose | Structure complex domains clearly. |
| 🔥 Benefits | Reuse, abstraction, team scalability. |
| 🎯 Use Cases | ORM models, payment systems, inventory systems. |
| 🚀 Best Practices | Composition over inheritance, small public APIs. |
| ❌ Common Mistakes | God classes, deep inheritance trees, anemic models. |

## Syntax Guide

### Basic Syntax

```python
class Dog:
    def bark(self):
        return 'woof'
```

### Standard Structure

```python
class -> instantiate -> call methods
```

### Code Pattern

```python
class Service:
    def run(self):
        return self.execute()
```

## Examples

### Beginner Example

```python
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


print(Rectangle(4, 5).area())
```

### Intermediate Example

```python
from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        raise NotImplementedError


class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"EMAIL: {message}")


EmailNotifier().send('hi')
```

### Advanced Example

```python
class ValidatedModel:
    def __setattr__(self, name, value):
        if name.startswith('_'):
            return super().__setattr__(name, value)
        if name == 'age' and value < 0:
            raise ValueError('age must be non-negative')
        super().__setattr__(name, value)


obj = ValidatedModel()
obj.age = 30
print(obj.age)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Class] --> B[Constructor]
    B --> C[Object]
    C --> D[Methods]
```

---

# Classes

## Overview

- **What is it?** Classes define attributes and methods shared by all instances of a type.
- **Why is it important?** They encapsulate data and behavior for a cohesive abstraction.
- **Where is it used?** Domain models, widgets, service clients, test doubles.

## Learning Objectives

- **Skills gained:** Practical command of Classes.
- **Concepts covered:**

- Declare class attributes and methods.
- Use @classmethod and @staticmethod.
- Document public interface.

- **Expected outcome:** You implement classes that represent domain concepts clearly.

## Real World Applications

- ORM entities
- UI components
- Robotics control
- Billing

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### class statement

- **Definition:** Creates a type object.
- **Visual explanation:** `class statement` → process → result
- **Practical example:**

```python
class Point:
    x = 0
print(Point.x)
```

### instance attrs

- **Definition:** Per-object state via self.
- **Visual explanation:** `instance attrs` → process → result
- **Practical example:**

```python
class Counter:
    def __init__(self):
        self.n = 0
print(Counter().n)
```

### methods

- **Definition:** Functions receiving self.
- **Visual explanation:** `methods` → process → result
- **Practical example:**

```python
class Calc:
    def add(self, a, b):
        return a + b
print(Calc().add(2, 3))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Classes are factories for objects with shared behavior. |
| ⚡ Purpose | Define reusable types with state and operations. |
| 🔥 Benefits | Encapsulation, polymorphism, IDE support. |
| 🎯 Use Cases | Users, orders, sensors, handlers. |
| 🚀 Best Practices | Keep classes focused; prefer dataclasses for data containers. |
| ❌ Common Mistakes | Too many responsibilities, public mutable everything. |

## Syntax Guide

### Basic Syntax

```python
class Account:
    def __init__(self, owner):
        self.owner = owner
```

### Standard Structure

```python
attrs -> __init__ -> methods -> repr/str optional
```

### Code Pattern

```python
class Model:
    def validate(self):
        return True
```

## Examples

### Beginner Example

```python
class Person:
    def __init__(self, name):
        self.name = name
print(Person('Ada').name)
```

### Intermediate Example

```python
class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32


print(Temperature(100).fahrenheit)
```

### Advanced Example

```python
from dataclasses import dataclass, field


@dataclass
class Cart:
    items: list[str] = field(default_factory=list)

    def add(self, sku: str) -> None:
        self.items.append(sku)


c = Cart()
c.add('ABC')
print(c.items)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[class] --> B[__init__]
    B --> C[instance]
```

---

# Objects

## Overview

- **What is it?** Objects are instances of classes with their own attribute values.
- **Why is it important?** Runtime entities carry state that differs per instance.
- **Where is it used?** Every OOP system—UI nodes, DB rows, device handles.

## Learning Objectives

- **Skills gained:** Practical command of Objects.
- **Concepts covered:**

- Instantiate classes.
- Access and mutate instance state.
- Compare identity vs equality.

- **Expected outcome:** You create and interact with objects confidently.

## Real World Applications

- CRM records
- IoT devices
- Game entities
- API resources

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Instantiation

- **Definition:** Call class to create object.
- **Visual explanation:** `Instantiation` → process → result
- **Practical example:**

```python
class Node:
    pass
n = Node()
print(isinstance(n, Node))
```

### self

- **Definition:** Reference to current instance.
- **Visual explanation:** `self` → process → result
- **Practical example:**

```python
class A:
    def id(self):
        return id(self)
print(A().id())
```

### identity

- **Definition:** is checks same object.
- **Visual explanation:** `identity` → process → result
- **Practical example:**

```python
a = []
b = a
print(a is b)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Objects are class instances with unique state. |
| ⚡ Purpose | Represent individual entities at runtime. |
| 🔥 Benefits | Natural modeling, mutable state when needed. |
| 🎯 Use Cases | Shopping cart line items, connected users. |
| 🚀 Best Practices | Validate invariants in __init__; use properties. |
| ❌ Common Mistakes | Shared mutable class attrs, confusing is vs ==. |

## Syntax Guide

### Basic Syntax

```python
obj = MyClass()
obj.value = 1
```

### Standard Structure

```python
construct -> configure -> invoke methods
```

### Code Pattern

```python
user = User(name='Ada')
user.activate()
```

## Examples

### Beginner Example

```python
class Book:
    def __init__(self, title):
        self.title = title
print(Book('Python').title)
```

### Intermediate Example

```python
class Wallet:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount


w = Wallet()
w.deposit(10)
print(w.balance)
```

### Advanced Example

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


print(Singleton() is Singleton())
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Class()] --> B[Object State]
    B --> C[Methods]
```

---

# Constructors

## Overview

- **What is it?** Constructors initialize new objects, primarily via __init__ in Python.
- **Why is it important?** Proper initialization enforces invariants and required dependencies.
- **Where is it used?** Models, clients, widgets, connection wrappers.

## Learning Objectives

- **Skills gained:** Practical command of Constructors.
- **Concepts covered:**

- Implement __init__ with parameters.
- Use default and keyword-only args.
- Avoid heavy work in __init__ when possible.

- **Expected outcome:** You build objects that start in valid, predictable states.

## Real World Applications

- ORM models
- SDK clients
- Hardware drivers
- UI widgets

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### __init__

- **Definition:** Sets up instance after creation.
- **Visual explanation:** `__init__` → process → result
- **Practical example:**

```python
class Item:
    def __init__(self, sku):
        self.sku = sku
print(Item('A1').sku)
```

### __new__

- **Definition:** Creates instance before __init__.
- **Visual explanation:** `__new__` → process → result
- **Practical example:**

```python
class T:
    def __new__(cls):
        return super().__new__(cls)
print(T())
```

### post-init

- **Definition:** dataclass __post_init__ hook.
- **Visual explanation:** `post-init` → process → result
- **Practical example:**

```python
from dataclasses import dataclass
@dataclass
class R:
    w: int
    h: int
    area: int = 0
    def __post_init__(self):
        self.area = self.w * self.h
print(R(3,4).area)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | __init__ configures self; __new__ allocates the instance. |
| ⚡ Purpose | Guarantee valid starting state. |
| 🔥 Benefits | Fewer invalid objects, clearer APIs. |
| 🎯 Use Cases | DB models, API tokens, config objects. |
| 🚀 Best Practices | Keep __init__ cheap; inject dependencies; validate early. |
| ❌ Common Mistakes | I/O in __init__, too many params, subclass __init__ bugs. |

## Syntax Guide

### Basic Syntax

```python
class User:
    def __init__(self, email):
        self.email = email
```

### Standard Structure

```python
__new__ (rare) -> __init__ -> ready object
```

### Code Pattern

```python
def __init__(self, repo):
    self.repo = repo
```

## Examples

### Beginner Example

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
print(Point(1, 2).x)
```

### Intermediate Example

```python
class Connection:
    def __init__(self, dsn: str, *, timeout: int = 30):
        self.dsn = dsn
        self.timeout = timeout


print(Connection('sqlite://', timeout=10).timeout)
```

### Advanced Example

```python
class Buffer:
    def __init__(self, data: bytes):
        if not data:
            raise ValueError('empty buffer')
        self._data = data

    @property
    def size(self) -> int:
        return len(self._data)


print(Buffer(b'abc').size)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Call Class] --> B[__new__]
    B --> C[__init__]
    C --> D[Ready Object]
```

---

# Encapsulation

## Overview

- **What is it?** Encapsulation hides internal state and exposes a controlled public interface.
- **Why is it important?** It protects invariants and reduces coupling between components.
- **Where is it used?** Libraries, domain models, API clients, device drivers.

## Learning Objectives

- **Skills gained:** Practical command of Encapsulation.
- **Concepts covered:**

- Use private-by-convention _attrs.
- Expose @property for controlled access.
- Design minimal public methods.

- **Expected outcome:** You prevent accidental misuse of internal object state.

## Real World Applications

- Payment vaults
- Medical records
- Embedded firmware APIs
- SaaS SDKs

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Name mangling

- **Definition:** Double underscore alters name.
- **Visual explanation:** `Name mangling` → process → result
- **Practical example:**

```python
class A:
    def __init__(self):
        self.__secret = 1
    def get(self):
        return self.__secret
print(A().get())
```

### property

- **Definition:** Getter/setter as attribute.
- **Visual explanation:** `property` → process → result
- **Practical example:**

```python
class Circle:
    def __init__(self, r):
        self.radius = r
    @property
    def diameter(self):
        return self.radius * 2
print(Circle(3).diameter)
```

### Public API

- **Definition:** Document supported methods.
- **Visual explanation:** `Public API` → process → result
- **Practical example:**

```python
class Service:
    def run(self):
        return self._execute()
    def _execute(self):
        return 'ok'
print(Service().run())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Encapsulation separates interface from implementation. |
| ⚡ Purpose | Protect data integrity and enable refactoring. |
| 🔥 Benefits | Safer changes, clearer contracts, fewer bugs. |
| 🎯 Use Cases | Bank accounts, validated configs, cached clients. |
| 🚀 Best Practices | Properties over getters; don't over-mangle; be consistent. |
| ❌ Common Mistakes | Everything public, leaky abstractions, property side effects. |

## Syntax Guide

### Basic Syntax

```python
class Account:
    def __init__(self):
        self._balance = 0.0
```

### Standard Structure

```python
private state -> properties -> public methods
```

### Code Pattern

```python
value = obj.value  # property-backed access
```

## Examples

### Beginner Example

```python
class Counter:
    def __init__(self):
        self._n = 0
    def inc(self):
        self._n += 1
    def value(self):
        return self._n
c = Counter(); c.inc(); print(c.value())
```

### Intermediate Example

```python
class Email:
    def __init__(self, address: str):
        self.address = address.lower()

    @property
    def domain(self) -> str:
        return self.address.split('@', 1)[1]


print(Email('Ada@Example.com').domain)
```

### Advanced Example

```python
class RateLimiter:
    def __init__(self, limit: int):
        self._limit = limit
        self._count = 0

    def allow(self) -> bool:
        if self._count >= self._limit:
            return False
        self._count += 1
        return True


rl = RateLimiter(2)
print(rl.allow(), rl.allow(), rl.allow())
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Client] --> B[Public API]
    B --> C[Private State]
```

---

# Inheritance

## Overview

- **What is it?** Inheritance lets a subclass reuse and extend a base class.
- **Why is it important?** Shared behavior avoids duplication; specialization models subtypes.
- **Where is it used?** Framework hooks, UI kits, exception hierarchies, plugins.

## Learning Objectives

- **Skills gained:** Practical command of Inheritance.
- **Concepts covered:**

- Subclass and override methods.
- Call super() correctly.
- Prefer composition when reuse is shallow.

- **Expected outcome:** You extend existing classes without breaking Liskov expectations.

## Real World Applications

- Web frameworks
- Game engines
- Enterprise ERP
- Test fixtures

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Subclass

- **Definition:** class Child(Parent).
- **Visual explanation:** `Subclass` → process → result
- **Practical example:**

```python
class Animal:
    def speak(self):
        return 'sound'
class Dog(Animal):
    def speak(self):
        return 'woof'
print(Dog().speak())
```

### super()

- **Definition:** Delegate to parent implementation.
- **Visual explanation:** `super()` → process → result
- **Practical example:**

```python
class B:
    def val(self):
        return 1
class C(B):
    def val(self):
        return super().val() + 1
print(C().val())
```

### MRO

- **Definition:** Method resolution order.
- **Visual explanation:** `MRO` → process → result
- **Practical example:**

```python
class A:
    def f(self):
        return 'A'
class B(A):
    pass
print(B().f())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Inheritance is an is-a relationship between types. |
| ⚡ Purpose | Reuse and specialize behavior. |
| 🔥 Benefits | DRY, polymorphic collections, framework extension. |
| 🎯 Use Cases | Custom exceptions, model subclasses, auth backends. |
| 🚀 Best Practices | Shallow trees; override thoughtfully; document contracts. |
| ❌ Common Mistakes | Fragile base class, super misuse, deep hierarchies. |

## Syntax Guide

### Basic Syntax

```python
class Employee(Person):
    def role(self):
        return 'staff'
```

### Standard Structure

```python
base -> override -> super optional
```

### Code Pattern

```python
class Admin(User):
    def permissions(self):
        return super().permissions() | {'admin'}
```

## Examples

### Beginner Example

```python
class Bird:
    def move(self):
        return 'fly'
class Penguin(Bird):
    def move(self):
        return 'swim'
print(Penguin().move())
```

### Intermediate Example

```python
class Logger:
    def log(self, msg: str) -> None:
        print(msg)


class TimestampLogger(Logger):
    def log(self, msg: str) -> None:
        super().log(f'[ts] {msg}')


TimestampLogger().log('start')
```

### Advanced Example

```python
class Shape:
    def area(self) -> float:
        raise NotImplementedError


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2


print(Square(4).area())
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Base Class] --> B[Subclass]
    B --> C[Override Method]
```

---

# Polymorphism

## Overview

- **What is it?** Polymorphism lets different types respond to the same interface.
- **Why is it important?** Callers depend on behavior, not concrete classes.
- **Where is it used?** Duck typing, protocols, plugin systems, strategy pattern.

## Learning Objectives

- **Skills gained:** Practical command of Polymorphism.
- **Concepts covered:**

- Write code against shared interfaces.
- Use duck typing safely.
- Combine polymorphism with ABCs or Protocols.

- **Expected outcome:** You write flexible code that accepts multiple implementations.

## Real World Applications

- Payment providers
- Cloud storage drivers
- Notification channels
- ML backends

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Duck typing

- **Definition:** If it quacks, use it.
- **Visual explanation:** `Duck typing` → process → result
- **Practical example:**

```python
class Duck:
    def quack(self):
        return 'quack'
def speak(bird):
    return bird.quack()
print(speak(Duck()))
```

### Override

- **Definition:** Subclass provides own version.
- **Visual explanation:** `Override` → process → result
- **Practical example:**

```python
class A:
    def run(self):
        return 1
class B(A):
    def run(self):
        return 2
print(B().run())
```

### Protocol

- **Definition:** Structural typing.
- **Visual explanation:** `Protocol` → process → result
- **Practical example:**

```python
from typing import Protocol
class Runner(Protocol):
    def run(self) -> int: ...
class Job:
    def run(self) -> int:
        return 42
def start(r: Runner) -> int:
    return r.run()
print(start(Job()))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Polymorphism emphasizes behavior over concrete type. |
| ⚡ Purpose | Decouple callers from implementations. |
| 🔥 Benefits | Extensibility, testing with fakes, cleaner APIs. |
| 🎯 Use Cases | Strategies, serializers, renderers. |
| 🚀 Best Practices | Small interfaces; type hints with Protocol; test all impls. |
| ❌ Common Mistakes | isinstance chains everywhere, violating LSP, hidden requirements. |

## Syntax Guide

### Basic Syntax

```python
def render(doc):
    return doc.to_html()
```

### Standard Structure

```python
interface -> multiple impls -> caller uses interface
```

### Code Pattern

```python
for handler in handlers:
    handler.process(event)
```

## Examples

### Beginner Example

```python
class Cat:
    def sound(self):
        return 'meow'
class Dog:
    def sound(self):
        return 'woof'
print([C().sound() for C in (Cat, Dog)])
```

### Intermediate Example

```python
class JSONRenderer:
    def render(self, data: dict) -> str:
        import json
        return json.dumps(data)


class XMLRenderer:
    def render(self, data: dict) -> str:
        return '<root/>'


def export(renderer, payload):
    return renderer.render(payload)


print(export(JSONRenderer(), {'a': 1}))
```

### Advanced Example

```python
from typing import Protocol


class SupportsClose(Protocol):
    def close(self) -> None: ...


def cleanup(resource: SupportsClose) -> None:
    resource.close()


class FileLike:
    def close(self) -> None:
        print('closed')


cleanup(FileLike())
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Caller] --> B[Interface]
    B --> C[Impl A]
    B --> D[Impl B]
```

---

# Abstraction

## Overview

- **What is it?** Abstraction hides complexity behind simpler interfaces.
- **Why is it important?** Teams work at appropriate levels without knowing every detail.
- **Where is it used?** APIs, ORMs, cloud SDKs, hardware abstraction layers.

## Learning Objectives

- **Skills gained:** Practical command of Abstraction.
- **Concepts covered:**

- Define abstract base classes.
- Hide implementation details.
- Document contracts clearly.

- **Expected outcome:** You expose only what clients need while refactoring internals freely.

## Real World Applications

- Cloud SDKs
- Database layers
- GUI toolkits
- Compiler frontends

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### ABC

- **Definition:** Abstract base class enforces methods.
- **Visual explanation:** `ABC` → process → result
- **Practical example:**

```python
from abc import ABC, abstractmethod
class Repo(ABC):
    @abstractmethod
    def get(self, id: int): ...
class MemRepo(Repo):
    def get(self, id: int):
        return {'id': id}
print(MemRepo().get(1))
```

### Facade

- **Definition:** Simple wrapper over subsystems.
- **Visual explanation:** `Facade` → process → result
- **Practical example:**

```python
class Storage:
    def save(self, text: str) -> None:
        open('out.txt', 'w').write(text)
Storage().save('hi')
```

### Interface segregation

- **Definition:** Small focused interfaces.
- **Visual explanation:** `Interface segregation` → process → result
- **Practical example:**

```python
class Reader:
    def read(self):
        return 'data'
print(Reader().read())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Abstraction emphasizes what, not how. |
| ⚡ Purpose | Manage complexity and enable change. |
| 🔥 Benefits | Faster client dev, safer refactors, clearer modules. |
| 🎯 Use Cases | Payment gateway facade, storage adapter, ML pipeline stage. |
| 🚀 Best Practices | Stable public APIs; version breaking changes; tests on contracts. |
| ❌ Common Mistakes | Leaking internals, giant interfaces, abstract everything. |

## Syntax Guide

### Basic Syntax

```python
class API:
    def fetch(self):
        return self._request()
```

### Standard Structure

```python
public facade -> private implementation
```

### Code Pattern

```python
class Service:
    def run(self):
        return self._pipeline()
```

## Examples

### Beginner Example

```python
class Clock:
    def now_iso(self):
        from datetime import datetime, timezone
        return datetime.now(timezone.utc).isoformat()
print(Clock().now_iso()[:4])
```

### Intermediate Example

```python
from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount: float) -> str:
        raise NotImplementedError


class FakeGateway(PaymentGateway):
    def charge(self, amount: float) -> str:
        return f'charged {amount:.2f}'


print(FakeGateway().charge(9.99))
```

### Advanced Example

```python
class Database:
    def __init__(self):
        self._connected = True

    def query(self, sql: str) -> list[tuple]:
        return [('row',)] if self._connected else []


class UserRepository:
    def __init__(self, db: Database):
        self._db = db

    def list_users(self) -> list[tuple]:
        return self._db.query('SELECT 1')


print(UserRepository(Database()).list_users())
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Client] --> B[Abstract API]
    B --> C[Hidden Impl]
```

---

# Magic Methods

## Overview

- **What is it?** Magic methods (dunders) customize operator and protocol behavior.
- **Why is it important?** They make user-defined objects feel like built-ins.
- **Where is it used?** Domain models, containers, context managers, iterators.

## Learning Objectives

- **Skills gained:** Practical command of Magic Methods.
- **Concepts covered:**

- Implement __repr__, __str__, __len__, __eq__.
- Support context manager and iteration protocols.
- Avoid overloading operators without need.

- **Expected outcome:** You make classes Pythonic and interoperable with syntax.

## Real World Applications

- Numeric libs
- Custom collections
- ORM fields
- Simulation

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### __repr__

- **Definition:** Unambiguous debug representation.
- **Visual explanation:** `__repr__` → process → result
- **Practical example:**

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
print(repr(Point(1,2)))
```

### __eq__

- **Definition:** Value equality.
- **Visual explanation:** `__eq__` → process → result
- **Practical example:**

```python
class V:
    def __init__(self, n):
        self.n = n
    def __eq__(self, other):
        return isinstance(other, V) and self.n == other.n
print(V(1) == V(1))
```

### __len__

- **Definition:** Support len(obj).
- **Visual explanation:** `__len__` → process → result
- **Practical example:**

```python
class Bag:
    def __init__(self, items):
        self.items = items
    def __len__(self):
        return len(self.items)
print(len(Bag([1,2])))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Dunders hook into Python data model. |
| ⚡ Purpose | Integrate objects with language features. |
| 🔥 Benefits | Readable syntax, less boilerplate at call sites. |
| 🎯 Use Cases | Vectors, stacks, money types, smart paths. |
| 🚀 Best Practices | Keep semantics intuitive; document equality/hash contract. |
| ❌ Common Mistakes | Broken __hash__ with mutable __eq__, surprising operators. |

## Syntax Guide

### Basic Syntax

```python
def __repr__(self):
    return f'MyObj({self.id})'
```

### Standard Structure

```python
identify protocol -> implement dunders -> test
```

### Code Pattern

```python
def __enter__(self):
    return self
```

## Examples

### Beginner Example

```python
class Title:
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return self.text.upper()
print(str(Title('hi')))
```

### Intermediate Example

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def __len__(self):
        return len(self._items)


s = Stack()
s.push(1)
print(len(s))
```

### Advanced Example

```python
class Vector:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'


print(Vector(1, 2) + Vector(3, 4))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Object] --> B[Magic Method]
    B --> C[Python Syntax]
```

---

# Iterators

## Overview

- **What is it?** Iterators expose __iter__ and __next__ to produce elements lazily.
- **Why is it important?** Lazy iteration saves memory on large or infinite sequences.
- **Where is it used?** File scanning, streaming APIs, custom collections, pipelines.

## Learning Objectives

- **Skills gained:** Practical command of Iterators.
- **Concepts covered:**

- Use iter() and next().
- Implement iterator protocol.
- Understand StopIteration.

- **Expected outcome:** You build lazy sequence producers and consumers.

## Real World Applications

- Log streaming
- Genomics pipelines
- Market data feeds
- Pagination

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### __iter__

- **Definition:** Returns iterator object.
- **Visual explanation:** `__iter__` → process → result
- **Practical example:**

```python
data = [1, 2]
it = iter(data)
print(next(it))
```

### __next__

- **Definition:** Produces next value or raises StopIteration.
- **Visual explanation:** `__next__` → process → result
- **Practical example:**

```python
class Countdown:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1
print(list(Countdown(3)))
```

### StopIteration

- **Definition:** Signals exhaustion.
- **Visual explanation:** `StopIteration` → process → result
- **Practical example:**

```python
it = iter([])
try:
    next(it)
except StopIteration:
    print('done')
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Iterators generate values on demand. |
| ⚡ Purpose | Traverse data without loading all at once. |
| 🔥 Benefits | Memory efficient, composable pipelines. |
| 🎯 Use Cases | CSV row scan, socket read loop, paginated API. |
| 🚀 Best Practices | Separate iterable from iterator when reused; handle StopIteration. |
| ❌ Common Mistakes | Non-resetting iterators, confusing iterable vs iterator. |

## Syntax Guide

### Basic Syntax

```python
for item in iterable:
    print(item)
```

### Standard Structure

```python
__iter__ -> __next__ loop -> StopIteration
```

### Code Pattern

```python
it = iter(source)
while True:
    try:
        item = next(it)
    except StopIteration:
        break
    print(item)
```

## Examples

### Beginner Example

```python
it = iter(['a', 'b'])
print(next(it), next(it))
```

### Intermediate Example

```python
class Range:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        value = self.i
        self.i += 1
        return value


print(list(Range(3)))
```

### Advanced Example

```python
def line_generator(path: str):
    with open(path, encoding='utf-8') as handle:
        for line in handle:
            yield line.rstrip('\n')


print(sum(1 for _ in line_generator('README.md')))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Iterable] --> B[Iterator]
    B --> C[next()]
```

---

# Generators

## Overview

- **What is it?** Generators are iterators created by functions with yield.
- **Why is it important?** They simplify lazy pipelines with readable syntax.
- **Where is it used?** Streaming transforms, pagination, infinite sequences, coroutine precursors.

## Learning Objectives

- **Skills gained:** Practical command of Generators.
- **Concepts covered:**

- Write generator functions with yield.
- Use yield from for delegation.
- Chain generator pipelines.

- **Expected outcome:** You implement memory-efficient data pipelines with generators.

## Real World Applications

- ETL streaming
- Observability pipelines
- Audio processing
- Crawler fetch queues

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### yield

- **Definition:** Pauses function retaining state.
- **Visual explanation:** `yield` → process → result
- **Practical example:**

```python
def gen():
    yield 1
    yield 2
print(list(gen()))
```

### generator expr

- **Definition:** Like list comp but lazy.
- **Visual explanation:** `generator expr` → process → result
- **Practical example:**

```python
g = (x * x for x in range(3))
print(sum(g))
```

### yield from

- **Definition:** Delegate to sub-generator.
- **Visual explanation:** `yield from` → process → result
- **Practical example:**

```python
def a():
    yield from range(2)
print(list(a()))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Generators produce values lazily via yield. |
| ⚡ Purpose | Stream processing with minimal memory. |
| 🔥 Benefits | Simple syntax, composable stages, fast startup. |
| 🎯 Use Cases | Log tailers, batch readers, fibonacci stream. |
| 🚀 Best Practices | Document exhaustion; close generators when needed. |
| ❌ Common Mistakes | Mixing return values with yield confusingly, not iterating once. |

## Syntax Guide

### Basic Syntax

```python
def count_to(n):
    for i in range(n):
        yield i
```

### Standard Structure

```python
produce -> yield -> resume -> StopIteration
```

### Code Pattern

```python
def read_chunks(f):
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        yield chunk
```

## Examples

### Beginner Example

```python
def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
print(list(evens(6)))
```

### Intermediate Example

```python
def moving_average(values, size=3):
    window = []
    for value in values:
        window.append(value)
        if len(window) == size:
            yield sum(window) / size
            window.pop(0)


print(list(moving_average([1, 2, 3, 4, 5])))
```

### Advanced Example

```python
def pipeline(*stages):
    def run(source):
        gen = source
        for stage in stages:
            gen = stage(gen)
        yield from gen

    return run


def double(iterable):
    for x in iterable:
        yield x * 2


print(list(pipeline(double)(iter([1, 2, 3]))))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Generator] --> B[yield]
    B --> C[Consumer for-loop]
```

---

# Decorators

## Overview

- **What is it?** Decorators wrap functions or classes to extend behavior without modifying their source.
- **Why is it important?** Cross-cutting concerns like logging, timing, auth belong in decorators.
- **Where is it used?** Web frameworks, CLI, testing, caching layers.

## Learning Objectives

- **Skills gained:** Practical command of Decorators.
- **Concepts covered:**

- Write function decorators with functools.wraps.
- Create parameterized decorators.
- Stack decorators safely.

- **Expected outcome:** You add reusable behavior around callables cleanly.

## Real World Applications

- Web APIs
- Auth middleware
- Performance tooling
- Feature flags

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### @syntax

- **Definition:** Syntactic sugar for wrapping.
- **Visual explanation:** `@syntax` → process → result
- **Practical example:**

```python
def deco(f):
    def wrap(*a, **k):
        return f(*a, **k)
    return wrap
@deco
def hi():
    return 'hi'
print(hi())
```

### wraps

- **Definition:** Preserve metadata.
- **Visual explanation:** `wraps` → process → result
- **Practical example:**

```python
from functools import wraps
def deco(f):
    @wraps(f)
    def wrap():
        return f()
    return wrap
@deco
def work():
    'doc'
    return 1
print(work.__name__)
```

### Param decorator

- **Definition:** Decorator factory.
- **Visual explanation:** `Param decorator` → process → result
- **Practical example:**

```python
def repeat(n):
    def deco(f):
        def wrap():
            return [f() for _ in range(n)]
        return wrap
    return deco
@repeat(2)
def one():
    return 1
print(one())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Decorators are higher-order functions applying wrappers. |
| ⚡ Purpose | Inject before/after logic around callables. |
| 🔥 Benefits | DRY, composable, framework-friendly. |
| 🎯 Use Cases | Timing, retries, access control, memoization. |
| 🚀 Best Practices | Use wraps; keep wrappers thin; type the wrapped callable. |
| ❌ Common Mistakes | Forgetting wraps, decorator order confusion, heavy work at import. |

## Syntax Guide

### Basic Syntax

```python
def logged(func):
    def wrapper(*args, **kwargs):
        print('call', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

### Standard Structure

```python
define wrapper -> apply with @ -> preserve metadata
```

### Code Pattern

```python
def view():
    return 'ok'


print(view())
```

## Examples

### Beginner Example

```python
def uppercase(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper

@uppercase
def greet(name):
    return f'hello {name}'

print(greet('ada'))
```

### Intermediate Example

```python
from functools import wraps


def retry(times: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last = None
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last = exc
            raise last

        return wrapper

    return decorator


@retry(3)
def flaky():
    return 'ok'


print(flaky())
```

### Advanced Example

```python
import time
from functools import wraps


def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f'{func.__name__} took {time.perf_counter() - start:.4f}s')
        return result

    return wrapper


@timed
def compute(n: int) -> int:
    return sum(range(n))


print(compute(1000))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Function] --> B[Decorator]
    B --> C[Wrapped Callable]
```

---

# Context Managers

## Overview

- **What is it?** Context managers setup and teardown resources with the with statement.
- **Why is it important?** Guaranteed cleanup prevents leaks even when errors occur.
- **Where is it used?** Files, locks, DB transactions, temporary directories.

## Learning Objectives

- **Skills gained:** Practical command of Context Managers.
- **Concepts covered:**

- Use with for files and locks.
- Implement __enter__/__exit__.
- Use contextlib.contextmanager.

- **Expected outcome:** You manage resources safely with with blocks.

## Real World Applications

- Database apps
- Concurrent services
- Infra automation
- Desktop apps

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### with

- **Definition:** Calls __enter__ and __exit__.
- **Visual explanation:** `with` → process → result
- **Practical example:**

```python
from contextlib import contextmanager
@contextmanager
def tag(name):
    print(f'<{name}>')
    yield
    print(f'</{name}>')
with tag('p'):
    print('hi')
```

### __exit__

- **Definition:** Receives exception info.
- **Visual explanation:** `__exit__` → process → result
- **Practical example:**

```python
class Demo:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc, tb):
        print('cleanup', exc_type is None)
        return False
with Demo():
    pass
```

### contextmanager

- **Definition:** Generator-based manager.
- **Visual explanation:** `contextmanager` → process → result
- **Practical example:**

```python
from contextlib import contextmanager
@contextmanager
def opened(path):
    f = open(path, encoding='utf-8')
    try:
        yield f
    finally:
        f.close()
with opened('README.md') as fh:
    print(fh.readline()[:5])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Context managers pair acquisition with release. |
| ⚡ Purpose | Deterministic setup/teardown. |
| 🔥 Benefits | Exception-safe cleanup, readable scope. |
| 🎯 Use Cases | Transactions, temp dirs, timing blocks. |
| 🚀 Best Practices | Avoid suppressing exceptions unless intended; keep __exit__ fast. |
| ❌ Common Mistakes | Manual open/close, swallowing errors, re-entrant locks misuse. |

## Syntax Guide

### Basic Syntax

```python
with open('file.txt', encoding='utf-8') as f:
    data = f.read()
```

### Standard Structure

```python
__enter__ -> body -> __exit__
```

### Code Pattern

```python
with lock:
    mutate_shared_state()
```

## Examples

### Beginner Example

```python
from contextlib import suppress
with suppress(ValueError):
    int('x')
print('ok')
```

### Intermediate Example

```python
from contextlib import contextmanager


@contextmanager
def temporary(value: str):
    print('set', value)
    try:
        yield value
    finally:
        print('unset', value)


with temporary('config') as cfg:
    print('use', cfg)
```

### Advanced Example

```python
import threading


class LockGuard:
    def __init__(self, lock: threading.Lock):
        self.lock = lock

    def __enter__(self):
        self.lock.acquire()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.lock.release()
        return False


lock = threading.Lock()
with LockGuard(lock):
    print('critical section')
```

## Workflow Diagram

```mermaid
flowchart TD
    A[with] --> B[__enter__]
    B --> C[Body]
    C --> D[__exit__]
```

---

# Regular Expressions

## Overview

- **What is it?** Regular expressions match and manipulate text via pattern rules.
- **Why is it important?** They extract, validate, and replace structured text efficiently.
- **Where is it used?** Log parsing, input validation, web scraping, data cleaning.

## Learning Objectives

- **Skills gained:** Practical command of Regular Expressions.
- **Concepts covered:**

- Use re.search, re.findall, re.sub.
- Read basic regex syntax.
- Prefer compiled patterns for reuse.

- **Expected outcome:** You solve text pattern tasks without fragile manual parsing.

## Real World Applications

- Security analytics
- SEO tools
- Support automation
- Compliance scanning

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### re.search

- **Definition:** Find first match.
- **Visual explanation:** `re.search` → process → result
- **Practical example:**

```python
import re
print(re.search(r'\d+', 'Room 42').group())
```

### groups

- **Definition:** Capture subpatterns.
- **Visual explanation:** `groups` → process → result
- **Practical example:**

```python
import re
m = re.match(r'(?P<user>\w+)@(?P<dom>\w+)', 'ada@example.com')
print(m.group('user'))
```

### re.sub

- **Definition:** Replace matches.
- **Visual explanation:** `re.sub` → process → result
- **Practical example:**

```python
import re
print(re.sub(r'\s+', '-', 'hello world'))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Regex engines match patterns over strings. |
| ⚡ Purpose | Parse semi-structured text reliably. |
| 🔥 Benefits | Powerful, compact, standard library support. |
| 🎯 Use Cases | Emails, IPs, URLs, log levels. |
| 🚀 Best Practices | Compile patterns; use raw strings; test edge cases. |
| ❌ Common Mistakes | Catastrophic backtracking, over-regex, not anchoring when needed. |

## Syntax Guide

### Basic Syntax

```python
import re
re.findall(r'\w+', 'Hello World')
```

### Standard Structure

```python
compile -> search/match -> group/sub
```

### Code Pattern

```python
import re
PATTERN = re.compile(r'\d+')
print(PATTERN.findall('a1b22'))
```

## Examples

### Beginner Example

```python
import re
print(bool(re.fullmatch(r'\d{3}-\d{4}', '555-1234')))
```

### Intermediate Example

```python
import re

LOG = re.compile(r'(?P<level>\w+) (?P<msg>.+)')
line = 'ERROR disk full'
match = LOG.match(line)
print(match.groupdict())
```

### Advanced Example

```python
import re

def redact(text: str) -> str:
    return re.sub(r'\b\d{4}-\d{4}-\d{4}-\d{4}\b', '[CARD]', text)


print(redact('paid 4111-1111-1111-1111'))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Text] --> B[Regex Engine]
    B --> C[Match/Replace]
```

---

# JSON Processing

## Overview

- **What is it?** JSON processing serializes Python objects to JSON and parses JSON text.
- **Why is it important?** JSON is the lingua franca of web APIs and config files.
- **Where is it used?** REST APIs, NoSQL docs, CLI configs, message queues.

## Learning Objectives

- **Skills gained:** Practical command of JSON Processing.
- **Concepts covered:**

- Use json.dumps and json.loads.
- Handle custom types with default=.
- Validate payloads before use.

- **Expected outcome:** You exchange structured data with JSON safely.

## Real World Applications

- Microservices
- Mobile backends
- Serverless
- Browser apps

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### dumps

- **Definition:** Python to JSON string.
- **Visual explanation:** `dumps` → process → result
- **Practical example:**

```python
import json
print(json.dumps({'a': 1}))
```

### loads

- **Definition:** JSON string to Python.
- **Visual explanation:** `loads` → process → result
- **Practical example:**

```python
import json
print(json.loads('{"a": 1}')['a'])
```

### indent

- **Definition:** Pretty-print JSON.
- **Visual explanation:** `indent` → process → result
- **Practical example:**

```python
import json
print(json.dumps([1, 2], indent=2))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | JSON maps to dict/list/str/number/bool/null. |
| ⚡ Purpose | Interoperable data exchange. |
| 🔥 Benefits | Human-readable, universal, stdlib support. |
| 🎯 Use Cases | API bodies, config, event logs. |
| 🚀 Best Practices | UTF-8 encoding; schema validation at boundaries. |
| ❌ Common Mistakes | Non-JSON types without default, float money, trusting input. |

## Syntax Guide

### Basic Syntax

```python
import json
json.loads('{"ok": true}')
```

### Standard Structure

```python
parse -> validate -> use -> serialize
```

### Code Pattern

```python
payload = json.loads(text)
response = json.dumps(result)
```

## Examples

### Beginner Example

```python
import json
data = {'name': 'Ada', 'score': 99}
print(json.dumps(data))
```

### Intermediate Example

```python
import json
from datetime import datetime


def default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(type(obj))


print(json.dumps({'at': datetime(2026, 1, 1)}, default=default))
```

### Advanced Example

```python
import json

class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'to_json'):
            return obj.to_json()
        return super().default(obj)


class User:
    def __init__(self, name: str):
        self.name = name

    def to_json(self):
        return {'name': self.name}


print(json.dumps(User('Ada'), cls=UserEncoder))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Python Object] --> B[dumps]
    B --> C[JSON Text]
    C --> D[loads]
```

---

# CSV Processing

## Overview

- **What is it?** CSV processing reads and writes comma-separated tabular files.
- **Why is it important?** Spreadsheets and legacy systems still exchange CSV widely.
- **Where is it used?** Finance exports, marketing lists, ETL staging, reports.

## Learning Objectives

- **Skills gained:** Practical command of CSV Processing.
- **Concepts covered:**

- Use csv.reader and csv.DictReader.
- Write rows with csv.writer.
- Handle headers and dialects.

- **Expected outcome:** You import and export tabular CSV data reliably.

## Real World Applications

- Accounting
- Retail analytics
- HR systems
- Science datasets

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### reader

- **Definition:** Iterate rows as lists.
- **Visual explanation:** `reader` → process → result
- **Practical example:**

```python
import csv
from io import StringIO
rows = list(csv.reader(StringIO('a,b\n1,2')))
print(rows)
```

### DictReader

- **Definition:** Rows as dicts by header.
- **Visual explanation:** `DictReader` → process → result
- **Practical example:**

```python
import csv
from io import StringIO
r = csv.DictReader(StringIO('name,score\nAda,99'))
print(list(r)[0]['name'])
```

### writer

- **Definition:** Serialize rows.
- **Visual explanation:** `writer` → process → result
- **Practical example:**

```python
import csv
from io import StringIO
buf = StringIO()
w = csv.writer(buf)
w.writerow(['x', 'y'])
print(buf.getvalue().strip())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | CSV is text rows with delimiter-separated fields. |
| ⚡ Purpose | Interchange tabular data simply. |
| 🔥 Benefits | Universal, streaming-friendly, stdlib module. |
| 🎯 Use Cases | Sales exports, survey results, bulk imports. |
| 🚀 Best Practices | Use DictReader; specify newline=''; handle encoding. |
| ❌ Common Mistakes | Locale comma issues, not quoting embedded commas, huge memory load. |

## Syntax Guide

### Basic Syntax

```python
import csv
with open('data.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.reader(f))
```

### Standard Structure

```python
open -> reader/writer -> process rows
```

### Code Pattern

```python
for row in csv.DictReader(f):
    handle(row)
```

## Examples

### Beginner Example

```python
import csv
from io import StringIO

print(list(csv.reader(StringIO('id,name\n1,Ada'))))
```

### Intermediate Example

```python
import csv
from io import StringIO

source = StringIO('sku,qty\nA1,2\nB2,1\n')
total = sum(int(row['qty']) for row in csv.DictReader(source))
print(total)
```

### Advanced Example

```python
import csv
from io import StringIO

def filter_rows(text: str, min_qty: int) -> list[dict]:
    rows = csv.DictReader(StringIO(text))
    return [r for r in rows if int(r['qty']) >= min_qty]


data = 'sku,qty\nA,5\nB,1\n'
print(filter_rows(data, 2))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[CSV File] --> B[Reader]
    B --> C[Rows]
    C --> D[Process]
```

---

# XML Processing

## Overview

- **What is it?** XML processing parses and builds hierarchical tagged documents.
- **Why is it important?** Enterprise systems, SOAP, RSS, and config still use XML.
- **Where is it used?** Legacy integrations, Android layouts, publishing pipelines.

## Learning Objectives

- **Skills gained:** Practical command of XML Processing.
- **Concepts covered:**

- Parse XML with ElementTree.
- Navigate elements and attributes.
- Build XML safely.

- **Expected outcome:** You read and produce XML without fragile string concat.

## Real World Applications

- Telecom
- Publishing
- Government
- Enterprise ERP

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### ElementTree

- **Definition:** Parse XML to tree.
- **Visual explanation:** `ElementTree` → process → result
- **Practical example:**

```python
import xml.etree.ElementTree as ET
root = ET.fromstring('<item id="1">A</item>')
print(root.tag, root.attrib)
```

### find/findall

- **Definition:** Query child elements.
- **Visual explanation:** `find/findall` → process → result
- **Practical example:**

```python
import xml.etree.ElementTree as ET
root = ET.fromstring('<root><a/><b/></root>')
print(len(root.findall('.')))
```

### tostring

- **Definition:** Serialize element.
- **Visual explanation:** `tostring` → process → result
- **Practical example:**

```python
import xml.etree.ElementTree as ET
e = ET.Element('note')
print(ET.tostring(e, encoding='unicode')[:5])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | XML is a tree of tagged nodes with attributes. |
| ⚡ Purpose | Structured document interchange. |
| 🔥 Benefits | Schema validation (XSD), namespaces, mature tooling. |
| 🎯 Use Cases | RSS feeds, SOAP envelopes, config files. |
| 🚀 Best Practices | Use ElementTree; avoid XML external entities; validate schema. |
| ❌ Common Mistakes | String templating XML, billion laughs, no namespaces handling. |

## Syntax Guide

### Basic Syntax

```python
import xml.etree.ElementTree as ET
ET.parse('file.xml')
```

### Standard Structure

```python
parse -> traverse -> mutate -> write
```

### Code Pattern

```python
for child in root.findall('record'):
    process(child)
```

## Examples

### Beginner Example

```python
import xml.etree.ElementTree as ET

xml = '<catalog><book id="bk1"/></catalog>'
root = ET.fromstring(xml)
print(root[0].tag)
```

### Intermediate Example

```python
import xml.etree.ElementTree as ET

data = '''<users><user name="Ada"/><user name="Lin"/></users>'''
names = [u.attrib['name'] for u in ET.fromstring(data).findall('user')]
print(names)
```

### Advanced Example

```python
import xml.etree.ElementTree as ET


def build_order(order_id: str, sku: str) -> str:
    root = ET.Element('order', id=order_id)
    item = ET.SubElement(root, 'item', sku=sku)
    item.text = '1'
    return ET.tostring(root, encoding='unicode')


print(build_order('100', 'ABC')[:20])
```

## Workflow Diagram

```mermaid
flowchart LR
    A[XML Text] --> B[Parser]
    B --> C[Element Tree]
```

---

# Logging

## Overview

- **What is it?** Logging records structured runtime events with levels and handlers.
- **Why is it important?** Print statements fail in production; logs enable observability.
- **Where is it used?** Servers, batch jobs, libraries, debugging production.

## Learning Objectives

- **Skills gained:** Practical command of Logging.
- **Concepts covered:**

- Configure logging levels and handlers.
- Log with context and exceptions.
- Use module loggers.

- **Expected outcome:** You instrument apps with production-grade logs.

## Real World Applications

- SRE
- Backend platforms
- Data pipelines
- Security ops

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### getLogger

- **Definition:** Named logger hierarchy.
- **Visual explanation:** `getLogger` → process → result
- **Practical example:**

```python
import logging
log = logging.getLogger(__name__)
log.warning('warn')
```

### levels

- **Definition:** DEBUG INFO WARNING ERROR CRITICAL.
- **Visual explanation:** `levels` → process → result
- **Practical example:**

```python
import logging
print(logging.INFO)
```

### exception

- **Definition:** Log traceback.
- **Visual explanation:** `exception` → process → result
- **Practical example:**

```python
import logging
logging.basicConfig(level=logging.ERROR)
try:
    1/0
except ZeroDivisionError:
    logging.exception('fail')
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Loggers emit records processed by handlers/formatters. |
| ⚡ Purpose | Trace behavior and diagnose failures. |
| 🔥 Benefits | Levels, rotation, structured fields, filtering. |
| 🎯 Use Cases | Request tracing, audit trails, metrics hooks. |
| 🚀 Best Practices | Log to stdout in containers; include correlation ids; no secrets. |
| ❌ Common Mistakes | Root logger misconfig, logging in tight loops, sensitive data in logs. |

## Syntax Guide

### Basic Syntax

```python
import logging
logging.info('message')
```

### Standard Structure

```python
configure -> getLogger -> log events
```

### Code Pattern

```python
logger.info('user=%s action=%s', user, action)
```

## Examples

### Beginner Example

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info('started')
```

### Intermediate Example

```python
import logging

logger = logging.getLogger('billing')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
logger.addHandler(handler)
logger.info('invoice created')
```

### Advanced Example

```python
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('app')
handler = RotatingFileHandler('app.log', maxBytes=1024, backupCount=2)
logger.addHandler(handler)
logger.error('rotated log example')
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Logger] --> B[Handler]
    B --> C[Formatter]
    C --> D[Output]
```

---

# Configuration Management

## Overview

- **What is it?** Configuration management loads settings from env vars, files, and defaults.
- **Why is it important?** Apps must behave differently per environment without code changes.
- **Where is it used?** 12-factor apps, microservices, CLI tools, notebooks.

## Learning Objectives

- **Skills gained:** Practical command of Configuration Management.
- **Concepts covered:**

- Load env with os.environ.
- Parse .env and YAML/TOML safely.
- Layer defaults < file < env.

- **Expected outcome:** You externalize settings with clear precedence rules.

## Real World Applications

- Cloud SaaS
- Kubernetes apps
- ML training jobs
- Mobile backends

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### os.environ

- **Definition:** Process environment variables.
- **Visual explanation:** `os.environ` → process → result
- **Practical example:**

```python
import os
os.environ['APP_MODE'] = 'test'
print(os.environ.get('APP_MODE'))
```

### defaults

- **Definition:** Fallback values.
- **Visual explanation:** `defaults` → process → result
- **Practical example:**

```python
import os
DEBUG = os.environ.get('DEBUG', '0') == '1'
print(DEBUG)
```

### dataclass settings

- **Definition:** Typed config object.
- **Visual explanation:** `dataclass settings` → process → result
- **Practical example:**

```python
from dataclasses import dataclass
@dataclass
class Settings:
    host: str = 'localhost'
    port: int = 8000
print(Settings().port)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Configuration separates policy from code. |
| ⚡ Purpose | Deploy same artifact to many environments. |
| 🔥 Benefits | Security (secrets via env), flexibility, testability. |
| 🎯 Use Cases | DB URLs, API keys, feature flags. |
| 🚀 Best Practices | Never commit secrets; validate on startup; document variables. |
| ❌ Common Mistakes | Hard-coded prod URLs, silent missing env, no typing. |

## Syntax Guide

### Basic Syntax

```python
import os
API_KEY = os.environ.get('API_KEY', '')
```

### Standard Structure

```python
defaults -> file -> env overrides -> validate
```

### Code Pattern

```python
settings = Settings.from_env()
```

## Examples

### Beginner Example

```python
import os
print(os.environ.get('PATH') is not None)
```

### Intermediate Example

```python
import os
from dataclasses import dataclass


@dataclass
class Config:
    database_url: str
    debug: bool


cfg = Config(database_url=os.getenv('DATABASE_URL', 'sqlite://'), debug=os.getenv('DEBUG') == '1')
print(cfg.database_url)
```

### Advanced Example

```python
import json
from pathlib import Path


def load_settings(path: Path) -> dict:
    data = json.loads(path.read_text(encoding='utf-8'))
    data.update({k.lower(): v for k, v in __import__('os').environ.items() if k.startswith('APP_')})
    return data


print('keys' in load_settings.__name__ or callable(load_settings))
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Defaults] --> B[File Config]
    B --> C[Env Overrides]
    C --> D[App]
```

---

# Multithreading

## Overview

- **What is it?** Multithreading runs concurrent threads within one process sharing memory.
- **Why is it important?** Threads overlap I/O wait times for network and disk workloads.
- **Where is it used?** Socket servers, downloaders, UI backends, parallel I/O.

## Learning Objectives

- **Skills gained:** Practical command of Multithreading.
- **Concepts covered:**

- Start threads with threading module.
- Protect shared state with locks.
- Know GIL limits on CPU-bound work.

- **Expected outcome:** You parallelize I/O-bound tasks with threads safely.

## Real World Applications

- Web crawlers
- Chat servers
- Monitoring agents
- Desktop apps

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Thread

- **Definition:** Concurrent execution unit.
- **Visual explanation:** `Thread` → process → result
- **Practical example:**

```python
import threading
def work():
    print('run')
t = threading.Thread(target=work)
t.start()
t.join()
```

### Lock

- **Definition:** Mutual exclusion.
- **Visual explanation:** `Lock` → process → result
- **Practical example:**

```python
import threading
lock = threading.Lock()
count = 0
def inc():
    global count
    with lock:
        count += 1
inc()
print(count)
```

### ThreadPoolExecutor

- **Definition:** Managed pool.
- **Visual explanation:** `ThreadPoolExecutor` → process → result
- **Practical example:**

```python
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=2) as ex:
    print(list(ex.map(lambda x: x * 2, [1, 2, 3])))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Threads share memory; locks coordinate access. |
| ⚡ Purpose | Concurrent I/O and responsiveness. |
| 🔥 Benefits | Simple shared state, low overhead for I/O. |
| 🎯 Use Cases | Parallel HTTP fetches, worker queues. |
| 🚀 Best Practices | Avoid shared mutable state; use queues; pool executors. |
| ❌ Common Mistakes | CPU-bound threading, deadlocks, race conditions. |

## Syntax Guide

### Basic Syntax

```python
threading.Thread(target=func, args=(1,)).start()
```

### Standard Structure

```python
define worker -> start threads -> join
```

### Code Pattern

```python
with ThreadPoolExecutor() as pool:
    pool.map(fn, items)
```

## Examples

### Beginner Example

```python
import threading

def hello():
    print('hello from thread')

t = threading.Thread(target=hello)
t.start()
t.join()
```

### Intermediate Example

```python
import threading

counter = {'n': 0}
lock = threading.Lock()

def worker():
    with lock:
        counter['n'] += 1

threads = [threading.Thread(target=worker) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(counter['n'])
```

### Advanced Example

```python
from concurrent.futures import ThreadPoolExecutor, as_completed


def fetch(n: int) -> int:
    return n * n


with ThreadPoolExecutor(max_workers=4) as pool:
    futures = [pool.submit(fetch, i) for i in range(6)]
    results = [f.result() for f in as_completed(futures)]
print(sorted(results))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Main Thread] --> B[Worker Threads]
    B --> C[Shared State + Locks]
```

---

# Multiprocessing

## Overview

- **What is it?** Multiprocessing spawns separate processes to bypass the GIL for CPU work.
- **Why is it important?** True parallelism for CPU-bound Python tasks requires processes.
- **Where is it used?** Data crunching, image processing, scientific compute, batch jobs.

## Learning Objectives

- **Skills gained:** Practical command of Multiprocessing.
- **Concepts covered:**

- Use multiprocessing.Process and Pool.
- Pass data via queues and pipes.
- Guard entry with if __name__ == '__main__'.

- **Expected outcome:** You parallelize CPU-bound workloads across cores.

## Real World Applications

- Quant analytics
- Video encoding
- ML preprocessing
- Simulation

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Process

- **Definition:** Independent Python interpreter.
- **Visual explanation:** `Process` → process → result
- **Practical example:**

```python
import multiprocessing as mp
def f(x):
    return x + 1
if __name__ == '__main__':
    p = mp.Process(target=f, args=(1,))
    p.start()
    p.join()
```

### Pool

- **Definition:** Worker process pool.
- **Visual explanation:** `Pool` → process → result
- **Practical example:**

```python
from multiprocessing import Pool
if __name__ == '__main__':
    with Pool(2) as pool:
        print(pool.map(lambda x: x * 2, [1, 2, 3]))
```

### Queue

- **Definition:** Inter-process messaging.
- **Visual explanation:** `Queue` → process → result
- **Practical example:**

```python
from multiprocessing import Process, Queue
def worker(q):
    q.put('done')
if __name__ == '__main__':
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    print(q.get())
    p.join()
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Processes have separate memory spaces. |
| ⚡ Purpose | CPU parallelism and isolation. |
| 🔥 Benefits | Uses multiple cores, fault isolation. |
| 🎯 Use Cases | Monte Carlo, batch transforms, parallel tests. |
| 🚀 Best Practices | Protect main; pick spawn on Windows; minimize large pickles. |
| ❌ Common Mistakes | Forgetting main guard, huge shared objects, too many processes. |

## Syntax Guide

### Basic Syntax

```python
if __name__ == '__main__':
    Process(target=work).start()
```

### Standard Structure

```python
spawn workers -> communicate -> join
```

### Code Pattern

```python
with Pool(n) as pool:
    pool.map(func, data)
```

## Examples

### Beginner Example

```python
from multiprocessing import Process


def double(x):
    print(x * 2)


if __name__ == '__main__':
    p = Process(target=double, args=(21,))
    p.start()
    p.join()
```

### Intermediate Example

```python
from multiprocessing import Pool


def square(x: int) -> int:
    return x * x


if __name__ == '__main__':
    with Pool(2) as pool:
        print(pool.map(square, range(5)))
```

### Advanced Example

```python
from concurrent.futures import ProcessPoolExecutor


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as ex:
        print(list(ex.map(fib, [10, 12, 14])))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Parent Process] --> B[Child Processes]
    B --> C[Results via Queue/Pool]
```

---

# Async Programming

## Overview

- **What is it?** Async programming coordinates many I/O tasks with async/await and an event loop.
- **Why is it important?** It scales concurrent network I/O without thread-per-connection overhead.
- **Where is it used?** Web servers, websockets, chat, microservices, IoT gateways.

## Learning Objectives

- **Skills gained:** Practical command of Async Programming.
- **Concepts covered:**

- Define async def and await coroutines.
- Run asyncio.run main loops.
- Gather concurrent tasks.

- **Expected outcome:** You build concurrent I/O services with asyncio.

## Real World Applications

- Real-time APIs
- Streaming platforms
- Telecom
- Fintech feeds

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### async def

- **Definition:** Defines coroutine function.
- **Visual explanation:** `async def` → process → result
- **Practical example:**

```python
async def hi():
    return 'hi'
```

### await

- **Definition:** Pause until awaitable completes.
- **Visual explanation:** `await` → process → result
- **Practical example:**

```python
import asyncio
async def main():
    await asyncio.sleep(0)
    return 1
print(asyncio.run(main()))
```

### gather

- **Definition:** Run tasks concurrently.
- **Visual explanation:** `gather` → process → result
- **Practical example:**

```python
import asyncio
async def work(n):
    return n
async def main():
    print(await asyncio.gather(work(1), work(2)))
asyncio.run(main())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Event loop schedules awaitable tasks cooperatively. |
| ⚡ Purpose | High concurrency for I/O-bound workloads. |
| 🔥 Benefits | Low memory vs threads, structured concurrency primitives. |
| 🎯 Use Cases | HTTP clients, websockets, background workers. |
| 🚀 Best Practices | Never block loop; use asyncio.to_thread for blocking code. |
| ❌ Common Mistakes | Blocking calls in async routes, unhandled task exceptions. |

## Syntax Guide

### Basic Syntax

```python
import asyncio


async def main():
    return 'done'


print(asyncio.run(main()))
```

### Standard Structure

```python
create coroutines -> schedule -> await results
```

### Code Pattern

```python
await asyncio.gather(*tasks)
```

## Examples

### Beginner Example

```python
import asyncio

async def greet(name: str) -> str:
    return f'Hello, {name}'

print(asyncio.run(greet('Ada')))
```

### Intermediate Example

```python
import asyncio

async def fetch(n: int) -> int:
    await asyncio.sleep(0.01)
    return n * 2

async def main():
    results = await asyncio.gather(*(fetch(i) for i in range(3)))
    print(results)

asyncio.run(main())
```

### Advanced Example

```python
import asyncio

async def producer(queue: asyncio.Queue[int]) -> None:
    for i in range(3):
        await queue.put(i)
    await queue.put(-1)

async def consumer(queue: asyncio.Queue[int]) -> list[int]:
    items = []
    while True:
        item = await queue.get()
        if item == -1:
            break
        items.append(item * 2)
    return items

async def main():
    q: asyncio.Queue[int] = asyncio.Queue()
    prod = asyncio.create_task(producer(q))
    result = await consumer(q)
    await prod
    print(result)

asyncio.run(main())
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Event Loop] --> B[Task 1]
    A --> C[Task 2]
    B --> D[Await I/O]
```

---

# API Development

## Overview

- **What is it?** API development builds HTTP (or RPC) interfaces for clients and services.
- **Why is it important?** APIs expose business capabilities to web and mobile clients and other services.
- **Where is it used?** SaaS products, mobile backends, partner integrations, ML serving.

## Learning Objectives

- **Skills gained:** Practical command of API Development.
- **Concepts covered:**

- Design RESTful routes and status codes.
- Validate request/response schemas.
- Implement auth and error handling.

- **Expected outcome:** You ship documented, testable HTTP APIs.

## Real World Applications

- Fintech APIs
- Health platforms
- E-commerce
- Internal platforms

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Routes

- **Definition:** Map paths to handlers.
- **Visual explanation:** `Routes` → process → result
- **Practical example:**

```python
ROUTES = {'/health': lambda: {'status': 'ok'}}
print(ROUTES['/health']())
```

### Status codes

- **Definition:** Communicate outcome.
- **Visual explanation:** `Status codes` → process → result
- **Practical example:**

```python
STATUS = {200: 'OK', 404: 'Not Found'}
print(STATUS[200])
```

### Schema validation

- **Definition:** Reject bad payloads early.
- **Visual explanation:** `Schema validation` → process → result
- **Practical example:**

```python
payload = {'email': 'a@b.com'}
assert 'email' in payload
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | APIs are contracts between producer and consumer. |
| ⚡ Purpose | Enable interoperable software integration. |
| 🔥 Benefits | Decoupling, multi-client support, monetization. |
| 🎯 Use Cases | CRUD resources, webhooks, public developer platforms. |
| 🚀 Best Practices | Version APIs; paginate lists; consistent errors; OpenAPI docs. |
| ❌ Common Mistakes | Breaking changes, no auth, leaking stack traces. |

## Syntax Guide

### Basic Syntax

```python
def get_user(user_id: int) -> dict:
    return {'id': user_id}
```

### Standard Structure

```python
router -> handler -> service -> repository
```

### Code Pattern

```python
def read_item(item_id: int) -> dict:
    return {'id': item_id}


print(read_item(1))
```

## Examples

### Beginner Example

```python
def create_response(data: dict, status: int = 200) -> dict:
    return {'status': status, 'data': data}


print(create_response({'ok': True}))
```

### Intermediate Example

```python
from dataclasses import dataclass


@dataclass
class User:
    id: int
    email: str


USERS = {1: User(1, 'a@b.com')}


def get_user(user_id: int) -> User:
    if user_id not in USERS:
        raise KeyError('not found')
    return USERS[user_id]


print(get_user(1).email)
```

### Advanced Example

```python
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"status":"ok"}')


def run_server():
    server = HTTPServer(('127.0.0.1', 0), Handler)
    host, port = server.server_address
    print(f'listening {port}')
    server.handle_request()


run_server()
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Client] --> B[API Gateway]
    B --> C[Handler]
    C --> D[Service/DB]
```

---

# API Consumption

## Overview

- **What is it?** API consumption calls external HTTP/JSON services from Python clients.
- **Why is it important?** Most apps integrate payment, maps, auth, and data providers via APIs.
- **Where is it used?** Mobile backends, ETL, automation, partner integrations.

## Learning Objectives

- **Skills gained:** Practical command of API Consumption.
- **Concepts covered:**

- Perform GET/POST with proper headers.
- Handle timeouts and retries.
- Parse and validate responses.

- **Expected outcome:** You integrate third-party APIs reliably.

## Real World Applications

- Travel aggregators
- Marketing stacks
- Ops automation
- Open banking

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### GET request

- **Definition:** Fetch resources.
- **Visual explanation:** `GET request` → process → result
- **Practical example:**

```python
import urllib.request
with urllib.request.urlopen('https://example.com') as r:
    print(r.status)
```

### JSON body

- **Definition:** Parse response content.
- **Visual explanation:** `JSON body` → process → result
- **Practical example:**

```python
import json
print(json.loads('{"ok": true}')['ok'])
```

### errors

- **Definition:** Check status codes.
- **Visual explanation:** `errors` → process → result
- **Practical example:**

```python
class APIError(Exception):
    pass
raise APIError('404')
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Clients must treat remote APIs as unreliable external dependencies. |
| ⚡ Purpose | Compose services into richer applications. |
| 🔥 Benefits | Faster feature delivery, leverage best-in-class vendors. |
| 🎯 Use Cases | Stripe charges, Slack posts, weather data. |
| 🚀 Best Practices | Set timeouts; exponential backoff; cache idempotent reads. |
| ❌ Common Mistakes | No timeout, no retry limits, trusting response shape. |

## Syntax Guide

### Basic Syntax

```python
import urllib.request
urllib.request.urlopen(url, timeout=5)
```

### Standard Structure

```python
build request -> send -> handle status -> parse
```

### Code Pattern

```python
response = client.get('/users/1')
response.raise_for_status()
```

## Examples

### Beginner Example

```python
import json
import urllib.request

class DummyResponse:
    def read(self):
        return b'{"value": 42}'

data = json.loads(DummyResponse().read())
print(data['value'])
```

### Intermediate Example

```python
import json
import urllib.error
import urllib.request


def fetch_json(url: str) -> dict:
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        return {'error': exc.code}


print('error' in fetch_json('https://example.com') or True)
```

### Advanced Example

```python
import time


def retry_get(fetch, attempts=3, delay=0.01):
    last = None
    for _ in range(attempts):
        try:
            return fetch()
        except Exception as exc:
            last = exc
            time.sleep(delay)
    raise last


print(retry_get(lambda: {'ok': True}))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Python Client] --> B[HTTP Request]
    B --> C[Remote API]
    C --> D[Parsed Data]
```

---

# Requests Library

## Overview

- **What is it?** Requests is a popular HTTP client library with a friendly API.
- **Why is it important?** It simplifies headers, sessions, JSON, and auth compared to urllib.
- **Where is it used?** Scripts, data ingestion, tests hitting HTTP services.

## Learning Objectives

- **Skills gained:** Practical command of Requests Library.
- **Concepts covered:**

- Use requests.get/post with params and JSON.
- Reuse Session for cookies/headers.
- Handle timeouts and exceptions.

- **Expected outcome:** You call HTTP APIs ergonomically with requests.

## Real World Applications

- Data ingestion
- QA automation
- Internal tools
- Prototyping

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### get/post

- **Definition:** HTTP verbs.
- **Visual explanation:** `get/post` → process → result
- **Practical example:**

```python
import requests
print(hasattr(requests, 'get'))
```

### json=

- **Definition:** Send JSON bodies.
- **Visual explanation:** `json=` → process → result
- **Practical example:**

```python
payload = {'a': 1}
print(payload['a'])
```

### Session

- **Definition:** Persistent client.
- **Visual explanation:** `Session` → process → result
- **Practical example:**

```python
class Session:
    def __init__(self):
        self.headers = {}
s = Session()
s.headers['UA'] = 'demo'
print(s.headers['UA'])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Requests wraps HTTP into Pythonic calls. |
| ⚡ Purpose | Fast, readable HTTP client code. |
| 🔥 Benefits | Sessions, auth helpers, streaming, timeouts. |
| 🎯 Use Cases | REST integrations, health checks, scrapers (respect robots). |
| 🚀 Best Practices | Always set timeout; use sessions; verify TLS in prod. |
| ❌ Common Mistakes | No timeout, ignoring response.ok, huge response in memory. |

## Syntax Guide

### Basic Syntax

```python
import requests
requests.get('https://example.com', timeout=5)
```

### Standard Structure

```python
Session -> request -> raise_for_status -> json()
```

### Code Pattern

```python
with requests.Session() as s:
    s.get(url)
```

## Examples

### Beginner Example

```python
import requests
print(requests.__version__[:1].isdigit())
```

### Intermediate Example

```python
class FakeResponse:
    status_code = 200

    def json(self):
        return {'ok': True}


def fake_get(url, timeout=5):
    return FakeResponse()


print(fake_get('https://example.com').json())
```

### Advanced Example

```python
class RetryClient:
    def __init__(self, getter, retries=3):
        self.getter = getter
        self.retries = retries

    def get(self, url):
        last = None
        for _ in range(self.retries):
            try:
                resp = self.getter(url)
                if resp.status_code < 500:
                    return resp
            except Exception as exc:
                last = exc
        raise last


class Resp:
    status_code = 200


print(RetryClient(lambda u: Resp()).get('/').status_code)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[requests] --> B[HTTP]
    B --> C[Response]
```

---

# Database Fundamentals

## Overview

- **What is it?** Database fundamentals cover relational models, SQL, transactions, and connections.
- **Why is it important?** Persistent structured storage underpins most applications.
- **Where is it used?** CRUD apps, analytics, auth systems, inventory, billing.

## Learning Objectives

- **Skills gained:** Practical command of Database Fundamentals.
- **Concepts covered:**

- Explain tables, keys, and relationships.
- Write basic SELECT/INSERT/UPDATE.
- Understand ACID transactions.

- **Expected outcome:** You design and query relational data confidently.

## Real World Applications

- Banking
- Retail
- Healthcare records
- SaaS multitenant

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Table

- **Definition:** Rows and columns.
- **Visual explanation:** `Table` → process → result
- **Practical example:**

```python
ROW = {'id': 1, 'name': 'Ada'}
print(ROW['name'])
```

### Primary key

- **Definition:** Unique row identifier.
- **Visual explanation:** `Primary key` → process → result
- **Practical example:**

```python
ids = {1, 2}
assert len(ids) == 2
```

### Transaction

- **Definition:** All-or-nothing changes.
- **Visual explanation:** `Transaction` → process → result
- **Practical example:**

```python
balance = 100
balance -= 30
assert balance == 70
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Relational DBs store normalized data queried with SQL. |
| ⚡ Purpose | Durable, queryable structured storage. |
| 🔥 Benefits | Consistency, joins, mature tooling. |
| 🎯 Use Cases | Users, orders, ledgers, inventory. |
| 🚀 Best Practices | Use migrations; index wisely; least privilege credentials. |
| ❌ Common Mistakes | N+1 queries, no transactions, string-built SQL (injection). |

## Syntax Guide

### Basic Syntax

```python
SQL = 'SELECT id, name FROM users WHERE active = 1'
print(SQL.split()[0])
```

### Standard Structure

```python
connect -> cursor -> execute -> commit/rollback
```

### Code Pattern

```python
BEGIN -> statements -> COMMIT
```

## Examples

### Beginner Example

```python
SQL = 'SELECT 1 AS one'
print(SQL.split()[0])
```

### Intermediate Example

```python
def transfer(balance: dict, src: str, dst: str, amount: float) -> None:
    if balance[src] < amount:
        raise ValueError('insufficient funds')
    balance[src] -= amount
    balance[dst] += amount


b = {'A': 100.0, 'B': 0.0}
transfer(b, 'A', 'B', 40)
print(b)
```

### Advanced Example

```python
class Transaction:
    def __init__(self, conn):
        self.conn = conn

    def __enter__(self):
        self.conn['in_tx'] = True
        return self.conn

    def __exit__(self, exc_type, exc, tb):
        self.conn['in_tx'] = False
        self.conn['committed'] = exc_type is None
        return False


conn = {'in_tx': False, 'committed': False}
with Transaction(conn):
    conn['rows'] = 1
print(conn['committed'])
```

## Workflow Diagram

```mermaid
flowchart LR
    A[App] --> B[Connection]
    B --> C[SQL]
    C --> D[DB]
```

---

# SQLite

## Overview

- **What is it?** SQLite is a serverless embedded SQL database in a single file.
- **Why is it important?** It is ideal for local apps, prototypes, tests, and edge devices.
- **Where is it used?** Mobile apps, desktop tools, unit tests, small web apps.

## Learning Objectives

- **Skills gained:** Practical command of SQLite.
- **Concepts covered:**

- Connect with sqlite3 module.
- Execute SQL safely with parameters.
- Use context managers for connections.

- **Expected outcome:** You persist data locally with SQLite and Python.

## Real World Applications

- Mobile
- IoT gateways
- Developer tools
- Testing

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### connect

- **Definition:** Open database file.
- **Visual explanation:** `connect` → process → result
- **Practical example:**

```python
import sqlite3
conn = sqlite3.connect(':memory:')
print(type(conn).__name__)
```

### parameterized SQL

- **Definition:** Prevent injection.
- **Visual explanation:** `parameterized SQL` → process → result
- **Practical example:**

```python
import sqlite3
conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE t (id INTEGER)')
conn.execute('INSERT INTO t VALUES (?)', (1,))
print(conn.execute('SELECT id FROM t').fetchone()[0])
```

### row factory

- **Definition:** Dict-like rows.
- **Visual explanation:** `row factory` → process → result
- **Practical example:**

```python
import sqlite3
conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row
print(callable(conn.row_factory))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | SQLite runs in-process without separate server. |
| ⚡ Purpose | Lightweight relational persistence. |
| 🔥 Benefits | Zero config, fast for small/medium data, portable file. |
| 🎯 Use Cases | App cache DB, integration tests, prototypes. |
| 🚀 Best Practices | Use WAL mode for concurrency; migrate schema; backup file. |
| ❌ Common Mistakes | Writing SQL with f-strings, no indexes, huge blobs in DB. |

## Syntax Guide

### Basic Syntax

```python
import sqlite3
conn = sqlite3.connect('app.db')
```

### Standard Structure

```python
connect -> execute -> commit -> close
```

### Code Pattern

```python
conn.execute('SELECT id FROM users WHERE id=?', (user_id,))
```

## Examples

### Beginner Example

```python
import sqlite3

conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
conn.execute('INSERT INTO users (name) VALUES (?)', ('Ada',))
print(conn.execute('SELECT name FROM users').fetchone()[0])
```

### Intermediate Example

```python
import sqlite3

with sqlite3.connect(':memory:') as conn:
    conn.execute('CREATE TABLE items (sku TEXT, qty INTEGER)')
    conn.executemany('INSERT INTO items VALUES (?, ?)', [('A', 2), ('B', 1)])
    total = conn.execute('SELECT SUM(qty) FROM items').fetchone()[0]
    print(total)
```

### Advanced Example

```python
import sqlite3

def init(conn: sqlite3.Connection) -> None:
    conn.execute('CREATE TABLE IF NOT EXISTS audit (id INTEGER PRIMARY KEY AUTOINCREMENT, msg TEXT)')
    conn.commit()


conn = sqlite3.connect(':memory:')
init(conn)
conn.execute('INSERT INTO audit (msg) VALUES (?)', ('created',))
print(conn.execute('SELECT COUNT(*) FROM audit').fetchone()[0])
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Python] --> B[sqlite3]
    B --> C[.db file]
```

---

# MySQL Integration

## Overview

- **What is it?** MySQL integration connects Python apps to MySQL/MariaDB servers.
- **Why is it important?** MySQL powers many web stacks and hosted relational workloads.
- **Where is it used?** LAMP/LEMP stacks, WordPress backends, SaaS multitenant DBs.

## Learning Objectives

- **Skills gained:** Practical command of MySQL Integration.
- **Concepts covered:**

- Connect with a DB-API driver.
- Use parameterized queries.
- Manage connection pools in production.

- **Expected outcome:** You read and write MySQL data safely from Python.

## Real World Applications

- Web hosting
- E-commerce
- Content platforms
- Internal CRMs

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### DB-API

- **Definition:** PEP 249 cursor pattern.
- **Visual explanation:** `DB-API` → process → result
- **Practical example:**

```python
class Cursor:
    def execute(self, sql, params=()):
        return sql, params
c = Cursor()
print(c.execute('SELECT ?', (1,))[1])
```

### Connection string

- **Definition:** Host, user, database.
- **Visual explanation:** `Connection string` → process → result
- **Practical example:**

```python
DSN = {'host': 'localhost', 'database': 'app'}
print(DSN['database'])
```

### Pool

- **Definition:** Reuse connections.
- **Visual explanation:** `Pool` → process → result
- **Practical example:**

```python
POOL = []
def acquire():
    return POOL[0] if POOL else object()
print(acquire())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Drivers translate Python calls to MySQL protocol. |
| ⚡ Purpose | Remote relational storage at scale. |
| 🔥 Benefits | Mature ecosystem, replication, hosting support. |
| 🎯 Use Cases | Web apps, reporting replicas, CMS data. |
| 🚀 Best Practices | Use mysqlclient or PyMySQL; SSL; least privilege user. |
| ❌ Common Mistakes | SQL injection, no connection timeout, storing plaintext passwords. |

## Syntax Guide

### Basic Syntax

```python
conn = connect(host='localhost', user='app', password='***', database='app')
```

### Standard Structure

```python
pool -> connection -> cursor -> commit
```

### Code Pattern

```python
cursor.execute('SELECT * FROM users WHERE id=%s', (user_id,))
```

## Examples

### Beginner Example

```python
CONFIG = {'driver': 'mysql', 'host': '127.0.0.1'}
print(CONFIG['driver'])
```

### Intermediate Example

```python
def query_users(cursor, active_only=True):
    sql = 'SELECT id, email FROM users'
    if active_only:
        sql += ' WHERE active = 1'
    return cursor.execute(sql)


class Cur:
    def execute(self, sql):
        return [('1', 'a@b.com')]


print(query_users(Cur()))
```

### Advanced Example

```python
class MySQLPool:
    def __init__(self, size: int = 5):
        self._size = size
        self._in_use = 0

    def connection(self):
        if self._in_use >= self._size:
            raise RuntimeError('pool exhausted')
        self._in_use += 1
        return self

    def close(self):
        self._in_use -= 1


pool = MySQLPool(2)
conn = pool.connection()
conn.close()
print(pool._in_use)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Python App] --> B[Driver]
    B --> C[MySQL Server]
```

---

# PostgreSQL Integration

## Overview

- **What is it?** PostgreSQL integration connects Python to advanced open-source RDBMS features.
- **Why is it important?** Postgres offers JSONB, extensions, and strong SQL compliance.
- **Where is it used?** SaaS platforms, geospatial apps, analytics, Django stacks.

## Learning Objectives

- **Skills gained:** Practical command of PostgreSQL Integration.
- **Concepts covered:**

- Connect with psycopg.
- Use transactions and RETURNING.
- Leverage Postgres types from Python.

- **Expected outcome:** You integrate Python services with PostgreSQL effectively.

## Real World Applications

- SaaS
- Geospatial
- Data warehouses
- Fintech ledgers

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### psycopg

- **Definition:** Popular Postgres adapter.
- **Visual explanation:** `psycopg` → process → result
- **Practical example:**

```python
print('psycopg'[:5])
```

### JSONB

- **Definition:** Document columns in SQL.
- **Visual explanation:** `JSONB` → process → result
- **Practical example:**

```python
import json
print(json.dumps({'a': 1}))
```

### RETURNING

- **Definition:** Get inserted rows.
- **Visual explanation:** `RETURNING` → process → result
- **Practical example:**

```python
SQL = 'INSERT INTO t (name) VALUES (%s) RETURNING id'
print('RETURNING' in SQL)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Drivers map Python types to Postgres types. |
| ⚡ Purpose | Robust transactional storage with rich SQL. |
| 🔥 Benefits | Extensions, CTEs, strong consistency, JSONB. |
| 🎯 Use Cases | Multi-tenant SaaS, GIS, event sourcing. |
| 🚀 Best Practices | Use connection pools; migrations; explain analyze slow queries. |
| ❌ Common Mistakes | Not closing connections, serializing JSON manually wrong, superuser in app. |

## Syntax Guide

### Basic Syntax

```python
conn = psycopg.connect('postgresql://user:pass@localhost/db')
```

### Standard Structure

```python
connect -> cursor -> execute -> commit
```

### Code Pattern

```python
class Connection:
    def transaction(self):
        return self

    def execute(self, sql):
        return []


conn = Connection()
with conn.transaction():
    rows = conn.execute('SELECT 1')
print(rows)
```

## Examples

### Beginner Example

```python
DSN = 'postgresql://localhost/app'
print(DSN.startswith('postgresql'))
```

### Intermediate Example

```python
def insert_user(repo, email: str) -> int:
    return repo.execute('INSERT INTO users(email) VALUES (%s) RETURNING id', (email,))


class Repo:
    def execute(self, sql, params):
        return 42


print(insert_user(Repo(), 'a@b.com'))
```

### Advanced Example

```python
class PGTransaction:
    def __init__(self, conn):
        self.conn = conn

    def __enter__(self):
        self.conn['tx'] = True
        return self.conn

    def __exit__(self, exc_type, exc, tb):
        self.conn['tx'] = False
        self.conn['ok'] = exc_type is None
        return False


c = {'tx': False, 'ok': False}
with PGTransaction(c):
    c['work'] = True
print(c['ok'])
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Python] --> B[psycopg]
    B --> C[PostgreSQL]
```

---

# SQLAlchemy ORM

## Overview

- **What is it?** SQLAlchemy ORM maps Python classes to database tables and queries.
- **Why is it important?** It reduces boilerplate SQL and eases schema evolution.
- **Where is it used?** Web apps, data services, admin tools, migration-heavy systems.

## Learning Objectives

- **Skills gained:** Practical command of SQLAlchemy ORM.
- **Concepts covered:**

- Declare mapped classes and sessions.
- Query with Session.query or select().
- Manage migrations with Alembic.

- **Expected outcome:** You persist domain objects with SQLAlchemy patterns.

## Real World Applications

- Django-adjacent services
- Enterprise apps
- Internal tools
- Analytics apps

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Engine

- **Definition:** Connection factory.
- **Visual explanation:** `Engine` → process → result
- **Practical example:**

```python
class Engine:
    def connect(self):
        return {'connected': True}
print(Engine().connect())
```

### Session

- **Definition:** Unit of work.
- **Visual explanation:** `Session` → process → result
- **Practical example:**

```python
class Session:
    def add(self, obj):
        self.obj = obj
s = Session()
s.add({'id': 1})
print(s.obj)
```

### Mapped class

- **Definition:** Class <-> table.
- **Visual explanation:** `Mapped class` → process → result
- **Practical example:**

```python
class User:
    __tablename__ = 'users'
    id = 1
print(User.__tablename__)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | ORM translates objects to SQL and back. |
| ⚡ Purpose | Productive relational persistence in Python. |
| 🔥 Benefits | Composable queries, connection pooling, dialect abstraction. |
| 🎯 Use Cases | User models, orders, reporting entities. |
| 🚀 Best Practices | Explicit sessions; avoid lazy loading N+1; use Alembic. |
| ❌ Common Mistakes | Session leaks, implicit autoflush surprises, god models. |

## Syntax Guide

### Basic Syntax

```python
session.add(obj)
session.commit()
```

### Standard Structure

```python
engine -> sessionmaker -> session -> query/commit
```

### Code Pattern

```python
with Session(engine) as session:
    session.add(user)
```

## Examples

### Beginner Example

```python
class User:
    def __init__(self, email: str):
        self.email = email


user = User('a@b.com')
print(user.email)
```

### Intermediate Example

```python
class Repository:
    def __init__(self, session):
        self.session = session

    def create_user(self, email: str):
        user = {'email': email}
        self.session['users'] = self.session.get('users', []) + [user]
        return user


session = {}
repo = Repository(session)
print(repo.create_user('a@b.com'))
```

### Advanced Example

```python
class UnitOfWork:
    def __init__(self):
        self.new = []
        self.dirty = []

    def register_new(self, entity):
        self.new.append(entity)

    def commit(self):
        saved = len(self.new) + len(self.dirty)
        self.new.clear()
        self.dirty.clear()
        return saved


uow = UnitOfWork()
uow.register_new({'id': 1})
print(uow.commit())
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Mapped Class] --> B[Session]
    B --> C[Engine]
    C --> D[Database]
```

---

# Unit Testing

## Overview

- **What is it?** Unit testing verifies small units of code behave as expected automatically.
- **Why is it important?** Tests prevent regressions and document intended behavior.
- **Where is it used?** Every professional Python codebase and CI pipeline.

## Learning Objectives

- **Skills gained:** Practical command of Unit Testing.
- **Concepts covered:**

- Write tests with unittest or pytest.
- Use assertions and test cases.
- Organize tests mirroring package structure.

- **Expected outcome:** You protect core logic with fast automated unit tests.

## Real World Applications

- SaaS
- Libraries
- Quant systems
- Safety-critical tooling

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### test function

- **Definition:** Assert expected behavior.
- **Visual explanation:** `test function` → process → result
- **Practical example:**

```python
def test_add():
    assert 1 + 1 == 2
test_add()
```

### TestCase

- **Definition:** unittest grouping.
- **Visual explanation:** `TestCase` → process → result
- **Practical example:**

```python
import unittest
class Tests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)
unittest.main(argv=[''], exit=False)
```

### arrange-act-assert

- **Definition:** Test structure.
- **Visual explanation:** `arrange-act-assert` → process → result
- **Practical example:**

```python
def test_double():
    value = 2
    result = value * 2
    assert result == 4
test_double()
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Unit tests isolate one behavior per test. |
| ⚡ Purpose | Catch bugs early and enable refactoring. |
| 🔥 Benefits | Confidence, living documentation, safer CI. |
| 🎯 Use Cases | Pure functions, validators, parsers. |
| 🚀 Best Practices | One assertion focus; descriptive names; fast tests. |
| ❌ Common Mistakes | Testing implementation details, flaky tests, no CI run. |

## Syntax Guide

### Basic Syntax

```python
def test_something():
    assert func() == expected
```

### Standard Structure

```python
arrange -> act -> assert
```

### Code Pattern

```python
result = system_under_test(input)
assert result == expected
```

## Examples

### Beginner Example

```python
def inc(x):
    return x + 1
assert inc(2) == 3
```

### Intermediate Example

```python
import unittest


def is_palindrome(text: str) -> bool:
    cleaned = text.lower().replace(' ', '')
    return cleaned == cleaned[::-1]


class PalindromeTests(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome('Level'))


unittest.main(argv=[''], exit=False, verbosity=0)
```

### Advanced Example

```python
from dataclasses import dataclass


@dataclass
class TestResult:
    name: str
    passed: bool


def run_tests(cases):
    return [TestResult(name, fn()) for name, fn in cases]


print(run_tests([('ok', lambda: True)]))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Code Change] --> B[Run Tests]
    B --> C{Pass?}
    C -->|yes| D[Merge]
    C -->|no| E[Fix]
```

---

# Pytest

## Overview

- **What is it?** Pytest is a flexible testing framework with simple tests and powerful fixtures.
- **Why is it important?** It reduces boilerplate versus unittest and has rich plugin ecosystem.
- **Where is it used?** Open source Python, FastAPI/Django projects, libraries.

## Learning Objectives

- **Skills gained:** Practical command of Pytest.
- **Concepts covered:**

- Write test_ functions and assert.
- Use fixtures for setup/teardown.
- Parametrize tests for edge cases.

- **Expected outcome:** You build expressive test suites with pytest.

## Real World Applications

- Web APIs
- PyPI packages
- Data platforms
- ML pipelines

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### test_ prefix

- **Definition:** Auto-discovered tests.
- **Visual explanation:** `test_ prefix` → process → result
- **Practical example:**

```python
def test_sum():
    assert sum([1, 2]) == 3
test_sum()
```

### fixtures

- **Definition:** Reusable setup.
- **Visual explanation:** `fixtures` → process → result
- **Practical example:**

```python
def sample_data():
    return [1, 2, 3]
assert len(sample_data()) == 3
```

### parametrize

- **Definition:** Multiple inputs.
- **Visual explanation:** `parametrize` → process → result
- **Practical example:**

```python
cases = [(1, 2), (2, 4)]
for n, expected in cases:
    assert n * 2 == expected
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Pytest collects tests and runs with rich reporting. |
| ⚡ Purpose | Productive testing with minimal ceremony. |
| 🔥 Benefits | Fixtures, plugins, clear failures, parametrize. |
| 🎯 Use Cases | API tests, unit tests, snapshot testing. |
| 🚀 Best Practices | Use conftest.py; mark slow tests; isolate I/O. |
| ❌ Common Mistakes | Shared mutable fixtures, testing order dependence. |

## Syntax Guide

### Basic Syntax

```python
def test_example():
    assert True
```

### Standard Structure

```python
fixtures -> test functions -> pytest runner
```

### Code Pattern

```python
class Client:
    def post(self, path, json=None):
        return {'path': path, 'json': json}


def test_user_creation(client):
    return client.post('/users', json={'email': 'a@b.com'})


print(test_user_creation(Client()))
```

## Examples

### Beginner Example

```python
def test_upper():
    assert 'hi'.upper() == 'HI'
test_upper()
```

### Intermediate Example

```python
def pytest_style_double(n):
    return n * 2


def test_double():
    assert pytest_style_double(3) == 6
```

### Advanced Example

```python
def parametrize(cases):
    def decorator(func):
        def runner():
            for args in cases:
                func(*args)
        return runner
    return decorator


@parametrize([(2, 4), (3, 6)])
def test_double(n, expected):
    assert n * 2 == expected


test_double()
```

## Workflow Diagram

```mermaid
flowchart LR
    A[pytest] --> B[Collect Tests]
    B --> C[Fixtures]
    C --> D[Run/Report]
```

---

# Mocking

## Overview

- **What is it?** Mocking replaces real dependencies with test doubles during unit tests.
- **Why is it important?** Tests must be isolated from networks, databases, and non-determinism.
- **Where is it used?** Unit tests for services, API clients, time, randomness.

## Learning Objectives

- **Skills gained:** Practical command of Mocking.
- **Concepts covered:**

- Use unittest.mock.Mock and patch.
- Assert calls and return values.
- Avoid over-mocking internal details.

- **Expected outcome:** You test components in isolation with controlled dependencies.

## Real World Applications

- Microservices
- SDK development
- Payment integrations
- CI pipelines

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Mock

- **Definition:** Fake object with methods.
- **Visual explanation:** `Mock` → process → result
- **Practical example:**

```python
from unittest.mock import Mock
m = Mock(return_value=42)
print(m())
```

### patch

- **Definition:** Replace symbol temporarily.
- **Visual explanation:** `patch` → process → result
- **Practical example:**

```python
from unittest.mock import patch
with patch('builtins.len', return_value=3):
    print(len([]))
```

### assert_called

- **Definition:** Verify interactions.
- **Visual explanation:** `assert_called` → process → result
- **Practical example:**

```python
from unittest.mock import Mock
m = Mock()
m.save('x')
m.save.assert_called_once_with('x')
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Mocks simulate collaborators with controlled behavior. |
| ⚡ Purpose | Isolate unit under test. |
| 🔥 Benefits | Fast, deterministic tests without external systems. |
| 🎯 Use Cases | API client tests, DB repository tests, clock control. |
| 🚀 Best Practices | Mock boundaries not internals; verify outcomes and key calls. |
| ❌ Common Mistakes | Mocking everything, brittle call assertions, patching wrong path. |

## Syntax Guide

### Basic Syntax

```python
from unittest.mock import Mock
service = Mock()
service.fetch.return_value = {'ok': True}
```

### Standard Structure

```python
patch dependency -> exercise code -> assert behavior
```

### Code Pattern

```python
from unittest.mock import patch


def flow(mock_call):
    mock_call.return_value = {'ok': True}
    return mock_call()


with patch('builtins.len', return_value=3):
    print(flow(len))
```

## Examples

### Beginner Example

```python
from unittest.mock import Mock

repo = Mock()
repo.get.return_value = {'id': 1}
print(repo.get(1)['id'])
```

### Intermediate Example

```python
from unittest.mock import patch


def send_email(client, to: str):
    return client.post('/email', json={'to': to})


class FakeClient:
    def post(self, path, json=None):
        return {'path': path, 'json': json}


with patch('builtins.print'):
    result = send_email(FakeClient(), 'a@b.com')
print(result['json']['to'])
```

### Advanced Example

```python
from unittest.mock import MagicMock


def process(payment_gateway, amount: float) -> str:
    receipt = payment_gateway.charge(amount)
    return receipt['id']


gateway = MagicMock()
gateway.charge.return_value = {'id': 'rcpt_123'}
print(process(gateway, 10.0))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Unit Under Test] --> B[Mock Dependency]
    B --> C[Controlled Response]
```

---

# Packaging Python Projects

## Overview

- **What is it?** Packaging Python projects prepares installable distributions with metadata and entry points.
- **Why is it important?** Packaging enables pip install, versioning, and publishing to PyPI.
- **Where is it used?** Open source libraries, internal packages, CLI tools.

## Learning Objectives

- **Skills gained:** Practical command of Packaging Python Projects.
- **Concepts covered:**

- Configure pyproject.toml with build backend.
- Declare dependencies and optional extras.
- Build wheels and sdist.

- **Expected outcome:** You build and publish Python packages correctly.

## Real World Applications

- PyPI ecosystem
- Enterprise internal PyPI
- CLI products
- SDK vendors

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### pyproject.toml

- **Definition:** Project metadata and tools.
- **Visual explanation:** `pyproject.toml` → process → result
- **Practical example:**

```python
print('[project]' in '[project]\nname="demo"')
```

### wheel

- **Definition:** Built distribution format.
- **Visual explanation:** `wheel` → process → result
- **Practical example:**

```python
print('whl' in 'package-1.0-py3-none-any.whl')
```

### entry points

- **Definition:** Console scripts.
- **Visual explanation:** `entry points` → process → result
- **Practical example:**

```python
ENTRY = {'console_scripts': ['mycli=mypkg.cli:main']}
print(ENTRY['console_scripts'][0].split('=')[0])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Build backends produce standardized artifacts. |
| ⚡ Purpose | Share and install Python code reliably. |
| 🔥 Benefits | Version pinning, dependency resolution, script installation. |
| 🎯 Use Cases | Libraries, CLIs, plugins. |
| 🚀 Best Practices | Semantic versioning; README on PyPI; classifiers; license file. |
| ❌ Common Mistakes | Missing MANIFEST/pyproject deps, not testing install in clean venv. |

## Syntax Guide

### Basic Syntax

```python
[project]
name = "my-package"
version = "0.1.0"
```

### Standard Structure

```python
src layout -> pyproject -> build -> publish
```

### Code Pattern

```python
commands = ['python', '-m', 'build']
print(' '.join(commands))
```

## Examples

### Beginner Example

```python
from pathlib import Path
print(Path('scripts/generate_all_snippets.py').exists())
```

### Intermediate Example

```python
METADATA = {
    'name': 'demo_pkg',
    'version': '0.1.0',
    'dependencies': ['requests>=2.0'],
}
print(METADATA['name'])
```

### Advanced Example

```python
def build_console_script(module: str, func: str = 'main') -> str:
    return f'{module.split('.')[-1]}={module}:{func}'


print(build_console_script('myapp.cli'))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Source] --> B[build]
    B --> C[wheel/sdist]
    C --> D[pip install]
```

---

# CLI Applications

## Overview

- **What is it?** CLI applications expose commands via terminal interfaces using argparse, click, or typer.
- **Why is it important?** Operators and developers automate workflows from the shell.
- **Where is it used?** DevOps tools, data utilities, codegen, admin tasks.

## Learning Objectives

- **Skills gained:** Practical command of CLI Applications.
- **Concepts covered:**

- Parse args and subcommands.
- Provide --help and sensible defaults.
- Return proper exit codes.

- **Expected outcome:** You ship user-friendly command-line tools in Python.

## Real World Applications

- SRE tooling
- Data ops
- Security scanners
- Build systems

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### argparse

- **Definition:** Stdlib CLI parser.
- **Visual explanation:** `argparse` → process → result
- **Practical example:**

```python
import argparse
p = argparse.ArgumentParser()
p.add_argument('name')
args = p.parse_args(['Ada'])
print(args.name)
```

### subcommands

- **Definition:** Nested CLI verbs.
- **Visual explanation:** `subcommands` → process → result
- **Practical example:**

```python
COMMANDS = {'run': lambda: 0, 'status': lambda: 0}
print(COMMANDS['run']())
```

### exit codes

- **Definition:** Signal success/failure.
- **Visual explanation:** `exit codes` → process → result
- **Practical example:**

```python
import sys
sys.exit(0)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | CLI = argv parsing + action + exit status. |
| ⚡ Purpose | Automate tasks from terminal and scripts. |
| 🔥 Benefits | Scriptable, remote-friendly, fast iteration. |
| 🎯 Use Cases | Deploy tools, ETL triggers, db migrations. |
| 🚀 Best Practices | Support --help; validate input; log to stderr; test CLI. |
| ❌ Common Mistakes | Printing only help on error, no exit codes, hidden global state. |

## Syntax Guide

### Basic Syntax

```python
if __name__ == '__main__':
    main()
```

### Standard Structure

```python
parse args -> dispatch command -> exit code
```

### Code Pattern

```python
parser = argparse.ArgumentParser()
parser.parse_args()
```

## Examples

### Beginner Example

```python
import sys

if len(sys.argv) > 1:
    print(f'Hello, {sys.argv[1]}')
else:
    print('Hello, world')
```

### Intermediate Example

```python
import argparse


def main(argv=None):
    parser = argparse.ArgumentParser(description='Greet users')
    parser.add_argument('name')
    args = parser.parse_args(argv)
    print(f'Hello, {args.name}')


main(['Ada'])
```

### Advanced Example

```python
import argparse


def build_parser():
    parser = argparse.ArgumentParser(prog='tool')
    sub = parser.add_subparsers(dest='command', required=True)
    run = sub.add_parser('run')
    run.add_argument('--dry-run', action='store_true')
    return parser


args = build_parser().parse_args(['run', '--dry-run'])
print(args.command, args.dry_run)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[argv] --> B[Parser]
    B --> C[Command Handler]
    C --> D[Exit Code]
```

---

## Level 3: Advanced

# Data Structures Internals

## Overview

- **What is it?** Data structures internals explain how Python lists, dicts, and sets are implemented.
- **Why is it important?** Understanding internals guides performance and memory decisions.
- **Where is it used?** High-scale services, competitive programming, library authors.

## Learning Objectives

- **Skills gained:** Practical command of Data Structures Internals.
- **Concepts covered:**

- Explain dynamic arrays and hash tables at high level.
- Know amortized costs of list/dict ops.
- Choose structures based on access patterns.

- **Expected outcome:** You reason about Python collection performance accurately.

## Real World Applications

- High-frequency systems
- Database engines
- Game servers
- ML infra

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Dynamic array

- **Definition:** Lists over-allocate for append.
- **Visual explanation:** `Dynamic array` → process → result
- **Practical example:**

```python
items = []
items.append(1)
print(len(items))
```

### Hash table

- **Definition:** Dicts map keys via hashing.
- **Visual explanation:** `Hash table` → process → result
- **Practical example:**

```python
d = {'a': 1}
print('a' in d)
```

### Load factor

- **Definition:** Dicts resize when crowded.
- **Visual explanation:** `Load factor` → process → result
- **Practical example:**

```python
print(len({i: i for i in range(1000)}))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | CPython collections trade memory for speed with tuned C implementations. |
| ⚡ Purpose | Pick the right structure and avoid hidden costs. |
| 🔥 Benefits | Predictable performance, fewer production surprises. |
| 🎯 Use Cases | Caches, indexes, buffers, queues. |
| 🚀 Best Practices | Use deque for FIFO; set for membership; pre-size when known. |
| ❌ Common Mistakes | Assuming list insert is O(1), using dict as ordered log without need. |

## Syntax Guide

### Basic Syntax

```python
from collections import deque
q = deque([1, 2])
q.append(3)
```

### Standard Structure

```python
analyze access pattern -> pick structure -> benchmark
```

### Code Pattern

```python
needs_membership = True
print('set' if needs_membership else 'list')
```

## Examples

### Beginner Example

```python
from collections import deque
print(deque([1, 2, 3])[0])
```

### Intermediate Example

```python
import sys

small = {}
big = {i: i for i in range(1000)}
print(sys.getsizeof(small) < sys.getsizeof(big))
```

### Advanced Example

```python
from collections import OrderedDict

cache = OrderedDict()
cache['a'] = 1
cache['b'] = 2
cache.move_to_end('a')
print(list(cache.keys()))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Operation] --> B[List/Dict/Set]
    B --> C[CPython C API]
```

---

# Algorithms in Python

## Overview

- **What is it?** Algorithms in Python implement classic CS techniques for searching, sorting, and graphs.
- **Why is it important?** Correct algorithms reduce time and memory at scale.
- **Where is it used?** Interviews, data pipelines, routing, recommendation engines.

## Learning Objectives

- **Skills gained:** Practical command of Algorithms in Python.
- **Concepts covered:**

- Implement search and sort algorithms.
- Analyze Big-O complexity.
- Use heapq and bisect when appropriate.

- **Expected outcome:** You choose and implement algorithms suited to problem constraints.

## Real World Applications

- Big tech
- Logistics
- Ads ranking
- Bioinformatics

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Binary search

- **Definition:** Divide sorted space.
- **Visual explanation:** `Binary search` → process → result
- **Practical example:**

```python
def bs(a, t):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == t: return mid
        if a[mid] < t: lo = mid + 1
        else: hi = mid - 1
    return -1
print(bs([1,3,5], 3))
```

### Sorting

- **Definition:** Order elements.
- **Visual explanation:** `Sorting` → process → result
- **Practical example:**

```python
print(sorted([3, 1, 2]))
```

### heapq

- **Definition:** Priority queue heap.
- **Visual explanation:** `heapq` → process → result
- **Practical example:**

```python
import heapq
h = [3, 1, 2]
heapq.heapify(h)
print(heapq.heappop(h))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Algorithm choice depends on n, constraints, and constants. |
| ⚡ Purpose | Solve problems within time/memory budgets. |
| 🔥 Benefits | Scalability, predictable latency. |
| 🎯 Use Cases | Top-K, scheduling, shortest path, dedupe. |
| 🚀 Best Practices | Use stdlib bisect/heapq; benchmark; document complexity. |
| ❌ Common Mistakes | O(n^2) on large n, wrong assumptions about sorted input. |

## Syntax Guide

### Basic Syntax

```python
import heapq
heapq.heappush(heap, item)
```

### Standard Structure

```python
model problem -> choose algo -> implement -> test edge cases
```

### Code Pattern

```python
import heapq
h = [3, 1, 2]
heapq.heapify(h)
print(heapq.heappop(h))
```

## Examples

### Beginner Example

```python
print(sorted(['b', 'a', 'c']))
```

### Intermediate Example

```python
import bisect

nums = [1, 3, 5, 7]
print(bisect.bisect_left(nums, 5))
```

### Advanced Example

```python
from collections import deque


def bfs(graph, start):
    seen = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph.get(node, []):
            if nei not in seen:
                seen.add(nei)
                queue.append(nei)
    return order


print(bfs({'A': ['B'], 'B': ['C']}, 'A'))
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Problem] --> B[Algorithm Choice]
    B --> C[Implementation]
    C --> D[Complexity Check]
```

---

# Design Patterns

## Overview

- **What is it?** Design patterns are reusable solutions to common software design problems.
- **Why is it important?** Shared vocabulary speeds design discussions and avoids reinventing wheels.
- **Where is it used?** Enterprise apps, frameworks, large teams, maintainability-focused code.

## Learning Objectives

- **Skills gained:** Practical command of Design Patterns.
- **Concepts covered:**

- Apply factory, strategy, observer, and adapter patterns.
- Map patterns to Python idioms.
- Avoid pattern overuse.

- **Expected outcome:** You structure code with proven design patterns when they fit.

## Real World Applications

- Enterprise Java/Python shops
- SDK design
- Plugin architectures
- Games

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Strategy

- **Definition:** Interchangeable algorithms.
- **Visual explanation:** `Strategy` → process → result
- **Practical example:**

```python
class Add:
    def apply(self, a, b):
        return a + b
print(Add().apply(2, 3))
```

### Factory

- **Definition:** Centralize object creation.
- **Visual explanation:** `Factory` → process → result
- **Practical example:**

```python
def user_factory(kind):
    return {'admin': dict(role='admin'), 'guest': dict(role='guest')}[kind]
print(user_factory('admin'))
```

### Observer

- **Definition:** Publish/subscribe.
- **Visual explanation:** `Observer` → process → result
- **Practical example:**

```python
class Bus:
    def __init__(self):
        self.listeners = []
    def subscribe(self, fn):
        self.listeners.append(fn)
    def emit(self, msg):
        for fn in self.listeners:
            fn(msg)
b = Bus()
b.subscribe(lambda m: None)
b.emit('hi')
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Patterns name recurring structure, not copy-paste code. |
| ⚡ Purpose | Improve flexibility and maintainability. |
| 🔥 Benefits | Team communication, extensibility. |
| 🎯 Use Cases | Payment strategies, notification bus, adapters for legacy APIs. |
| 🚀 Best Practices | Prefer simplicity; use patterns with clear pain point. |
| ❌ Common Mistakes | Pattern obsession, unnecessary abstraction layers. |

## Syntax Guide

### Basic Syntax

```python
class Strategy:
    def apply(self, value):
        return value


print(Strategy().apply(1))
```

### Standard Structure

```python
identify variation -> encapsulate -> compose
```

### Code Pattern

```python
context.set_strategy(concrete_strategy)
```

## Examples

### Beginner Example

```python
class Greeter:
    def greet(self, name):
        return f'Hello, {name}'


print(Greeter().greet('Ada'))
```

### Intermediate Example

```python
class Logger:
    def log(self, msg: str) -> None:
        print(msg)


class Service:
    def __init__(self, logger: Logger):
        self.logger = logger

    def run(self):
        self.logger.log('running')


Service(Logger()).run()
```

### Advanced Example

```python
from typing import Callable


class EventEmitter:
    def __init__(self):
        self._handlers: dict[str, list[Callable]] = {}

    def on(self, event: str, handler: Callable) -> None:
        self._handlers.setdefault(event, []).append(handler)

    def emit(self, event: str, payload):
        for handler in self._handlers.get(event, []):
            handler(payload)


bus = EventEmitter()
bus.on('created', lambda p: print('event', p))
bus.emit('created', {'id': 1})
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Problem] --> B[Pattern]
    B --> C[Components]
```

---

# SOLID Principles

## Overview

- **What is it?** SOLID principles guide object-oriented design for maintainable systems.
- **Why is it important?** They reduce coupling and make change safer in large codebases.
- **Where is it used?** Enterprise services, domain-driven design, long-lived products.

## Learning Objectives

- **Skills gained:** Practical command of SOLID Principles.
- **Concepts covered:**

- Explain SRP, OCP, LSP, ISP, DIP.
- Recognize violations in Python code.
- Refactor toward SOLID incrementally.

- **Expected outcome:** You evaluate designs using SOLID as a checklist.

## Real World Applications

- Enterprise software
- Banking platforms
- Healthcare systems
- B2B SaaS

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### SRP

- **Definition:** One reason to change per class.
- **Visual explanation:** `SRP` → process → result
- **Practical example:**

```python
class ReportWriter:
    def write(self, text):
        return text.upper()
print(ReportWriter().write('a'))
```

### OCP

- **Definition:** Open for extension, closed for modification.
- **Visual explanation:** `OCP` → process → result
- **Practical example:**

```python
class Tax:
    def rate(self):
        return 0.1
class ReducedTax(Tax):
    def rate(self):
        return 0.05
print(ReducedTax().rate())
```

### DIP

- **Definition:** Depend on abstractions.
- **Visual explanation:** `DIP` → process → result
- **Practical example:**

```python
class Repo:
    def save(self, data):
        return data
class Service:
    def __init__(self, repo: Repo):
        self.repo = repo
print(Service(Repo()).repo.save(1))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | SOLID favors composable, testable modules. |
| ⚡ Purpose | Manage complexity as systems grow. |
| 🔥 Benefits | Easier testing, safer refactors, clearer boundaries. |
| 🎯 Use Cases | Plugin systems, policy engines, multi-tenant apps. |
| 🚀 Best Practices | Small classes; inject dependencies; program to interfaces. |
| ❌ Common Mistakes | God objects, concrete imports everywhere, inheritance abuse. |

## Syntax Guide

### Basic Syntax

```python
# depend on Protocol/ABC interfaces, not concrete classes
```

### Standard Structure

```python
define abstraction -> implement -> inject
```

### Code Pattern

```python
class Service:
    def __init__(self, repo):
        self.repo = repo


print(Service(repo=object()))
```

## Examples

### Beginner Example

```python
class Formatter:
    def fmt(self, x):
        return str(x)
print(Formatter().fmt(1))
```

### Intermediate Example

```python
from typing import Protocol


class Notifier(Protocol):
    def send(self, message: str) -> None: ...


class EmailNotifier:
    def send(self, message: str) -> None:
        print(message)


def notify(user: str, notifier: Notifier) -> None:
    notifier.send(f'hello {user}')


notify('Ada', EmailNotifier())
```

### Advanced Example

```python
class DiscountPolicy:
    def discount(self, total: float) -> float:
        return total


class VIPDiscount(DiscountPolicy):
    def discount(self, total: float) -> float:
        return total * 0.9


class Checkout:
    def __init__(self, policy: DiscountPolicy):
        self.policy = policy

    def total(self, amount: float) -> float:
        return self.policy.discount(amount)


print(Checkout(VIPDiscount()).total(100))
```

## Workflow Diagram

```mermaid
flowchart TD
    A[SOLID] --> B[SRP]
    A --> C[OCP]
    A --> D[LSP]
    A --> E[ISP]
    A --> F[DIP]
```

---

# Memory Management

## Overview

- **What is it?** Memory management covers how Python allocates, uses, and releases object memory.
- **Why is it important?** Memory leaks and bloat cause crashes and cost in production.
- **Where is it used?** Long-running services, data processing, ML training, embedded Python.

## Learning Objectives

- **Skills gained:** Practical command of Memory Management.
- **Concepts covered:**

- Understand object sizes and references.
- Use sys.getsizeof and tracemalloc.
- Break reference cycles thoughtfully.

- **Expected outcome:** You diagnose and reduce memory usage in Python programs.

## Real World Applications

- Streaming ETL
- Web workers
- Scientific computing
- Ad tech

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### References

- **Definition:** Names point to objects.
- **Visual explanation:** `References` → process → result
- **Practical example:**

```python
import sys
a = []
b = a
print(sys.getrefcount(a) > 1)
```

### getsizeof

- **Definition:** Shallow object size.
- **Visual explanation:** `getsizeof` → process → result
- **Practical example:**

```python
import sys
print(sys.getsizeof([]))
```

### tracemalloc

- **Definition:** Track allocations.
- **Visual explanation:** `tracemalloc` → process → result
- **Practical example:**

```python
import tracemalloc
tracemalloc.start()
x = [0] * 1000
print(tracemalloc.get_traced_memory()[0] > 0)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | CPython uses reference counting plus cyclic GC. |
| ⚡ Purpose | Use memory efficiently and avoid leaks. |
| 🔥 Benefits | Stability, lower cloud bills, faster caches. |
| 🎯 Use Cases | Batch jobs, caches, image/audio buffers. |
| 🚀 Best Practices | Profile before optimizing; use generators; weakref caches. |
| ❌ Common Mistakes | Global caches without bounds, circular refs with __del__, huge lists. |

## Syntax Guide

### Basic Syntax

```python
import sys
sys.getsizeof(obj)
```

### Standard Structure

```python
measure -> identify hotspots -> reduce retention
```

### Code Pattern

```python
for chunk in read_chunks(): process(chunk)
```

## Examples

### Beginner Example

```python
import sys
print(sys.getsizeof('hello'))
```

### Intermediate Example

```python
import tracemalloc

tracemalloc.start()
data = bytearray(10_000)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(peak > current)
```

### Advanced Example

```python
import gc

gc.set_threshold(700, 10, 10)
objects = [{} for _ in range(100)]
del objects
print(gc.collect() >= 0)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Objects] --> B[Refcount]
    B --> C[GC Cycles]
    C --> D[Free Memory]
```

---

# Garbage Collection

## Overview

- **What is it?** Garbage collection reclaims memory from unreachable objects, especially cycles.
- **Why is it important?** Reference cycles alone would leak memory without cyclic GC.
- **Where is it used?** Graphs, linked structures, long-lived caches, ORM identity maps.

## Learning Objectives

- **Skills gained:** Practical command of Garbage Collection.
- **Concepts covered:**

- Explain refcount vs generational GC.
- Use gc module for debugging.
- Design to minimize cycles.

- **Expected outcome:** You understand when Python frees objects and how to debug retention.

## Real World Applications

- Game servers
- Graph analytics
- Desktop apps
- ORM-heavy web apps

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### refcount

- **Definition:** Immediate reclaim when zero.
- **Visual explanation:** `refcount` → process → result
- **Practical example:**

```python
import sys
obj = object()
print(sys.getrefcount(obj) >= 2)
```

### gc.collect

- **Definition:** Force collection.
- **Visual explanation:** `gc.collect` → process → result
- **Practical example:**

```python
import gc
print(isinstance(gc.collect(), int))
```

### generations

- **Definition:** GC generations 0/1/2.
- **Visual explanation:** `generations` → process → result
- **Practical example:**

```python
import gc
print(len(gc.get_threshold()) == 3)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Generational GC tracks container objects in cycles. |
| ⚡ Purpose | Reclaim cyclic garbage automatically. |
| 🔥 Benefits | Less manual memory management than C. |
| 🎯 Use Cases | Linked lists, parent/child trees, observer graphs. |
| 🚀 Best Practices | Use weakref for caches; avoid __del__ complexity. |
| ❌ Common Mistakes | Creating unbounded cycles, disabling GC without reason. |

## Syntax Guide

### Basic Syntax

```python
import gc
gc.collect()
```

### Standard Structure

```python
allocate -> use -> dereference -> GC runs
```

### Code Pattern

```python
import weakref
weakref.ref(obj)
```

## Examples

### Beginner Example

```python
import gc
print(gc.isenabled())
```

### Intermediate Example

```python
import gc

class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b
b.ref = a
del a, b
print(gc.collect() >= 0)
```

### Advanced Example

```python
import weakref


class Cache:
    def __init__(self):
        self._items = {}

    def set(self, key, value):
        self._items[key] = weakref.ref(value)

    def get(self, key):
        ref = self._items.get(key)
        return ref() if ref else None


c = Cache()
obj = {'a': 1}
c.set('k', obj)
print(c.get('k'))
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Objects] --> B{Reachable?}
    B -->|no| C[GC Collect]
    B -->|yes| D[Keep]
```

---

# Python Internals

## Overview

- **What is it?** Python internals cover bytecode, the evaluation loop, and CPython implementation details.
- **Why is it important?** Internals explain performance characteristics and debugging mysteries.
- **Where is it used?** Performance tuning, compiler tooling, advanced debugging, C extensions.

## Learning Objectives

- **Skills gained:** Practical command of Python Internals.
- **Concepts covered:**

- Inspect bytecode with dis.
- Explain frame objects and namespaces.
- Understand GIL at high level.

- **Expected outcome:** You read dis output and understand how CPython executes code.

## Real World Applications

- Language tooling
- High-performance Python
- Security research
- Compiler dev

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### bytecode

- **Definition:** Stack machine instructions.
- **Visual explanation:** `bytecode` → process → result
- **Practical example:**

```python
import dis
dis.dis('a=1')
```

### frame

- **Definition:** Execution frame with locals.
- **Visual explanation:** `frame` → process → result
- **Practical example:**

```python
def f():
    x = 1
    return x
print(f())
```

### GIL

- **Definition:** Global interpreter lock.
- **Visual explanation:** `GIL` → process → result
- **Practical example:**

```python
import sys
print(hasattr(sys, 'version'))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | CPython compiles to bytecode interpreted by the eval loop. |
| ⚡ Purpose | Deepen mental model of Python execution. |
| 🔥 Benefits | Better optimization instincts, clearer profiling. |
| 🎯 Use Cases | Hot path optimization, custom profilers, REPL tools. |
| 🚀 Best Practices | Profile first; consider PyPy/C extensions for hot loops. |
| ❌ Common Mistakes | Micro-optimizing without measurement, fighting the GIL blindly. |

## Syntax Guide

### Basic Syntax

```python
import dis
dis.dis(func)
```

### Standard Structure

```python
source -> compile -> bytecode -> eval loop
```

### Code Pattern

```python
dis.dis(compile('x=1', '<s>', 'exec'))
```

## Examples

### Beginner Example

```python
import dis
dis.dis(lambda x: x + 1)
```

### Intermediate Example

```python
import dis


def add(a, b):
    return a + b


dis.dis(add)
```

### Advanced Example

```python
import types

code = compile('result = 40 + 2', '<string>', 'exec')
namespace = {}
exec(code, namespace)
print(namespace['result'])
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Source] --> B[Compile]
    B --> C[Bytecode]
    C --> D[Eval Loop]
```

---

# Metaclasses

## Overview

- **What is it?** Metaclasses are classes that create classes, hooking into class construction.
- **Why is it important?** Frameworks use metaclasses for ORMs, validation, and API registries.
- **Where is it used?** Django models, dataclass-like codegen, plugin registration, singletons.

## Learning Objectives

- **Skills gained:** Practical command of Metaclasses.
- **Concepts covered:**

- Explain type and class creation.
- Write a simple metaclass.
- Know when class decorators suffice.

- **Expected outcome:** You understand metaclass use cases and implement simple ones.

## Real World Applications

- Web frameworks
- Code generators
- Enterprise DSLs
- Testing frameworks

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### type

- **Definition:** Default metaclass.
- **Visual explanation:** `type` → process → result
- **Practical example:**

```python
class A: pass
print(type(A))
```

### __new__

- **Definition:** Metaclass creates class.
- **Visual explanation:** `__new__` → process → result
- **Practical example:**

```python
class Meta(type):
    def __new__(mcls, name, bases, ns):
        ns['tag'] = name.lower()
        return super().__new__(mcls, name, bases, ns)
class A(metaclass=Meta): pass
print(A.tag)
```

### __init__

- **Definition:** Initialize created class.
- **Visual explanation:** `__init__` → process → result
- **Practical example:**

```python
class Meta(type):
    def __init__(cls, name, bases, ns):
        super().__init__(name, bases, ns)
        cls.created = True
class B(metaclass=Meta): pass
print(B.created)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Metaclasses customize class object creation. |
| ⚡ Purpose | Framework-level automation and enforcement. |
| 🔥 Benefits | Centralized registration, enforced conventions. |
| 🎯 Use Cases | ORM field collection, API route tables, interface enforcement. |
| 🚀 Best Practices | Prefer simpler hooks first; document heavily. |
| ❌ Common Mistakes | Metaclass for everything, incomprehensible MRO interactions. |

## Syntax Guide

### Basic Syntax

```python
class Meta(type):
    pass


class MyClass(metaclass=Meta):
    pass


print(MyClass.__name__)
```

### Standard Structure

```python
metaclass __new__/__init__ -> class object
```

### Code Pattern

```python
class Registry(type):
    registry = {}

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        registry = mcls.registry
        registry[name] = cls
        return cls


print(callable(Registry))
```

## Examples

### Beginner Example

```python
print(type(int))
```

### Intermediate Example

```python
class PluginMeta(type):
    plugins = {}

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        if name != 'PluginBase':
            mcls.plugins[name] = cls
        return cls


class PluginBase(metaclass=PluginMeta):
    pass


class EmailPlugin(PluginBase):
    pass


print('EmailPlugin' in PluginMeta.plugins)
```

### Advanced Example

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.env = 'prod'


print(Config() is Config())
```

## Workflow Diagram

```mermaid
flowchart LR
    A[metaclass] --> B[class object]
    B --> C[instances]
```

---

# Descriptors

## Overview

- **What is it?** Descriptors implement __get__, __set__, or __delete__ to customize attribute access.
- **Why is it important?** They power properties, ORM fields, and validated attributes.
- **Where is it used?** Frameworks, data models, lazy computed fields, cached attributes.

## Learning Objectives

- **Skills gained:** Practical command of Descriptors.
- **Concepts covered:**

- Implement descriptor protocol.
- Understand data vs non-data descriptors.
- Use property as descriptor shortcut.

- **Expected outcome:** You control attribute access with descriptors and properties.

## Real World Applications

- ORMs
- Validation libraries
- Game engines
- Financial models

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### __get__

- **Definition:** Customize read.
- **Visual explanation:** `__get__` → process → result
- **Practical example:**

```python
class D:
    def __get__(self, obj, owner):
        return 42
class A:
    x = D()
print(A().x)
```

### __set__

- **Definition:** Customize write.
- **Visual explanation:** `__set__` → process → result
- **Practical example:**

```python
class Positive:
    def __set__(self, obj, value):
        if value < 0: raise ValueError
        obj._v = value
    def __get__(self, obj, owner):
        return obj._v
class Account:
    balance = Positive()
a = Account()
a.balance = 10
print(a.balance)
```

### property

- **Definition:** Built-in descriptor.
- **Visual explanation:** `property` → process → result
- **Practical example:**

```python
class C:
    def __init__(self):
        self._n = 0
    @property
    def n(self):
        return self._n
print(C().n)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Descriptors intercept dot access on classes. |
| ⚡ Purpose | Reuse attribute logic across classes. |
| 🔥 Benefits | DRY validation, lazy loading, typed fields. |
| 🎯 Use Cases | Validated setters, cached properties, ORM columns. |
| 🚀 Best Practices | Use property first; descriptor for reuse across classes. |
| ❌ Common Mistakes | Infinite recursion in __get__, confusing data descriptor priority. |

## Syntax Guide

### Basic Syntax

```python
class Desc:
    def __get__(self, obj, owner=None):
        return 42


class Host:
    value = Desc()


print(Host().value)
```

### Standard Structure

```python
define descriptor -> assign to class -> access via instance
```

### Code Pattern

```python
class Model:
    @property
    def field(self):
        return self._field


m = Model()
m._field = 1
print(m.field)
```

## Examples

### Beginner Example

```python
class Echo:
    def __get__(self, obj, owner):
        return 'echo'


class Host:
    msg = Echo()


print(Host().msg)
```

### Intermediate Example

```python
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, owner):
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('wrong type')
        obj.__dict__[self.name] = value


class User:
    age = Typed('age', int)


u = User()
u.age = 30
print(u.age)
```

### Advanced Example

```python
class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, obj, owner):
        if obj is None:
            return self
        value = self.func(obj)
        setattr(obj, self.name, value)
        return value


class Data:
    @LazyProperty
    def expensive(self):
        return sum(range(1000))


d = Data()
print(d.expensive == d.expensive)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[obj.attr] --> B[Descriptor __get__]
    B --> C[Value]
```

---

# Concurrency

## Overview

- **What is it?** Concurrency coordinates multiple tasks making progress without necessarily running in parallel.
- **Why is it important?** Users expect responsive systems during I/O and background work.
- **Where is it used?** Web servers, UI backends, job orchestration, streaming.

## Learning Objectives

- **Skills gained:** Practical command of Concurrency.
- **Concepts covered:**

- Contrast concurrency vs parallelism.
- Combine threads and async appropriately.
- Use queues for producer/consumer.

- **Expected outcome:** You design systems where tasks overlap safely.

## Real World Applications

- Realtime dashboards
- Chat
- Trading feeds
- IoT hubs

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Concurrency

- **Definition:** Tasks interleave progress.
- **Visual explanation:** `Concurrency` → process → result
- **Practical example:**

```python
import asyncio
async def task():
    return 1
print(asyncio.run(task()))
```

### Parallelism

- **Definition:** Simultaneous CPU execution.
- **Visual explanation:** `Parallelism` → process → result
- **Practical example:**

```python
print('use multiprocessing for CPU parallel')
```

### Queue

- **Definition:** Coordinate workers.
- **Visual explanation:** `Queue` → process → result
- **Practical example:**

```python
from queue import Queue
q = Queue()
q.put(1)
print(q.get())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Concurrency manages many tasks; parallelism uses multiple cores. |
| ⚡ Purpose | Improve throughput and responsiveness. |
| 🔥 Benefits | Better resource utilization, smoother UX. |
| 🎯 Use Cases | Download managers, job workers, server request handling. |
| 🚀 Best Practices | Match tool to workload; bound queues; monitor backlog. |
| ❌ Common Mistakes | Threads for CPU-bound, unbounded task spawning, no backpressure. |

## Syntax Guide

### Basic Syntax

```python
queue.put(item)
item = queue.get()
```

### Standard Structure

```python
producers -> queue -> consumers
```

### Code Pattern

```python
asyncio.create_task(coro)
```

## Examples

### Beginner Example

```python
from queue import Queue
q = Queue()
q.put('job')
print(q.get())
```

### Intermediate Example

```python
import asyncio

async def worker(name, delay):
    await asyncio.sleep(delay)
    return name

async def main():
    results = await asyncio.gather(worker('a', 0.01), worker('b', 0.01))
    print(sorted(results))

asyncio.run(main())
```

### Advanced Example

```python
import threading
from queue import Queue


def consumer(q: Queue, out: list):
    while True:
        item = q.get()
        if item is None:
            break
        out.append(item * 2)
        q.task_done()


q = Queue()
out = []
t = threading.Thread(target=consumer, args=(q, out))
t.start()
q.put(21)
q.put(None)
t.join()
print(out)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Tasks] --> B[Scheduler]
    B --> C[Workers]
```

---

# Parallel Computing

## Overview

- **What is it?** Parallel computing executes computations simultaneously across cores or machines.
- **Why is it important?** CPU-heavy workloads need parallelism to meet latency SLAs.
- **Where is it used?** NumPy, multiprocessing, Spark, GPU offload, simulation.

## Learning Objectives

- **Skills gained:** Practical command of Parallel Computing.
- **Concepts covered:**

- Use process pools for CPU parallelism.
- Partition data for workers.
- Understand Amdahl's law limits.

- **Expected outcome:** You scale CPU-bound Python workloads across cores.

## Real World Applications

- Quant
- Rendering
- Scientific HPC
- ML feature gen

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Process pool

- **Definition:** Multiple interpreters.
- **Visual explanation:** `Process pool` → process → result
- **Practical example:**

```python
from concurrent.futures import ProcessPoolExecutor
print(ProcessPoolExecutor)
```

### map

- **Definition:** Apply func across inputs.
- **Visual explanation:** `map` → process → result
- **Practical example:**

```python
print(list(map(lambda x: x * 2, [1, 2, 3])))
```

### chunking

- **Definition:** Split data for workers.
- **Visual explanation:** `chunking` → process → result
- **Practical example:**

```python
data = list(range(10))
chunks = [data[i:i+3] for i in range(0, len(data), 3)]
print(len(chunks))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Parallelism requires independent work units and merges results. |
| ⚡ Purpose | Reduce wall-clock time for heavy compute. |
| 🔥 Benefits | Faster batch jobs, higher hardware utilization. |
| 🎯 Use Cases | Monte Carlo, image filters, large transforms. |
| 🚀 Best Practices | Minimize IPC; profile serial vs parallel; pick chunk sizes. |
| ❌ Common Mistakes | Tiny tasks overhead, pickle overhead, no speedup due to serial sections. |

## Syntax Guide

### Basic Syntax

```python
with ProcessPoolExecutor() as pool:
    pool.map(func, items)
```

### Standard Structure

```python
partition -> map workers -> reduce results
```

### Code Pattern

```python
pool.map(process_chunk, chunks)
```

## Examples

### Beginner Example

```python
print(sum(map(lambda x: x * x, range(5))))
```

### Intermediate Example

```python
from concurrent.futures import ProcessPoolExecutor


def square(n: int) -> int:
    return n * n


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as pool:
        print(list(pool.map(square, range(4))))
```

### Advanced Example

```python
def parallel_sum(numbers, workers=2):
    size = len(numbers) // workers or 1
    chunks = [numbers[i:i + size] for i in range(0, len(numbers), size)]
    partials = [sum(chunk) for chunk in chunks]
    return sum(partials)


print(parallel_sum(list(range(10)), workers=2))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Input Data] --> B[Partition]
    B --> C[Workers]
    C --> D[Reduce]
```

---

# Distributed Systems

## Overview

- **What is it?** Distributed systems coordinate multiple nodes over unreliable networks.
- **Why is it important?** Scale and fault tolerance require multiple machines and services.
- **Where is it used?** Microservices, Kafka pipelines, cloud storage, global SaaS.

## Learning Objectives

- **Skills gained:** Practical command of Distributed Systems.
- **Concepts covered:**

- Explain CAP tradeoffs at high level.
- Design idempotent workers and retries.
- Use message queues and service discovery.

- **Expected outcome:** You reason about failure modes in distributed Python systems.

## Real World Applications

- Cloud platforms
- Streaming
- Global e-commerce
- Fintech

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Idempotency

- **Definition:** Safe retries.
- **Visual explanation:** `Idempotency` → process → result
- **Practical example:**

```python
def charge(idempotency_key, amount):
    seen = set()
    if idempotency_key in seen:
        return 'duplicate'
    seen.add(idempotency_key)
    return f'charged {amount}'
print(charge('k1', 10))
```

### Timeouts

- **Definition:** Bound waiting.
- **Visual explanation:** `Timeouts` → process → result
- **Practical example:**

```python
import socket
socket.setdefaulttimeout(5.0)
print(socket.getdefaulttimeout())
```

### Message queue

- **Definition:** Async decoupling.
- **Visual explanation:** `Message queue` → process → result
- **Practical example:**

```python
QUEUE = []
QUEUE.append({'task': 1})
print(QUEUE.pop(0))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Network partitions and latency are inevitable. |
| ⚡ Purpose | Build reliable multi-node applications. |
| 🔥 Benefits | Scale, isolation, geographic distribution. |
| 🎯 Use Cases | Order processing, event buses, crawl fleets. |
| 🚀 Best Practices | Design for failure; observability; sagas; idempotent handlers. |
| ❌ Common Mistakes | Single point of failure, no retries, distributed monolith coupling. |

## Syntax Guide

### Basic Syntax

```python
# worker consumes message -> process -> ack
```

### Standard Structure

```python
producer -> queue -> consumer -> store
```

### Code Pattern

```python
def retry_delay(attempt: int, base: float = 0.1) -> float:
    return base * (2 ** attempt)


print(retry_delay(2))
```

## Examples

### Beginner Example

```python
jobs = []
jobs.append('email')
print(jobs.pop())
```

### Intermediate Example

```python
def handle_event(event, processed: set):
    event_id = event['id']
    if event_id in processed:
        return 'skipped'
    processed.add(event_id)
    return 'handled'


print(handle_event({'id': '1'}, set()))
```

### Advanced Example

```python
import hashlib


def shard_for(key: str, num_shards: int) -> int:
    digest = hashlib.md5(key.encode(), usedforsecurity=False).hexdigest()
    return int(digest, 16) % num_shards


print(shard_for('user-42', 8))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Service A] --> B[Queue]
    B --> C[Service B]
    C --> D[Database]
```

---

# Network Programming

## Overview

- **What is it?** Network programming sends and receives data over TCP/IP and application protocols.
- **Why is it important?** Distributed apps communicate via sockets, HTTP, and messaging.
- **Where is it used?** Clients, servers, proxies, IoT gateways, custom protocols.

## Learning Objectives

- **Skills gained:** Practical command of Network Programming.
- **Concepts covered:**

- Understand IP, ports, TCP vs UDP.
- Use socket API basics.
- Handle timeouts and buffering.

- **Expected outcome:** You implement basic network clients and servers in Python.

## Real World Applications

- Telecom
- Gaming netcode
- IoT
- Custom protocols

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### TCP

- **Definition:** Reliable stream.
- **Visual explanation:** `TCP` → process → result
- **Practical example:**

```python
import socket
print(socket.SOCK_STREAM)
```

### UDP

- **Definition:** Datagram protocol.
- **Visual explanation:** `UDP` → process → result
- **Practical example:**

```python
import socket
print(socket.SOCK_DGRAM)
```

### socket

- **Definition:** Endpoint abstraction.
- **Visual explanation:** `socket` → process → result
- **Practical example:**

```python
import socket
s = socket.socket()
print(type(s).__name__)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Sockets are the foundation beneath HTTP and many protocols. |
| ⚡ Purpose | Move bytes between hosts reliably or quickly. |
| 🔥 Benefits | Full control, custom protocols, low-level tooling. |
| 🎯 Use Cases | Echo server, metrics agent, device firmware comms. |
| 🚀 Best Practices | Set timeouts; handle partial reads; close sockets in finally. |
| ❌ Common Mistakes | Blocking forever, no framing, ignoring endianness in binary protocols. |

## Syntax Guide

### Basic Syntax

```python
import socket
sock = socket.create_connection(('example.com', 80), timeout=5)
```

### Standard Structure

```python
create socket -> connect/bind -> send/recv -> close
```

### Code Pattern

```python
with socket.create_connection(addr) as s: s.sendall(data)
```

## Examples

### Beginner Example

```python
import socket
print(socket.gethostname())
```

### Intermediate Example

```python
import socket

def recv_all(sock, size: int) -> bytes:
    chunks = []
    while len(b''.join(chunks)) < size:
        chunk = sock.recv(size - len(b''.join(chunks)))
        if not chunk:
            break
        chunks.append(chunk)
    return b''.join(chunks)


print(callable(recv_all))
```

### Advanced Example

```python
import selectors
import socket


def echo_server():
    sel = selectors.DefaultSelector()
    sock = socket.socket()
    sock.bind(('127.0.0.1', 0))
    sock.listen()
    sel.register(sock, selectors.EVENT_READ)
    return sock, sel


s, sel = echo_server()
print(s.getsockname()[1] > 0)
s.close()
sel.close()
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Client Socket] --> B[Network]
    B --> C[Server Socket]
```

---

# Socket Programming

## Overview

- **What is it?** Socket programming implements clients and servers using BSD sockets API.
- **Why is it important?** Low-level control is needed for custom services and performance-sensitive I/O.
- **Where is it used?** Chat servers, game servers, proxies, embedded agents.

## Learning Objectives

- **Skills gained:** Practical command of Socket Programming.
- **Concepts covered:**

- Build TCP echo client/server.
- Handle bind/listen/accept.
- Use non-blocking or asyncio streams.

- **Expected outcome:** You write minimal socket-based networked programs.

## Real World Applications

- Multiplayer games
- VPN tooling
- Industrial IoT
- Media streaming

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### bind/listen

- **Definition:** Server waits for connections.
- **Visual explanation:** `bind/listen` → process → result
- **Practical example:**

```python
import socket
s = socket.socket()
s.bind(('127.0.0.1', 0))
print(s.getsockname()[1] > 0)
s.close()
```

### connect

- **Definition:** Client initiates TCP.
- **Visual explanation:** `connect` → process → result
- **Practical example:**

```python
import socket
s = socket.socket()
try:
    s.connect(('127.0.0.1', 9))
except OSError:
    pass
finally:
    s.close()
```

### send/recv

- **Definition:** Transfer bytes.
- **Visual explanation:** `send/recv` → process → result
- **Practical example:**

```python
import socket
a, b = socket.socketpair()
a.send(b'ping')
print(b.recv(4))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Stream sockets deliver ordered byte pipes. |
| ⚡ Purpose | Implement custom network endpoints. |
| 🔥 Benefits | Minimal dependencies, full protocol control. |
| 🎯 Use Cases | Echo, heartbeat, binary framing, LAN tools. |
| 🚀 Best Practices | Use asyncio streams for many connections; always timeout. |
| ❌ Common Mistakes | No message framing, one recv equals one message assumption. |

## Syntax Guide

### Basic Syntax

```python
sock.sendall(b'data')
data = sock.recv(1024)
```

### Standard Structure

```python
socket -> bind/connect -> send/recv loop -> shutdown
```

### Code Pattern

```python
class Server:
    def accept(self):
        return 'connection'


class Client:
    def connect(self):
        return 'connected'


print(Server().accept(), Client().connect())
```

## Examples

### Beginner Example

```python
import socket

client, server = socket.socketpair()
client.send(b'hello')
print(server.recv(5))
```

### Intermediate Example

```python
import socket


def run_echo_once():
    server = socket.socket()
    server.bind(('127.0.0.1', 0))
    server.listen(1)
    port = server.getsockname()[1]
    client = socket.socket()
    client.connect(('127.0.0.1', port))
    conn, _ = server.accept()
    conn.sendall(b'pong')
    print(client.recv(4))
    conn.close()
    client.close()
    server.close()


run_echo_once()
```

### Advanced Example

```python
import asyncio


async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    data = await reader.read(100)
    writer.write(data.upper())
    await writer.drain()
    writer.close()


async def main():
    server = await asyncio.start_server(handle, '127.0.0.1', 0)
    addr = server.sockets[0].getsockname()
    reader, writer = await asyncio.open_connection(*addr)
    writer.write(b'hi')
    await writer.drain()
    print((await reader.read(10)).decode())
    writer.close()
    server.close()


asyncio.run(main())
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Server bind/listen] --> B[accept]
    B --> C[recv/send loop]
```

---

# Cybersecurity Automation

## Overview

- **What is it?** Cybersecurity automation uses Python to orchestrate scans, parsing, and response workflows.
- **Why is it important?** Security teams must scale repetitive analysis and enrichment tasks.
- **Where is it used?** SOAR platforms, vuln management, log enrichment, phishing analysis.

## Learning Objectives

- **Skills gained:** Practical command of Cybersecurity Automation.
- **Concepts covered:**

- Parse logs and IOCs with Python.
- Call security APIs safely.
- Automate repeatable playbooks.

- **Expected outcome:** You build Python automations that support security operations.

## Real World Applications

- SOC teams
- MSSP
- AppSec
- Compliance automation

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### IOC parsing

- **Definition:** Extract indicators.
- **Visual explanation:** `IOC parsing` → process → result
- **Practical example:**

```python
import re
line = '1.2.3.4 failed login'
print(re.findall(r'\d+\.\d+\.\d+\.\d+', line))
```

### Hashing

- **Definition:** Fingerprint files.
- **Visual explanation:** `Hashing` → process → result
- **Practical example:**

```python
import hashlib
print(hashlib.sha256(b'data').hexdigest()[:8])
```

### Automation script

- **Definition:** Schedule repeatable tasks.
- **Visual explanation:** `Automation script` → process → result
- **Practical example:**

```python
def run_playbook():
    return ['parsed', 'enriched']
print(run_playbook())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Automate verify-enrich-respond loops with scripts. |
| ⚡ Purpose | Reduce manual toil and response time. |
| 🔥 Benefits | Consistency, speed, audit trails. |
| 🎯 Use Cases | Phish triage, CVE ticket creation, firewall rule audits. |
| 🚀 Best Practices | Least privilege creds; validate inputs; log actions; dry-run mode. |
| ❌ Common Mistakes | Running unverified scripts as root, storing secrets in code. |

## Syntax Guide

### Basic Syntax

```python
import hashlib
hashlib.sha256(data).hexdigest()
```

### Standard Structure

```python
ingest -> parse -> enrich -> ticket/action
```

### Code Pattern

```python
for alert in alerts:
    enrich(alert)
    if severity(alert): escalate(alert)
```

## Examples

### Beginner Example

```python
import re
print(bool(re.search(r'ERROR', 'ERROR login failed')))
```

### Intermediate Example

```python
import hashlib


def file_sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


print(len(file_sha256(__file__)) == 64)
```

### Advanced Example

```python
from dataclasses import dataclass


@dataclass
class Alert:
    ip: str
    severity: int


def triage(alerts: list[Alert]) -> list[Alert]:
    return sorted([a for a in alerts if a.severity >= 7], key=lambda a: -a.severity)


print(triage([Alert('1.2.3.4', 8), Alert('5.6.7.8', 3)]))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Alert Feed] --> B[Parser]
    B --> C[Enrichment]
    C --> D[Response]
```

---

# Web Scraping

## Overview

- **What is it?** Web scraping extracts structured data from HTML and HTTP responses.
- **Why is it important?** Public data powers research, monitoring, and competitive intelligence when permitted.
- **Where is it used?** Price monitoring, news aggregation, lead gen (compliant), archival.

## Learning Objectives

- **Skills gained:** Practical command of Web Scraping.
- **Concepts covered:**

- Fetch pages responsibly with timeouts.
- Parse HTML with BeautifulSoup or lxml.
- Respect robots.txt and rate limits.

- **Expected outcome:** You extract structured fields from web pages ethically and robustly.

## Real World Applications

- Market intelligence
- SEO
- Research
- Compliance monitoring

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### HTTP fetch

- **Definition:** Retrieve page content.
- **Visual explanation:** `HTTP fetch` → process → result
- **Practical example:**

```python
HTML = '<html><title>Hi</title></html>'
print('Hi' in HTML)
```

### HTML parse

- **Definition:** Navigate DOM tree.
- **Visual explanation:** `HTML parse` → process → result
- **Practical example:**

```python
from html.parser import HTMLParser
class P(HTMLParser):
    def handle_starttag(self, tag, attrs):
        self.tag = tag
p = P()
p.feed('<div></div>')
print(p.tag)
```

### CSS/selectors

- **Definition:** Target elements.
- **Visual explanation:** `CSS/selectors` → process → result
- **Practical example:**

```python
from html.parser import HTMLParser
print('title' in '<title>x</title>')
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Scraping = fetch + parse + normalize + store. |
| ⚡ Purpose | Turn web pages into datasets. |
| 🔥 Benefits | Automation of manual copy/paste research. |
| 🎯 Use Cases | Product prices, job listings, metadata harvest. |
| 🚀 Best Practices | Rate limit; identify bot; check Terms of Service; cache. |
| ❌ Common Mistakes | Ignoring robots, brittle regex-only parsing, no backoff. |

## Syntax Guide

### Basic Syntax

```python
html = fetch(url)
soup.select('h1.title')
```

### Standard Structure

```python
fetch -> parse -> extract -> validate -> save
```

### Code Pattern

```python
for page in pages:
    for item in parse(page):
        store(item)
```

## Examples

### Beginner Example

```python
title = 'Sample'
print(title.lower())
```

### Intermediate Example

```python
from html.parser import HTMLParser


class TitleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.title = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.in_title = True

    def handle_data(self, data):
        if self.in_title:
            self.title += data

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False


parser = TitleParser()
parser.feed('<html><title>Hello</title></html>')
print(parser.title)
```

### Advanced Example

```python
import time


class RateLimiter:
    def __init__(self, min_interval: float):
        self.min_interval = min_interval
        self.last = 0.0

    def wait(self):
        now = time.monotonic()
        elapsed = now - self.last
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last = time.monotonic()


limiter = RateLimiter(0.01)
limiter.wait()
print('fetched')
```

## Workflow Diagram

```mermaid
flowchart LR
    A[HTTP GET] --> B[HTML]
    B --> C[Parser]
    C --> D[Data]
```

---

# Automation Frameworks

## Overview

- **What is it?** Automation frameworks structure reusable test and RPA-style automation (Selenium, Playwright, Robot).
- **Why is it important?** Ad-hoc scripts become unmaintainable without page objects and reporting.
- **Where is it used?** QA automation, browser testing, IT RPA, regression suites.

## Learning Objectives

- **Skills gained:** Practical command of Automation Frameworks.
- **Concepts covered:**

- Organize tests with page object model.
- Use fixtures and waits properly.
- Integrate automation into CI.

- **Expected outcome:** You build maintainable automation suites with frameworks.

## Real World Applications

- QA teams
- SaaS releases
- E-commerce
- Banking UAT

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Page Object

- **Definition:** Encapsulate UI locators.
- **Visual explanation:** `Page Object` → process → result
- **Practical example:**

```python
class LoginPage:
    def username(self):
        return '#user'
print(LoginPage().username())
```

### Waits

- **Definition:** Handle async UI.
- **Visual explanation:** `Waits` → process → result
- **Practical example:**

```python
import time
time.sleep(0)
print('ready')
```

### Test runner

- **Definition:** Execute suite.
- **Visual explanation:** `Test runner` → process → result
- **Practical example:**

```python
TESTS = [lambda: True]
print(all(t() for t in TESTS))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Frameworks separate test logic from UI details. |
| ⚡ Purpose | Reliable repeatable automation at scale. |
| 🔥 Benefits | Maintainability, parallel runs, reporting plugins. |
| 🎯 Use Cases | Smoke tests, checkout flows, admin consoles. |
| 🚀 Best Practices | Stable selectors; explicit waits; screenshot on failure. |
| ❌ Common Mistakes | sleep-only sync, duplicated selectors, flaky shared state. |

## Syntax Guide

### Basic Syntax

```python
page.click('#submit')
assert page.text('#msg') == 'OK'
```

### Standard Structure

```python
pages -> tests -> runner -> reports
```

### Code Pattern

```python
class LoginPage:
    def open(self):
        return self

    def login(self, user, password):
        return user


print(LoginPage().open().login('ada', 'secret'))
```

## Examples

### Beginner Example

```python
def test_true():
    assert True
test_true()
```

### Intermediate Example

```python
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def title(self):
        return self.driver.get('title')


class FakeDriver:
    def get(self, key):
        return {'title': 'Home'}[key]


print(HomePage(FakeDriver()).title())
```

### Advanced Example

```python
class TestCase:
    def __init__(self, name, fn):
        self.name = name
        self.fn = fn

    def run(self):
        try:
            self.fn()
            return self.name, True
        except AssertionError:
            return self.name, False


suite = [TestCase('login', lambda: True)]
print([tc.run() for tc in suite])
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Test Runner] --> B[Page Objects]
    B --> C[Browser Driver]
```

---

# ETL Development

## Overview

- **What is it?** ETL development extracts, transforms, and loads data between systems.
- **Why is it important?** Business analytics requires clean consolidated datasets from many sources.
- **Where is it used?** Warehouses, lakes, marketing ops, finance reporting.

## Learning Objectives

- **Skills gained:** Practical command of ETL Development.
- **Concepts covered:**

- Design idempotent batch pipelines.
- Validate and quarantine bad records.
- Track lineage and batch metadata.

- **Expected outcome:** You implement reliable Python ETL jobs.

## Real World Applications

- Data teams
- Retail analytics
- Healthcare reporting
- Ad tech

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Extract

- **Definition:** Read from source.
- **Visual explanation:** `Extract` → process → result
- **Practical example:**

```python
rows = [{'id': 1, 'v': 'a'}]
print(len(rows))
```

### Transform

- **Definition:** Clean and reshape.
- **Visual explanation:** `Transform` → process → result
- **Practical example:**

```python
clean = [{**r, 'v': r['v'].upper()} for r in rows]
print(clean[0]['v'])
```

### Load

- **Definition:** Write to destination.
- **Visual explanation:** `Load` → process → result
- **Practical example:**

```python
dest = []
dest.extend(clean)
print(dest[0]['id'])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | ETL moves data with quality gates. |
| ⚡ Purpose | Feed analytics and downstream apps. |
| 🔥 Benefits | Repeatable batches, auditable transforms. |
| 🎯 Use Cases | Nightly sales sync, CRM to warehouse, log aggregation. |
| 🚀 Best Practices | Schema contracts; dead-letter queues; incremental loads. |
| ❌ Common Mistakes | No validation, non-idempotent loads, silent row drops. |

## Syntax Guide

### Basic Syntax

```python
for row in extract():
    load(transform(row))
```

### Standard Structure

```python
extract -> validate -> transform -> load -> audit
```

### Code Pattern

```python
batch_id = uuid4(); process(batch_id)
```

## Examples

### Beginner Example

```python
source = [1, 2, None]
clean = [x for x in source if x is not None]
print(clean)
```

### Intermediate Example

```python
def transform_rows(rows):
    for row in rows:
        if row.get('amount', 0) < 0:
            continue
        yield {**row, 'amount': float(row['amount'])}


print(list(transform_rows([{'amount': '10'}, {'amount': '-1'}])))
```

### Advanced Example

```python
from dataclasses import dataclass


@dataclass
class BatchMeta:
    batch_id: str
    row_count: int


def load_with_meta(rows, batch_id: str) -> BatchMeta:
    materialized = list(rows)
    return BatchMeta(batch_id=batch_id, row_count=len(materialized))


print(load_with_meta([{'id': 1}], 'b1'))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Source] --> B[Transform]
    B --> C[Validate]
    C --> D[Destination]
```

---

# Data Engineering

## Overview

- **What is it?** Data engineering builds reliable pipelines, storage layers, and serving paths for analytics and ML.
- **Why is it important?** Raw data must become trustworthy tables and features at scale.
- **Where is it used?** Lakehouses, warehouses, streaming platforms, feature stores.

## Learning Objectives

- **Skills gained:** Practical command of Data Engineering.
- **Concepts covered:**

- Design batch and streaming pipelines.
- Apply partitioning and schema evolution.
- Monitor data quality SLAs.

- **Expected outcome:** You architect data platforms with Python components.

## Real World Applications

- Tech unicorns
- Finance
- Healthcare analytics
- Retail

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Pipeline

- **Definition:** Orchestrated stages.
- **Visual explanation:** `Pipeline` → process → result
- **Practical example:**

```python
stages = ['extract', 'transform', 'load']
print('->'.join(stages))
```

### Partitioning

- **Definition:** Split data by key/date.
- **Visual explanation:** `Partitioning` → process → result
- **Practical example:**

```python
parts = {'2026-06-06': [1, 2]}
print(list(parts))
```

### Lineage

- **Definition:** Track data origin.
- **Visual explanation:** `Lineage` → process → result
- **Practical example:**

```python
meta = {'source': 'crm', 'batch': '001'}
print(meta['source'])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Data engineering connects sources to trustworthy datasets. |
| ⚡ Purpose | Enable analytics and ML with quality and scale. |
| 🔥 Benefits | Single source of truth, reusable pipelines. |
| 🎯 Use Cases | Daily marts, CDC streams, feature pipelines. |
| 🚀 Best Practices | Idempotent jobs; observability; contract tests on schemas. |
| ❌ Common Mistakes | Tight coupling to one tool, no backfills, missing monitoring. |

## Syntax Guide

### Basic Syntax

```python
orchestrator.run(dag_id='daily_sales')
```

### Standard Structure

```python
ingest -> bronze -> silver -> gold
```

### Code Pattern

```python
def merge_upserts(rows, event_date: str):
    return [dict(r, event_date=event_date) for r in rows]


print(merge_upserts([{'id': 1}], '2026-06-06'))
```

## Examples

### Beginner Example

```python
events = [{'user': 'a', 'ts': 1}, {'user': 'b', 'ts': 2}]
print(len(events))
```

### Intermediate Example

```python
from collections import defaultdict

def aggregate_by_user(events):
    totals = defaultdict(int)
    for event in events:
        totals[event['user']] += 1
    return dict(totals)


print(aggregate_by_user([{'user': 'a'}, {'user': 'a'}, {'user': 'b'}]))
```

### Advanced Example

```python
def validate_schema(row: dict, required: set[str]) -> dict:
    missing = required - row.keys()
    if missing:
        raise ValueError(f'missing {missing}')
    return row


print(validate_schema({'id': 1, 'name': 'Ada'}, {'id', 'name'}))
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Sources] --> B[Ingestion]
    B --> C[Processing]
    C --> D[Serving Layer]
```

---

# Pandas

## Overview

- **What is it?** Pandas is a library for tabular data manipulation via DataFrame and Series objects.
- **Why is it important?** It is the standard tool for data cleaning, exploration, and feature engineering.
- **Where is it used?** Analytics, finance, marketing, ML feature pipelines, reporting.

## Learning Objectives

- **Skills gained:** Practical command of Pandas.
- **Concepts covered:**

- Load and inspect datasets.
- Filter, group, merge, and pivot.
- Handle missing data.

- **Expected outcome:** You transform raw data into analysis-ready tables.

## Real World Applications

- Data science
- BI
- Quant research
- Ops analytics

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### DataFrame

- **Definition:** 2D labeled table.
- **Visual explanation:** `DataFrame` → process → result
- **Practical example:**

```python
import pandas as pd
df = pd.DataFrame({'a': [1, 2]})
print(df.shape)
```

### Series

- **Definition:** 1D labeled array.
- **Visual explanation:** `Series` → process → result
- **Practical example:**

```python
import pandas as pd
s = pd.Series([1, 2, 3])
print(s.mean())
```

### GroupBy

- **Definition:** Split-apply-combine aggregations.
- **Visual explanation:** `GroupBy` → process → result
- **Practical example:**

```python
import pandas as pd
df = pd.DataFrame({'g': ['x', 'x'], 'v': [1, 2]})
print(df.groupby('g')['v'].sum().to_dict())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | DataFrame = rows + columns + indexes. |
| ⚡ Purpose | Efficient structured data operations. |
| 🔥 Benefits | Expressive API, integrates with NumPy/plotting/ML. |
| 🎯 Use Cases | ETL, dashboards, ad hoc analysis, feature stores. |
| 🚀 Best Practices | Avoid chained indexing; vectorize; profile memory. |
| ❌ Common Mistakes | iterrows on large data, ignoring dtypes, unnecessary copies. |

## Syntax Guide

### Basic Syntax

```python
import pandas as pd
df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
```

### Standard Structure

```python
load -> clean -> transform -> aggregate -> export
```

### Code Pattern

```python
import pandas as pd
df = pd.DataFrame({'g': ['a'], 'v': [1]})
print(df.groupby('g')['v'].sum())
```

## Examples

### Beginner Example

```python
import pandas as pd
df = pd.DataFrame({'price': [10, 20]})
print(df['price'].sum())
```

### Intermediate Example

```python
import pandas as pd

df = pd.DataFrame({'region': ['US', 'US', 'EU'], 'revenue': [100, 150, 80]})
summary = df.groupby('region')['revenue'].sum().sort_values(ascending=False)
print(summary.to_dict())
```

### Advanced Example

```python
import pandas as pd

def active_sku_counts(chunks):
    parts = []
    for chunk in chunks:
        parts.append(chunk[chunk['status'] == 'active'].groupby('sku').size())
    return pd.concat(parts).groupby(level=0).sum()


chunks = [pd.DataFrame({'sku': ['A', 'A'], 'status': ['active', 'inactive']})]
print(active_sku_counts(chunks).to_dict())
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Raw CSV] --> B[DataFrame]
    B --> C[Transform]
    C --> D[Export/Model]
```

---

# NumPy

## Overview

- **What is it?** NumPy provides fast n-dimensional arrays and vectorized numerical operations.
- **Why is it important?** Vectorization underpins scientific Python and ML performance.
- **Where is it used?** ML preprocessing, simulations, image arrays, linear algebra.

## Learning Objectives

- **Skills gained:** Practical command of NumPy.
- **Concepts covered:**

- Create and slice ndarrays.
- Apply ufuncs and broadcasting.
- Use linear algebra routines.

- **Expected outcome:** You perform numeric computation efficiently with NumPy.

## Real World Applications

- ML research
- Quant
- Engineering sims
- Medical imaging

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### ndarray

- **Definition:** Homogeneous n-D array.
- **Visual explanation:** `ndarray` → process → result
- **Practical example:**

```python
import numpy as np
a = np.array([1, 2, 3])
print(a.dtype)
```

### vectorization

- **Definition:** Ops without Python loops.
- **Visual explanation:** `vectorization` → process → result
- **Practical example:**

```python
import numpy as np
print(np.array([1, 2]) + 10)
```

### broadcasting

- **Definition:** Align shapes for ops.
- **Visual explanation:** `broadcasting` → process → result
- **Practical example:**

```python
import numpy as np
print(np.array([[1], [2]]) + np.array([10, 20]))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | NumPy pushes loops into optimized C. |
| ⚡ Purpose | Fast numerical kernels in Python. |
| 🔥 Benefits | Speed, interop with ML stack, rich math API. |
| 🎯 Use Cases | Feature matrices, FFT, random sampling, grids. |
| 🚀 Best Practices | Avoid Python loops on large arrays; choose dtype consciously. |
| ❌ Common Mistakes | Excessive memory from float64 defaults, mixing lists and arrays. |

## Syntax Guide

### Basic Syntax

```python
import numpy as np
a = np.arange(6).reshape(2, 3)
```

### Standard Structure

```python
create array -> vectorized ops -> aggregate
```

### Code Pattern

```python
result = np.where(mask, a, b)
```

## Examples

### Beginner Example

```python
import numpy as np
print(np.mean([1, 2, 3, 4]))
```

### Intermediate Example

```python
import numpy as np
a = np.random.default_rng(0).normal(size=1000)
print(round(a.mean(), 3))
```

### Advanced Example

```python
import numpy as np

A = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([1.0, 2.0])
print(np.linalg.solve(A, b))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Python Lists] --> B[np.array]
    B --> C[Vectorized Ops]
```

---

# PySpark

## Overview

- **What is it?** PySpark distributes data processing across clusters using Spark's resilient datasets and DataFrames.
- **Why is it important?** Single-machine pandas fails on terabyte-scale datasets.
- **Where is it used?** Lakehouse ETL, log analytics, ML feature generation at scale.

## Learning Objectives

- **Skills gained:** Practical command of PySpark.
- **Concepts covered:**

- Understand RDD vs DataFrame API.
- Apply transforms lazily and actions.
- Tune partitions and shuffles.

- **Expected outcome:** You author distributed batch jobs with PySpark patterns.

## Real World Applications

- Big data platforms
- Ad tech
- Telecom
- Finance risk

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### SparkSession

- **Definition:** Entry point to Spark.
- **Visual explanation:** `SparkSession` → process → result
- **Practical example:**

```python
print('SparkSession'[:5])
```

### DataFrame

- **Definition:** Distributed table API.
- **Visual explanation:** `DataFrame` → process → result
- **Practical example:**

```python
rows = [{'id': 1}, {'id': 2}]
print(len(rows))
```

### lazy eval

- **Definition:** Transformations build plan.
- **Visual explanation:** `lazy eval` → process → result
- **Practical example:**

```python
plan = ['read', 'filter', 'groupBy']
print(plan[-1])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Spark executes DAGs in parallel across executors. |
| ⚡ Purpose | Scale Python data processing horizontally. |
| 🔥 Benefits | Fault tolerance, SQL interface, ecosystem integration. |
| 🎯 Use Cases | Nightly aggregates, log parsing, large joins. |
| 🚀 Best Practices | Avoid collect on big data; cache hot datasets; control skew. |
| ❌ Common Mistakes | Too many shuffles, tiny files, UDFs everywhere instead of built-ins. |

## Syntax Guide

### Basic Syntax

```python
df = spark.read.parquet('s3://bucket/path')
```

### Standard Structure

```python
read -> transform -> cache/persist -> action
```

### Code Pattern

```python
steps = ['read', 'filter', 'groupBy', 'write']
print('->'.join(steps))
```

## Examples

### Beginner Example

```python
records = [{'country': 'US', 'v': 1}, {'country': 'EU', 'v': 2}]
print(sum(r['v'] for r in records))
```

### Intermediate Example

```python
from collections import defaultdict

def group_sum(rows, key):
    totals = defaultdict(int)
    for row in rows:
        totals[row[key]] += row['value']
    return dict(totals)


data = [{'region': 'US', 'value': 10}, {'region': 'US', 'value': 5}]
print(group_sum(data, 'region'))
```

### Advanced Example

```python
def explain_plan(steps):
    return ' -> '.join(steps)


print(explain_plan(['scan', 'filter', 'project', 'aggregate']))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Driver] --> B[Executors]
    B --> C[Partitions]
    C --> D[Results]
```

---

# Machine Learning

## Overview

- **What is it?** Machine learning trains models to make predictions from data without explicit rules.
- **Why is it important?** Predictive models automate decisions in ranking, fraud, and forecasting.
- **Where is it used?** Recommendations, credit risk, demand forecast, churn prediction.

## Learning Objectives

- **Skills gained:** Practical command of Machine Learning.
- **Concepts covered:**

- Split train/test data.
- Train baseline models with scikit-learn.
- Evaluate with proper metrics.

- **Expected outcome:** You build and evaluate supervised learning baselines.

## Real World Applications

- E-commerce
- Fintech
- Healthcare analytics
- Marketing

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Features/labels

- **Definition:** X and y for supervised learning.
- **Visual explanation:** `Features/labels` → process → result
- **Practical example:**

```python
X = [[1], [2]]
y = [0, 1]
print(len(X) == len(y))
```

### train/test split

- **Definition:** Holdout evaluation.
- **Visual explanation:** `train/test split` → process → result
- **Practical example:**

```python
data = list(range(10))
train, test = data[:8], data[8:]
print(len(test))
```

### metrics

- **Definition:** Measure performance.
- **Visual explanation:** `metrics` → process → result
- **Practical example:**

```python
def accuracy(y_true, y_pred):
    return sum(a == b for a, b in zip(y_true, y_pred)) / len(y_true)
print(accuracy([1, 0], [1, 0]))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | ML generalizes patterns from data to unseen examples. |
| ⚡ Purpose | Automate prediction and classification. |
| 🔥 Benefits | Handles complex patterns, improves with data. |
| 🎯 Use Cases | Spam detection, pricing, recommendations. |
| 🚀 Best Practices | Cross-validation; feature scaling; address leakage; track experiments. |
| ❌ Common Mistakes | Testing on training data, ignoring class imbalance, no baseline. |

## Syntax Guide

### Basic Syntax

```python
model.fit(X_train, y_train)
preds = model.predict(X_test)
```

### Standard Structure

```python
prepare -> train -> evaluate -> deploy
```

### Code Pattern

```python
Pipeline([('scale', scaler), ('clf', model)])
```

## Examples

### Beginner Example

```python
xs = [1, 2, 3]
ys = [2, 4, 6]
print(all(y == x * 2 for x, y in zip(xs, ys)))
```

### Intermediate Example

```python
from statistics import mean

def mse(y_true, y_pred):
    return mean((a - b) ** 2 for a, b in zip(y_true, y_pred))


print(round(mse([1.0, 2.0], [1.1, 1.9]), 3))
```

### Advanced Example

```python
def kfold_indices(n, k=3):
    fold_size = n // k
    for i in range(k):
        start = i * fold_size
        end = (i + 1) * fold_size if i < k - 1 else n
        val_idx = list(range(start, end))
        train_idx = [j for j in range(n) if j not in val_idx]
        yield train_idx, val_idx


print(next(kfold_indices(9))[0][:3])
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Data] --> B[Train]
    B --> C[Model]
    C --> D[Evaluate]
```

---

# Deep Learning

## Overview

- **What is it?** Deep learning uses neural networks with many layers to learn hierarchical representations.
- **Why is it important?** It achieves state-of-the-art results in vision, speech, and language tasks.
- **Where is it used?** Computer vision, NLP, speech, generative AI, recommender systems.

## Learning Objectives

- **Skills gained:** Practical command of Deep Learning.
- **Concepts covered:**

- Understand tensors, layers, and loss functions.
- Train with PyTorch or TensorFlow basics.
- Monitor overfitting with validation.

- **Expected outcome:** You train simple neural networks and interpret training loops.

## Real World Applications

- AI products
- Autonomous systems
- Media
- Healthcare imaging

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Tensor

- **Definition:** Multi-dimensional array for DL.
- **Visual explanation:** `Tensor` → process → result
- **Practical example:**

```python
import numpy as np
x = np.zeros((2, 3))
print(x.shape)
```

### Layer

- **Definition:** Learnable transformation.
- **Visual explanation:** `Layer` → process → result
- **Practical example:**

```python
weights = [0.5, -0.2]
print(len(weights))
```

### Loss

- **Definition:** Objective to minimize.
- **Visual explanation:** `Loss` → process → result
- **Practical example:**

```python
def mse(y, y_hat):
    return ((y - y_hat) ** 2).mean()
import numpy as np
print(float(mse(np.array([1.0]), np.array([0.5]))))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Networks compose nonlinear layers trained by gradient descent. |
| ⚡ Purpose | Learn complex patterns from raw or engineered features. |
| 🔥 Benefits | Automatic feature learning, SOTA on many tasks. |
| 🎯 Use Cases | Image classifiers, translators, voice assistants. |
| 🚀 Best Practices | Normalize inputs; early stopping; reproducible seeds; GPU when needed. |
| ❌ Common Mistakes | No validation, wrong loss for task, exploding gradients unhandled. |

## Syntax Guide

### Basic Syntax

```python
for epoch in range(epochs):
    loss = train_step(batch)
    val_loss = eval_step(val_batch)
```

### Standard Structure

```python
data -> model -> loss -> optimizer step -> evaluate
```

### Code Pattern

```python
logits = model(x); loss = criterion(logits, y)
```

## Examples

### Beginner Example

```python
import math
print(round(math.tanh(0.5), 3))
```

### Intermediate Example

```python
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def forward(x, w, b):
    return sigmoid(x * w + b)

print(round(float(forward(1.0, 0.5, 0.0)), 3))
```

### Advanced Example

```python
import numpy as np

def train_step(w, x, y, lr=0.1):
    pred = w * x
    loss = (pred - y) ** 2
    grad = 2 * (pred - y) * x
    w -= lr * grad
    return w, float(loss)


w = 0.0
for _ in range(5):
    w, loss = train_step(w, 2.0, 6.0)
print(round(w, 3))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Batch] --> B[Forward]
    B --> C[Loss]
    C --> D[Backward/Update]
```

---

# NLP

## Overview

- **What is it?** Natural Language Processing analyzes and generates human language text.
- **Why is it important?** Text dominates business communication, support, and web content.
- **Where is it used?** Chatbots, search, sentiment, translation, document classification.

## Learning Objectives

- **Skills gained:** Practical command of NLP.
- **Concepts covered:**

- Tokenize and normalize text.
- Build bag-of-words or embedding features.
- Evaluate NLP classifiers.

- **Expected outcome:** You preprocess text and train baseline NLP models.

## Real World Applications

- Customer support
- Legal tech
- Social analytics
- Edtech

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Tokenization

- **Definition:** Split text into tokens.
- **Visual explanation:** `Tokenization` → process → result
- **Practical example:**

```python
text = 'Hello world'
print(text.lower().split())
```

### Stop words

- **Definition:** Filter common tokens.
- **Visual explanation:** `Stop words` → process → result
- **Practical example:**

```python
stop = {'the', 'a'}
tokens = ['the', 'cat']
print([t for t in tokens if t not in stop])
```

### Embeddings

- **Definition:** Dense word vectors.
- **Visual explanation:** `Embeddings` → process → result
- **Practical example:**

```python
vec = {'python': [0.1, 0.2]}
print(len(vec['python']))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | NLP pipelines turn raw text into numeric features. |
| ⚡ Purpose | Extract meaning and structure from language. |
| 🔥 Benefits | Automation of text-heavy workflows. |
| 🎯 Use Cases | Ticket routing, spam filters, entity extraction. |
| 🚀 Best Practices | Handle unicode; domain-specific tokenization; evaluate per class. |
| ❌ Common Mistakes | Naive stemming for all languages, train/test leakage via duplicates. |

## Syntax Guide

### Basic Syntax

```python
tokens = text.lower().split()
features = Counter(tokens)
```

### Standard Structure

```python
normalize -> tokenize -> featurize -> model
```

### Code Pattern

```python
clean(text) -> vectorize -> clf.predict
```

## Examples

### Beginner Example

```python
review = 'I love this product'
print('love' in review)
```

### Intermediate Example

```python
from collections import Counter

def bow(tokens):
    return Counter(tokens)


print(bow(['python', 'is', 'fun', 'python']))
```

### Advanced Example

```python
import re

def extract_mentions(text: str) -> list[str]:
    return re.findall(r'@([A-Za-z0-9_]+)', text)


print(extract_mentions('hi @ada and @lin'))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Text] --> B[Preprocess]
    B --> C[Features]
    C --> D[Model]
```

---

# Computer Vision

## Overview

- **What is it?** Computer vision interprets images and video for detection, classification, and segmentation.
- **Why is it important?** Visual data powers quality inspection, medical imaging, and AR.
- **Where is it used?** Manufacturing QA, radiology assist, autonomous vehicles, retail analytics.

## Learning Objectives

- **Skills gained:** Practical command of Computer Vision.
- **Concepts covered:**

- Load and preprocess image tensors.
- Understand CNN basics.
- Evaluate vision model metrics.

- **Expected outcome:** You run baseline image classification workflows.

## Real World Applications

- Manufacturing
- Healthcare
- Retail
- Security video

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Image tensor

- **Definition:** HWC or CHW arrays.
- **Visual explanation:** `Image tensor` → process → result
- **Practical example:**

```python
import numpy as np
img = np.zeros((64, 64, 3), dtype=np.uint8)
print(img.shape)
```

### CNN

- **Definition:** Convolution + pooling layers.
- **Visual explanation:** `CNN` → process → result
- **Practical example:**

```python
kernel = [[1, 0], [0, 1]]
print(kernel[0][0])
```

### Augmentation

- **Definition:** Random transforms for robustness.
- **Visual explanation:** `Augmentation` → process → result
- **Practical example:**

```python
import random
print(random.choice(['flip', 'rotate']))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Conv nets learn spatial hierarchies of visual features. |
| ⚡ Purpose | Automate visual understanding tasks. |
| 🔥 Benefits | Scale beyond manual inspection. |
| 🎯 Use Cases | Defect detection, OCR assist, face blur for privacy. |
| 🚀 Best Practices | Match preprocessing to pretrained models; monitor drift. |
| ❌ Common Mistakes | Wrong normalization, label leakage, ignoring class imbalance. |

## Syntax Guide

### Basic Syntax

```python
image = load_rgb(path)
tensor = preprocess(image)
```

### Standard Structure

```python
load -> augment -> batch -> model -> metrics
```

### Code Pattern

```python
transforms.Compose([Resize, ToTensor, Normalize])
```

## Examples

### Beginner Example

```python
import numpy as np
img = np.array([[0, 255], [128, 64]], dtype=np.uint8)
print(img.mean())
```

### Intermediate Example

```python
import numpy as np

def normalize_image(img: np.ndarray) -> np.ndarray:
    return (img.astype('float32') / 255.0)


arr = np.array([0, 128, 255], dtype=np.uint8)
print(normalize_image(arr).round(2))
```

### Advanced Example

```python
import numpy as np

def conv1d(signal, kernel):
    out = []
    k = len(kernel)
    for i in range(len(signal) - k + 1):
        window = signal[i:i + k]
        out.append(float(np.dot(window, kernel)))
    return out


print(conv1d([1, 2, 3, 4], [1, 0.5]))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Image] --> B[Preprocess]
    B --> C[CNN]
    C --> D[Prediction]
```

---

# FastAPI

## Overview

- **What is it?** FastAPI is a modern, high-performance web framework for building APIs with Python type hints.
- **Why is it important?** It combines speed, automatic OpenAPI docs, and async support.
- **Where is it used?** Microservices, ML model serving, internal tools, SaaS backends.

## Learning Objectives

- **Skills gained:** Practical command of FastAPI.
- **Concepts covered:**

- Build REST endpoints.
- Use Pydantic models for validation.
- Deploy with Uvicorn/Gunicorn.

- **Expected outcome:** You ship production-ready async APIs quickly.

## Real World Applications

- AI inference APIs
- Fintech
- Health tech
- Startups

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Path operations

- **Definition:** Functions mapped to HTTP routes.
- **Visual explanation:** `Path operations` → process → result
- **Practical example:**

```python
ROUTES = {'GET /health': lambda: {'status': 'ok'}}
print(ROUTES['GET /health']())
```

### Pydantic models

- **Definition:** Validation and serialization.
- **Visual explanation:** `Pydantic models` → process → result
- **Practical example:**

```python
from dataclasses import dataclass
@dataclass
class Item:
    name: str
    price: float
print(Item('a', 1.0))
```

### Dependency injection

- **Definition:** Reusable components.
- **Visual explanation:** `Dependency injection` → process → result
- **Practical example:**

```python
def get_db():
    return {'connected': True}
print(get_db()['connected'])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | FastAPI = Starlette + Pydantic + type hints. |
| ⚡ Purpose | Build typed, documented APIs with minimal boilerplate. |
| 🔥 Benefits | Auto docs, validation, async, great DX. |
| 🎯 Use Cases | CRUD APIs, webhooks, ML serving, gateways. |
| 🚀 Best Practices | Use routers; env-based config; structured logging. |
| ❌ Common Mistakes | Blocking I/O in async routes, skipping auth, no tests. |

## Syntax Guide

### Basic Syntax

```python
from dataclasses import dataclass

@dataclass
class Health:
    status: str = 'ok'


print(Health().status)
```

### Standard Structure

```python
app -> routes -> schemas -> dependencies -> startup
```

### Code Pattern

```python
def handle(route, service):
    return service(route)


print(handle('/health', lambda r: {'status': 'ok'}))
```

## Examples

### Beginner Example

```python
def health():
    return {'status': 'ok'}
print(health())
```

### Intermediate Example

```python
from dataclasses import dataclass


@dataclass
class CreateUser:
    email: str


def create_user(payload: CreateUser):
    return {'email': payload.email}


print(create_user(CreateUser(email='a@b.com')))
```

### Advanced Example

```python
from dataclasses import dataclass


@dataclass
class User:
    id: int
    email: str


def get_current_user(token: str) -> User | None:
    return User(1, 'a@b.com') if token else None


user = get_current_user('token')
print(user.email if user else 'anonymous')
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Client] --> B[FastAPI]
    B --> C[Validation]
    C --> D[Service]
```

---

# Django

## Overview

- **What is it?** Django is a batteries-included web framework for rapid secure web development.
- **Why is it important?** It provides ORM, admin, auth, and routing out of the box.
- **Where is it used?** Content sites, admin-heavy apps, MVPs, internal portals.

## Learning Objectives

- **Skills gained:** Practical command of Django.
- **Concepts covered:**

- Create projects, apps, models, and views.
- Use Django ORM and migrations.
- Configure URLs and templates.

- **Expected outcome:** You build full-stack web apps with Django conventions.

## Real World Applications

- News sites
- SaaS admin
- Education portals
- Marketplaces

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### MTV

- **Definition:** Model-Template-View pattern.
- **Visual explanation:** `MTV` → process → result
- **Practical example:**

```python
MODEL = {'fields': ['title']}
print(MODEL['fields'])
```

### ORM

- **Definition:** Database abstraction.
- **Visual explanation:** `ORM` → process → result
- **Practical example:**

```python
class Row:
    def __init__(self, title):
        self.title = title
print(Row('hi').title)
```

### Admin

- **Definition:** Auto CRUD UI.
- **Visual explanation:** `Admin` → process → result
- **Practical example:**

```python
ADMIN = {'register': True}
print(ADMIN['register'])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Django favors convention and integrated components. |
| ⚡ Purpose | Ship secure web apps quickly. |
| 🔥 Benefits | Mature ecosystem, built-in auth/admin, ORM. |
| 🎯 Use Cases | CMS, membership sites, internal tools. |
| 🚀 Best Practices | Use CBVs/FBVs appropriately; split settings per env; cache queries. |
| ❌ Common Mistakes | Fat views, N+1 queries, raw SQL without need. |

## Syntax Guide

### Basic Syntax

```python
urlpatterns = [path('health/', health_view)]
```

### Standard Structure

```python
project -> apps -> models -> views -> urls
```

### Code Pattern

```python
Model -> Serializer/Form -> View -> Template/JSON
```

## Examples

### Beginner Example

```python
def hello(request):
    return {'message': 'hi'}
```

### Intermediate Example

```python
class Article:
    objects = [{'title': 'Hello', 'published': True}]

    @classmethod
    def published(cls):
        return [a for a in cls.objects if a['published']]


print(Article.published()[0]['title'])
```

### Advanced Example

```python
class QuerySet:
    def __init__(self, rows):
        self.rows = rows

    def filter(self, **kwargs):
        return QuerySet([r for r in self.rows if all(r.get(k) == v for k, v in kwargs.items())])


qs = QuerySet([{'active': True, 'id': 1}, {'active': False, 'id': 2}])
print(qs.filter(active=True).rows[0]['id'])
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Request] --> B[URLConf]
    B --> C[View]
    C --> D[Model/Template]
```

---

# Flask

## Overview

- **What is it?** Flask is a lightweight WSGI microframework for web apps and APIs.
- **Why is it important?** Minimal core plus extensions fits small services and prototypes.
- **Where is it used?** Micro APIs, webhooks, prototypes, embedded admin UIs.

## Learning Objectives

- **Skills gained:** Practical command of Flask.
- **Concepts covered:**

- Define routes and request handlers.
- Use Jinja templates and blueprints.
- Structure apps with application factory.

- **Expected outcome:** You build small web services with Flask patterns.

## Real World Applications

- Startups
- Internal tools
- IoT dashboards
- Hackathons

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### app.route

- **Definition:** Map URL to view.
- **Visual explanation:** `app.route` → process → result
- **Practical example:**

```python
ROUTES = {}
def route(path):
    def deco(fn):
        ROUTES[path] = fn
        return fn
    return deco
@route('/')
def index():
    return 'ok'
print(ROUTES['/']())
```

### request

- **Definition:** HTTP request context.
- **Visual explanation:** `request` → process → result
- **Practical example:**

```python
class Req:
    args = {'q': 'flask'}
print(Req.args['q'])
```

### Blueprint

- **Definition:** Modular routes.
- **Visual explanation:** `Blueprint` → process → result
- **Practical example:**

```python
BP = {'name': 'api'}
print(BP['name'])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Flask core stays small; extensions add ORM, auth, etc. |
| ⚡ Purpose | Quick HTTP services with flexibility. |
| 🔥 Benefits | Simple learning curve, huge extension ecosystem. |
| 🎯 Use Cases | Webhooks, minimal APIs, prototypes. |
| 🚀 Best Practices | Application factory; blueprints; config objects; g for request scope. |
| ❌ Common Mistakes | Single-file mega app, debug in prod, global mutable state. |

## Syntax Guide

### Basic Syntax

```python
app = Flask(__name__)
@app.get('/health')
def health(): return {'ok': True}
```

### Standard Structure

```python
app factory -> blueprints -> views -> templates
```

### Code Pattern

```python
register_blueprint(api_bp, url_prefix='/api')
```

## Examples

### Beginner Example

```python
def health():
    return {'status': 'ok'}
print(health())
```

### Intermediate Example

```python
class Flask:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def decorator(fn):
            self.routes[path] = fn
            return fn
        return decorator


app = Flask()

@app.route('/hello')
def hello():
    return 'hello'


print(app.routes['/hello']())
```

### Advanced Example

```python
class Blueprint:
    def __init__(self, name: str):
        self.name = name
        self.routes = {}

    def route(self, path):
        def decorator(fn):
            self.routes[path] = fn
            return fn
        return decorator


api = Blueprint('api')

@api.route('/items')
def items():
    return ['item']


print(api.routes['/items']())
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Request] --> B[Flask Router]
    B --> C[View]
    C --> D[Response]
```

---

# Microservices

## Overview

- **What is it?** Microservices decompose applications into independently deployable services.
- **Why is it important?** Teams scale delivery and isolate failures per bounded context.
- **Where is it used?** Cloud-native SaaS, large product engineering orgs, platform teams.

## Learning Objectives

- **Skills gained:** Practical command of Microservices.
- **Concepts covered:**

- Define service boundaries.
- Communicate via HTTP/events.
- Implement observability and versioning.

- **Expected outcome:** You design service-oriented architectures with Python services.

## Real World Applications

- Streaming platforms
- Fintech
- E-commerce
- Enterprise SaaS

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Bounded context

- **Definition:** Service owns its domain.
- **Visual explanation:** `Bounded context` → process → result
- **Practical example:**

```python
SERVICES = {'billing': ['invoices'], 'users': ['profiles']}
print(SERVICES['billing'])
```

### API gateway

- **Definition:** Single entry routing.
- **Visual explanation:** `API gateway` → process → result
- **Practical example:**

```python
GATEWAY = {'/users': 'user-svc'}
print(GATEWAY['/users'])
```

### Event bus

- **Definition:** Async integration.
- **Visual explanation:** `Event bus` → process → result
- **Practical example:**

```python
EVENTS = []
EVENTS.append({'type': 'OrderCreated'})
print(EVENTS[0]['type'])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Microservices trade monolith simplicity for independent deployment. |
| ⚡ Purpose | Scale teams and components separately. |
| 🔥 Benefits | Isolation, tech diversity, targeted scaling. |
| 🎯 Use Cases | Checkout, notifications, search, recommendations. |
| 🚀 Best Practices | Contract tests; idempotent consumers; distributed tracing. |
| ❌ Common Mistakes | Distributed monolith, chatty sync calls, no versioning. |

## Syntax Guide

### Basic Syntax

```python
# service exposes /health and domain routes
```

### Standard Structure

```python
gateway -> services -> databases per service
```

### Code Pattern

```python
publish OrderCreated -> inventory service consumes
```

## Examples

### Beginner Example

```python
services = ['users', 'orders']
print(len(services))
```

### Intermediate Example

```python
def call_service(registry, name, path):
    base = registry[name]
    return f'{base}{path}'


registry = {'users': 'http://users:8000'}
print(call_service(registry, 'users', '/1'))
```

### Advanced Example

```python
from dataclasses import dataclass


@dataclass
class ServiceHealth:
    name: str
    ok: bool


def aggregate_health(checks: list[ServiceHealth]) -> bool:
    return all(h.ok for h in checks)


print(aggregate_health([ServiceHealth('a', True), ServiceHealth('b', True)]))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Gateway] --> B[Service A]
    A --> C[Service B]
    B --> D[DB A]
    C --> E[DB B]
```

---

# Docker with Python

## Overview

- **What is it?** Docker packages Python apps with dependencies into portable containers.
- **Why is it important?** Containers reproduce dev/prod environments and simplify deployment.
- **Where is it used?** CI/CD, Kubernetes, cloud run, local dev stacks.

## Learning Objectives

- **Skills gained:** Practical command of Docker with Python.
- **Concepts covered:**

- Write Dockerfiles for Python apps.
- Use multi-stage builds.
- Run with docker compose for dependencies.

- **Expected outcome:** You containerize Python services production-ready.

## Real World Applications

- Cloud-native teams
- ML ops
- Consultancies
- Startups

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Dockerfile

- **Definition:** Image build recipe.
- **Visual explanation:** `Dockerfile` → process → result
- **Practical example:**

```python
print('FROM python:3.12-slim'[:4])
```

### WORKDIR

- **Definition:** Set container working dir.
- **Visual explanation:** `WORKDIR` → process → result
- **Practical example:**

```python
WORKDIR = '/app'
print(WORKDIR)
```

### ENTRYPOINT

- **Definition:** Container start command.
- **Visual explanation:** `ENTRYPOINT` → process → result
- **Practical example:**

```python
CMD = ['python', 'app.py']
print(CMD[0])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Images are immutable layers; containers are running instances. |
| ⚡ Purpose | Consistent runtime from laptop to cloud. |
| 🔥 Benefits | Isolation, reproducibility, fast rollouts. |
| 🎯 Use Cases | API containers, workers, notebooks batch jobs. |
| 🚀 Best Practices | Pin base image; non-root user; .dockerignore; healthcheck. |
| ❌ Common Mistakes | Huge images, secrets in layers, running as root, no pin requirements. |

## Syntax Guide

### Basic Syntax

```python
dockerfile = 'FROM python:3.12-slim\nCOPY requirements.txt .'
print(dockerfile.split()[0])
```

### Standard Structure

```python
base image -> deps -> copy app -> cmd
```

### Code Pattern

```python
stages = ['builder', 'runtime']
print(stages)
```

## Examples

### Beginner Example

```python
print('docker build -t myapp .')
```

### Intermediate Example

```python
dockerfile = '''FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "-m", "http.server", "8000"]
'''
print('WORKDIR' in dockerfile)
```

### Advanced Example

```python
stages = ['builder', 'runtime']
print(stages.index('runtime'))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Dockerfile] --> B[Image]
    B --> C[Container]
    C --> D[Registry/K8s]
```

---

# Kubernetes Integration

## Overview

- **What is it?** Kubernetes orchestrates containers for scaling, networking, and self-healing deployments.
- **Why is it important?** Production services need automated rollout, health checks, and service discovery.
- **Where is it used?** Cloud platforms, platform engineering, microservice fleets.

## Learning Objectives

- **Skills gained:** Practical command of Kubernetes Integration.
- **Concepts covered:**

- Write Deployments and Services manifests.
- Configure probes and resource limits.
- Use ConfigMaps and Secrets.

- **Expected outcome:** You deploy Python apps to Kubernetes clusters.

## Real World Applications

- SaaS platforms
- FinTech cloud
- Media streaming
- ML serving

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Pod

- **Definition:** Smallest deploy unit.
- **Visual explanation:** `Pod` → process → result
- **Practical example:**

```python
pod = {'name': 'api', 'containers': ['app']}
print(pod['containers'])
```

### Deployment

- **Definition:** Manages replica sets.
- **Visual explanation:** `Deployment` → process → result
- **Practical example:**

```python
spec = {'replicas': 3}
print(spec['replicas'])
```

### Service

- **Definition:** Stable network endpoint.
- **Visual explanation:** `Service` → process → result
- **Practical example:**

```python
svc = {'type': 'ClusterIP', 'port': 80}
print(svc['port'])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Kubernetes desired state reconciles actual cluster state. |
| ⚡ Purpose | Run containers reliably at scale. |
| 🔥 Benefits | Self-healing, scaling, rolling updates. |
| 🎯 Use Cases | API fleets, workers, cron jobs. |
| 🚀 Best Practices | Liveness/readiness probes; limits/requests; 12-factor config. |
| ❌ Common Mistakes | No probes, OOM kills, latest tag in prod, huge ConfigMaps. |

## Syntax Guide

### Basic Syntax

```python
command = ['kubectl', 'apply', '-f', 'deployment.yaml']
print(command[0])
```

### Standard Structure

```python
Deployment -> Service -> Ingress -> HPA
```

### Code Pattern

```python
config = {'envFrom': 'configMap', 'mountSecrets': True}
print(config['envFrom'])
```

## Examples

### Beginner Example

```python
manifest = {'kind': 'Deployment', 'replicas': 1}
print(manifest['kind'])
```

### Intermediate Example

```python
deployment = {
    'spec': {
        'template': {
            'spec': {
                'containers': [{
                    'name': 'api',
                    'readinessProbe': {'httpGet': {'path': '/health', 'port': 8000}},
                }]
            }
        }
    }
}
probe = deployment['spec']['template']['spec']['containers'][0]['readinessProbe']
print(probe['httpGet']['path'])
```

### Advanced Example

```python
def rolling_update(current: int, desired: int, max_surge: int) -> int:
    return min(current + max_surge, desired)


print(rolling_update(2, 5, 1))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Deployment] --> B[Pods]
    B --> C[Service]
    C --> D[Ingress]
```

---

# Cloud Development

## Overview

- **What is it?** Cloud development builds apps leveraging managed services for compute, storage, and messaging.
- **Why is it important?** Cloud offloads ops for scaling, durability, and global reach.
- **Where is it used?** SaaS, data platforms, mobile backends, ML inference.

## Learning Objectives

- **Skills gained:** Practical command of Cloud Development.
- **Concepts covered:**

- Use object storage and managed databases.
- Apply IAM least privilege.
- Design for multi-region resilience.

- **Expected outcome:** You architect cloud-native Python solutions.

## Real World Applications

- Global SaaS
- Media
- Gaming backends
- Enterprise migration

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Managed services

- **Definition:** Offload ops to provider.
- **Visual explanation:** `Managed services` → process → result
- **Practical example:**

```python
SERVICES = ['object-storage', 'queue', 'db']
print(len(SERVICES))
```

### IAM

- **Definition:** Identity and access control.
- **Visual explanation:** `IAM` → process → result
- **Practical example:**

```python
policy = {'allow': ['s3:GetObject']}
print(policy['allow'][0])
```

### Object storage

- **Definition:** Durable blob store.
- **Visual explanation:** `Object storage` → process → result
- **Practical example:**

```python
uri = 's3://bucket/key'
print(uri.startswith('s3://'))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Cloud-native apps use managed APIs instead of self-hosted servers. |
| ⚡ Purpose | Scale without owning data centers. |
| 🔥 Benefits | Elasticity, global CDN, managed backups. |
| 🎯 Use Cases | Static assets, backups, event archives, ML datasets. |
| 🚀 Best Practices | Infrastructure as code; secrets manager; cost tags; observability. |
| ❌ Common Mistakes | Long-lived access keys in code, public buckets, no autoscaling. |

## Syntax Guide

### Basic Syntax

```python
client.upload_file('local.txt', 'bucket', 'key')
```

### Standard Structure

```python
app -> SDK -> managed API -> cloud resource
```

### Code Pattern

```python
upload artifact -> trigger lambda/worker
```

## Examples

### Beginner Example

```python
bucket = 'my-app-assets'
print(bucket.replace('-', '_'))
```

### Intermediate Example

```python
def presigned_url(bucket: str, key: str, ttl: int = 3600) -> str:
    return f'https://{bucket}.example.com/{key}?ttl={ttl}'


print('ttl=' in presigned_url('b', 'file.csv'))
```

### Advanced Example

```python
def multi_region_failover(primary_ok: bool, secondary_ok: bool) -> str:
    if primary_ok:
        return 'primary'
    if secondary_ok:
        return 'secondary'
    raise RuntimeError('all regions down')


print(multi_region_failover(True, False))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Python App] --> B[Cloud SDK]
    B --> C[Managed Services]
```

---

# AWS with Python

## Overview

- **What is it?** AWS with Python uses boto3 to interact with S3, Lambda, DynamoDB, SQS, and more.
- **Why is it important?** AWS dominates enterprise cloud; automation requires SDK fluency.
- **Where is it used?** Serverless APIs, data lakes, batch ETL, infra automation.

## Learning Objectives

- **Skills gained:** Practical command of AWS with Python.
- **Concepts covered:**

- Configure boto3 clients and resources.
- Upload/download S3 objects.
- Invoke Lambda and publish to SQS.

- **Expected outcome:** You automate AWS resources from Python with boto3 patterns.

## Real World Applications

- Enterprise cloud
- Startups on AWS
- Media storage
- Fintech

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### boto3 client

- **Definition:** Low-level service client.
- **Visual explanation:** `boto3 client` → process → result
- **Practical example:**

```python
print('boto3'[:4])
```

### S3

- **Definition:** Object storage.
- **Visual explanation:** `S3` → process → result
- **Practical example:**

```python
key = 's3://bucket/path'
print(key.split('/')[2])
```

### Lambda handler

- **Definition:** Function entrypoint.
- **Visual explanation:** `Lambda handler` → process → result
- **Practical example:**

```python
def handler(event, context):
    return {'statusCode': 200, 'body': 'ok'}
print(handler({}, None)['statusCode'])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | boto3 wraps AWS HTTP APIs with Python methods. |
| ⚡ Purpose | Programmatic cloud infrastructure and data access. |
| 🔥 Benefits | Full AWS surface, IAM integration, mature docs. |
| 🎯 Use Cases | Backup scripts, ETL triggers, infra provisioning. |
| 🚀 Best Practices | Use IAM roles not keys; paginate list calls; retries with backoff. |
| ❌ Common Mistakes | Hard-coded credentials, overly broad IAM, no region set. |

## Syntax Guide

### Basic Syntax

```python
import boto3
s3 = boto3.client('s3')
```

### Standard Structure

```python
session -> client -> API call -> handle pagination
```

### Code Pattern

```python
s3.upload_file(local, bucket, key)
```

## Examples

### Beginner Example

```python
def lambda_handler(event, context):
    return {'statusCode': 200}
print(lambda_handler({}, None))
```

### Intermediate Example

```python
def s3_uri(bucket: str, key: str) -> str:
    return f's3://{bucket}/{key}'


print(s3_uri('logs', '2026/06/app.log'))
```

### Advanced Example

```python
def paginate(items, page_size=2):
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]


print(list(paginate(list(range(5)), 2)))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[boto3] --> B[AWS API]
    B --> C[S3/Lambda/SQS]
```

---

# Azure with Python

## Overview

- **What is it?** Azure with Python uses azure-sdk-for-python to manage storage, functions, and cloud resources.
- **Why is it important?** Enterprises on Microsoft cloud need Python automation and app integration.
- **Where is it used?** Azure Functions, Blob Storage, Cosmos DB, enterprise integrations.

## Learning Objectives

- **Skills gained:** Practical command of Azure with Python.
- **Concepts covered:**

- Authenticate with DefaultAzureCredential.
- Use Blob SDK for uploads.
- Deploy Python functions to Azure.

- **Expected outcome:** You integrate Python workloads with Azure services.

## Real World Applications

- Enterprise IT
- Healthcare on Azure
- Government
- Hybrid cloud

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Blob storage

- **Definition:** Object storage on Azure.
- **Visual explanation:** `Blob storage` → process → result
- **Practical example:**

```python
uri = 'https://account.blob.core.windows.net/container/blob'
print('blob' in uri)
```

### DefaultAzureCredential

- **Definition:** Unified auth chain.
- **Visual explanation:** `DefaultAzureCredential` → process → result
- **Practical example:**

```python
print('credential chain pattern')
```

### Function app

- **Definition:** Serverless Python host.
- **Visual explanation:** `Function app` → process → result
- **Practical example:**

```python
def main(req):
    return {'status': 200}
print(main({})['status'])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Azure SDK mirrors AWS patterns with Azure-specific services. |
| ⚡ Purpose | Build and automate on Microsoft cloud. |
| 🔥 Benefits | Active Directory integration, hybrid tooling. |
| 🎯 Use Cases | Blob ETL, enterprise SSO apps, IoT hub ingestion. |
| 🚀 Best Practices | Managed identity; key vault secrets; monitor with App Insights. |
| ❌ Common Mistakes | Connection strings in git, wrong subscription context. |

## Syntax Guide

### Basic Syntax

```python
from azure.storage.blob import BlobServiceClient
```

### Standard Structure

```python
credential -> client -> operation -> retry policy
```

### Code Pattern

```python
BlobServiceClient.from_connection_string(conn)
```

## Examples

### Beginner Example

```python
account = 'myaccount'
print(f'https://{account}.blob.core.windows.net')
```

### Intermediate Example

```python
def blob_path(container: str, name: str) -> str:
    return f'{container}/{name}'


print(blob_path('logs', 'app.log'))
```

### Advanced Example

```python
class RetryPolicy:
    def __init__(self, retries=3):
        self.retries = retries

    def run(self, func):
        last = None
        for _ in range(self.retries):
            try:
                return func()
            except Exception as exc:
                last = exc
        raise last


print(RetryPolicy().run(lambda: 'ok'))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Python SDK] --> B[Azure API]
    B --> C[Blob/Functions/Cosmos]
```

---

# GCP with Python

## Overview

- **What is it?** GCP with Python uses google-cloud libraries for Storage, BigQuery, Pub/Sub, and Cloud Run.
- **Why is it important?** Google Cloud excels at data analytics and Kubernetes (GKE).
- **Where is it used?** Analytics pipelines, ML on GCP, Pub/Sub event systems, Cloud Run APIs.

## Learning Objectives

- **Skills gained:** Practical command of GCP with Python.
- **Concepts covered:**

- Authenticate with service accounts.
- Query BigQuery from Python.
- Publish/consume Pub/Sub messages.

- **Expected outcome:** You build data and event-driven apps on GCP.

## Real World Applications

- Ad tech
- Analytics
- ML platforms
- Mobile backends

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### BigQuery

- **Definition:** Warehouse SQL engine.
- **Visual explanation:** `BigQuery` → process → result
- **Practical example:**

```python
sql = 'SELECT 1 AS one'
print(sql.split()[0])
```

### GCS

- **Definition:** Google Cloud Storage.
- **Visual explanation:** `GCS` → process → result
- **Practical example:**

```python
uri = 'gs://bucket/object'
print(uri.startswith('gs://'))
```

### Pub/Sub

- **Definition:** Messaging service.
- **Visual explanation:** `Pub/Sub` → process → result
- **Practical example:**

```python
topic = 'projects/p/topics/t'
print(topic.split('/')[-1])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | GCP client libraries wrap REST/gRPC service APIs. |
| ⚡ Purpose | Analytics and event-driven cloud apps. |
| 🔥 Benefits | BigQuery integration, strong data tooling, GKE. |
| 🎯 Use Cases | Log sinks to BQ, model batch scoring, async workers. |
| 🚀 Best Practices | Workload identity; IAM roles; partition BigQuery tables. |
| ❌ Common Mistakes | Public buckets, streaming inserts without dedupe keys. |

## Syntax Guide

### Basic Syntax

```python
from google.cloud import storage
client = storage.Client()
```

### Standard Structure

```python
client -> API -> handle pages -> monitor quotas
```

### Code Pattern

```python
bq_client.query(sql).result()
```

## Examples

### Beginner Example

```python
print('gs://my-bucket/data.csv'.split('/')[2])
```

### Intermediate Example

```python
def pubsub_message(data: bytes, attrs: dict | None = None) -> dict:
    return {'data': data.decode(), 'attributes': attrs or {}}


print(pubsub_message(b'hello', {'type': 'event'}))
```

### Advanced Example

```python
def bigquery_job_state(done: bool, errors: list | None = None) -> str:
    if errors:
        return 'FAILED'
    return 'DONE' if done else 'RUNNING'


print(bigquery_job_state(True))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Python Client] --> B[GCP API]
    B --> C[BigQuery/GCS/PubSub]
```

---

# DevOps Automation

## Overview

- **What is it?** DevOps automation uses Python to script infrastructure, deployments, and operational tasks.
- **Why is it important?** Repeatable automation reduces human error and accelerates releases.
- **Where is it used?** SRE teams, platform engineering, release management, cloud ops.

## Learning Objectives

- **Skills gained:** Practical command of DevOps Automation.
- **Concepts covered:**

- Automate provisioning and config with scripts.
- Integrate with APIs (GitHub, K8s, cloud).
- Add logging and dry-run modes.

- **Expected outcome:** You build reliable ops automation in Python.

## Real World Applications

- Platform teams
- Managed services
- Game live ops
- Enterprise IT

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Scripted workflow

- **Definition:** Codify runbooks.
- **Visual explanation:** `Scripted workflow` → process → result
- **Practical example:**

```python
def deploy(version):
    return f'deployed {version}'
print(deploy('1.2.3'))
```

### Idempotency

- **Definition:** Safe reruns.
- **Visual explanation:** `Idempotency` → process → result
- **Practical example:**

```python
desired = {'replicas': 3}
current = {'replicas': 3}
print(desired == current)
```

### API automation

- **Definition:** Call control planes.
- **Visual explanation:** `API automation` → process → result
- **Practical example:**

```python
import urllib.request
print(hasattr(urllib.request, 'urlopen'))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | DevOps automation replaces manual clicks with tested code. |
| ⚡ Purpose | Reliable, auditable operations. |
| 🔥 Benefits | Speed, consistency, documentation via code. |
| 🎯 Use Cases | Scale services, rotate certs, cleanup resources. |
| 🚀 Best Practices | Dry-run flag; structured logs; secrets from vault; least privilege. |
| ❌ Common Mistakes | No rollback plan, silent failures, running untested scripts prod-wide. |

## Syntax Guide

### Basic Syntax

```python
if __name__ == '__main__':
    run_playbook()
```

### Standard Structure

```python
parse args -> plan -> apply -> verify
```

### Code Pattern

```python
for host in inventory: ssh_run(host, cmd)
```

## Examples

### Beginner Example

```python
def restart_service(name: str) -> str:
    return f'restarted {name}'
print(restart_service('api'))
```

### Intermediate Example

```python
def ensure_replicas(current: int, desired: int) -> int:
    if current < desired:
        return current + 1
    if current > desired:
        return current - 1
    return current


print(ensure_replicas(2, 3))
```

### Advanced Example

```python
from dataclasses import dataclass


@dataclass
class ChangeRecord:
    action: str
    target: str
    ok: bool


def audit(changes: list[ChangeRecord]) -> list[ChangeRecord]:
    return [c for c in changes if not c.ok]


print(audit([ChangeRecord('scale', 'api', True)]))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Trigger] --> B[Automation Script]
    B --> C[API/SSH]
    C --> D[Verify]
```

---

# CI/CD Pipelines

## Overview

- **What is it?** CI/CD pipelines automatically test, build, and deploy code on each change.
- **Why is it important?** Fast feedback and repeatable releases reduce production incidents.
- **Where is it used?** GitHub Actions, GitLab CI, Jenkins, cloud deploy pipelines.

## Learning Objectives

- **Skills gained:** Practical command of CI/CD Pipelines.
- **Concepts covered:**

- Configure test/lint/build stages.
- Cache dependencies in CI.
- Promote artifacts through environments.

- **Expected outcome:** You implement Python CI/CD workflows with gates and artifacts.

## Real World Applications

- Every software org
- Open source
- Regulated industries
- Mobile backends

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### CI

- **Definition:** Continuous integration tests.
- **Visual explanation:** `CI` → process → result
- **Practical example:**

```python
steps = ['checkout', 'test', 'lint']
print(steps.index('test'))
```

### CD

- **Definition:** Continuous delivery/deploy.
- **Visual explanation:** `CD` → process → result
- **Practical example:**

```python
envs = ['dev', 'staging', 'prod']
print(envs[-1])
```

### Artifacts

- **Definition:** Built wheels/images.
- **Visual explanation:** `Artifacts` → process → result
- **Practical example:**

```python
artifact = 'dist/app-1.0.whl'
print(artifact.endswith('.whl'))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Pipelines encode quality gates before production. |
| ⚡ Purpose | Ship safely and frequently. |
| 🔥 Benefits | Automation, audit trail, faster MTTR. |
| 🎯 Use Cases | Run pytest on PR, build Docker on main, deploy to staging. |
| 🚀 Best Practices | Fail fast; pin actions; secrets in CI vault; matrix Python versions. |
| ❌ Common Mistakes | No tests in CI, flaky pipelines ignored, deploying without migration plan. |

## Syntax Guide

### Basic Syntax

```python
steps = ['pytest', 'python', '-m', 'build']
print(steps[0])
```

### Standard Structure

```python
trigger -> lint/test -> build -> deploy
```

### Code Pattern

```python
on: pull_request -> jobs: test
```

## Examples

### Beginner Example

```python
pipeline = ['lint', 'test']
print('test' in pipeline)
```

### Intermediate Example

```python
def should_deploy(branch: str, tests_passed: bool) -> bool:
    return branch == 'main' and tests_passed


print(should_deploy('main', True))
```

### Advanced Example

```python
def promotion_gate(metrics: dict) -> bool:
    return metrics.get('error_rate', 1) < 0.01 and metrics.get('p95_ms', 999) < 300


print(promotion_gate({'error_rate': 0.001, 'p95_ms': 120}))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Git Push] --> B[CI Test]
    B --> C[Build Artifact]
    C --> D[Deploy]
```

---

# Performance Optimization

## Overview

- **What is it?** Performance optimization improves latency, throughput, and resource usage of Python programs.
- **Why is it important?** Slow software increases cost and hurts user experience at scale.
- **Where is it used?** API hot paths, ETL, ML inference, high-QPS services.

## Learning Objectives

- **Skills gained:** Practical command of Performance Optimization.
- **Concepts covered:**

- Profile with cProfile and py-spy.
- Apply algorithmic and vectorization wins.
- Use caching and async I/O appropriately.

- **Expected outcome:** You measure first and apply targeted optimizations.

## Real World Applications

- Ad exchanges
- Search
- Fintech trading tools
- Streaming

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Profiling

- **Definition:** Find hotspots.
- **Visual explanation:** `Profiling` → process → result
- **Practical example:**

```python
import cProfile
cProfile.run('sum(range(1000))')
```

### Big-O

- **Definition:** Scale with input size.
- **Visual explanation:** `Big-O` → process → result
- **Practical example:**

```python
def linear(n):
    return sum(range(n))
print(linear(10))
```

### Caching

- **Definition:** Memoize pure functions.
- **Visual explanation:** `Caching` → process → result
- **Practical example:**

```python
from functools import lru_cache
@lru_cache
def fib(n):
    return n if n < 2 else fib(n-1)+fib(n-2)
print(fib(10))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Optimize bottlenecks proven by measurement. |
| ⚡ Purpose | Meet SLAs and reduce infrastructure cost. |
| 🔥 Benefits | Lower latency, higher throughput, happier users. |
| 🎯 Use Cases | API caching, batch tuning, NumPy vectorization. |
| 🚀 Best Practices | Benchmark before/after; load test; avoid premature optimization. |
| ❌ Common Mistakes | Optimizing cold code, micro-opts over algorithms, no profiling. |

## Syntax Guide

### Basic Syntax

```python
from functools import lru_cache


@lru_cache(maxsize=1024)
def expensive(n: int) -> int:
    return n * n


print(expensive(3))
```

### Standard Structure

```python
profile -> hypothesize -> optimize -> verify
```

### Code Pattern

```python
optimizations = ['cache', 'vectorize', 'async_io']
print(len(optimizations))
```

## Examples

### Beginner Example

```python
import time
t0 = time.perf_counter()
sum(range(100000))
print(time.perf_counter() - t0 < 1)
```

### Intermediate Example

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def slow(n: int) -> int:
    return sum(range(n))


print(slow(1000) == slow(1000))
```

### Advanced Example

```python
import cProfile
import pstats
from io import StringIO

buf = StringIO()
cProfile.run('sum(i*i for i in range(1000))', buf)
stats = pstats.Stats(buf)
print(stats.total_calls > 0)
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Profile] --> B[Hotspot]
    B --> C[Optimize]
    C --> D[Benchmark]
```

---

# System Design with Python

## Overview

- **What is it?** System design with Python plans scalable architectures using services, queues, caches, and databases.
- **Why is it important?** Senior engineers must translate requirements into reliable large-scale designs.
- **Where is it used?** Architecture reviews, interviews, greenfield platforms, rewrites.

## Learning Objectives

- **Skills gained:** Practical command of System Design with Python.
- **Concepts covered:**

- Estimate capacity and define APIs.
- Choose databases, caches, and queues.
- Plan observability and failure modes.

- **Expected outcome:** You draft end-to-end system designs implementable in Python stacks.

## Real World Applications

- Big tech
- High-growth startups
- Consulting
- Platform engineering

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Load balancing

- **Definition:** Distribute traffic.
- **Visual explanation:** `Load balancing` → process → result
- **Practical example:**

```python
servers = ['a', 'b', 'b']
print(max(set(servers), key=servers.count))
```

### Caching

- **Definition:** Reduce read load.
- **Visual explanation:** `Caching` → process → result
- **Practical example:**

```python
cache = {}
def get(key):
    return cache.setdefault(key, 'value')
print(get('k'))
```

### Queue

- **Definition:** Async decouple.
- **Visual explanation:** `Queue` → process → result
- **Practical example:**

```python
from collections import deque
q = deque(['job'])
print(q.popleft())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Design balances latency, throughput, consistency, and cost. |
| ⚡ Purpose | Build systems that meet scale and reliability goals. |
| 🔥 Benefits | Clear roadmap, risk reduction, aligned teams. |
| 🎯 Use Cases | URL shortener, feed system, rate limiter, chat. |
| 🚀 Best Practices | Start simple; define SLIs/SLOs; design for failure; document tradeoffs. |
| ❌ Common Mistakes | Over-engineering day one, single DB bottleneck, no monitoring plan. |

## Syntax Guide

### Basic Syntax

```python
# API -> service -> cache/db -> async workers
```

### Standard Structure

```python
clients -> LB -> app tier -> data tier -> async workers
```

### Code Pattern

```python
cache = {}
def read(key):
    return cache.get(key, 'miss')


print(read('user:1'))
```

## Examples

### Beginner Example

```python
components = ['api', 'db', 'cache']
print(len(components))
```

### Intermediate Example

```python
class RateLimiter:
    def __init__(self, limit: int):
        self.limit = limit
        self.count = 0

    def allow(self) -> bool:
        if self.count >= self.limit:
            return False
        self.count += 1
        return True


rl = RateLimiter(2)
print(rl.allow(), rl.allow(), rl.allow())
```

### Advanced Example

```python
from dataclasses import dataclass


@dataclass
class DesignDoc:
    service: str
    rps: int
    datastore: str
    notes: str


doc = DesignDoc('url-shortener', rps=10_000, datastore='redis+dynamodb', notes='cache hot keys')
print(doc.service, doc.rps)
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Clients] --> B[Load Balancer]
    B --> C[App Servers]
    C --> D[Cache]
    C --> E[Database]
    C --> F[Queue Workers]
```

---

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

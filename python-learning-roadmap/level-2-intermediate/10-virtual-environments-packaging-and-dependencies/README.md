# Virtual Environments, Packaging, and Dependencies

## Overview

- **What is it?** Project isolation, third-party library management, and distribution practices.
- **Why is it important?** Real projects depend on external packages and need reproducible environments.
- **Where is it used?** Every modern Python app, data project, package, service, and deployment pipeline.

## Learning Objectives

- Create and activate virtual environments.
- Install and pin dependencies.
- Understand project metadata and packaging basics.
- Expected outcome: you can manage project dependencies without polluting system Python.

## Real World Applications

- Sharing reproducible analysis notebooks.
- Deploying web services.
- Publishing internal tools.
- Career relevance for professional software, DevOps, data science, and ML engineering.

## Core Concepts

### Virtual Environment

- **Definition:** An isolated Python environment with its own packages.
- **Visual explanation:** `project -> .venv -> isolated dependencies`
- **Practical example:**

```bash
python -m venv .venv
```

### Dependency

- **Definition:** External code your project imports and relies on.
- **Visual explanation:** `your code -> package -> reusable capability`
- **Practical example:**

```bash
python -m pip install requests
```

### Project Metadata

- **Definition:** Configuration describing package name, version, dependencies, and tooling.
- **Visual explanation:** `pyproject.toml -> build/install/test tools`
- **Practical example:**

```toml
[project]
name = "example"
version = "0.1.0"
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Isolate projects and declare dependencies. |
| ⚡ Purpose | Make development and deployment reproducible. |
| 🔥 Benefits | Fewer version conflicts, easier onboarding, cleaner builds. |
| 🎯 Use Cases | Apps, packages, data projects, automation tools. |
| 🚀 Best Practices | Use one environment per project, commit dependency manifests, avoid global installs. |
| ❌ Common Mistakes | Installing into system Python, unpinned production dependencies, mixing package managers blindly. |

## Syntax Guide

### Basic Syntax

```bash
python -m venv .venv
python -m pip install package-name
```

### Standard Structure

```text
project/
  pyproject.toml
  src/
  tests/
  README.md
```

### Code Pattern

```python
import third_party_package

result = third_party_package.do_work()
```

## Examples

### Beginner Example

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install rich
```

### Intermediate Example

```python
from importlib.metadata import version


print(version("pip"))
```

### Advanced Example

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "acme-tools"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["requests"]
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Create Project] --> B[Create Virtual Environment]
    B --> C[Install Dependencies]
    C --> D[Record Metadata]
    D --> E[Run Tests]
    E --> F[Build or Deploy]
```

---

## Student Learning Support

### Curriculum Metadata

| Field | Details |
| --- | --- |
| Roadmap level | Level 2: Intermediate |
| Topic number | 10 |
| Difficulty | Intermediate |
| Recommended study format | One to two focused study sessions |
| Best studied after | Modules, Command-line basics |

### Before You Start

- Modules
- Command-line basics

### Key Vocabulary

- Virtual environment
- Dependency
- Package
- pyproject.toml
- Build backend
- Version

### Student Study Plan

1. Read the overview and learning objectives before running any code.
2. Type each beginner example manually to build muscle memory.
3. Modify the intermediate example with your own data.
4. Explain the advanced example line by line in plain language.
5. Complete the practice tasks and compare your output with the expected behavior.

### Guided Practice Tasks

- Create a .venv and install one package.
- List installed packages and explain where they live.
- Sketch a src-based project layout.

### Self-Check Questions

- Can I explain why global installs are risky?
- Can I activate and deactivate an environment?
- Can I identify project metadata?

### Evidence of Mastery

A student can isolate a Python project and describe how its dependencies are declared and installed.

### Instructor Notes

- Ask the student to explain their code before asking them to optimize it.
- Encourage small, frequent experiments in the Python interpreter.
- Review mistakes as feedback about the mental model, not as failure.

---

## More Nested Student Breakdown

For smaller study units, open the [`deep-dive/`](./deep-dive/) directory. It breaks this topic into overview, objectives, applications, concepts, syntax, examples, workflow, questions, code files, and answer guidance.


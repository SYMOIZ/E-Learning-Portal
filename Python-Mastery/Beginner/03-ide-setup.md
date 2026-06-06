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

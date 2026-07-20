> **Level 1: Beginner** · Topic 2 of 35

[← Introduction to Python](./01-introduction-to-python.md) · [↑ Level index](../README.md) · [IDE Setup →](./03-ide-setup.md)

# Installing Python

## Overview
- **What is it?** Installing Python provides the interpreter, standard library, and package installer needed to run local programs.
- **Why is it important?** A verified installation prevents command, version, and path problems before coding begins.
- **Where is it used?** Developers install Python on workstations, build servers, classrooms, and automation hosts.

## Learning Objectives
- Choose a supported Python 3 release from a trusted source.
- Verify the interpreter and pip through the same Python executable.
- Diagnose a missing command or unexpected executable path.

## Real World Applications
- Prepare a laptop for coursework.
- Match a team's supported runtime version.
- Confirm which interpreter a deployment or script uses.

## Core Concepts

### Interpreter installation
- **Definition:** The installation places a Python executable and its standard library on the system.
- **Visual explanation:** `installer -> executable + standard library`
- **Practical example:** Python can report its own runtime version.

```python
import platform
print(platform.python_version())
```

### Command resolution
- **Definition:** The shell searches its `PATH` to decide which executable a command name starts.
- **Visual explanation:** `python command -> PATH search -> executable`
- **Practical example:** The `sys.executable` path identifies the running interpreter.

```python
import sys
print(sys.executable)
```

### Installer verification
- **Definition:** `python -m pip` runs pip with the selected interpreter, avoiding a mismatched standalone pip command.
- **Visual explanation:** `selected Python -> -m pip -> matching site-packages`
- **Practical example:** Python can invoke pip's version check as a subprocess.

```python
import subprocess
import sys

subprocess.run([sys.executable, "-m", "pip", "--version"], check=True)
```

## Infographic Summary

| Infographic Block | Topic-Specific Takeaway |
| --- | --- |
| 📌 Concept | Installing Python provides the interpreter, standard library, and package installer needed to run local programs. |
| ⚡ Purpose | Provide a verified interpreter, standard library, and package installer for local Python work. |
| 🔥 Benefits | A verified installation prevents command, version, and path problems before coding begins. |
| 🎯 Use Cases | Developers install Python on workstations, build servers, classrooms, and automation hosts. |
| 🚀 Best Practices | Use the official installer or operating-system package manager and verify both version and executable path. |
| ❌ Common Mistakes | Running `pip` and `python` from different installations without checking which interpreter owns the packages. |

## Syntax Guide

### Basic Syntax

```python
import sys
print(sys.version)
```

### Standard Structure

```python
import sys
print(f"Executable: {sys.executable}")
print(f"Version: {sys.version_info.major}.{sys.version_info.minor}")
```

### Code Pattern

```python
import shutil
import sys

command = shutil.which("python3") or shutil.which("python")
print({"running": sys.executable, "shell_command": command})
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
minimum = (3, 10)
print("Supported:", sys.version_info >= minimum)
```

### Advanced Example

```python
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-c", "print(6 * 7)"],
    capture_output=True,
    text=True,
    check=True,
)
print(result.stdout.strip())
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Choose trusted installer]
    B[Install Python 3]
    C[Open a new terminal]
    D[Verify version and path]
    E[Run a test program]
    A --> B
    B --> C
    C --> D
    D --> E
```

---

[← Introduction to Python](./01-introduction-to-python.md) · [↑ Level index](../README.md) · [IDE Setup →](./03-ide-setup.md)

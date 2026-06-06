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

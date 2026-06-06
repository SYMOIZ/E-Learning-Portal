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

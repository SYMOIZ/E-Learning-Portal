# Python Quick Reference Cheat Sheet

## Syntax Essentials

| Element | Example |
| --- | --- |
| Variable | `count = 0` |
| Function | `def add(a, b): return a + b` |
| Class | `class User: pass` |
| List comp | `[x * 2 for x in range(5)]` |
| Dict comp | `{k: v for k, v in pairs}` |
| f-string | `f"Hello {name}"` |
| Context mgr | `with open("f.txt") as f: ...` |
| Decorator | `@app.get("/")` |

## Collections

| Type | Mutable | Ordered | Duplicates |
| --- | --- | --- | --- |
| `list` | Yes | Yes | Yes |
| `tuple` | No | Yes | Yes |
| `set` | Yes | No | No |
| `dict` | Yes | Yes (3.7+) | Keys unique |

## Common Imports

```python
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Optional, List
```

## Testing Snippet

```python
def test_add():
    assert add(2, 3) == 5
```

## FastAPI Minimal

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}
```

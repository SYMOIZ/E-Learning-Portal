# Advanced Systems Cheat Sheet

[← Cheat sheets](./README.md) · [Advanced lessons](../Advanced/01-data-structures-internals.md)

## Internals and Performance

| Question | First check |
| --- | --- |
| Slow code | Profile before rewriting |
| Memory growth | References, caches, and `__slots__` only with evidence |
| CPU-bound work | Processes or native extensions, not extra threads in CPython |
| I/O-bound work | Threads or asyncio with bounds and timeouts |

```python
from collections import Counter

counts = Counter(tokens)
top = counts.most_common(10)
```

## Architecture Choices

| Style | Use when |
| --- | --- |
| FastAPI | JSON APIs with validation and OpenAPI |
| Django | Batteries-included web products |
| Flask | Small services with explicit extensions |
| Pandas / PySpark | Tabular transforms; Spark when data exceeds one machine |
| Docker + CI | Repeatable build, test, and release |

## Safety Defaults

- Never interpolate untrusted text into SQL, shell, or HTML.
- Keep secrets in the environment or a secret manager, never in images.
- Make jobs and HTTP handlers idempotent where retries are possible.
- Prefer allowlisted parsers over executing untrusted code.

Related lessons: [Concurrency](../Advanced/10-concurrency.md), [ETL Development](../Advanced/18-etl-development.md), [FastAPI](../Advanced/27-fastapi.md), [Docker with Python](../Advanced/31-docker-with-python.md), [System Design with Python](../Advanced/40-system-design-with-python.md).

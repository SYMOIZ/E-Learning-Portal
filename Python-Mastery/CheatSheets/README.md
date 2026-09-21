# Python Cheat Sheets

[← Knowledge base](../README.md)

Level-specific sheets for quick retrieval. This page remains the combined reference.

| Level | Sheet |
| --- | --- |
| Beginner | [Syntax, collections, files](./01-beginner.md) |
| Intermediate | [Objects, data, tests](./02-intermediate.md) |
| Advanced | [Internals, architecture, safety](./03-advanced.md) |

## Core Syntax

| Goal | Pattern | Note |
| --- | --- | --- |
| Assign a value | `name = "Ada"` | Names reference objects. |
| Branch | `if condition: ... elif other: ... else: ...` | Indentation defines each block. |
| Iterate | `for item in iterable: ...` | Prefer direct iteration to indexes. |
| Define behavior | `def function(arg: str) -> str: ...` | Keep one clear responsibility. |
| Handle failure | `try: ... except ValueError as error: ...` | Catch the narrowest useful exception. |
| Manage a resource | `with open(path) as stream: ...` | Context managers guarantee cleanup. |
| Transform values | `[f(x) for x in values if valid(x)]` | Use a loop when logic becomes dense. |
| Model data | `@dataclass class Item: ...` | Add types and explicit invariants. |

## Collection Selection

| Type | Ordered | Mutable | Unique | Best fit |
| --- | --- | --- | --- | --- |
| `list` | Yes | Yes | No | Sequence that changes |
| `tuple` | Yes | No | No | Fixed record or return group |
| `set` | No | Yes | Yes | Membership and deduplication |
| `dict` | Yes | Yes | Keys | Keyed records and lookup |

## Complexity Quick Reference

| Operation | Typical cost | Caveat |
| --- | --- | --- |
| List index | O(1) | Insert near the front is O(n). |
| Dictionary lookup | O(1) average | Hash collisions affect worst cases. |
| Set membership | O(1) average | Members must be hashable. |
| Sort | O(n log n) | Key functions run once per item. |
| Linear scan | O(n) | Stop early when possible. |

## Standard Library Starter Kit

| Need | Module |
| --- | --- |
| Paths and files | `pathlib`, `shutil` |
| Dates and time zones | `datetime`, `zoneinfo` |
| Structured data | `json`, `csv`, `sqlite3` |
| CLI parsing | `argparse` |
| Testing | `unittest`, `unittest.mock` |
| Concurrency | `threading`, `multiprocessing`, `asyncio` |
| Diagnostics | `logging`, `traceback`, `cProfile` |
| Iteration tools | `itertools`, `functools`, `collections` |

## OOP and Protocols

| Goal | Pattern | Note |
| --- | --- | --- |
| Construct an object | `def __init__(self, ...):` | Validate invariants early. |
| Represent for debugging | `def __repr__(self) -> str:` | Prefer unambiguous developer output. |
| Make an object iterable | `def __iter__(self): yield ...` | Or return an iterator from `__iter__`. |
| Support `with` | `def __enter__` / `def __exit__` | Or use `@contextmanager`. |
| Wrap a callable | `@decorator` / `functools.wraps` | Preserve metadata for tools and docs. |
| Abstract a contract | `abc.ABC` + `@abstractmethod` | Prefer protocols when duck typing is enough. |

## Testing Quick Reference

| Goal | Pattern | Note |
| --- | --- | --- |
| Assert equality | `assert result == expected` | Prefer exact expected values. |
| Assert failure | `with pytest.raises(ValueError):` | Check the exception type you care about. |
| Parametrize cases | `@pytest.mark.parametrize(...)` | Keep case data readable. |
| Isolate collaborators | `unittest.mock.Mock` / `patch` | Mock only at true boundaries. |
| Temporary files | `tmp_path` fixture | Avoid writing into the repo tree. |

## Data and API Checklist

| Concern | Prefer | Avoid |
| --- | --- | --- |
| HTTP JSON | Explicit status checks and schema validation | Assuming every response is 200 + perfect JSON |
| SQL | Parameterized queries / ORM binds | String-interpolated SQL |
| Config | Environment or config files outside code | Hard-coded secrets and hosts |
| Logging | Structured events without PII | Logging passwords, tokens, or full payloads |
| Retries | Idempotent operations + backoff | Blind infinite retry loops |

> Treat cheat sheets as retrieval aids, not substitutes for the topic lessons or hands-on practice.

# Python Cheat Sheets

[← Knowledge base](../README.md)

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

> Treat cheat sheets as retrieval aids, not substitutes for the topic lessons or hands-on practice.

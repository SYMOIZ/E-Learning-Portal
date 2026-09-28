# Installable Task CLI

[← Project catalog](./README.md) · [Packaging Python Projects](../Intermediate/34-packaging-python-projects.md)

**Level:** Intermediate  
**Lessons:** argparse, logging, packaging, pytest, virtual environments

## Problem

A team wants an installable `tasks` command that adds a task, lists open tasks, and writes a log line without printing secrets.

## Non-goals

- No cloud sync.
- No graphical interface.

## Requirements

- Expose a console script from `pyproject.toml`.
- Store tasks in a JSON file under a path from an environment variable, with a local default.
- Log the action name at info level and failures at error level.
- Ship at least two pytest tests that use a temporary directory.

## Starter

```python
import argparse
import json
from pathlib import Path


def load_tasks(path):
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def add_task(path, title):
    tasks = load_tasks(path)
    tasks.append({"title": title, "done": False})
    path.write_text(json.dumps(tasks, indent=2), encoding="utf-8")
    return tasks


def build_parser():
    parser = argparse.ArgumentParser(prog="tasks")
    parser.add_argument("title", nargs="?")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    if not args.title:
        print("usage: tasks TITLE")
        return 2
    add_task(Path("tasks.json"), args.title)
    print("added")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## Acceptance checks

- `pip install -e .` creates the `tasks` command inside a virtual environment.
- Tests do not read or write the developer's real home directory.
- A missing title returns exit code `2`.
- The README documents configuration and the log format.

## Extension

Add a `done` subcommand that is idempotent when the task is already complete.

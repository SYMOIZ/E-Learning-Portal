# Expense Tracker CLI

[← Project catalog](./README.md) · [File Handling](../Beginner/31-file-handling.md)

**Level:** Beginner  
**Lessons:** input and output, functions, dictionaries, files, exceptions, project structure

## Problem

A household wants a command-line ledger that records an expense amount and category, saves it, and reports a category total after the program restarts.

## Non-goals

- No web interface.
- No multi-user accounts.
- No currency conversion.

## Requirements

- Reject a non-numeric or non-positive amount with a clear error.
- Persist entries as JSON in a path passed to the program.
- Reload existing entries instead of overwriting them.
- Print the total for one requested category.

## Starter

```python
import json
from pathlib import Path


def load_entries(path):
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_entries(path, entries):
    path.write_text(json.dumps(entries, indent=2), encoding="utf-8")


def add_entry(entries, amount, category):
    if amount <= 0:
        raise ValueError("amount must be positive")
    entries.append({"amount": amount, "category": category})
    return entries


def total_for(entries, category):
    return sum(item["amount"] for item in entries if item["category"] == category)


def main():
    path = Path("expenses.json")
    entries = load_entries(path)
    add_entry(entries, 12.5, "food")
    save_entries(path, entries)
    print(total_for(entries, "food"))


if __name__ == "__main__":
    main()
```

## Acceptance checks

- A second run adds to the file rather than replacing it with one row.
- `total_for([], "food")` is `0`.
- A negative amount raises `ValueError` and does not write a new row.
- The README lists the command, the file format, and one limitation.

## Extension

Group the report by category and sort categories by total descending.

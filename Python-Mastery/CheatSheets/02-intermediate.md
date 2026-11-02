# Intermediate Engineering Cheat Sheet

[← Cheat sheets](./README.md) · [Intermediate lessons](../Intermediate/01-object-oriented-programming.md)

## Objects and Protocols

```python
class Account:
    def __init__(self, owner: str, balance: int) -> None:
        self.owner = owner
        self._balance = balance

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def __repr__(self) -> str:
        return f"Account({self.owner!r}, {self._balance})"
```

| Goal | Pattern |
| --- | --- |
| Iterate lazily | `def items(): yield value` |
| Wrap a function | `@decorator` plus `functools.wraps` |
| Manage a resource | `with context as resource:` |
| Customize construction | `def __init__(self, ...):` |

## Data and Config

```python
import csv
import json
from pathlib import Path

payload = json.loads(Path("event.json").read_text(encoding="utf-8"))
with Path("rows.csv").open(encoding="utf-8", newline="") as handle:
    rows = list(csv.DictReader(handle))
```

| Concern | Prefer |
| --- | --- |
| SQL | Parameterized queries or ORM binds |
| HTTP | Status checks and schema validation |
| Config | Environment values outside source |
| Logs | Structured events without secrets |

## Tests and Packaging

```python
def test_deposit_increases_balance():
    account = Account("Ada", 10)
    account.deposit(5)
    assert account._balance == 15
```

Ship with `pyproject.toml`, a virtual environment, and a CLI entry point. Related lessons: [Decorators](../Intermediate/12-decorators.md), [Logging](../Intermediate/18-logging.md), [Pytest](../Intermediate/32-pytest.md), [CLI Applications](../Intermediate/35-cli-applications.md).

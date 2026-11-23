> **Level 2: Intermediate** · Topic 27 of 35

[← Database Fundamentals](./26-database-fundamentals.md) · [↑ Level index](../README.md) · [MySQL Integration →](./28-mysql-integration.md)

# SQLite

## Overview
- **What is it?** SQLite is an embedded relational database accessed in Python through the built-in sqlite3 module.
- **Why is it important?** It gives durable SQL storage with zero server setup—ideal for local apps, tests, and small tools.
- **Where is it used?** Desktop apps, prototypes, mobile-ish local stores, CI fixtures, and edge devices.

## Learning Objectives
- Manage sqlite3 connections and transactions.
- Use placeholders and row factories.
- Understand locking, foreign keys, and file lifetime.

## Real World Applications
- Persist CLI app state without running a database server.
- Ship integration tests with a disposable file database.
- Prototype schemas before migrating to Postgres or MySQL.

## Core Concepts

### Embedded connection
- **Definition:** sqlite3 connects directly to a database file or :memory: database inside the current process.
- **Visual explanation:** ``Python process -> sqlite3 connection -> database file``
- **Practical example:**

```python
import sqlite3
connection = sqlite3.connect(":memory:")
print(connection.execute("SELECT sqlite_version()").fetchone())
```

### Rows and parameters
- **Definition:** SQLite uses `?` for positional parameters and `:name` for named parameters; `row_factory` can expose name-addressable rows.
- **Visual explanation:** ``SQL + tuple values -> cursor -> Row``
- **Practical example:**

```python
import sqlite3
connection = sqlite3.connect(":memory:")
connection.row_factory = sqlite3.Row
```

### Transactions and constraints
- **Definition:** A connection context commits on normal exit and rolls back on exceptions; foreign keys must be enabled per connection.
- **Visual explanation:** ``with connection -> transaction -> commit/rollback``
- **Practical example:**

```python
import sqlite3
connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON")
```

## Infographic Summary

| Infographic Block | Topic-specific guidance |
| --- | --- |
| 📌 Concept | SQLite is an embedded relational database accessed in Python through the built-in sqlite3 module. |
| ⚡ Purpose | SQLite stores a transactional database in one file and needs no server, making it ideal for local tools and modest workloads. |
| 🔥 Benefits | Zero-service relational storage, transactional local data, and fast setup for tools and tests. |
| 🎯 Use Cases | desktop and CLI state, local caches, tests and prototypes |
| 🚀 Best Practices | Use short transactions, parameter binding, and PRAGMA foreign_keys = ON. |
| ❌ Common Mistakes | Sharing one connection freely across threads or expecting server-scale concurrent writers. |

## Syntax Guide

### Basic Syntax

```python
import sqlite3

with sqlite3.connect("app.db") as connection:
    connection.execute("CREATE TABLE IF NOT EXISTS note (text TEXT NOT NULL)")
```

### Standard Structure

```python
import sqlite3

connection = sqlite3.connect("app.db")
connection.row_factory = sqlite3.Row
connection.execute("PRAGMA foreign_keys = ON")
row = connection.execute(
    "SELECT id, text FROM note WHERE id = ?",
    (note_id,),
).fetchone()
```

### Code Pattern

```python
# Connect to a specific file.
# Enable required pragmas.
# Bind values with ? placeholders.
# Keep writes in short connection-context transactions.
```

## Examples

### Beginner Example

```python
import sqlite3

with sqlite3.connect(":memory:") as connection:
    connection.execute("CREATE TABLE note (id INTEGER PRIMARY KEY, text TEXT NOT NULL)")
    connection.execute("INSERT INTO note (text) VALUES (?)", ("Learn SQLite",))
    print(connection.execute("SELECT text FROM note").fetchone()[0])
```

### Intermediate Example

```python
import sqlite3

with sqlite3.connect(":memory:") as connection:
    connection.row_factory = sqlite3.Row
    connection.execute(
        "CREATE TABLE inventory (sku TEXT PRIMARY KEY, quantity INTEGER NOT NULL)"
    )
    connection.executemany(
        "INSERT INTO inventory VALUES (?, ?)",
        [("A1", 3), ("B2", 7)],
    )
    rows = connection.execute(
        "SELECT sku, quantity FROM inventory WHERE quantity >= ? ORDER BY sku",
        (5,),
    )
    print([dict(row) for row in rows])
```

### Advanced Example

```python
import sqlite3

def reserve(connection, sku: str, amount: int) -> None:
    if amount <= 0:
        raise ValueError("amount must be positive")
    with connection:
        result = connection.execute(
            "UPDATE inventory SET quantity = quantity - ? "
            "WHERE sku = ? AND quantity >= ?",
            (amount, sku, amount),
        )
        if result.rowcount != 1:
            raise ValueError("unknown sku or insufficient stock")

connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE inventory (sku TEXT PRIMARY KEY, quantity INTEGER CHECK(quantity >= 0))")
connection.execute("INSERT INTO inventory VALUES (?, ?)", ("A1", 4))
reserve(connection, "A1", 2)
print(connection.execute("SELECT quantity FROM inventory").fetchone()[0])
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Open file connection] --> B[Configure pragmas and rows]
    B --> C[Execute bound SQL]
    C --> D[Commit or roll back]
    D --> E[Close connection]
```

---

[← Database Fundamentals](./26-database-fundamentals.md) · [↑ Level index](../README.md) · [MySQL Integration →](./28-mysql-integration.md)

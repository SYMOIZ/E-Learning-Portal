# MySQL Integration

## Overview

- **What is it?** MySQL integration connects Python apps to MySQL/MariaDB servers.
- **Why is it important?** MySQL powers many web stacks and hosted relational workloads.
- **Where is it used?** LAMP/LEMP stacks, WordPress backends, SaaS multitenant DBs.

## Learning Objectives

- **Skills gained:** Practical command of MySQL Integration.
- **Concepts covered:**

- Connect with a DB-API driver.
- Use parameterized queries.
- Manage connection pools in production.

- **Expected outcome:** You read and write MySQL data safely from Python.

## Real World Applications

- Web hosting
- E-commerce
- Content platforms
- Internal CRMs

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### DB-API

- **Definition:** PEP 249 cursor pattern.
- **Visual explanation:** `DB-API` → process → result
- **Practical example:**

```python
class Cursor:
    def execute(self, sql, params=()):
        return sql, params
c = Cursor()
print(c.execute('SELECT ?', (1,))[1])
```

### Connection string

- **Definition:** Host, user, database.
- **Visual explanation:** `Connection string` → process → result
- **Practical example:**

```python
DSN = {'host': 'localhost', 'database': 'app'}
print(DSN['database'])
```

### Pool

- **Definition:** Reuse connections.
- **Visual explanation:** `Pool` → process → result
- **Practical example:**

```python
POOL = []
def acquire():
    return POOL[0] if POOL else object()
print(acquire())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Drivers translate Python calls to MySQL protocol. |
| ⚡ Purpose | Remote relational storage at scale. |
| 🔥 Benefits | Mature ecosystem, replication, hosting support. |
| 🎯 Use Cases | Web apps, reporting replicas, CMS data. |
| 🚀 Best Practices | Use mysqlclient or PyMySQL; SSL; least privilege user. |
| ❌ Common Mistakes | SQL injection, no connection timeout, storing plaintext passwords. |

## Syntax Guide

### Basic Syntax

```python
conn = connect(host='localhost', user='app', password='***', database='app')
```

### Standard Structure

```python
pool -> connection -> cursor -> commit
```

### Code Pattern

```python
cursor.execute('SELECT * FROM users WHERE id=%s', (user_id,))
```

## Examples

### Beginner Example

```python
CONFIG = {'driver': 'mysql', 'host': '127.0.0.1'}
print(CONFIG['driver'])
```

### Intermediate Example

```python
def query_users(cursor, active_only=True):
    sql = 'SELECT id, email FROM users'
    if active_only:
        sql += ' WHERE active = 1'
    return cursor.execute(sql)


class Cur:
    def execute(self, sql):
        return [('1', 'a@b.com')]


print(query_users(Cur()))
```

### Advanced Example

```python
class MySQLPool:
    def __init__(self, size: int = 5):
        self._size = size
        self._in_use = 0

    def connection(self):
        if self._in_use >= self._size:
            raise RuntimeError('pool exhausted')
        self._in_use += 1
        return self

    def close(self):
        self._in_use -= 1


pool = MySQLPool(2)
conn = pool.connection()
conn.close()
print(pool._in_use)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Python App] --> B[Driver]
    B --> C[MySQL Server]
```

---

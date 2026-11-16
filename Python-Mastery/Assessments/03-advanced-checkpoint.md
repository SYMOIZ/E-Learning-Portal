# Advanced Checkpoint

[← Assessments](./README.md) · [Answer key](./03-advanced-answers.md)

These prompts are defensive and architectural. Describe safe designs. Do not include exploit steps, payloads, or credential-theft procedures.

## Short answers

1. Why can extra threads fail to speed up a tight loop of pure Python arithmetic in CPython?
2. How can reference counting miss garbage that a cyclic collector can reclaim?
3. What makes an ETL load step idempotent?
4. When is `__slots__` worth considering, and when is it the wrong default?
5. What is a descriptor, in one practical sentence?
6. Why is a secret baked into a container image a production defect?
7. Name one consistency tradeoff you accept when two services update their own databases.
8. Which signals tell you to profile before you rewrite an algorithm?

## Read the code

Write the printed result.

### Item 9

```python
from collections import Counter

print(Counter("abca").most_common(1))
```

### Item 10

```python
class Positive:
    def __set_name__(self, owner, name):
        self.private = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("value must be positive")
        setattr(obj, self.private, value)

class Order:
    quantity = Positive()

    def __init__(self, quantity):
        self.quantity = quantity

order = Order(3)
print(order.quantity)
```

### Item 11

```python
cache = {}

def fib(n):
    if n < 2:
        return n
    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]

print(fib(6))
```

### Item 12

```python
events = [
    {"id": "a", "status": "ok"},
    {"id": "b", "status": "error"},
    {"id": "a", "status": "ok"},
]
seen = set()
unique = []
for event in events:
    if event["id"] in seen:
        continue
    seen.add(event["id"])
    unique.append(event["status"])
print(unique)
```

When you are finished, open the [answer key](./03-advanced-answers.md).

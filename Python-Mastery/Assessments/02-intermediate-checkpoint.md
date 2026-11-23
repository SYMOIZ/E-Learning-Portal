# Intermediate Checkpoint

[← Assessments](./README.md) · [Answer key](./02-intermediate-answers.md)

## Short answers

1. When should you prefer composition over inheritance?
2. What does a generator give you that a list does not, and what do you give up?
3. What does `@functools.wraps` preserve on a decorated function, and why does that matter?
4. Why must SQL values travel as parameters instead of f-string interpolation?
5. For a workload of thousands of outbound HTTP calls, when would you choose `asyncio` instead of one thread per call?
6. What is the difference between logging an exception and letting it propagate?
7. How can a mock make a test pass while the production code is still wrong?
8. What belongs in a Python package's project metadata rather than inside a business module?

## Read the code

Write the printed result. Do not run the snippets yet.

### Item 9

```python
class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1
        return self

counter = Counter()
counter.inc().inc()
print(counter.value)
```

### Item 10

```python
def pairs(items):
    for item in items:
        yield item, item.upper()

print(list(pairs(["a", "b"])))
```

### Item 11

```python
class Truncate:
    def __init__(self, limit):
        self.limit = limit

    def __call__(self, text):
        return text[: self.limit]

shorten = Truncate(4)
print(shorten("documentation"))
```

### Item 12

```python
rows = [("a", 2), ("b", 1), ("a", 3)]
totals = {}
for key, amount in rows:
    totals[key] = totals.get(key, 0) + amount
print(sorted(totals.items()))
```

When you are finished, open the [answer key](./02-intermediate-answers.md).

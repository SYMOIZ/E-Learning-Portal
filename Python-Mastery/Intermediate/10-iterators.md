# Iterators

## Overview

- **What is it?** Iterators expose __iter__ and __next__ to produce elements lazily.
- **Why is it important?** Lazy iteration saves memory on large or infinite sequences.
- **Where is it used?** File scanning, streaming APIs, custom collections, pipelines.

## Learning Objectives

- **Skills gained:** Practical command of Iterators.
- **Concepts covered:**

- Use iter() and next().
- Implement iterator protocol.
- Understand StopIteration.

- **Expected outcome:** You build lazy sequence producers and consumers.

## Real World Applications

- Log streaming
- Genomics pipelines
- Market data feeds
- Pagination

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### __iter__

- **Definition:** Returns iterator object.
- **Visual explanation:** `__iter__` → process → result
- **Practical example:**

```python
data = [1, 2]
it = iter(data)
print(next(it))
```

### __next__

- **Definition:** Produces next value or raises StopIteration.
- **Visual explanation:** `__next__` → process → result
- **Practical example:**

```python
class Countdown:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1
print(list(Countdown(3)))
```

### StopIteration

- **Definition:** Signals exhaustion.
- **Visual explanation:** `StopIteration` → process → result
- **Practical example:**

```python
it = iter([])
try:
    next(it)
except StopIteration:
    print('done')
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Iterators generate values on demand. |
| ⚡ Purpose | Traverse data without loading all at once. |
| 🔥 Benefits | Memory efficient, composable pipelines. |
| 🎯 Use Cases | CSV row scan, socket read loop, paginated API. |
| 🚀 Best Practices | Separate iterable from iterator when reused; handle StopIteration. |
| ❌ Common Mistakes | Non-resetting iterators, confusing iterable vs iterator. |

## Syntax Guide

### Basic Syntax

```python
for item in iterable:
    print(item)
```

### Standard Structure

```python
__iter__ -> __next__ loop -> StopIteration
```

### Code Pattern

```python
it = iter(source)
while True:
    try:
        item = next(it)
    except StopIteration:
        break
    print(item)
```

## Examples

### Beginner Example

```python
it = iter(['a', 'b'])
print(next(it), next(it))
```

### Intermediate Example

```python
class Range:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        value = self.i
        self.i += 1
        return value


print(list(Range(3)))
```

### Advanced Example

```python
def line_generator(path: str):
    with open(path, encoding='utf-8') as handle:
        for line in handle:
            yield line.rstrip('\n')


print(sum(1 for _ in line_generator('README.md')))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Iterable] --> B[Iterator]
    B --> C[next()]
```

---

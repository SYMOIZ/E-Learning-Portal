> **Level 2: Intermediate** · Topic 10 of 35

[← Magic Methods](./09-magic-methods.md) · [↑ Level index](../README.md) · [Generators →](./11-generators.md)

# Iterators

## Overview
- **What is it?** Iterators are pull-based objects that produce one item at a time through the iterator protocol (__iter__/__next__).
- **Why is it important?** They enable lazy processing of large or infinite streams without loading everything into memory.
- **Where is it used?** File readers, database cursors, pagination clients, pipelines, and custom collections.

## Learning Objectives
- Distinguish iterable from iterator.
- Implement __iter__ and __next__.
- Use iter(callable, sentinel) and iterator tools.

## Real World Applications
- Stream log lines from multi-gigabyte files safely.
- Page through API results without buffering every record.
- Build custom collections that work with for-loops and comprehensions.

## Core Concepts

### Iterable protocol
- **Definition:** An iterable's __iter__ returns a fresh iterator or, for an iterator, itself.
- **Visual explanation:** ``iterable --iter()--> iterator``
- **Practical example:**

```python
numbers = [1, 2]
iterator = iter(numbers)
print(next(iterator))
```

### Iterator protocol
- **Definition:** An iterator's __next__ returns the next value and raises StopIteration permanently after exhaustion.
- **Visual explanation:** ``next -> value -> ... -> StopIteration``
- **Practical example:**

```python
iterator = iter("ab")
print(next(iterator), next(iterator))
```

### Stateful consumption
- **Definition:** Iterators are single-pass cursors; consuming through one reference advances the same underlying state.
- **Visual explanation:** ``shared cursor: consumer A advances consumer B``
- **Practical example:**

```python
cursor = iter([10, 20, 30])
first = next(cursor)
rest = list(cursor)
```

## Infographic Summary

| Infographic Block | Topic-specific guidance |
| --- | --- |
| 📌 Concept | Iterators are pull-based objects that produce one item at a time through the iterator protocol (__iter__/__next__). |
| ⚡ Purpose | An iterable creates an iterator; an iterator tracks traversal state and raises StopIteration when exhausted. |
| 🔥 Benefits | Memory-efficient traversal, explicit single-pass state, and compatibility with Python iteration tools. |
| 🎯 Use Cases | custom collections, streaming parsers, lazy data pipelines |
| 🚀 Best Practices | Return a fresh iterator from reusable container objects. |
| ❌ Common Mistakes | Expecting an exhausted iterator to restart automatically. |

## Syntax Guide

### Basic Syntax

```python
iterator = iter([10, 20])
print(next(iterator))
print(next(iterator))
```

### Standard Structure

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
```

### Code Pattern

```python
# Iterable produces an iterator.
# Iterator owns traversal state.
# __next__ returns one item.
# Exhaustion is signaled with StopIteration.
```

## Examples

### Beginner Example

```python
colors = ["red", "green", "blue"]
cursor = iter(colors)
print(next(cursor))
print(list(cursor))
```

### Intermediate Example

```python
class StepRange:
    def __init__(self, start: int, stop: int, step: int):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

print(list(StepRange(1, 8, 2)))
```

### Advanced Example

```python
class LogEntries:
    def __init__(self, lines):
        self.lines = list(lines)

    def __iter__(self):
        return LogEntryIterator(self.lines)

class LogEntryIterator:
    def __init__(self, lines):
        self._source = iter(lines)

    def __iter__(self):
        return self

    def __next__(self):
        line = next(self._source)
        timestamp, message = line.split(" ", 1)
        return {"timestamp": timestamp, "message": message}

entries = LogEntries(["09:00 started", "09:01 ready"])
print(list(entries))
print(list(entries))  # fresh traversal
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Request iter()] --> B[Obtain iterator]
    B --> C[Call next()]
    C --> D[Return item and advance]
    D --> E[Raise StopIteration]
```

---

[← Magic Methods](./09-magic-methods.md) · [↑ Level index](../README.md) · [Generators →](./11-generators.md)

> **Level 2: Intermediate** · Topic 22 of 35

[← Multiprocessing](./21-multiprocessing.md) · [↑ Level index](../README.md) · [API Development →](./23-api-development.md)

# Async Programming

## Overview
- **What is it?** Async Programming is the intermediate Python topic of cooperatively overlapping many non-blocking I/O operations on an event loop.
- **Why is it important?** asyncio scales I/O concurrency with tasks that yield control at await points; it does not make CPU work parallel.
- **Where is it used?** many network connections, concurrent service calls, event-driven workers.

## Learning Objectives
- Explain coroutine, task, and event-loop roles.
- Use await, gather, TaskGroup, and timeouts.
- Keep blocking and CPU-heavy work off the event loop.

## Real World Applications
- **Engineering:** Many network connections rely on this topic.
- **Product work:** It supports concurrent service calls.
- **Operations:** It appears in event-driven workers.

## Core Concepts

### Coroutines and await
- **Definition:** Calling async def creates a coroutine; await suspends the current task until the awaited operation is ready.
- **Visual explanation:** ``coroutine -> await I/O -> suspend -> resume``
- **Practical example:**

```python
import asyncio

async def pause():
    await asyncio.sleep(0)

asyncio.run(pause())
```

### Tasks and structured concurrency
- **Definition:** A Task schedules a coroutine; TaskGroup scopes sibling lifetimes and propagates failures as a group.
- **Visual explanation:** ``TaskGroup -> child tasks -> wait/cancel together``
- **Practical example:**

```python
import asyncio

async def main():
    async with asyncio.TaskGroup() as group:
        group.create_task(asyncio.sleep(0))

asyncio.run(main())
```

### Blocking boundaries
- **Definition:** Blocking calls freeze the loop; use asynchronous libraries, asyncio.to_thread for blocking I/O, or processes for CPU-bound work.
- **Visual explanation:** ``event loop -> async I/O | to_thread blocking I/O | process CPU``
- **Practical example:**

```python
import asyncio
from pathlib import Path

async def read_text(path):
    return await asyncio.to_thread(Path(path).read_text)
```

## Infographic Summary

| Infographic Block | Topic-specific guidance |
| --- | --- |
| 📌 Concept | Coroutines and await, Tasks and structured concurrency, Blocking boundaries |
| ⚡ Purpose | asyncio scales I/O concurrency with tasks that yield control at await points; it does not make CPU work parallel. |
| 🔥 Benefits | High I/O concurrency, efficient task scheduling, and structured cancellation and timeout handling. |
| 🎯 Use Cases | many network connections, concurrent service calls, event-driven workers |
| 🚀 Best Practices | Create concurrency explicitly and bound fan-out with semaphores or worker pools. |
| ❌ Common Mistakes | Calling time.sleep or synchronous HTTP clients inside a coroutine. |

## Syntax Guide

### Basic Syntax

```python
import asyncio

async def main():
    await asyncio.sleep(0.1)

asyncio.run(main())
```

### Standard Structure

```python
import asyncio

async def fetch_all(urls):
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(fetch(url)) for url in urls]
    return [task.result() for task in tasks]
```

### Code Pattern

```python
# Start one top-level event loop.
# Schedule independent I/O as bounded tasks.
# await operations that can suspend.
# Cancel, time out, and collect failures explicitly.
```

## Examples

### Beginner Example

```python
import asyncio

async def greet_after(delay: float, name: str):
    await asyncio.sleep(delay)
    return f"Hello, {name}"

async def main():
    print(await greet_after(0.01, "Ada"))

asyncio.run(main())
```

### Intermediate Example

```python
import asyncio

async def request(identifier: int) -> str:
    await asyncio.sleep(0.01)  # represents non-blocking network I/O
    return f"item-{identifier}"

async def main():
    results = await asyncio.gather(*(request(i) for i in range(4)))
    print(results)

asyncio.run(main())
```

### Advanced Example

```python
import asyncio

async def bounded_call(identifier: int, limit: asyncio.Semaphore):
    async with limit:
        async with asyncio.timeout(1):
            await asyncio.sleep(0.01)
            return f"result-{identifier}"

async def main():
    limit = asyncio.Semaphore(3)
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(bounded_call(i, limit)) for i in range(8)]
    print([task.result() for task in tasks])

asyncio.run(main())
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Create event loop] --> B[Schedule coroutines as tasks]
    B --> C[Task awaits I/O]
    C --> D[Loop runs another ready task]
    D --> E[Resume and collect results]
```

---

[← Multiprocessing](./21-multiprocessing.md) · [↑ Level index](../README.md) · [API Development →](./23-api-development.md)

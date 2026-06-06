# Multithreading

## Overview

- **What is it?** Multithreading runs concurrent threads within one process sharing memory.
- **Why is it important?** Threads overlap I/O wait times for network and disk workloads.
- **Where is it used?** Socket servers, downloaders, UI backends, parallel I/O.

## Learning Objectives

- **Skills gained:** Practical command of Multithreading.
- **Concepts covered:**

- Start threads with threading module.
- Protect shared state with locks.
- Know GIL limits on CPU-bound work.

- **Expected outcome:** You parallelize I/O-bound tasks with threads safely.

## Real World Applications

- Web crawlers
- Chat servers
- Monitoring agents
- Desktop apps

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Thread

- **Definition:** Concurrent execution unit.
- **Visual explanation:** `Thread` → process → result
- **Practical example:**

```python
import threading
def work():
    print('run')
t = threading.Thread(target=work)
t.start()
t.join()
```

### Lock

- **Definition:** Mutual exclusion.
- **Visual explanation:** `Lock` → process → result
- **Practical example:**

```python
import threading
lock = threading.Lock()
count = 0
def inc():
    global count
    with lock:
        count += 1
inc()
print(count)
```

### ThreadPoolExecutor

- **Definition:** Managed pool.
- **Visual explanation:** `ThreadPoolExecutor` → process → result
- **Practical example:**

```python
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=2) as ex:
    print(list(ex.map(lambda x: x * 2, [1, 2, 3])))
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Threads share memory; locks coordinate access. |
| ⚡ Purpose | Concurrent I/O and responsiveness. |
| 🔥 Benefits | Simple shared state, low overhead for I/O. |
| 🎯 Use Cases | Parallel HTTP fetches, worker queues. |
| 🚀 Best Practices | Avoid shared mutable state; use queues; pool executors. |
| ❌ Common Mistakes | CPU-bound threading, deadlocks, race conditions. |

## Syntax Guide

### Basic Syntax

```python
threading.Thread(target=func, args=(1,)).start()
```

### Standard Structure

```python
define worker -> start threads -> join
```

### Code Pattern

```python
with ThreadPoolExecutor() as pool:
    pool.map(fn, items)
```

## Examples

### Beginner Example

```python
import threading

def hello():
    print('hello from thread')

t = threading.Thread(target=hello)
t.start()
t.join()
```

### Intermediate Example

```python
import threading

counter = {'n': 0}
lock = threading.Lock()

def worker():
    with lock:
        counter['n'] += 1

threads = [threading.Thread(target=worker) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(counter['n'])
```

### Advanced Example

```python
from concurrent.futures import ThreadPoolExecutor, as_completed


def fetch(n: int) -> int:
    return n * n


with ThreadPoolExecutor(max_workers=4) as pool:
    futures = [pool.submit(fetch, i) for i in range(6)]
    results = [f.result() for f in as_completed(futures)]
print(sorted(results))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Main Thread] --> B[Worker Threads]
    B --> C[Shared State + Locks]
```

---

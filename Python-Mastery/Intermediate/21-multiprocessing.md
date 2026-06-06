# Multiprocessing

## Overview

- **What is it?** Multiprocessing spawns separate processes to bypass the GIL for CPU work.
- **Why is it important?** True parallelism for CPU-bound Python tasks requires processes.
- **Where is it used?** Data crunching, image processing, scientific compute, batch jobs.

## Learning Objectives

- **Skills gained:** Practical command of Multiprocessing.
- **Concepts covered:**

- Use multiprocessing.Process and Pool.
- Pass data via queues and pipes.
- Guard entry with if __name__ == '__main__'.

- **Expected outcome:** You parallelize CPU-bound workloads across cores.

## Real World Applications

- Quant analytics
- Video encoding
- ML preprocessing
- Simulation

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Process

- **Definition:** Independent Python interpreter.
- **Visual explanation:** `Process` → process → result
- **Practical example:**

```python
import multiprocessing as mp
def f(x):
    return x + 1
if __name__ == '__main__':
    p = mp.Process(target=f, args=(1,))
    p.start()
    p.join()
```

### Pool

- **Definition:** Worker process pool.
- **Visual explanation:** `Pool` → process → result
- **Practical example:**

```python
from multiprocessing import Pool
if __name__ == '__main__':
    with Pool(2) as pool:
        print(pool.map(lambda x: x * 2, [1, 2, 3]))
```

### Queue

- **Definition:** Inter-process messaging.
- **Visual explanation:** `Queue` → process → result
- **Practical example:**

```python
from multiprocessing import Process, Queue
def worker(q):
    q.put('done')
if __name__ == '__main__':
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    print(q.get())
    p.join()
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Processes have separate memory spaces. |
| ⚡ Purpose | CPU parallelism and isolation. |
| 🔥 Benefits | Uses multiple cores, fault isolation. |
| 🎯 Use Cases | Monte Carlo, batch transforms, parallel tests. |
| 🚀 Best Practices | Protect main; pick spawn on Windows; minimize large pickles. |
| ❌ Common Mistakes | Forgetting main guard, huge shared objects, too many processes. |

## Syntax Guide

### Basic Syntax

```python
if __name__ == '__main__':
    Process(target=work).start()
```

### Standard Structure

```python
spawn workers -> communicate -> join
```

### Code Pattern

```python
with Pool(n) as pool:
    pool.map(func, data)
```

## Examples

### Beginner Example

```python
from multiprocessing import Process


def double(x):
    print(x * 2)


if __name__ == '__main__':
    p = Process(target=double, args=(21,))
    p.start()
    p.join()
```

### Intermediate Example

```python
from multiprocessing import Pool


def square(x: int) -> int:
    return x * x


if __name__ == '__main__':
    with Pool(2) as pool:
        print(pool.map(square, range(5)))
```

### Advanced Example

```python
from concurrent.futures import ProcessPoolExecutor


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as ex:
        print(list(ex.map(fib, [10, 12, 14])))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Parent Process] --> B[Child Processes]
    B --> C[Results via Queue/Pool]
```

---

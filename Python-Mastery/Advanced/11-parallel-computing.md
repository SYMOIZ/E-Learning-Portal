> **Level 3: Advanced** · Topic 11 of 40

[← Concurrency](./10-concurrency.md) · [↑ Level index](../README.md) · [Distributed Systems →](./12-distributed-systems.md)

# Parallel Computing

## Overview
- **What is it?** Parallel computing executes CPU work simultaneously across cores or machines, commonly using processes to bypass CPython's global interpreter lock.
- **Why is it important?** Speedup depends on task size, serialization cost, memory bandwidth, core count, and the serial fraction of the workload.
- **Where is it used?** It supports numerical transforms, media processing, simulations, compilation, and independent batch computation.

## Learning Objectives
- Distinguish concurrency from actual multi-core parallel execution.
- Use process pools with picklable, coarse-grained tasks and explicit shutdown.
- Evaluate speedup against serialization and scheduling overhead.

## Real World Applications
- Parallel image transforms, document parsing, simulation runs, and feature extraction.
- Partitioning independent CPU-bound records across worker processes.
- Using shared memory when copying large arrays would dominate runtime.

## Core Concepts

### Process Isolation
- **Definition:** Worker processes have separate Python heaps; arguments and results normally cross process boundaries through serialization.
- **Visual explanation:** `parent object → pickle/IPC → worker heap → result IPC`
- **Practical example:**

```python
from concurrent.futures import ProcessPoolExecutor

def square(value: int) -> int:
    return value * value

if __name__ == "__main__":
    with ProcessPoolExecutor() as pool:
        print(list(pool.map(square, range(5))))
```

### Granularity and Amdahl's Law
- **Definition:** Parallelism helps when each submitted unit contains enough CPU work to amortize startup, scheduling, and transfer costs.
- **Visual explanation:** `serial setup + parallel fraction / workers + communication overhead`
- **Practical example:**

```python
def theoretical_speedup(parallel_fraction: float, workers: int) -> float:
    serial = 1.0 - parallel_fraction
    return 1.0 / (serial + parallel_fraction / workers)

print(theoretical_speedup(0.9, 8))
```

### Shared Memory
- **Definition:** Shared memory exposes one byte buffer to multiple processes, avoiding copies but requiring disciplined ownership and synchronization.
- **Visual explanation:** `shared segment ↔ process views; coordinate writes explicitly`
- **Practical example:**

```python
from multiprocessing import shared_memory

segment = shared_memory.SharedMemory(create=True, size=4)
try:
    segment.buf[:4] = b"data"
    print(bytes(segment.buf[:4]))
finally:
    segment.close()
    segment.unlink()
```

## Infographic Summary

| Infographic Block | Topic-specific takeaway |
| --- | --- |
| 📌 Concept | Parallel computing executes CPU work simultaneously across cores or machines, commonly using processes to bypass CPython's global interpreter lock. |
| ⚡ Purpose | Speedup depends on task size, serialization cost, memory bandwidth, core count, and the serial fraction of the workload. |
| 🔥 Benefits | Builds the ability to distinguish concurrency from actual multi-core parallel execution; it also helps practitioners use process pools with picklable, coarse-grained tasks and explicit shutdown. |
| 🎯 Use Cases | Parallel image transforms, document parsing, simulation runs, and feature extraction. Partitioning independent CPU-bound records across worker processes. |
| 🚀 Best Practices | Benchmark sequential and parallel versions on production-shaped data. |
| ❌ Common Mistakes | Ignoring the guardrail “Do not submit tiny tasks one future at a time”. |

## Syntax Guide

### Basic Syntax

```python
from concurrent.futures import ProcessPoolExecutor

def cube(value: int) -> int:
    return value ** 3
```

### Standard Structure

```python
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as executor:
        values = list(executor.map(cube, range(10), chunksize=2))
```

### Code Pattern

```python
from multiprocessing import get_context

if __name__ == "__main__":
    context = get_context("spawn")
    with context.Pool(processes=2) as pool:
        values = pool.map(abs, [-3, -2, -1])
```

## Examples

### Beginner Example

```python
def count_primes(limit: int) -> int:
    def is_prime(value: int) -> bool:
        return value > 1 and all(value % divisor for divisor in range(2, int(value ** 0.5) + 1))
    return sum(is_prime(value) for value in range(limit))
```

### Intermediate Example

```python
from concurrent.futures import ProcessPoolExecutor

def count_primes(limit: int) -> int:
    def is_prime(value: int) -> bool:
        return value > 1 and all(value % divisor for divisor in range(2, int(value ** 0.5) + 1))
    return sum(is_prime(value) for value in range(limit))

limits = [10_000, 11_000, 12_000]
if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        counts = list(executor.map(count_primes, limits))
    print(counts)
```

### Advanced Example

```python
from concurrent.futures import ProcessPoolExecutor, as_completed

def count_primes(limit: int) -> int:
    def is_prime(value: int) -> bool:
        return value > 1 and all(value % divisor for divisor in range(2, int(value ** 0.5) + 1))
    return sum(is_prime(value) for value in range(limit))

limits = [10_000, 11_000, 12_000]
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(count_primes, limit): limit for limit in limits}
        for future in as_completed(futures):
            limit = futures[future]
            try:
                print(limit, future.result())
            except Exception as error:
                print(limit, type(error).__name__)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Measure sequential baseline] --> B[Partition coarse tasks]
    B --> C[Choose process topology]
    C --> D[Run and collect failures]
    D --> E[Compare speedup and memory]
    E -. feedback .-> A
```

---

[← Concurrency](./10-concurrency.md) · [↑ Level index](../README.md) · [Distributed Systems →](./12-distributed-systems.md)

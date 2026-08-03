> **Level 2: Intermediate** · Topic 21 of 35

[← Multithreading](./20-multithreading.md) · [↑ Level index](../README.md) · [Async Programming →](./22-async-programming.md)

# Multiprocessing

## Overview
- **What is it?** Multiprocessing runs work in separate processes so CPU-bound Python tasks can use multiple cores.
- **Why is it important?** It bypasses the GIL for parallel computation at the cost of higher memory and IPC complexity.
- **Where is it used?** Image processing, numerical jobs, data transforms, and batch crunching.

## Learning Objectives
- Choose processes for coarse CPU-bound tasks.
- Protect entry points for spawn compatibility.
- Use pools and IPC without assuming shared memory.

## Real World Applications
- Resize thousands of images across CPU cores.
- Parallelize CPU-heavy feature engineering steps.
- Isolate crash-prone workers from the main process.

## Core Concepts

### Process isolation
- **Definition:** Each process owns its interpreter and address space; arguments and results are normally serialized between processes.
- **Visual explanation:** ``parent --pickle--> worker process --pickle--> result``
- **Practical example:**

```python
from multiprocessing import Process

process = Process(target=print, args=("child",))
process.start()
process.join()
```

### Process pools
- **Definition:** ProcessPoolExecutor keeps a bounded set of workers and maps independent CPU tasks onto them.
- **Visual explanation:** ``CPU tasks -> process pool -> cores -> results``
- **Practical example:**

```python
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as pool:
    values = list(pool.map(abs, [-1, -2]))
```

### Safe startup and IPC
- **Definition:** The __main__ guard prevents recursive child creation under spawn; queues and pipes explicitly exchange messages.
- **Visual explanation:** ``main guard -> spawn safely; Queue -> IPC``
- **Practical example:**

```python
def main():
    print("parent entry")

if __name__ == "__main__":
    main()
```

## Infographic Summary

| Infographic Block | Topic-specific guidance |
| --- | --- |
| 📌 Concept | Multiprocessing runs work in separate processes so CPU-bound Python tasks can use multiple cores. |
| ⚡ Purpose | Processes have independent interpreters and memory, bypassing the GIL at the cost of serialization and startup overhead. |
| 🔥 Benefits | Parallel CPU execution across cores, process isolation, and scalable batch computation. |
| 🎯 Use Cases | image transforms, numeric batch calculations, CPU-heavy parsing |
| 🚀 Best Practices | Send coarse, pickleable tasks and keep shared mutable state out of workers. |
| ❌ Common Mistakes | Expecting child mutations of ordinary objects to appear in the parent. |

## Syntax Guide

### Basic Syntax

```python
from multiprocessing import Process

if __name__ == "__main__":
    process = Process(target=compute, args=(input_value,))
    process.start()
    process.join()
```

### Standard Structure

```python
from concurrent.futures import ProcessPoolExecutor

def main():
    with ProcessPoolExecutor() as pool:
        return list(pool.map(cpu_heavy, inputs))

if __name__ == "__main__":
    print(main())
```

### Code Pattern

```python
# Confirm work is CPU-bound and independent.
# Define a top-level pickleable worker.
# Guard process creation with __main__.
# Collect results and handle worker exceptions.
```

## Examples

### Beginner Example

```python
from multiprocessing import Process

def calculate_square(value):
    print(value * value)

if __name__ == "__main__":
    process = Process(target=calculate_square, args=(12,))
    process.start()
    process.join()
    if process.exitcode != 0:
        raise RuntimeError("worker failed")
```

### Intermediate Example

```python
from concurrent.futures import ProcessPoolExecutor

def count_primes(limit: int) -> int:
    total = 0
    for candidate in range(2, limit):
        if all(candidate % divisor for divisor in range(2, int(candidate ** 0.5) + 1)):
            total += 1
    return total

def main():
    with ProcessPoolExecutor(max_workers=2) as pool:
        return list(pool.map(count_primes, [5000, 6000, 7000]))

if __name__ == "__main__":
    print(main())
```

### Advanced Example

```python
from concurrent.futures import ProcessPoolExecutor, as_completed

def checksum(chunk: bytes) -> tuple[int, int]:
    return len(chunk), sum(chunk) % 256

def checksums(chunks):
    with ProcessPoolExecutor(max_workers=3) as pool:
        future_to_index = {
            pool.submit(checksum, chunk): index
            for index, chunk in enumerate(chunks)
        }
        ordered = [None] * len(chunks)
        for future in as_completed(future_to_index):
            ordered[future_to_index[future]] = future.result()
        return ordered

if __name__ == "__main__":
    print(checksums([b"alpha", b"beta", b"gamma"]))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Identify CPU-bound chunks] --> B[Serialize task input]
    B --> C[Run on worker processes]
    C --> D[Serialize results]
    D --> E[Join pool and combine]
```

---

[← Multithreading](./20-multithreading.md) · [↑ Level index](../README.md) · [Async Programming →](./22-async-programming.md)

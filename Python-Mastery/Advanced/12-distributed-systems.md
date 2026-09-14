> **Level 3: Advanced** · Topic 12 of 40

[← Parallel Computing](./11-parallel-computing.md) · [↑ Level index](../README.md) · [Network Programming →](./13-network-programming.md)

# Distributed Systems

## Overview
- **What is it?** A distributed system coordinates independent processes across unreliable networks where delays, retries, duplication, reordering, and partial failure are normal.
- **Why is it important?** Correctness requires explicit delivery semantics, idempotency, timeouts, consistency choices, and observability rather than assuming remote calls behave like local functions.
- **Where is it used?** These principles underpin service architectures, job queues, replicated stores, event streams, and multi-region platforms.

## Learning Objectives
- Model partial failure, at-least-once delivery, and consistency trade-offs.
- Implement bounded retries, exponential backoff with jitter, and circuit breaking.
- Design idempotent operations and correlate work across service boundaries.

## Real World Applications
- Payment commands that may be delivered more than once.
- Service calls that degrade safely when a dependency is slow or unavailable.
- Replicated data and event pipelines with explicit ordering and recovery rules.

## Core Concepts

### Partial Failure and Deadlines
- **Definition:** A caller cannot distinguish a lost request from a lost response without protocol support, so every remote operation needs a deadline and an uncertainty policy.
- **Visual explanation:** `send → timeout? → outcome may be success, failure, or unknown`
- **Practical example:**

```python
from urllib.request import urlopen

def fetch_health(url: str, timeout: float = 2.0) -> bytes:
    with urlopen(url, timeout=timeout) as response:
        return response.read(1024)
```

### Idempotency and Delivery
- **Definition:** An idempotency key lets a receiver persist one outcome per logical command, making duplicate at-least-once deliveries return the original result.
- **Visual explanation:** `command + stable key → deduplication record → one side effect`
- **Practical example:**

```python
outcomes: dict[str, str] = {}

def reserve(command_id: str, sku: str) -> str:
    if command_id not in outcomes:
        outcomes[command_id] = f"reserved:{sku}"
    return outcomes[command_id]

assert reserve("cmd-7", "book") == reserve("cmd-7", "book")
```

### Resilience Policies
- **Definition:** Retries target transient failures and must be bounded, delayed, jittered, and budgeted; circuit breakers stop amplifying a persistently unhealthy dependency.
- **Visual explanation:** `failure → classify → backoff+jitter → retry budget or open circuit`
- **Practical example:**

```python
import random
import time
from collections.abc import Callable

def retry(operation: Callable[[], str], attempts: int = 3) -> str:
    for attempt in range(attempts):
        try:
            return operation()
        except TimeoutError:
            if attempt + 1 == attempts:
                raise
            time.sleep((2 ** attempt + random.random()) / 10)
    raise AssertionError("unreachable")
```

## Infographic Summary

| Infographic Block | Topic-specific takeaway |
| --- | --- |
| 📌 Concept | A distributed system coordinates independent processes across unreliable networks where delays, retries, duplication, reordering, and partial failure are normal. |
| ⚡ Purpose | Correctness requires explicit delivery semantics, idempotency, timeouts, consistency choices, and observability rather than assuming remote calls behave like local functions. |
| 🔥 Benefits | Builds the ability to model partial failure, at-least-once delivery, and consistency trade-offs; it also helps practitioners implement bounded retries, exponential backoff with jitter, and circuit breaking. |
| 🎯 Use Cases | Payment commands that may be delivered more than once. Service calls that degrade safely when a dependency is slow or unavailable. |
| 🚀 Best Practices | Circuit breakers protect both caller and dependency during sustained failure. |
| ❌ Common Mistakes | Ignoring the guardrail “Exactly-once effects require durable coordination, not a queue setting alone”. |

## Syntax Guide

### Basic Syntax

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Command:
    idempotency_key: str
    payload: dict[str, str]
```

### Standard Structure

```python
import random

def backoff(attempt: int, cap: float = 10.0) -> float:
    maximum = min(cap, 0.25 * (2 ** attempt))
    return random.uniform(0.0, maximum)
```

### Code Pattern

```python
from enum import Enum, auto

class CircuitState(Enum):
    CLOSED = auto()
    OPEN = auto()
    HALF_OPEN = auto()
```

## Examples

### Beginner Example

```python
processed: set[str] = set()

def handle(message_id: str) -> bool:
    if message_id in processed:
        return False
    processed.add(message_id)
    return True
```

### Intermediate Example

```python
from dataclasses import dataclass
from time import monotonic

@dataclass
class Deadline:
    expires_at: float

    @classmethod
    def after(cls, seconds: float) -> "Deadline":
        return cls(monotonic() + seconds)

    def remaining(self) -> float:
        return max(0.0, self.expires_at - monotonic())
```

### Advanced Example

```python
from dataclasses import dataclass
from time import monotonic

@dataclass
class CircuitBreaker:
    threshold: int = 3
    reset_after: float = 10.0
    failures: int = 0
    opened_at: float | None = None

    def allow(self) -> bool:
        return self.opened_at is None or monotonic() - self.opened_at >= self.reset_after

    def record_failure(self) -> None:
        self.failures += 1
        if self.failures >= self.threshold:
            self.opened_at = monotonic()

    def record_success(self) -> None:
        self.failures = 0
        self.opened_at = None
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Receive command] --> B[Check deadline and idempotency]
    B --> C[Attempt dependency call]
    C --> D[Back off or open circuit]
    D --> E[Record outcome and telemetry]
    E -. feedback .-> A
```

---

[← Parallel Computing](./11-parallel-computing.md) · [↑ Level index](../README.md) · [Network Programming →](./13-network-programming.md)

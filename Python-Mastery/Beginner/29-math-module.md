> **Level 1: Beginner** · Topic 29 of 35

[← Date and Time](./28-date-and-time.md) · [↑ Level index](../README.md) · [Random Module →](./30-random-module.md)

# Math Module

## Overview
- **What is it?** The standard-library `math` module provides constants and real-number functions beyond basic arithmetic operators.
- **Why is it important?** Its tested implementations cover roots, rounding directions, logarithms, trigonometry, and accurate aggregation.
- **Where is it used?** Geometry, simulations, analytics, finance, and scientific calculations use these functions.

## Learning Objectives
- Import and call common `math` functions.
- Use constants and choose floor, ceil, truncation, or closeness checks correctly.
- Recognize that `math` generally operates on real numbers, not arbitrary collections.

## Real World Applications
- Calculate geometric measurements.
- Round resource counts up to whole units.
- Compare floating-point results with a tolerance.

## Core Concepts

### Constants and roots
- **Definition:** `math.pi`, `math.e`, `sqrt`, and related functions provide standard numeric definitions.
- **Visual explanation:** `numeric input -> math function -> float result`
- **Practical example:**

```python
import math
radius = 3
print(math.pi * radius ** 2, math.sqrt(81))
```

### Rounding direction
- **Definition:** `floor` rounds down, `ceil` rounds up, and `trunc` removes the fractional part toward zero.
- **Visual explanation:** `real number -> chosen rounding rule -> integer`
- **Practical example:**

```python
import math
print(math.floor(2.9), math.ceil(2.1), math.trunc(-2.9))
```

### Floating-point reliability
- **Definition:** `isclose` compares approximate values using relative and absolute tolerances; `fsum` reduces summation error.
- **Visual explanation:** `floating results + tolerance -> reliable comparison`
- **Practical example:**

```python
import math
total = math.fsum([0.1, 0.1, 0.1])
print(total, math.isclose(total, 0.3))
```

## Infographic Summary

| Infographic Block | Topic-Specific Takeaway |
| --- | --- |
| 📌 Concept | The standard-library `math` module provides constants and real-number functions beyond basic arithmetic operators. |
| ⚡ Purpose | Apply standard mathematical constants and real-number functions reliably. |
| 🔥 Benefits | Its tested implementations cover roots, rounding directions, logarithms, trigonometry, and accurate aggregation. |
| 🎯 Use Cases | Geometry, simulations, analytics, finance, and scientific calculations use these functions. |
| 🚀 Best Practices | Choose the function whose mathematical rule matches the domain, and use `isclose` instead of exact float equality. |
| ❌ Common Mistakes | Using `round` or `int` when the requirement specifically says always round up or always round down. |

## Syntax Guide

### Basic Syntax

```python
import math
print(math.sqrt(144))
print(math.pi)
```

### Standard Structure

```python
import math
items = 23
box_capacity = 5
boxes = math.ceil(items / box_capacity)
print(boxes)
```

### Code Pattern

```python
import math
points = [(0, 0), (3, 4), (6, 8)]
distances = []
for (x1, y1), (x2, y2) in zip(points, points[1:]):
    distances.append(math.hypot(x2 - x1, y2 - y1))
print(math.fsum(distances))
```

## Examples

### Beginner Example

```python
import math
radius = 5
print(math.tau * radius)
```

### Intermediate Example

```python
import math
angle_degrees = 30
angle_radians = math.radians(angle_degrees)
print(math.sin(angle_radians))
```

### Advanced Example

```python
import math

def compound(principal, annual_rate, years):
    return principal * math.pow(1 + annual_rate, years)

future = compound(1000, 0.05, 10)
print(f"${future:.2f}")
print(math.isfinite(future))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Identify mathematical rule]
    B[Select math constant or function]
    C[Pass numeric arguments]
    D[Check finite or approximate result]
    E[Use value in domain calculation]
    A --> B
    B --> C
    C --> D
    D --> E
```

---

[← Date and Time](./28-date-and-time.md) · [↑ Level index](../README.md) · [Random Module →](./30-random-module.md)

> **Level 2: Intermediate** · Topic 2 of 35

[← Object Oriented Programming](./01-object-oriented-programming.md) · [↑ Level index](../README.md) · [Objects →](./03-objects.md)

# Classes

## Overview
- **What is it?** A class is a blueprint that defines the attributes and methods shared by its instances.
- **Why is it important?** Classes let you create many related objects from one validated definition and keep behavior next to the data it operates on.
- **Where is it used?** Domain models, ORM entities, framework extensions, adapters, and configuration objects.

## Learning Objectives
- Define instance, class, and static methods correctly.
- Distinguish class attributes from instance attributes.
- Use class methods as named alternative constructors.

## Real World Applications
- Define validated product, user, or ticket types used across an application.
- Extend framework base classes for web views, serializers, or widgets.
- Build reusable adapters that wrap external services behind a stable interface.

## Core Concepts

### Class body and namespace
- **Definition:** Executing a class statement creates a namespace and then a class object whose attributes come from that namespace.
- **Visual explanation:** ``class statement -> namespace -> class object``
- **Practical example:**

```python
class Plan:
    currency = "USD"

print(Plan.currency)
```

### Instance methods
- **Definition:** An instance method is a function descriptor that binds the receiving instance to its first parameter, conventionally self.
- **Visual explanation:** ``plan.price() -> Plan.price(plan)``
- **Practical example:**

```python
class Plan:
    def label(self):
        return f"{self.name} plan"

plan = Plan()
plan.name = "Pro"
print(plan.label())
```

### Class and static methods
- **Definition:** A class method receives the class and supports polymorphic factories; a static method is namespaced utility code with no implicit receiver.
- **Visual explanation:** ``cls factory | static utility``
- **Practical example:**

```python
class User:
    @classmethod
    def guest(cls):
        return cls("guest")

    def __init__(self, name):
        self.name = name
```

## Infographic Summary

| Infographic Block | Topic-specific guidance |
| --- | --- |
| 📌 Concept | A class is a blueprint that defines the attributes and methods shared by its instances. |
| ⚡ Purpose | A class is the blueprint and namespace; it is not an individual runtime object. |
| 🔥 Benefits | Reusable type definitions, shared behavior, and expressive construction APIs. |
| 🎯 Use Cases | validated domain types, framework models, reusable adapters |
| 🚀 Best Practices | Put shared constants on the class and per-object mutable state on each instance. |
| ❌ Common Mistakes | Using a mutable class attribute as if every instance owned a separate value. |

## Syntax Guide

### Basic Syntax

```python
class Product:
    category = "book"

    def title_line(self):
        return self.title.upper()
```

### Standard Structure

```python
class Distance:
    def __init__(self, meters: float):
        self.meters = meters

    @classmethod
    def from_kilometers(cls, kilometers: float):
        return cls(kilometers * 1000)
```

### Code Pattern

```python
# Class attribute: shared definition-level data
# Instance attribute: state unique to one object
# Instance method: behavior using self
# Class method: factory using cls
```

## Examples

### Beginner Example

```python
class Greeter:
    greeting = "Hello"

    def greet(self, name):
        return f"{self.greeting}, {name}"

print(Greeter().greet("Ada"))
```

### Intermediate Example

```python
class InventoryItem:
    tax_rate = 0.2

    def __init__(self, name: str, net_price: float):
        self.name = name
        self.net_price = net_price

    def gross_price(self) -> float:
        return self.net_price * (1 + self.tax_rate)

print(InventoryItem("Keyboard", 50).gross_price())
```

### Advanced Example

```python
class Color:
    def __init__(self, red: int, green: int, blue: int):
        self.red, self.green, self.blue = red, green, blue

    @classmethod
    def from_hex(cls, value: str):
        value = value.removeprefix("#")
        if len(value) != 6:
            raise ValueError("expected six hexadecimal digits")
        return cls(*(int(value[index:index + 2], 16) for index in (0, 2, 4)))

    @staticmethod
    def channel_is_valid(channel: int) -> bool:
        return 0 <= channel <= 255

print(vars(Color.from_hex("#336699")))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Execute class body] --> B[Create class object]
    B --> C[Call class]
    C --> D[Bind methods to instance]
    D --> E[Run behavior]
```

---

[← Object Oriented Programming](./01-object-oriented-programming.md) · [↑ Level index](../README.md) · [Objects →](./03-objects.md)

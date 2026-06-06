# Objects

## Overview

- **What is it?** Objects are instances of classes with their own attribute values.
- **Why is it important?** Runtime entities carry state that differs per instance.
- **Where is it used?** Every OOP system—UI nodes, DB rows, device handles.

## Learning Objectives

- **Skills gained:** Practical command of Objects.
- **Concepts covered:**

- Instantiate classes.
- Access and mutate instance state.
- Compare identity vs equality.

- **Expected outcome:** You create and interact with objects confidently.

## Real World Applications

- CRM records
- IoT devices
- Game entities
- API resources

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Instantiation

- **Definition:** Call class to create object.
- **Visual explanation:** `Instantiation` → process → result
- **Practical example:**

```python
class Node:
    pass
n = Node()
print(isinstance(n, Node))
```

### self

- **Definition:** Reference to current instance.
- **Visual explanation:** `self` → process → result
- **Practical example:**

```python
class A:
    def id(self):
        return id(self)
print(A().id())
```

### identity

- **Definition:** is checks same object.
- **Visual explanation:** `identity` → process → result
- **Practical example:**

```python
a = []
b = a
print(a is b)
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Objects are class instances with unique state. |
| ⚡ Purpose | Represent individual entities at runtime. |
| 🔥 Benefits | Natural modeling, mutable state when needed. |
| 🎯 Use Cases | Shopping cart line items, connected users. |
| 🚀 Best Practices | Validate invariants in __init__; use properties. |
| ❌ Common Mistakes | Shared mutable class attrs, confusing is vs ==. |

## Syntax Guide

### Basic Syntax

```python
obj = MyClass()
obj.value = 1
```

### Standard Structure

```python
construct -> configure -> invoke methods
```

### Code Pattern

```python
user = User(name='Ada')
user.activate()
```

## Examples

### Beginner Example

```python
class Book:
    def __init__(self, title):
        self.title = title
print(Book('Python').title)
```

### Intermediate Example

```python
class Wallet:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount


w = Wallet()
w.deposit(10)
print(w.balance)
```

### Advanced Example

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


print(Singleton() is Singleton())
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Class()] --> B[Object State]
    B --> C[Methods]
```

---

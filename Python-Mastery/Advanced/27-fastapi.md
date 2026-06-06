# FastAPI

## Overview

- **What is it?** FastAPI is a modern, high-performance web framework for building APIs with Python type hints.
- **Why is it important?** It combines speed, automatic OpenAPI docs, and async support.
- **Where is it used?** Microservices, ML model serving, internal tools, SaaS backends.

## Learning Objectives

- **Skills gained:** Practical command of FastAPI.
- **Concepts covered:**

- Build REST endpoints.
- Use Pydantic models for validation.
- Deploy with Uvicorn/Gunicorn.

- **Expected outcome:** You ship production-ready async APIs quickly.

## Real World Applications

- AI inference APIs
- Fintech
- Health tech
- Startups

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### Path operations

- **Definition:** Functions mapped to HTTP routes.
- **Visual explanation:** `Path operations` → process → result
- **Practical example:**

```python
ROUTES = {'GET /health': lambda: {'status': 'ok'}}
print(ROUTES['GET /health']())
```

### Pydantic models

- **Definition:** Validation and serialization.
- **Visual explanation:** `Pydantic models` → process → result
- **Practical example:**

```python
from dataclasses import dataclass
@dataclass
class Item:
    name: str
    price: float
print(Item('a', 1.0))
```

### Dependency injection

- **Definition:** Reusable components.
- **Visual explanation:** `Dependency injection` → process → result
- **Practical example:**

```python
def get_db():
    return {'connected': True}
print(get_db()['connected'])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | FastAPI = Starlette + Pydantic + type hints. |
| ⚡ Purpose | Build typed, documented APIs with minimal boilerplate. |
| 🔥 Benefits | Auto docs, validation, async, great DX. |
| 🎯 Use Cases | CRUD APIs, webhooks, ML serving, gateways. |
| 🚀 Best Practices | Use routers; env-based config; structured logging. |
| ❌ Common Mistakes | Blocking I/O in async routes, skipping auth, no tests. |

## Syntax Guide

### Basic Syntax

```python
from dataclasses import dataclass

@dataclass
class Health:
    status: str = 'ok'


print(Health().status)
```

### Standard Structure

```python
app -> routes -> schemas -> dependencies -> startup
```

### Code Pattern

```python
def handle(route, service):
    return service(route)


print(handle('/health', lambda r: {'status': 'ok'}))
```

## Examples

### Beginner Example

```python
def health():
    return {'status': 'ok'}
print(health())
```

### Intermediate Example

```python
from dataclasses import dataclass


@dataclass
class CreateUser:
    email: str


def create_user(payload: CreateUser):
    return {'email': payload.email}


print(create_user(CreateUser(email='a@b.com')))
```

### Advanced Example

```python
from dataclasses import dataclass


@dataclass
class User:
    id: int
    email: str


def get_current_user(token: str) -> User | None:
    return User(1, 'a@b.com') if token else None


user = get_current_user('token')
print(user.email if user else 'anonymous')
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Client] --> B[FastAPI]
    B --> C[Validation]
    C --> D[Service]
```

---

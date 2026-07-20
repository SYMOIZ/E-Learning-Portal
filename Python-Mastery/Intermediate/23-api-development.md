> **Level 2: Intermediate** · Topic 23 of 35

[← Async Programming](./22-async-programming.md) · [↑ Level index](../README.md) · [API Consumption →](./24-api-consumption.md)

# API Development

## Overview
- **What is it?** API Development is the intermediate Python topic of designing and implementing HTTP endpoints that expose a stable service contract.
- **Why is it important?** API development covers server-side routing, validation, status codes, serialization, and operational behavior.
- **Where is it used?** web and mobile backends, internal microservices, automation interfaces.

## Learning Objectives
- Design resource-oriented endpoints and schemas.
- Return meaningful status codes and errors.
- Separate transport, business logic, and persistence.

## Real World Applications
- **Engineering:** Web and mobile backends rely on this topic.
- **Product work:** It supports internal microservices.
- **Operations:** It appears in automation interfaces.

## Core Concepts

### HTTP contract
- **Definition:** An endpoint contract defines method, path, parameters, body schema, status codes, and response representation.
- **Visual explanation:** ``request method + path + body -> status + headers + body``
- **Practical example:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```

### Validation and errors
- **Definition:** Request models reject malformed data at the boundary; domain failures should map consistently to documented HTTP responses.
- **Visual explanation:** ``untrusted request -> schema -> domain -> HTTP result``
- **Practical example:**

```python
from pydantic import BaseModel

class TaskInput(BaseModel):
    title: str
    priority: int = 1
```

### Layered handlers
- **Definition:** A route handler translates HTTP data and delegates business decisions to a service rather than embedding persistence logic.
- **Visual explanation:** ``HTTP adapter -> application service -> repository``
- **Practical example:**

```python
def create_task(payload, service):
    task = service.create(payload.title)
    return {"id": task.id}
```

## Infographic Summary

| Infographic Block | Topic-specific guidance |
| --- | --- |
| 📌 Concept | HTTP contract, Validation and errors, Layered handlers |
| ⚡ Purpose | API development covers server-side routing, validation, status codes, serialization, and operational behavior. |
| 🔥 Benefits | Stable service contracts, validated boundaries, and maintainable separation of HTTP and domain logic. |
| 🎯 Use Cases | web and mobile backends, internal microservices, automation interfaces |
| 🚀 Best Practices | Publish an explicit schema and make handlers thin, deterministic adapters. |
| ❌ Common Mistakes | Returning 200 for every outcome or exposing internal exceptions to clients. |

## Syntax Guide

### Basic Syntax

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"id": item_id}
```

### Standard Structure

```python
from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI()

class ItemCreate(BaseModel):
    name: str = Field(min_length=1)

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(command: ItemCreate):
    return {"id": 1, "name": command.name}
```

### Code Pattern

```python
# Route matches method and resource path.
# Schema validates external input.
# Service executes business behavior.
# Handler maps outcome to status and representation.
```

## Examples

### Beginner Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```

### Intermediate Example

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()
ITEMS = {1: {"id": 1, "name": "Keyboard"}}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = ITEMS.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item
```

### Advanced Example

```python
from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)

class TaskService:
    def __init__(self):
        self.tasks = {}

    def create(self, title: str):
        task = {"id": len(self.tasks) + 1, "title": title.strip()}
        self.tasks[task["id"]] = task
        return task

service = TaskService()

def get_service():
    return service

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(command: TaskCreate, tasks: TaskService = Depends(get_service)):
    if not command.title.strip():
        raise HTTPException(422, "blank title")
    return tasks.create(command.title)
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Route HTTP request] --> B[Validate request schema]
    B --> C[Call application service]
    C --> D[Map domain outcome]
    D --> E[Serialize HTTP response]
```

---

[← Async Programming](./22-async-programming.md) · [↑ Level index](../README.md) · [API Consumption →](./24-api-consumption.md)

> **Level 2: Intermediate** · Topic 19 of 35

[← Logging](./18-logging.md) · [↑ Level index](../README.md) · [Multithreading →](./20-multithreading.md)

# Configuration Management

## Overview
- **What is it?** Configuration management loads, validates, and layers settings outside application logic.
- **Why is it important?** Hard-coded settings block promotion across environments and create security risks.
- **Where is it used?** 12-factor apps, containers, CI pipelines, feature flags, and multi-tenant services.

## Learning Objectives
- Layer defaults, files, environment, and arguments.
- Parse strings into validated types.
- Keep secrets out of source control and logs.

## Real World Applications
- Separate local, staging, and production database credentials.
- Validate required env vars at startup before serving traffic.
- Toggle features without redeploying business logic.

## Core Concepts

### Configuration sources
- **Definition:** Settings may come from defaults, files, environment variables, or CLI flags with a documented precedence.
- **Visual explanation:** ``defaults < file < environment < CLI``
- **Practical example:**

```python
import os
port = int(os.getenv("APP_PORT", "8000"))
```

### Parsing and validation
- **Definition:** External configuration is text until converted; validation should reject missing, malformed, or unsafe values at startup.
- **Visual explanation:** ``raw strings -> convert -> validate -> Settings``
- **Practical example:**

```python
timeout = float("2.5")
if timeout <= 0:
    raise ValueError("timeout must be positive")
```

### Secrets
- **Definition:** Secret values belong in a secret manager or injected environment and must not be committed, printed, or embedded in defaults.
- **Visual explanation:** ``secret store -> process environment -> narrow consumer``
- **Practical example:**

```python
import os
token = os.environ["SERVICE_TOKEN"]
```

## Infographic Summary

| Infographic Block | Topic-specific guidance |
| --- | --- |
| 📌 Concept | Configuration management loads, validates, and layers settings outside application logic. |
| ⚡ Purpose | Configuration separates deployment-specific values from code while typed validation makes failures early and explicit. |
| 🔥 Benefits | Portable deployments, fail-fast startup validation, and secure separation of settings from code. |
| 🎯 Use Cases | environment-specific endpoints, feature switches, runtime limits |
| 🚀 Best Practices | Construct one immutable settings object at the composition root. |
| ❌ Common Mistakes | Reading environment variables throughout business logic. |

## Syntax Guide

### Basic Syntax

```python
import os

debug = os.getenv("APP_DEBUG", "false").lower() in {"1", "true", "yes"}
```

### Standard Structure

```python
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    endpoint: str
    timeout: float

settings = Settings(
    endpoint=os.environ["API_ENDPOINT"],
    timeout=float(os.getenv("API_TIMEOUT", "5")),
)
```

### Code Pattern

```python
# Load defaults and external sources.
# Apply explicit precedence.
# Parse and validate once at startup.
# Pass a typed settings object to consumers.
```

## Examples

### Beginner Example

```python
import os

host = os.getenv("APP_HOST", "127.0.0.1")
port = int(os.getenv("APP_PORT", "8000"))
print(f"http://{host}:{port}")
```

### Intermediate Example

```python
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    workers: int
    log_level: str

    @classmethod
    def from_environment(cls):
        workers = int(os.getenv("WORKERS", "2"))
        level = os.getenv("LOG_LEVEL", "INFO").upper()
        if workers < 1:
            raise ValueError("WORKERS must be positive")
        if level not in {"DEBUG", "INFO", "WARNING", "ERROR"}:
            raise ValueError("invalid LOG_LEVEL")
        return cls(workers, level)

print(Settings.from_environment())
```

### Advanced Example

```python
import argparse
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    region: str
    retries: int

def load_settings(arguments=None) -> Settings:
    parser = argparse.ArgumentParser()
    parser.add_argument("--region")
    parser.add_argument("--retries", type=int)
    options = parser.parse_args(arguments)
    region = options.region or os.getenv("APP_REGION", "eu-west")
    retries = options.retries if options.retries is not None else int(os.getenv("APP_RETRIES", "3"))
    if retries < 0:
        parser.error("retries cannot be negative")
    return Settings(region, retries)

print(load_settings(["--retries", "5"]))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Read ordered sources] --> B[Resolve precedence]
    B --> C[Convert text values]
    C --> D[Validate constraints]
    D --> E[Inject immutable settings]
```

---

[← Logging](./18-logging.md) · [↑ Level index](../README.md) · [Multithreading →](./20-multithreading.md)

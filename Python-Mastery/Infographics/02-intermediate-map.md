# Level 2 Intermediate Infographic Map

[← Infographics](./README.md) · [Intermediate lessons](../Intermediate/01-object-oriented-programming.md)

## Overview

Intermediate Python turns scripts into maintainable applications. Objects, protocols, data formats, concurrency, APIs, databases, tests, and packaging are the professional toolkit.

## Infographic Summary

| Infographic Block | Topic-Specific Takeaway |
| --- | --- |
| 📌 Concept | Professional Python organizes behavior behind objects, protocols, and tested interfaces. |
| ⚡ Purpose | Move from working scripts to applications other people can run, extend, and operate. |
| 🔥 Benefits | Clear boundaries, safer integrations, and evidence from automated tests. |
| 🎯 Use Cases | CLIs, REST clients, CRUD services, data parsers, and installable libraries. |
| 🚀 Best Practices | Prefer composition, validate at edges, log without secrets, and mock only true boundaries. |
| ❌ Common Mistakes | God classes, shared mutable state across threads, string-built SQL, and untested happy paths only. |

## Cluster Map

```mermaid
flowchart TB
    subgraph Objects[Objects]
        A1[OOP]
        A2[Classes and Objects]
        A3[Constructors]
        A4[Encapsulation]
        A5[Inheritance]
        A6[Polymorphism]
        A7[Abstraction]
        A8[Magic Methods]
        A1 --> A2 --> A3 --> A4 --> A5 --> A6 --> A7 --> A8
    end
    subgraph Protocols[Protocols]
        B1[Iterators]
        B2[Generators]
        B3[Decorators]
        B4[Context Managers]
        B1 --> B2 --> B3 --> B4
    end
    subgraph Integration[Integration]
        C1[Regex JSON CSV XML]
        C2[Logging and Config]
        C3[Threads Processes Async]
        C4[APIs and Requests]
        C5[SQL SQLite MySQL Postgres]
        C6[SQLAlchemy ORM]
        C1 --> C2 --> C3 --> C4 --> C5 --> C6
    end
    subgraph Quality[Quality]
        D1[Unit Testing]
        D2[Pytest]
        D3[Mocking]
        D4[Packaging]
        D5[CLI Applications]
        D1 --> D2 --> D3 --> D4 --> D5
    end
    Objects --> Protocols --> Integration --> Quality
```

## Study Path

| Cluster | Lessons | Outcome |
| --- | --- | --- |
| Objects | OOP through magic methods | Model a domain with validated state |
| Protocols | Iterators, generators, decorators, context managers | Compose reusable language hooks |
| Integration | Formats, logging, concurrency, APIs, databases | Connect systems safely |
| Quality | unittest, pytest, mocking, packaging, CLIs | Ship an installable, tested tool |

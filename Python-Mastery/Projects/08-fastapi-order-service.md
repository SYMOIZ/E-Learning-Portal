# FastAPI Order Service

[← Project catalog](./README.md) · [FastAPI](../Advanced/27-fastapi.md)

**Level:** Advanced  
**Lessons:** API design, validation, persistence, tests, containers

## Problem

A shop wants a small HTTP API to create an order and fetch it by id, with validation errors that clients can read.

## Non-goals

- No card handling.
- No multi-region deployment in the first slice.

## Requirements

- Validate quantity as a positive integer before business code runs.
- Persist orders so a restart can still fetch them, or document an explicit in-memory limitation.
- Return a stable error shape for validation failures.
- Add one test for the success path and one for a rejected quantity.
- Provide a container build that does not embed secrets.

## Starter

```python
def create_order(sku, quantity, store):
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("quantity must be a positive integer")
    order = {"id": len(store) + 1, "sku": sku, "quantity": quantity}
    store.append(order)
    return order


def main():
    store = []
    print(create_order("mug", 2, store))


if __name__ == "__main__":
    main()
```

## Acceptance checks

- OpenAPI documents the create and fetch operations.
- A quantity of `0` never reaches the database.
- Tests do not depend on a developer machine's fixed port being free.
- The image runs as a non-root user or the README explains why it does not yet.

## Extension

Add an idempotency key header so a retried create does not insert a second order.

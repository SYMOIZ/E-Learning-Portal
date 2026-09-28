# Inventory Service

[← Project catalog](./README.md) · [SQLite](../Intermediate/27-sqlite.md)

**Level:** Intermediate  
**Lessons:** classes, SQLite or SQLAlchemy, pytest, exceptions

## Problem

A small shop needs to create a product, adjust stock, and refuse to sell more units than are on hand.

## Non-goals

- No payment processing.
- No production database server required for the first version.

## Requirements

- Model `Product` with a name and a non-negative quantity.
- Persist rows in SQLite using parameterized SQL.
- A sale larger than available stock raises a domain error and rolls back.
- Tests use a temporary database file or `:memory:`.

## Starter

```python
class InventoryError(Exception):
    pass


class Product:
    def __init__(self, sku, name, quantity):
        if quantity < 0:
            raise InventoryError("quantity cannot be negative")
        self.sku = sku
        self.name = name
        self.quantity = quantity

    def sell(self, amount):
        if amount <= 0 or amount > self.quantity:
            raise InventoryError("insufficient stock")
        self.quantity -= amount
        return self.quantity


def main():
    product = Product("pen", "Blue pen", 5)
    print(product.sell(2))


if __name__ == "__main__":
    main()
```

## Acceptance checks

- Selling the exact remaining quantity leaves zero.
- A failed sale leaves the stored quantity unchanged.
- Queries pass values as parameters.
- The README includes the table schema.

## Extension

Record each stock change in an `audit` table inside the same transaction.

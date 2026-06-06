from dataclasses import dataclass

@dataclass
class InvoiceLine:
    description: str
    quantity: int
    unit_price: float

    @property
    def total(self):
        return self.quantity * self.unit_price

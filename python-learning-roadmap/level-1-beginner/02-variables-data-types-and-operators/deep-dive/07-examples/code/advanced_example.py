from decimal import Decimal

subtotal = Decimal("240.00")
tax_rate = Decimal("0.0825")
total = subtotal + (subtotal * tax_rate)
print(total.quantize(Decimal("0.01")))

subtotal = 240.00
discount = 0.15 if subtotal >= 200 else 0
total = subtotal * (1 - discount)
print(f"Total: ${total:.2f}")

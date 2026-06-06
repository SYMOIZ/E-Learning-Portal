orders = [
    {"id": "A100", "total": 120},
    {"id": "A101", "total": 80},
]
large_orders = [order for order in orders if order["total"] >= 100]
print(large_orders)

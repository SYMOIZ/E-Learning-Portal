users = [{"name": "Ari", "active": True}, {"name": "Bea", "active": False}]
active_names = [user["name"] for user in users if user["active"]]
print(active_names)

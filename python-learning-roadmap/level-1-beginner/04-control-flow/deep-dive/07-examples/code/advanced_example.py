events = [{"type": "login"}, {"type": "purchase"}, {"type": "logout"}]
for event in events:
    match event["type"]:
        case "login":
            print("Start session")
        case "purchase":
            print("Record revenue")
        case _:
            print("Other event")

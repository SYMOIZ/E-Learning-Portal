import sqlite3

with sqlite3.connect(":memory:") as connection:
    connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT)")
    connection.execute("INSERT INTO users (email) VALUES (?)", ("user@example.com",))
    rows = connection.execute("SELECT email FROM users WHERE id = ?", (1,)).fetchall()
    print(rows)

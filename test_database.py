import sqlite3


def test_order_data_is_saved_correctly():
    connection = sqlite3.connect(":memory:")

    try:
        connection.execute("""
            CREATE TABLE orders (
                id INTEGER PRIMARY KEY,
                amount INTEGER NOT NULL,
                status TEXT NOT NULL
            )
        """)

        connection.execute(
            "INSERT INTO orders (id, amount, status) VALUES (?, ?, ?)",
            (1, 280000, "PAID")
        )

        row = connection.execute(
            "SELECT amount, status FROM orders WHERE id = ?",
            (1,)
        ).fetchone()

        assert row == (280000, "PAID")

    finally:
        connection.close()

def test_nonexistent_order_returns_no_data():
    connection = sqlite3.connect(":memory:")

    try:
        connection.execute("""
            CREATE TABLE orders (
                id INTEGER PRIMARY KEY,
                amount INTEGER NOT NULL,
                status TEXT NOT NULL
            )
        """)

        connection.execute(
            "INSERT INTO orders (id, amount, status) VALUES (?, ?, ?)",
            (1, 280000, "PAID")
        )

        row = connection.execute(
            "SELECT amount, status FROM orders WHERE id = ?",
            (999,)
        ).fetchone()

        assert row is None

    finally:
        connection.close()
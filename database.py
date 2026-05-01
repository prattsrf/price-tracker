import sqlite3
from datetime import datetime

def create_table():
    conn = sqlite3.connect("prices.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            price REAL,
            date TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_price(url, price):
    conn = sqlite3.connect("prices.db")
    cursor = conn.cursor()

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO prices (url, price, date)
        VALUES (?, ?, ?)
    """, (url, price, date))

    conn.commit()
    conn.close()

def get_last_price(url):
    conn = sqlite3.connect("prices.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT price FROM prices
        WHERE url = ?
        ORDER BY id DESC
        LIMIT 1
    """, (url,))

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    return None

def get_price_history(url):
    import sqlite3

    conn = sqlite3.connect("prices.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT price, date FROM prices
        WHERE url = ?
        ORDER BY date ASC
    """, (url,))

    results = cursor.fetchall()

    conn.close()

    return results
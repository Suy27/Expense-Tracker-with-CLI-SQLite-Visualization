import sqlite3

def connect():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    date TEXT,
                    category TEXT,
                    amount REAL,
                    note TEXT)''')
    conn.commit()
    conn.close()
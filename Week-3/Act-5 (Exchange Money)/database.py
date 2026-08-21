import sqlite3

def create_connection():
    conn = sqlite3.connect("transactions.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            bank_id INTEGER,
            r_name TEXT NOT NULL,
            r_bid INTGER,
            s_amount FLOAT,
            r_amount FLOAT
        )
    ''')
    conn.commit()
    conn.close()
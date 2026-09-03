import sqlite3

def create_connection():
    conn = sqlite3.connect("college.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            courses TEXT
        )
    ''')
    conn.commit()
    conn.close()
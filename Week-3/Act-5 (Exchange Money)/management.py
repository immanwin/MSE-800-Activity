from database import create_connection
import sqlite3

def add_transaction(username, bank_id, r_name, r_bid, s_amount, r_amount):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (username, bank_id, r_name, r_bid, s_amount, r_amount)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (username, bank_id, r_name, r_bid, s_amount, r_amount))
    conn.commit()
    conn.close()

def view_transactions():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    conn.close()
    return rows
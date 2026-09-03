from database import create_connection
import sqlite3

def add_student(name, courses_str):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (name, courses) VALUES (?, ?)", (name, courses_str))
        conn.commit()
        print("Student added successfully.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, courses FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    if cursor.rowcount > 0:
        conn.commit()
        print("User deleted successfully.")
    else:
        print("Student ID not found.")
    conn.close()
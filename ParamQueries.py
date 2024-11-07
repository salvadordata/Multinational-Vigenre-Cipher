# Example in Python with SQLite
import sqlite3

def safe_query(db, user_input):
    cursor = db.cursor()
    # Using ? placeholders for parameterized queries
    cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))
    result = cursor.fetchall()
    cursor.close()
    return result

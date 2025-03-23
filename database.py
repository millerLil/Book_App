import sqlite3
import userStore

def get_db_connection():
    conn = sqlite3.connect('database.db', timeout=10.0)
    conn.row_factory = sqlite3.Row
    return conn
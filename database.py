import sqlite3
import userStore

def get_db_connection():
    conn = sqlite3.connect('userDB.db', timeout=10.0)
    conn.row_factory = sqlite3.Row
    return conn

def update_currentBook(userName, currentBook):
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        res = cur.execute("UPDATE users SET userCurrentBook = ? WHERE userName = ?", (currentBook, userName))
        userStore.set_currentBook(currentBook)
        message = "The current book you are reading is successfully updated"
        print(message)
    except sqlite3.Error as e:
        print(f"Database error: {e}") 

    conn.commit()
    cur.close()
    conn.close()   
    print("connection cleaned")

def get_CurrentBook_from_db(userName):
    conn = get_db_connection()
    cur = conn.cursor()
    currentBook = ''

    try:
        res = cur.execute("SELECT userCurrentBook FROM users WHERE userName = ?", (userName, ))
        result = cur.fetchone()
        weight = result[0]
        message = "Book you are reading is successfully retrieved"
        print(message)
    except sqlite3.Error as e:
        print(f"Database error: {e}")  # Prints the full error message

    conn.close()
    return currentBook
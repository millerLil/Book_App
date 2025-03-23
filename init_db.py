import sqlite3

# Connect to SQLite database (creates database.db if it doesn't exist)
conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Create the users table
cur.executescript("""
    DROP TABLE IF EXISTS users;

    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        email TEXT NOT NULL,
        userName TEXT NOT NULL UNIQUE,
        userPW TEXT NOT NULL,
        currentBook TEXT,
        userBio TEXT,
        userPhoto BLOB,
        userActive BOOLEAN DEFAULT 1
    );
""")

# Commit and close
conn.commit()
conn.close()

print("Database initialized successfully!")
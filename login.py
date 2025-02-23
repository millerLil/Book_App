from flask import Flask, Blueprint, request, redirect, url_for, render_template
import sqlite3
import database

login_bp = Blueprint("login", __name__)

def check_user(name, pw):
    # Get database connection
    conn = database.get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()
    cur.execute('SELECT userName, userPW FROM users WHERE userName = ?', (name,))    
    # First row returned (should be only)
    row = cur.fetchone()
    # Close connection
    conn.close()
    # Nothing returned - user not found
    if row is None: 
        # user not found
        print("User name not found")
    # Username found but password doesn't match
    elif row[1] != pw:
        print("Invalid password")
    else:
        print("Successful login")
        return True
       
    return False

@login_bp.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        import userStore
        if check_user(username, password):
            userStore.set_user(username)
            currentBook = database.get_currentBook_from_db(username)
            userStore.set_currentBook(currentBook)
        else:
            userStore.set_user("")
            message = "Incorrect Username or Password."

    html = f"""

    """
    return html
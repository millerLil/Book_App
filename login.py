from flask import Blueprint, request, redirect, url_for
import database
import userStore

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
      
        if check_user(username, password):
            userStore.set_user(username)
            return redirect(url_for("home.home"))

        else:
            userStore.set_user("")
            message = "Incorrect Username or Password."

    html = f"""
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Screen</title>
    </head>
    <body style="margin: 0; padding: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; font-family: Arial, sans-serif; background: #001f03;">

            
            <div style="text-align: center; width: 1550px; height: 750px; background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
                <!-- Title -->
                <h1 style="font-size: 64px; color: white; text-shadow: 2px 2px 5px #000; margin-bottom: 20px;">BookApp</h1>

                <!-- Form -->
                <form method="POST">
                    <div>
                        <label for="username" style="display: block; margin-bottom: 5px; font-weight: bold;">Username/Email:</label>
                        <input type="text" id="username" name="username" required style="width: 100%; padding: 10px; margin-top: 5px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;">
                    </div>
                    <div style="margin-top: 10px;">
                        <label for="password" style="display: block; margin-bottom: 5px; font-weight: bold;">Password:</label>
                        <input type="password" id="password" name="password" required style="width: 100%; padding: 10px; margin-top: 5px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;">
                    </div>
                    <div>
                        <button type="submit" style="padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; margin-top: 15px;">Login</button>
                    </div>
                </form>

                <!-- Link -->
                <div style="margin-top: 15px;">
                    <a href="./register" style="color: #007bff; text-decoration: none;">Create an account</a>
                </div>
                <div style="margin-top: 15px;">
                    <a href="./reset_login" style="color: #007bff; text-decoration: none;">Reset Password</a>
                </div>
                <p>{message}</p>
            </div>
    </body>
    </html>
    """
    return html
from flask import Flask, Blueprint, render_template_string, request, redirect, url_for
from jinja2 import Template
import sqlite3
import database
import userStore

profile_bp = Blueprint("profile_screen", __name__)

# profile structure
profile_data = {
    "firstName": "Enter first name here",
    "lastName": "Enter last name here",
    "email": "Enter email here",
    "userName": "Enter user name here",
    "userBio": "Enter biography here"
}

def get_data():
    userName = userStore.get_user()

    # Get database connection
    conn = database.get_db_connection()
    # Create cursor
    cur = conn.cursor()

    try:
        cur.execute("SELECT firstName, lastName, email, userBio, userPhoto FROM users WHERE userName = ?", (userName,))
        message = "Successful retrieval"
        data = cur.fetchone()
        if data == None:
            message = "No data retrieved"
            print(message)
        else:
            global profile_data
            profile_data.update({"firstName": data[0]})
            profile_data.update({"lastName": data[1]})
            profile_data.update({"userName": userName})
            profile_data.update({"email": data[2]})
            profile_data.update({"userBio": data[3]})
    except sqlite3.IntegrityError:
        message = "User Name does not exist."
        print(message)
        cur.close()
        conn.close()
        return message    

@profile_bp.route('/')
def profile():
    get_data()

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Book App - Profile</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #001f03;
            }
            nav ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                background-color: #333;
                overflow: hidden;
            }
            nav li {
                float: left;
            }
            nav li h2 {
                color: #32CD32;
                padding: 14px 16px;
                margin: 0;
            }
            nav li a {
                color: white;
                padding: 14px 16px;
                display: block;
                text-decoration: none;
            }
            nav li a:hover {
                background-color: lightblue;
                color: black;
            }
            .active {
                display: flex;
                justify-content: center;     
                align-items: center;         
                width: 70px;
                height: 70px;
                border-radius: 50%;
                background-color: #7efbb3;
                color: black;
                text-decoration: none;
                font-size: 12px;
                margin: 8px;
                text-align: center;
                line-height: normal;         
                padding: 0;
            }

            .profile-page {
                width: 100vw;
                height: 100vh;
                background:  #001f03;
                padding: 40px;
                box-sizing: border-box;
            }

            .top-section {
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 40px;
                margin-top: 40px;
            }

            .name-box {
                color: white;
                background-color: #003f1f;
                padding: 10px 15px;
                border: 2px solid #ccc;
                border-radius: 10px;
                font-size: 16px;
                text-align: center;
                min-width: 120px;
            }

            .book-icon-large {
                width: 160px;
                height: 200px;
                background-color: #ccc;
                border: 3px solid black;
            }

            .bio-box {
                color: white;
                max-width: 250px;
                text-align: center;
                font-size: 16px;
                padding: 10px;
                margin-top: 120px;
            }

            .profile-pic {
                width: 140px;
                height: 140px;
                background-color: #aaa;
                border-radius: 50%;
                border: 3px solid black;
            }


            .user-details {
                text-align: left;
                margin-top: 20px;
            }

            .user-details p {
                margin: 6px 0;
            }

            .middle-section {
                display: flex;
                justify-content: center;
                align-items: flex-start;
                gap: 40px;
                margin-top: 40px;
            }

            .book-grid {
                display: grid;
                grid-template-columns: repeat(3, 100px);  /* 2 columns */
                gap: 15px;
                row-gap: 55px:
                margin: 15px auto 0;
                width: 60%;  /* only take up half the page width */
                justify-content: center;
            }

           .book-icon {
            width: 90px;
            height: 130px;
            background-color: #ddd;
            border: 2px solid #999;
            border-radius: 5px;
        }

            .goals-box {
                color: white;
                background-color: #003f1f;
                padding: 10px 15px;
                border: 2px solid #ccc;
                border-radius: 10px;
                font-size: 16px;
                text-align: center;
                min-width: 120px;              
                margin: 15px auto 0;
                width: 30%;  
                justify-content: center;
            }
            
                
            .feed {
                margin-top: 20px;
                text-align: center;
                background: #eee;
                padding: 10px 20px;
                border-radius: 5px;
            }

            .active:hover {
                transform: scale(1.05);
            }

        </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><h2>Biblio</h2></li>
                <li><a class = "active" href="/home">Home</a></li>
                <li><a class = "active" href="/discover">Discover Books</a></li>
                <li><a class = "active" href="/community">Community</a></li>
                <li style="float:right"><a class="active" href="/logout">Logout</a></li>
                <li style="float:right"><a class="active" href="/edit">Edit Profile</a></li>
            </ul>
        </nav>

        <div class="top-section">
            <div class="name-box">
                <p><strong>{{ profile.firstName }} {{ profile.lastName }}</strong></p>
            </div>
            <div class="book-icon-large"></div>
            <div class="bio-box">
                <p><strong>Biography:</strong><br>{{ profile.userBio }}</p>
            </div>
            <div class="profile-pic"></div>
        </div>

            <div class="user-details">

            </div>

            <div class="middle-section">
                <div class="book-grid">
                    <div class="book-icon"></div>
                    <div class="book-icon"></div>
                    <div class="book-icon"></div>
                    <div class="book-icon"></div>
                    <div class="book-icon"></div>
                    <div class="book-icon"></div>
                </div>

                <div class="goals-box">
                    <p><strong>Goals</strong></p>
                    <p>✔️ Read 5 books this month</p>
                    <p>✔️ Finish "1984"</p>
                </div>
            </div>

            <div class="feed">
                <p><strong>Your Posts</strong></p>
                <p>✔️ Finished "The Hobbit"</p>
                <p>📌 Saved "Dune"</p>
            </div>


        </div>
    </body>
    </html>
    """

    return render_template_string(html, profile=profile_data)
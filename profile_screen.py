from flask import Flask, Blueprint, render_template_string, request, redirect, url_for
import sqlite3
import database
import userStore

profile_bp = Blueprint("profile_screen", __name__)

@profile_bp.route("/")
def profile():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Profile</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin: 0; padding: 0; background: #f4f4f4; }
            .container { width: 90%; max-width: 400px; margin: 20px auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            .profile-header { display: flex; align-items: center; justify-content: space-between; }
            .profile-pic { width: 60px; height: 60px; border-radius: 50%; background: #ccc; }
            .bio { text-align: left; margin-top: 10px; }
            .featured-book { width: 100px; height: 120px; background: #ddd; display: inline-block; margin: 20px; }
            .book-grid { display: flex; justify-content: center; gap: 10px; }
            .book-icon { width: 40px; height: 50px; background: #ddd; }
            .feed { margin-top: 20px; padding: 10px; background: #eee; border-radius: 10px; }
        </style>
    </head>
    <body>

        <div class="container">
            <div class="profile-header">
                <div class="profile-pic"></div>
                <div>
                    <h3>User Name</h3>
                    <p class="bio">This is the user bio. A short description goes here.</p>
                </div>
            </div>

            <div class="featured-book"></div>

            <div class="book-grid">
                <div class="book-icon"></div>
                <div class="book-icon"></div>
                <div class="book-icon"></div>
                <div class="book-icon"></div>
            </div>

            <div class="feed">
                <p><strong>User Activity</strong></p>
                <p>Finished reading "Book Title" 📖</p>
                <p>Added "Another Book" to wishlist ⭐</p>
            </div>
        </div>

    </body>
    </html>
    """
    return html
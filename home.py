from flask import Blueprint, redirect, url_for
from flask import Flask, request, jsonify
import sqlite3
import requests

home_bp = Blueprint("home", __name__)


# Open Library API Call
@home_bp.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "No search query provided"}), 400

    url = f"https://openlibrary.org/search.json?title={query}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({"error": "API request failed"}), 500

    data = response.json()
    if not data["docs"]:
        return jsonify({"error": "No books found"}), 404

    book = data["docs"][0]  # Get the first book result
    book_info = {
        "title": book.get("title", "Unknown Title"),
        "author": ", ".join(book.get("author_name", ["Unknown Author"])),
        "cover": f"https://covers.openlibrary.org/b/id/{book['cover_i']}-M.jpg" if "cover_i" in book else None
    }
    return jsonify(book_info)

# Get community posts (dummy for now)
@home_bp.route('/community-posts', methods=['GET'])
def community_posts():
    posts = [
        {"user": "Alice", "content": "I just finished an amazing book!"},
        {"user": "Bob", "content": "Any sci-fi recommendations?"},
    ]
    return jsonify(posts)


@home_bp.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        # Redirect to the workout page if the Workout button is clicked
        if request.form.get("action") == "Account":
            return redirect(url_for("account.account")) 
        if request.form.get("action") == "Profile":
            return redirect(url_for("profile.profile")) 
        


    # HTML for the home page
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Book Search</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; }
            .search-bar { padding: 10px; width: 80%; margin: 20px auto; }
            .book-info { margin-top: 20px; }
            .book-cover { max-width: 150px; margin-top: 10px; }

                        body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }

            nav ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #333;
            }

            nav li {
                float: left;
            }

            nav li h2 {
                display: block;
                color: lightblue;
                text-align: center;
                padding: 14px 16px;
                margin: 0;
            }

            nav li a {
                display: block;
                color: white;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }

            nav li a:hover {
                background-color: lightblue;
                color: black;
            }

            .active {
                background-color: lightskyblue;
                color: black;
            }


        </style>
    </head>
    <body>

         <nav>
         <ul>
            <li><h2>BookApp</h2></li>
            <li><a href="/Books">Books</a></li>
            <li><a href="/Community">Community</a></li>
            <li><a href="/Read">Read</a></li>
            <li style="float:right"><a class="active" href="/logout">Logout</a></li>
            <li style="float:right"><a class="active" href="/profile">Profile</a></li>
            </ul>
        </nav>

        <h2>Search for a Book</h2>
        <input type="text" id="search" class="search-bar" placeholder="Enter book title...">
        <button onclick="searchBook()">Search</button>

        <div class="book-info" id="book-info"></div>

        <script>
            function searchBook() {
                let query = document.getElementById("search").value;
                fetch(`/search?q=${query}`)
                    .then(response => response.json())
                    .then(data => {
                        let info = document.getElementById("book-info");
                        info.innerHTML = "";

                        if (data.error) {
                            info.innerHTML = "<p>No results found.</p>";
                            return;
                        }

                        let title = `<h3>${data.title}</h3>`;
                        let author = `<p>Author: ${data.author}</p>`;
                        let cover = data.cover ? `<img src="${data.cover}" class="book-cover">` : "<p>No cover available</p>";

                        info.innerHTML = title + author + cover;
                    });
            }
        </script>

    </body>
    </html>
    """
    return html

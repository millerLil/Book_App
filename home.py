from flask import Blueprint, redirect, url_for, request

home_bp = Blueprint("home", __name__)

@home_bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form.get("action") == "Profile":
            return redirect(url_for("profile.profile")) 
        if request.form.get("action") == "Discover Books":
            return redirect(url_for("discover.discover"))

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Book Search</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                text-align: center; 
                background-color: #001f03; 
                color: white;
                margin: 0; 
                padding: 0; 
            }
            .search-bar { 
                padding: 10px; 
                width: 80%; 
                margin: 
                20px auto; 
            }

            .message { 
                margin-top: 
                20px; c
                color: red; 
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
                color: #32CD32;
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

            .active:hover {
                transform: scale(1.05);
            }


            .book-section {
                display: flex;
                justify-content: space-around;
                margin: 30px auto;
                width: 80%;
            }

            .book-box {
                background-color: #3a5f3a;
                color: white;
                width: 40%;
                padding: 20px;
                border-radius: 12px;
                text-align: center;
                box-shadow: 0 4px 8px rgba(0,0,0,0.3);
                transition: transform 0.3s;
            }

            .book-box img {
                width: 100px;
                height: 150px;
                object-fit: cover;
                margin-bottom: 10px;
            }

            .recent-posts {
                width: 80%;
                margin: 40px auto;
                background-color: #2e4e2e;
                padding: 20px;
                border-radius: 12px;
                color: white;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            }

            <!--AI coded the the script/HTML?CSS for the like button-->
            .like-btn {
                background-color: #3a5f3a;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 8px;
                cursor: pointer;
                margin-top: 10px;
                font-size: 14px;
                transition: transform 0.2s ease;
            }

            .like-btn:hover {
                transform: scale(1.05);
                background-color: #7efbb3;
                color: black;
            }

        </style>
    </head>
    <body>

        <nav>
         <ul>
            <li><h2>Biblio</h2></li>
            <li><a class = "active" href="/discover">Discover Books</a></li>
            <li><a class = "active" href="/community">Community</a></li>
            <li style="float:right"><a class="active" href="/logout">Logout</a></li>
            <li style="float:right"><a class="active" href="/profile">Profile</a></li>
            </ul>
        </nav>

        <h2>Search for a Book</h2>
        <input type="text" id="search" class="search-bar" placeholder="Enter book title...">
        <button onclick="handleSearch()">Search</button>

        <div class="message" id="message"></div>


        <script>
            function handleSearch() {
                let query = document.getElementById("search").value.trim().toLowerCase();
                let messageBox = document.getElementById("message");

                if (query === "mutual interest") {
                    window.location.href = "/book1";
                } else {
                    messageBox.innerText = "Book not found. Try 'Mutual Interest'.";
                }
            }

                function incrementLike(button) {
                    let span = button.querySelector('span');
                    let count = parseInt(span.innerText);
                    span.innerText = count + 1;
                }


        </script>


        <div class="book-section">
            <div class="book-box">
                <h3>Featured Book of the Week</h3>
                <img src="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1706948037i/204316857.jpg" alt="Featured Book" />
                <p><strong>The Empusium</strong> by Olga Tokarczuk</p>
            </div>
            <div class="book-box">
                <h3>Most Popular Book</h3>
                <img src="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1706714441i/195391606.jpg" alt="Popular Book" />
                <p><strong>Trippy</strong> by Ernesto Londono</p>
            </div>
        </div>


        <div class="recent-posts">
            <h2>Recently Posted</h2>
            <div class="post">
                <h4>@jan5678</h4>
                <p>Just finished The Silent Patient and I could not put it down!</p>
                <button class="like-btn" onclick="incrementLike(this)">❤️ Like (<span>0</span>)</button>

            </div>
            <div class="post">
                <h4>@reader_love</h4>
                <p>Anyone else reading Dune this week????</p>
                <button class="like-btn" onclick="incrementLike(this)">❤️ Like (<span>0</span>)</button>

            </div>
            <div class="post">
                <h4>@jjki34334</h4>
                <p>Pachinko is my new fav! Highly recommend!</p>
                <button class="like-btn" onclick="incrementLike(this)">❤️ Like (<span>0</span>)</button>
            </div>
        </div>

    </body>
    </html>
    """
    return html



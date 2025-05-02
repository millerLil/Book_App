from flask import Blueprint, render_template_string

community_bp = Blueprint("community", __name__)

@community_bp.route("/", methods=["GET"])
def community():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Community Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #001f03;
                color: white;
                margin: 0;
                padding: 0;
            }

            .container {
                display: flex;
                padding: 20px;
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

            .post-feed {
                flex: 3;
                margin-right: 20px;
            }

            .post {
                background-color: #3a5f3a;
                border-radius: 10px;
                padding: 15px;
                margin-bottom: 20px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            }

            .sidebar {
                flex: 1;
                display: flex;
                flex-direction: column;
                gap: 20px;
            }

            .search-bar {
                padding: 10px;
                font-size: 16px;
                border-radius: 10px;
                border: none;
                width: 100%;
            }

            .bubble {
                background-color: #7efbb3;
                color: black;
                padding: 20px;
                border-radius: 20px;
                text-align: center;
                font-weight: bold;
                cursor: pointer;
                box-shadow: 0 4px 6px rgba(0,0,0,0.3);
                transition: transform 0.2s;
            }

            .bubble:hover {
                transform: scale(1.05);
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
            <li style="float:right"><a class="active" href="/logout">Logout</a></li>
            <li style="float:right"><a class="active" href="/profile">Profile</a></li>
            </ul>
        </nav>

        <div class="container">
            <!-- Left Column: Posts -->
            <div class="post-feed">
                <div class="post">📚 <strong>AliceK</strong> reviewed <em>"The Midnight Library "</em> Loved it!</div>
                <div class="post">💬 <strong>Bob</strong> started a discussion: "Who else cried reading The Book Thief?"</div>
                <div class="post">🌟 <strong>Clara</strong> rated <em>"Educated "</em>: 5 stars</div>
                <div class="post">💬 <strong>John123</strong> started a discussion: "What book are you reading?"</div>
                <div class="post">🌟 <strong>kay55</strong> rated <em>"Hyperspace"</em> 2.5 stars</div>
                <div class="post">🌟 <strong>SallyB89344</strong> rated <em>"Rejection"</em> 3.89 stars</div>
                <div class="post">📚 <strong>hope_bart</strong> reviewed <em>"Why Nations Failed "</em> Very interesting</div>


            </div>

            <!-- Right Column: Search + Bubbles -->
            <div class="sidebar">
                <input type="text" class="search-bar" placeholder="Search users or authors...">
                <div class="bubble">Join a Book Club</div>
                <div class="bubble">Discussions</div>
                <div class="bubble">Community Challenges</div>
                
            </div>
        </div>
    </body>
    </html>
    """
    return html
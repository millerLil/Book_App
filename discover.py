from flask import Blueprint, render_template_string

discover_bp = Blueprint("discover", __name__)

@discover_bp.route("/", methods=["GET"])
def discover():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Discover Books</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #001f03;
                margin: 0;
                padding: 0;
                text-align: center;
                color: white;

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

            .search-bar {
                padding: 10px;
                width: 80%;
                margin: 20px auto;
                font-size: 16px;
            }

            .box-container {
                display: flex;
                justify-content: space-around;
                padding: 20px;
                margin-top: 20px;
            }

            .box {
                background-color: #3a5f3a;
                color: white;
                width: 30%;
                height: 150px;
                border-radius: 10px;
                display: flex;
                justify-content: center;
                align-items: center;
                font-size: 20px;
                border: 2px solid #ccc;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
            }

            svg {
                width: 80%;
                height: auto;
                margin: 5px auto;
            }

            .continent {
                fill: #c0c0c0;
                stroke: #333;
                stroke-width: 1;
                transition: fill 0.3s ease;
                cursor: pointer;
            }

            .continent:hover {
                fill: lightgreen;
            }

            .box:hover {
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>

        <nav>
            <ul>
                <li><h2>Biblio</h2></li>
                <li><a class="active" href="/home">Home</a></li>
                <li><a class="active" href="/community">Community</a></li>
                <li style="float:right"><a class="active" href="/logout">Logout</a></li>
                <li style="float:right"><a class="active" href="/profile">Profile</a></li>

            </ul>
        </nav>

        <h2>Discover New Books</h2>
        <input type="text" id="search" class="search-bar" placeholder="Enter book title...">
        <button onclick="handleSearch()">Search</button>

        <div id="message" class="message"></div>


        <div class="box-container">
            <div class="box" id="recommended-box">Recommended</div>
            <div class="box">Genres</div>
            <div class="box">Top Picks</div>
        </div>

        
        <!--AI coded the world map-->
        <!-- SVG World Map -->
        <p>Click on a continent to discover books from that region:</p>
        <svg viewBox="0 0 1000 500" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="World Map">
            <title>Interactive World Map</title>
            <path id="Africa: Things Fall Apart by Chinua Achebe" class="continent" d="M500,250 L520,260 L530,300 L510,320 L490,310 Z" />
            <path id="Asia: The Kite Runner by Khaled Hosseini" class="continent" d="M600,200 L650,220 L670,250 L640,270 L610,260 Z" />
            <path id="Europe: The Book Thief by Mark Zusak" class="continent" d="M540,180 L560,190 L570,200 L550,210 L530,200 Z" />
            <path id="North-America: To Kill a Mockingbird by Harper Lee" class="continent" d="M300,150 L340,160 L360,190 L330,210 L310,200 Z" />
            <path id="South-America: One Hundred Years of Solitude by Gabriel Garcia" class="continent" d="M360,260 L380,280 L390,320 L370,340 L350,330 Z" />
            <path id="Australia: The Secret River by Kate Grenville" class="continent" d="M720,340 L740,350 L750,370 L730,380 L710,370 Z" />
        </svg>

        <script>
            document.querySelectorAll('.continent').forEach(function (elem) {
                elem.addEventListener('click', function () {
                    alert("You clicked on: " + this.id);
                });
            });


                   
            function handleSearch() {
                let query = document.getElementById("search").value.trim().toLowerCase();
                let messageBox = document.getElementById("message");

                if (query === "the godfather") {
                    window.location.href = "/book2";
                } else {
                    messageBox.innerText = "Book not found. Try 'The Godfather'.";
                }
            }

            document.getElementById("recommended-box").addEventListener("click", function () {alert("The Godfather");});

        </script>

    </body>
    </html>
    """
    return render_template_string(html)


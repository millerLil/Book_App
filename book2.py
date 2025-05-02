from flask import Flask, Blueprint, render_template_string


book2_bp = Blueprint("book2", __name__)



@book2_bp.route('/', methods=['GET'])
def book2():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Book Detail</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #001f03;
                color: white;
                margin: 0;
                padding: 0;
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
                color: lightblue;
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

            .header {
                padding: 40px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .header h1 {
                margin: 0;
                font-size: 40px;
                color: white;
            }

            .main-content {
                display: flex;
                fles
                padding: 40px;
                gap: 40px;
            }

            .book-cover {
                width: 160px;
                height: 220px;
                background-color: #ddd;
                border: 2px solid black;
                margin-left: 20px
            }

            .book-info {
                flex: 1;
            }

            .rating {
                font-size: 24px;
                margin: 10px 0;
                color: gold;
                margin-left: 10px
            }

            .small-box {
                width: 150px;
                height: 60px;
                background-color: #3a5f3a;
                border-radius: 10px;
                margin-bottom: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                margin-left: 35px

            }

            .button-row {
                display: flex;
                gap: 20px;
                margin-top: 20px;
            }

            .button {
                flex: 1;
                background-color: #3a5f3a;
                padding: 15px;
                border: 1px solid #777;
                border-radius: 10px;
                text-align: center;
                margin-bottom: 20px;
                margin-left: 20px
            }

            .description-box {
                margin: 40px auto;
                width: 40%;
                height: 300px;
                background-color: #3a5f3a;
                padding: 20px;
                border-radius: 10px;
            }

            .community-box {
                margin: 40px auto;
                width: 40%;
                height: 400px;
                background-color: #3a5f3a;
                padding: 20px;
                border-radius: 10px;
                text-align: center;  
            }

            .book-sections {
                width: 100%;
                display: flex;
                flex-direction: column;
                align-items: center;
            }

        </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><h2>Book App</h2></li>
                <li><a class = "active" href="/home">Home</a></li>
                <li><a class = "active" href="/discover">Discover Books</a></li>
                <li><a class = "active" href="/community">Community</a></li>
                <li style="float:right"><a class="active" href="/profile">Profile</a></li>
            </ul>
        </nav>

        <div class="header">
            <h1>The Godfather</h1>
            <h2> Mario Puzo</h2>
        </div>

        <div class="main-content">
            <div class="book-cover"> <img src="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1394988109i/22034.jpg" >
                <div class="rating">★ ★ ★ ★ ★</div>
                <div class="button-row">
                    <div class="button">Add to Shelf</div>
                    <div class="button">Mark as Read</div>
                </div>

                <div class="small-box">Buy</div>
                

            </div>

        </div>

        <div class="book-section">
            <div class="description-box">
                <p>The Godfather—the epic tale of crime and betrayal that became a global phenomenon. <br><br>
                    Almost fifty years ago, a classic was born. A searing portrayal of the Mafia underworld, The Godfather introduced readers to the first family of American crime fiction, the Corleones, and their powerful legacy of tradition, blood, and honor. The seduction of power, the pitfalls of greed, and the allegiance to family—these are the themes that have resonated with millions of readers around the world and made The Godfather the definitive novel of the violent subculture that, steeped in intrigue and controversy, remains indelibly etched in our collective consciousness.
                </p>
            </div>

            <div class="community-box">
                <p>Reviews</p>
                <p>“A dazzling, ambitious novel about the cost of ambition and the price of love.”</p>  
                <p>—Kirkus Reviews</p>
                <p>“A masterful exploration of the complexities of love, ambition, and the sacrifices we make for success.”</p> 
                <p>—BookPage</p>
                <p>“A gripping tale of love, ambition, and the sacrifices we make for success.”</p> 
                <p>—Book Riot</p>
                <p>“A mesmerizing novel about marriage and ambition, sexuality and secrecy, and the true costs of building an empire.”</p>
                <p>—Bookish</p>
                <p>“A classic in the making.”</p>   
                <p>—The New York Times Book Review</p>

            </div>
        </div>

    </body>
    </html>
    """
    return render_template_string(html)
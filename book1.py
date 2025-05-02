from flask import Flask, Blueprint, render_template_string


book1_bp = Blueprint("book1", __name__)



@book1_bp.route('/', methods=['GET'])
def book1():
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
                width: 80%;
                height: 400px;
                background-color: #3a5f3a;
                padding: 20px;
                border-radius: 10px;
            }

            .community-box {
                margin: 40px auto;
                width: 80%;
                height: 400px;
                background-color: #3a5f3a;
                padding: 20px;
                border-radius: 10px;
                text-align: center;  
            }

            a {
                text-decoration: none;
                color: inherit;  
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
                <li><a class = "active" href="/Books">Books</a></li>
                <li><a class = "active" href="/community">Community</a></li>
                <li style="float:right"><a class = "active" href="/profile">Profile</a></li>
            </ul>
        </nav>

        <div class="header">
            <h1>Mutual Interest</h1>
            <h2> Olivia Wolfgang-Smith</h2>
        </div>

        <div class="main-content">
            <div class="book-cover"> <img src="data:image/jpeg;base64,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"</div>
            <div class="book-info">
                <div class="rating">★ ★ ★ ★ ☆</div>
                <div class="button-row">
                    <div class="button">Add to Shelf</div>
                    <div class="button">Mark as Read</div>
                </div>

                <a href="https://www.thriftbooks.com/w/mutual-interest_olivia-wolfgang-smith/52710683/?srsltid=AfmBOooefeKrdBqn35qblJEmhoqMSCVjiP8V2Ij5oQ5AhfzQThA0RiE0#edition=71256582&idiq=64091585" target="_blank">
                <div class="small-box">Buy</div>
                </a>

            </div>

        </div>

        <div class="book-section">
            <div class="description-box">
                <p>A classic in the making: a mesmerizing novel about marriage and ambition, sexuality and secrecy, and the true costs of building an empire.<br><br>
                    At the turn of the 20th century, Vivian Lesperance is determined to flee her origins in Utica, New York, and avoid repeating her parents' dull, limited life. When she meets Oscar Schmidt, a middle manager at a soap company, Vivian finds a partner she can guide to build the life she wants-not least because, more interested in men himself, Oscar will leave Vivian to tend to her own romances with women. <br><br>
                    But Vivian's plans require capital, so the two pair up with Squire Clancey, scion of an old American fortune. Together they found Clancey & Schmidt, a preeminent manufacturer of soap, perfume, and candles. When Oscar and Squire fall in love, the trio form a new kind of partnership. <br><br>
                    Vivian reaches the pinnacle of her power building Clancey & Schmidt into an empire of personal care products while operating behind the image of both men. But exposure threatens, and all three partners are made aware of how much they have to lose. <br><br>
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

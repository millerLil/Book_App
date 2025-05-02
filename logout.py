from flask import Blueprint

logout_bp = Blueprint("logout", __name__)

@logout_bp.route("/")
def logout():
    message = ""

    import userStore
    userStore.set_user("")
    message = "userStore cleared."



    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Log out screen</title>
        <style>
            body { 
                font-family: Arial, sans-serif;
                background-color: #001f03;
                color: white;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh; 
                text-align: center;
                <!-- AI helped center this text -->
            }

            .button {
                display: inline-block; 
                padding: 10px 20px; 
                background-color: #4CAF50;
                color: white; 
                text-decoration: none; 
                border-radius: 5px; 
                font-family: Arial, sans-serif; 
                font-size: 16px;"

            }

        </style>
    </head>
    <body>

            <h1>Thank you for using Biblio! </h1>
            <h1>- Read more. Share more. </h1>

            <a class = "button" href="/login">Login</a>

    </body>
    </html
    """
    return html









#Run this file to start the application
# This file is the main entry point for the Flask application.

from flask import Flask, redirect
from login import login_bp
from register import register_bp
from home import home_bp
from profile_screen import profile_bp
from reset_login import reset_login_bp
from logout import logout_bp
from book1 import book1_bp
from book2 import book2_bp  
from discover import discover_bp     
from community import community_bp 


app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/login')  


# Registering blueprints
app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(register_bp, url_prefix="/register")
app.register_blueprint(home_bp, url_prefix="/home")
app.register_blueprint(profile_bp, url_prefix="/profile")
app.register_blueprint(reset_login_bp, url_prefix="/reset_login")
app.register_blueprint(logout_bp, url_prefix="/logout")
app.register_blueprint(book1_bp, url_prefix="/book1")
app.register_blueprint(book2_bp, url_prefix="/book2")
app.register_blueprint(discover_bp, url_prefix="/discover")
app.register_blueprint(community_bp, url_prefix="/community")

if __name__ == "__main__":
    app.run(debug=True)
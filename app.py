from flask import Flask
# Importing blueprints from other files
from login import login_bp
from register import register_bp
from home import home_bp
from profile_screen import profile_bp
from reset_login import reset_login_bp


app = Flask(__name__)


# Registering blueprints
app.register_blueprint(login_bp)
app.register_blueprint(register_bp, url_prefix="/register")
app.register_blueprint(home_bp, url_prefix="/home")
app.register_blueprint(profile_bp, url_prefix="/profile")
app.register_blueprint(reset_login_bp, url_prefix="/reset_login")



if __name__ == "__main__":
    app.run(debug=True)
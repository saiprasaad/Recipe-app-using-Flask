from flask import Flask
from routes import configure_app_routes

app = Flask(__name__)

configure_app_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
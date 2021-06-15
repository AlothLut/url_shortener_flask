from project import app
import os

@app.route("/")
def index():
    app_name = os.getenv("FLASK_ENV")

    if app_name:
        return "Hello from " + app_name  +" running in a Docker container behind Nginx!"

    return "Hello from Flask"

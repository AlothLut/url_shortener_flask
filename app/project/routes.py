from flask.helpers import url_for
from project import app, db
from project.controllers import Url
from flask import render_template, request, redirect
import os, json

@app.route("/", methods=['GET'])
def index():
    app_name = os.getenv("FLASK_ENV")
    return render_template('index.html')

@app.route("/add_url", methods=['POST'])
def add_url():
    status = Url.add()
    return json.dumps(status)

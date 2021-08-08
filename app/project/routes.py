from flask.helpers import url_for
from project import app, db
from project.controllers import Url
from flask import render_template, request, redirect
import os, json

@app.route("/", methods=['GET'])
def index():
    recaptcha_site_key = os.getenv("RECAPTCHA_SITE_KEY")
    return render_template('index.html', recaptcha = recaptcha_site_key)

@app.route("/add_url", methods=['POST'])
def add_url():
    status = Url.add()
    return json.dumps(status)

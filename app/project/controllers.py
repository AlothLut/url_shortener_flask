from project import app, db
from project.models import ShortUrl
from flask import request, redirect
from flask.helpers import url_for
from validation.recaptcha_v3 import RecaptchaV3

class Url():
    @staticmethod
    def add():
        try:
            url = request.form["url"].strip()
            alias = request.form["alias"].strip()
            token = request.form["recaptchaToken"]
            if RecaptchaV3.check(token) == False:
                return {
                    "success": False,
                    "message": "Recaptcha error"
                }

            if len(url) == 0 or len(alias) == 0:
                return {
                    "success": False,
                    "message": "Url or alias is empty"
                }
            elif ShortUrl.query.filter_by(short_url=alias).count() > 0:
                return {
                    "success": False,
                    "message": "Alias busy"
                }
            else:
                new_url = ShortUrl(original_url=url, short_url=alias)
                db.session.add(new_url)
                db.session.commit()
        except:
            return {
                "success": False,
                "message": "Something wrong, try next time"
            }
        else:
            return {
                "success": True,
                "message": "Alias has been created"
            }
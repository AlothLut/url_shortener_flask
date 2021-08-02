from project import app, db
from project.models import ShortUrl
from flask import request, redirect
from flask.helpers import url_for

class Url():

    @staticmethod
    def add():
        try:
            url = request.form["url"].strip()
            alias = request.form["alias"].strip()
            if len(url) == 0 or len(alias) == 0:
                return {
                    "success": False,
                    "code": "422",
                    "message": "Url or alias is empty"
                }
            elif ShortUrl.query.filter_by(short_url=alias).count() > 0:
                return {
                    "success": False,
                    "code": "422",
                    "message": "Alias busy"
                }
            else:
                new_url = ShortUrl(original_url=url, short_url=alias)
                db.session.add(new_url)
                db.session.commit()
        except:
            return {
                "success": False,
                "code": "500",
                "message": "Something wrong, try next time"
            }
        else:
            return {
                "success": True,
                "code": "200",
                "message": "Alias has been created"
            }
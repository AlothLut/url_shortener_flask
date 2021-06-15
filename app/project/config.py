import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://'\
        + os.getenv('POSTGRES_USER') \
        + ':' \
        + os.getenv('POSTGRES_PASSWORD') \
        + '@db-url-shortener:5432/' \
        + os.getenv('POSTGRES_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
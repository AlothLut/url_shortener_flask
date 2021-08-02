dependencies:
Tested on Linux(Ubuntu 20.04.1)

Docker

Docker-compose

for develop:
vscode + ms-python.python


helpfull commands:

docker-compose -f dev.yml up -d --build

docker-compose -f dev.yml exec app-url-shortener bash

docker-compose -f dev.yml logs app-url-shortener


Flask app with python interpreter inside docker container and example debug on vscode
because PyCharm Community edition not support connect to docker container.






create db and models

docker-compose -f dev.yml exec app-url-shortener python
from project import db
db.create_all()
from project.models import User
admin = User(username='admin', email='admin@example.com')
db.session.add(admin)
db.session.commit()
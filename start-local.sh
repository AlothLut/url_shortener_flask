#!/bin/bash

# Abort on any error (including if wait-for-it fails).
set -e

if [ "$EUID" -ne 0 ];  then
    echo "Not running as root"
    exit
fi

echo -e "\e[1;34m Add a rule to /etc/hosts\e[0m"

echo "10.10.0.11 app-url-shortener.loc" | sudo tee --append /etc/hosts > /dev/null

echo -e "\e[1;34m Build container\e[0m"

sudo docker-compose -f dev.yml up -d --build

echo -e "\e[1;34m Сreate a tables in the database\e[0m"

# fixed error: sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not connect to server: Connection refused
# w8 db container (10.10.0.12 - ipv4 for db-url-shortener) see dev.yml
while ! nc -z 10.10.0.12 5432; do
    sleep 3;
done

sudo docker-compose -f dev.yml exec app-url-shortener python -c "from project import db ; db.create_all()"
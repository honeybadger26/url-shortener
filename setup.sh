#!/bin/bash

timeout=3

while ! python testdb.py
do
    echo "Database is not ready. Checking again in $timeout seconds..."
    sleep $timeout
done

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000
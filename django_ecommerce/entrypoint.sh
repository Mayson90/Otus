#!/bin/bash

echo "1. Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

echo "2. DB is filling..."
python manage.py fill_db

echo "3. Users are creating..."
python manage.py create_users

echo "4. Server is starting..."
python manage.py runserver 0.0.0.0:8000

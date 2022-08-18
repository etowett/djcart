#!/bin/bash

python manage.py collectstatic --no-input

exec gunicorn --bind 0.0.0.0:8000 djcart.wsgi:application -w 2

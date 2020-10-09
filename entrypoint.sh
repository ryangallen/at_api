#!/bin/bash

python manage.py check
python manage.py collectstatic --no-input
python manage.py migrate --no-input

/usr/local/bin/gunicorn adventure_time.wsgi:application -w 2 -b :8000 --reload

#!/usr/bin/env sh

python manage.py migrate
python manage.py clearsessions

uwsgi --ini uwsgi.ini

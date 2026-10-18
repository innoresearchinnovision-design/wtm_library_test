#!/usr/bin/env bash
set -o errexit

pip install -r requirements_dev.txt

python manage.py collectstatic --no-input

python manage.py migrate
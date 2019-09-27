#! /bin/bash
python manage.py collectstatic

mkdir -p ../templates
cp ./gis_utils_frontend/dist/index.html ./templates
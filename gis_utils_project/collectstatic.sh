#! /bin/bash
rm -rf ./static/css
rm -rf ./static/js
python manage.py collectstatic

mkdir -p ./templates
cp ./gis_utils_frontend/dist/index.html ./templates
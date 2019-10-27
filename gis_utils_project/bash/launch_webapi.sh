#! /bin/bash
trap "echo unexpected exception" ERR
python $DJANGO_ROOT/gis_utils_app/web_api/news_api.py
exit 0

#! /bin/bash

if [ -z "$1" ]; then
    echo "invalid argument"
    exit 1
fi

trap "echo unexpected exception" ERR
python ./gis_utils_app/scraping/scraping_audit_client.py $1
exit 0

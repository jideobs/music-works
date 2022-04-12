#!/usr/bin/env bash

until python src/manage.py migrate --settings=musicworks.settings.base
do 
    echo "Waiting for postgres to be ready"
done

python src/manage.py runserver 0.0.0.0:8000 --settings=musicworks.settings.base

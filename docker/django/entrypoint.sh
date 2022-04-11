#!/usr/bin/env bash

until python manage.py migrate --settings=musicaggregator.settings.base
do 
    echo "Waiting for postgres to be ready"
done

python manage.py runserver 0.0.0.0:8000 --settings=musicaggregator.settings.base

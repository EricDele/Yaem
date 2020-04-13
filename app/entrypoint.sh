#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres... ON $SQL_HOST:$SQL_PORT"

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
python manage.py collectstatic --no-input --clear

# Load example data in the reference tables
python manage.py loaddata manager/fixtures.yaml

exec "$@"

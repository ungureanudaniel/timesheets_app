#!/bin/bash

function waitForServices() {
    python wait_for_services.py
}

waitForServices

# Run migrations and collect static files (if necessary)
python manage.py migrate
python manage.py makemigrations timesheet general users report admin_dashboard auth
python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"
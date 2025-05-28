#!/bin/bash
# Source .env.dev from parent folder
if [ -f ../.env.dev ]; then
  export $(grep -v '^#' ../.env.dev | xargs)
fi

set -e  # Exit immediately if a command exits with a non-zero status

function waitForServices() {
    python wait_for_services.py
}

waitForServices

# Run migrations and collect static files (if necessary)
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"
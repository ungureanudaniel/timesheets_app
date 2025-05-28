#!/bin/bash
# Source .env.dev from parent folder
if [ -f ../.env.prod ]; then
  export $(grep -v '^#' ../.env.dev | xargs)
fi

function waitForServices() {
    python wait_for_services.py
}

waitForServices

# Ensure proper permissions
find /app -type d -exec chmod 755 {} \;
find /app -type f -exec chmod 644 {} \;

# Run migrations and collect static files (if necessary)
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"
#!/bin/bash
# Source .env.dev from parent folder
if [ -f ../.env.dev ]; then
  export $(grep -v '^#' ../.env.dev | xargs)
fi

function waitForServices() {
    python wait_for_services.py
}

waitForServices

# Ensure proper permissions
find /app -type d -exec chmod 755 {} \;
find /app -type f -exec chmod 644 {} \;

exec "$@"
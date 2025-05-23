#!/bin/bash

function waitForServices() {
    python wait_for_services.py
}

waitForServices

# Ensure proper permissions
find /app -type d -exec chmod 755 {} \;
find /app -type f -exec chmod 644 {} \;

exec "$@"
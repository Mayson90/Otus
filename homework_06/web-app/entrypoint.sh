#!/usr/bin/env bash

echo "[entrypoint ECHO] Running migrations"
flask db upgrade

echo "[entrypoint ECHO] Starting app..."
exec "$@"

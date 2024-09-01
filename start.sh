#!/bin/sh
set -e

# Run migrations
uv run python manage.py migrate

# Start Gunicorn
exec uv run gunicorn onlydjango.wsgi:application --bind 0.0.0.0:8000 --workers 3 & uv run python manage.py run_huey -w 4 & uv run python manage.py collectstatic --noinput
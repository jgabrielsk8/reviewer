#!/bin/bash

# Run requirements
echo "Run requirements"
pip install -r requirements.txt

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Add super user
echo "Apply database migrations"
python manage.py add_superuser

# Start server
echo "Starting server"
supervisord -n

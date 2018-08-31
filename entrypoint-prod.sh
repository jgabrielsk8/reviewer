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
echo "Apply creating super user"
python manage.py add_superuser

# Add company
echo "Apply creating first company"
python manage.py add_company

# Start server
echo "Starting server"
supervisord -n

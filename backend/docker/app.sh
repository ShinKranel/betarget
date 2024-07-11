#!/bin/bash
echo "Script is running"
# Check if there are any .py files in migrations/versions
files=$(find migrations/versions -type f -name "*.py")
echo "Files found: $files"
# If no .py files are found, create a new revision
if [ -z "$files" ]; then
  echo "No migration files found. Creating a new revision."
  alembic -c alembic.ini revision --autogenerate -m "Init tables"
fi
files=$(find migrations/versions -type f -name "*.py")

# Run Alembic upgrade
alembic -c alembic.ini upgrade head
# Start Gunicorn server
exec gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8080

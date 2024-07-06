#!/bin/bash
alembic -c alembic.ini revision --autogenerate -m "Init tables"
alembic -c alembic.ini upgrade head
gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8080

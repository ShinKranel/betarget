#!/bin/bash

celery -A backend.src.tasks_celery.celery_app worker --loglevel=info
#!/bin/bash

celery -A src.tasks_celery.celery_app worker --loglevel=info
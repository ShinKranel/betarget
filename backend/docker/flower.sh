#!/bin/bash

sleep 10

celery -A src.tasks_celery.celery_app flower --port=5555
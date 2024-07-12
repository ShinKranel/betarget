from celery import Celery
from celery.schedules import crontab

from config import settings

celery_settings = settings.celery
celery_app = Celery(
    __name__,
    broker=celery_settings.CELERY_BROKER_URL,
    backend=celery_settings.CELERY_RESULT_BACKEND,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

# Ensure tasks are discovered
celery_app.autodiscover_tasks(['mail'])
celery_app.autodiscover_tasks(['vacancy'])

# Calls tasks at 00:00 every day
celery_app.conf.beat_schedule = {
    "check_expired_vacancies": {
        "task": "vacancy.tasks.check_expired_vacancies",
        "schedule": crontab(minute=0, hour=0),
    },
}

if settings.test.IS_TESTING:
    # Calls task every 15 seconds (only for test)
    celery_app.conf.beat_schedule = {
        "check_expired_vacancies": {
            "task": "vacancy.tasks.check_expired_vacancies",
            "schedule": 15.0,
        },
    }
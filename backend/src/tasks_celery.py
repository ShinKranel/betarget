from celery import Celery

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
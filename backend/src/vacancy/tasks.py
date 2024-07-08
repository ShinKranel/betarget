import json
import asyncio

from vacancy.service import get_expired_vacancies
from vacancy.models import Vacancy
from tasks_celery import celery_app
from logger import celery_logger as logger
from redis_ import redis_connection


@celery_app.task
def check_expired_vacancies():
    loop = asyncio.get_event_loop()
    expired_vacancies = loop.run_until_complete(get_expired_vacancies())
    logger.info(f"Found {len(expired_vacancies)} expired vacancies")
    
    serialized_expired_vacancies = [
        {"id": vacancy.id, "expired": vacancy.expiration_date}
        for vacancy in expired_vacancies
    ]
    
    if expired_vacancies:
        loop.run_until_complete(notify_expiration(expired_vacancies))
        return serialized_expired_vacancies
    else:
        logger.info("No expired vacancies found")
        return serialized_expired_vacancies


async def notify_expiration(vacancies: list[Vacancy]):
    logger.info(f"Vacancies {vacancies} expired")

    vacancies_id = [vacancy.id for vacancy in vacancies]

    event_data = json.dumps({
        "data": json.dumps(vacancies_id),  # Serialize vacancy IDs list to JSON
        "event": "vacancy_expiration"
    })

    await redis_connection.set("event_vacancy_expiration", event_data)
    logger.info(f"Event {event_data} published")
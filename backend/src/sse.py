import asyncio
import json

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse

from logger import sse_logger as logger
from redis_ import redis_connection
from config import settings


sse_settings = settings.sse
sse_router = APIRouter()


async def __handle_vacancy_expiration_event(event_info: dict):
    data = event_info.get('data')
    if data:
        vacancies_id = json.loads(event_info['data'])
        if vacancies_id:
            return f'data: {{"event": "{event_info.get("event")}", "data": "{vacancies_id}"}}\n\n'
    logger.info("No vacancies to expire")
    return "data: keep-alive\n\n"


@sse_router.get("/events")
async def event_stream(request: Request) -> StreamingResponse:
    async def event_generator(request: Request):
        client_ip = request.client.host
        logger.info(f"Client IP: {client_ip} is connected")
        while True:
            event_info = await redis_connection.get("event_vacancy_expiration")
            if event_info:
                event_info = json.loads(event_info.decode('utf-8'))
                logger.info(f"SSE Event: {event_info}")
                match event_info.get('event'):
                    case 'vacancy_expiration':
                       yield await __handle_vacancy_expiration_event(event_info)
                    case _:
                        logger.info("No vacancies to expire")
                        yield "data: keep-alive\n\n"
                await asyncio.sleep(sse_settings.EVENT_LOOP_RETRY_TIME)
            else:
                yield "data: keep-alive\n\n"

    return StreamingResponse(event_generator(request), media_type="text/event-stream")
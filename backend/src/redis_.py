import redis.asyncio as redis

from config import settings


redis_settings = settings.redis
redis_connection = redis.from_url(redis_settings.REDIS_URL, encoding="utf-8")
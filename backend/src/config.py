from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from fastapi_limiter.depends import RateLimiter
from dotenv import load_dotenv


PROJECT_PATH = Path(__file__).parent.parent
ENV_PATH = PROJECT_PATH / ".env"

if not ENV_PATH.exists():
    raise FileNotFoundError(f"{ENV_PATH} does not exist. Please create the .env file with the required variables.")

load_dotenv(dotenv_path=ENV_PATH)
 

class EnvSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=str(ENV_PATH), env_file_encoding="utf-8", extra="allow")


class MailSettings(EnvSettings):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: str
    MAIL_SERVER: str
    MAIL_TLS: str
    MAIL_SSL: str


class RedisSettings(EnvSettings):
    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_CONNECTION_RETRY: int = 5

    @property
    def REDIS_URL(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"


class DatabaseSettings(EnvSettings):
    DB_USER: str
    DB_PORT: str
    DB_PASS: str
    DB_HOST: str
    DB_NAME: str

    @property
    def DATABASE_URL_ASYNC(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @property
    def DATABASE_URL(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class TestDatabaseSettings(EnvSettings):
    DB_TEST_USER: str
    DB_TEST_PORT: str
    DB_TEST_PASS: str
    DB_TEST_HOST: str
    DB_TEST_NAME: str

    @property
    def DATABASE_URL_ASYNC(self):
        return f"postgresql+asyncpg://{self.DB_TEST_USER}:{self.DB_TEST_PASS}@{self.DB_TEST_HOST}:{self.DB_TEST_PORT}/{self.DB_TEST_NAME}"
    
    @property
    def DATABASE_URL(self):
        return f"postgresql+psycopg2://{self.DB_TEST_USER}:{self.DB_TEST_PASS}@{self.DB_TEST_HOST}:{self.DB_TEST_PORT}/{self.DB_TEST_NAME}"


class TestSettings:
    IS_TESTING = True
    BASE_URL = "http://localhost:9999"


class MiddlewareSettings:
    BACKEND_CORS_ORIGINS = [
        "http://localhost:8080",
        "http://localhost:8000",
    ]


class AuthSettings(EnvSettings):
    SECRET_MANAGER: str
    SECRET_JWT: str


class AdminSettings(EnvSettings):
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str
    SECRET_SESSION: str


class LoggingSettings:
    LOG_PATH = PROJECT_PATH / "logs"


class CelerySettings(EnvSettings):
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str


class S3StorageSettings(EnvSettings):
    S3_ACCESS_KEY: str
    S3_SECRET_KEY: str
    S3_BUCKET_NAME: str
    S3_ENDPOINT_URL: str
    S3_PUBLIC_DOMAIN: str


class RequestLimiterSettings:
    ENABLED = False
    DEFAULT_LIMIT: int = RateLimiter(times=3, seconds=5)


class VacancySettings:
    EXPIRATION_TIME: int = 30


class SSESettings:
    EVENT_LOOP_RETRY_TIME: int = 60


class Settings:
    auth = AuthSettings()
    admin = AdminSettings()
    celery = CelerySettings()
    database = DatabaseSettings()
    test_database = TestDatabaseSettings()
    test = TestSettings()
    middleware = MiddlewareSettings()
    mail = MailSettings()
    redis = RedisSettings()
    log = LoggingSettings()
    s3 = S3StorageSettings()
    request_limiter = RequestLimiterSettings()
    vacancy = VacancySettings()
    sse = SSESettings()


settings = Settings()

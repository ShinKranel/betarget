from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
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


class MiddlewareSettings(EnvSettings):
    BACKEND_CORS_ORIGINS: str


class AuthSettings(EnvSettings):
    SECRET_MANAGER: str
    SECRET_JWT: str


class AdminSettings(EnvSettings):
    SECRET_SESSION: str


class Settings:
    auth = AuthSettings()
    admin = AdminSettings()
    database = DatabaseSettings()
    test_database = TestDatabaseSettings()
    middleware = MiddlewareSettings()
    mail = MailSettings()
    redis = RedisSettings()


settings = Settings()

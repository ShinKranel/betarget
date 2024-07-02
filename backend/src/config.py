from dotenv import load_dotenv
import os
# TODO: change to BaseSettings from pydantic_settings
load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PORT = os.environ.get("DB_PORT")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")

DB_TEST_USER = os.environ.get("DB_TEST_USER")
DB_TEST_PORT = os.environ.get("DB_TEST_PORT")
DB_TEST_PASS = os.environ.get("DB_TEST_PASS")
DB_TEST_HOST = os.environ.get("DB_TEST_HOST")
DB_TEST_NAME = os.environ.get("DB_TEST_NAME")

BACKEND_CORS_ORIGINS = os.environ.get("BACKEND_CORS_ORIGINS")

SECRET_JWT = os.environ.get("SECRET_JWT")
SECRET_MANAGER = os.environ.get("SECRET_MANAGER")

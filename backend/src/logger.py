import logging
from logging.handlers import RotatingFileHandler

from backend.src.config import settings


def create_log_files_if_not_exist():
    log_settings = settings.log
    if not log_settings.LOG_PATH.exists():
        log_settings.LOG_PATH.mkdir(parents=True)


def setup_logger():
    logger = logging.getLogger('AppLogger')
    logger.setLevel(logging.DEBUG)

    log_settings = settings.log
    file_name = 'app.log'

    create_log_files_if_not_exist()

    file_handler = RotatingFileHandler(filename=log_settings.LOG_PATH / file_name, maxBytes=5*1024*1024, backupCount=2)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


logger = setup_logger()

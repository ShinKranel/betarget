import logging
from logging.handlers import RotatingFileHandler

from config import settings


def create_log_files_if_not_exist():
    log_settings = settings.log
    if not log_settings.LOG_PATH.exists():
        log_settings.LOG_PATH.mkdir(parents=True)


def setup_logger(logger_name: str, filename: str = 'app.log'):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    log_settings = settings.log

    create_log_files_if_not_exist()

    if not (log_settings.LOG_PATH / filename).exists():
        (log_settings.LOG_PATH / filename).touch()
        
    file_handler = RotatingFileHandler(filename=log_settings.LOG_PATH / filename, maxBytes=5*1024*1024, backupCount=2)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


def clear_log_files():
    log_settings = settings.log
    for file in log_settings.LOG_PATH.glob('*.log'):
        with open (file, 'w') as f:
            f.write('')


clear_log_files()
logger = setup_logger(logger_name='AppLogger')
celery_logger = setup_logger(logger_name='CeleryLogger', filename='celery.log')
sse_logger = setup_logger(logger_name='S3Logger', filename='sse.log')
db_query_logger = setup_logger(logger_name='DBQueryLogger', filename='db.log')
test_logger = setup_logger(logger_name='TestLogger', filename='test.log')

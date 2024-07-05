from fastapi_mail import ConnectionConfig

from config import settings


mail_settings = settings.mail

mail_config = ConnectionConfig(
    MAIL_USERNAME=mail_settings.MAIL_USERNAME,
    MAIL_PASSWORD=mail_settings.MAIL_PASSWORD,
    MAIL_FROM=mail_settings.MAIL_FROM,
    MAIL_PORT=mail_settings.MAIL_PORT,
    MAIL_SERVER=mail_settings.MAIL_SERVER,
    MAIL_SSL_TLS=bool(mail_settings.MAIL_SSL),
    USE_CREDENTIALS=True
)
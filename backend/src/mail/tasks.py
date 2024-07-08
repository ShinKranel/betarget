import asyncio

from fastapi_mail import FastMail, MessageSchema

from tasks_celery import celery_app
from logger import logger
from mail.mail import mail_config

@celery_app.task
def send_email(subject: str, recipients: list[str], body: str):
    logger.info(f"Sending email with subject {subject} to {recipients}")
    message = MessageSchema(
        subject=subject,
        recipients=recipients,
        body=body,
        subtype="html"
    )

    fm = FastMail(mail_config)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(fm.send_message(message))
    except Exception as e:
        logger.error(f"Error sending email with subject {subject} to {recipients}: {e}")

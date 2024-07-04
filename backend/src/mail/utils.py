from backend.src.mail.mail import send_email
from backend.src.auth.models import User


async def send_sucessful_login_msg(user: User):
    subject = "You successfully loggined to our service"
    body = f"Welcome {user.username}! Thank you for loggin."
    await send_email(subject, recipients=[user.email], body=body)


async def send_sucessful_register_msg(user: User):
    subject = "You successfully registered to our service"
    body = f"We are appreciate you, {user.username}! Do not forget to login!"
    await send_email(subject, recipients=[user.email], body=body)


async def send_sucessful_forgot_password_msg(user: User, reset_token: str):
    subject = "Password reset request"
    reset_link = f"http://localhost:9999/reset-password?token={reset_token}"
    body = f"Hello {user.username}, use the following link to reset your password: {reset_link}"
    await send_email(subject, recipients=[user.email], body=body)


async def send_sucessful_reset_password_msg(user: User):
    subject = "Password was successfully reset"
    body = f"Your password was successfully reset, {user.username}!"
    await send_email(subject, recipients=[user.email], body=body)


async def send_email_verification_msg(user: User, verification_token: str):
    subject = "Verify your account"
    verify_link = f"http://localhost:9999/verify-account?token={verification_token}"
    body = f"Hello {user.username}, use the following link to verify your account: {verify_link}"
    await send_email(subject, recipients=[user.email], body=body)
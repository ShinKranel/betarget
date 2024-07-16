from httpx_oauth.clients.google import GoogleOAuth2

from src.config import settings


auth_settings = settings.auth

google_auth_client = GoogleOAuth2(
    auth_settings.GOOGLE_CLIENT_ID, auth_settings.GOOGLE_CLIENT_SECRET
)

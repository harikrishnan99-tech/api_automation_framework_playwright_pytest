from config.settings import get_config_data
from helpers.logger import logger
from helpers.payload_manager import login_payload
from helpers.retry_manager import RetryException


class TokenManager:
    _access_token = None

    @classmethod
    async def get_token(cls, api_context):
        if cls._access_token:
            return cls._access_token

        logger.info("No active token found. Logging in...")

        resources = get_config_data('resources', 'user_login')  # or fetch from config

        response = await api_context.post(
            resources,
            data=login_payload()
        )

        response_body = await response.json()

        if response.status != 200:
            logger.error("Login failed while generating token")
            raise RetryException("Login failed")

        cls._access_token = response_body.get("accessToken")

        if not cls._access_token:
            logger.error("Access token missing in login response")
            raise Exception("Token not received")

        logger.info("Token generated successfully")
        return cls._access_token

    @classmethod
    def clear_token(cls):
        logger.warning("Clearing stored token")
        cls._access_token = None
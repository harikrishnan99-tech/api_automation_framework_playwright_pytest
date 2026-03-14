from helpers.logger import logger
from helpers.payload_manager import login_payload, add_user_payload, update_user_payload
from config.settings import get_config_data
from helpers.response_validator import ResponseValidator
from helpers.retry_manager import async_retry, RetryException
from helpers.token_manager import TokenManager


class APIUtils:

    # @async_retry(
    #     retries=3,
    #     delay=2,
    #     allowed_exceptions=(RetryException,)
    # )
    # async def user_login(self, api_context):
    #     resources = get_config_data('resources', 'user_login')
    #     logger.info(f"Starting user login → {resources}")
    #
    #     response = await api_context.post(
    #         resources,
    #         data=login_payload()
    #     )
    #     logger.debug(f"Login payload: {login_payload()}")
    #
    #     response_body = await ResponseValidator.validate_login_response(response)
    #     logger.info("Login successful")
    #
    #     return response_body["accessToken"]

    @async_retry(
        retries=2,
        delay=1,
        allowed_exceptions=(RetryException,)
    )
    async def get_current_user(self, api_context):
        resources = get_config_data('resources', 'get_current_user')
        logger.info("Fetching current user")
        access_token = await TokenManager.get_token(api_context)

        response = await api_context.get(
            resources,
            headers={"Authorization": access_token}
        )
        logger.debug(f"Token used: {access_token[:10]}...")

        await ResponseValidator.validate_get_current_user_response(response)
        logger.info("Fetched current user successfully")

    @async_retry(
        retries=2,
        delay=1,
        allowed_exceptions=(RetryException,)
    )
    async def get_all_users(self, api_context):
        resources = get_config_data('resources', 'get_all_users')
        logger.info("Fetching all users")

        response = await api_context.get(
            resources
        )

        await ResponseValidator.validate_get_all_users(response)
        logger.info("All users fetched successfully")

    @async_retry(
        retries=2,
        delay=1,
        allowed_exceptions=(RetryException,)
    )
    async def search_users(self, api_context):
        resources = get_config_data('resources', 'search_users')
        logger.info(f'Searching for user: {login_payload().get("username")}')

        response = await api_context.get(
            resources,
            params={"q": login_payload().get("username")}
        )

        await ResponseValidator.validate_get_all_users(response)
        logger.info("User fetched successfully")

    @async_retry(
        retries=3,
        delay=2,
        allowed_exceptions=(RetryException,)
    )
    async def add_user(self, api_context):
        resources = get_config_data('resources', 'add_user')
        logger.info("Adding user")

        response = await api_context.post(
            resources,
            data=add_user_payload()
        )

        await ResponseValidator.validate_add_user(response)
        logger.info("User added successfully")

    @async_retry(
        retries=3,
        delay=2,
        allowed_exceptions=(RetryException,)
    )
    async def update_user(self, api_context, user_id):
        resources = get_config_data('resources', 'get_all_users')
        logger.info(f"Updating user with id: {user_id}")

        response = await api_context.put(
            f'{resources}/{user_id}',
            data=update_user_payload()
        )

        await ResponseValidator.validate_update_user(response, user_id)
        logger.info(f"User with id: {user_id} updated successfully")

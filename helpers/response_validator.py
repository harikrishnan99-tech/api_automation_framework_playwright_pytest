from helpers.payload_manager import login_payload, update_user_payload
from helpers.retry_manager import RetryException
from helpers.logger import logger
from jsonschema import validate
import json


class ResponseValidator:

    @staticmethod
    async def validate_login_response(response):
        logger.info("Validating login response")

        response_body = await response.json()
        status = response.status

        logger.debug(f"Login response status: {status}")
        logger.debug(f"Login response body: {response_body}")

        if response_body.get("message") == "Username and password required":
            logger.error("Username or password missing in login request")
            raise ValueError("Validation Error: Username or Password missing")

        if status >= 500:
            logger.warning("Server error during login. Triggering retry.")
            raise RetryException("Server error during login")

        assert status == 200, f"Unexpected status: {status}"

        if "accessToken" not in response_body:
            logger.error("Login succeeded but accessToken missing")
            raise Exception("Login succeeded but token missing")

        assert response_body['username'] == login_payload().get('username')

        logger.info("Login response validation successful")
        return response_body

    @staticmethod
    async def validate_get_current_user_response(response):
        logger.info("Validating get current user response")

        response_body = await response.json()
        status = response.status

        logger.debug(f"Current user response: {response_body}")

        if response_body.get("message") == "Token expired":
            logger.warning("Token expired. Retry required.")
            raise RetryException("Token expired. Should refresh.")

        if response_body.get("message") == "invalid signature":
            logger.error("Invalid token signature detected")
            raise ValueError("Validation Error: Token Invalid")

        assert status == 200, "Unexpected status code"
        assert response_body['username'] == login_payload().get('username')

        logger.info("Current user validation successful")
        return response_body

    @staticmethod
    async def validate_get_all_users(response):
        logger.info("Validating get all users response")

        response_body = await response.json()
        logger.debug(f"Get all users response: {response_body}")

        required_keys = ["users", "total", "skip", "limit"]
        for key in required_keys:
            assert key in response_body, f"Missing key: {key}"

        assert isinstance(response_body["users"], list)
        assert isinstance(response_body["total"], int)
        assert isinstance(response_body["skip"], int)
        assert isinstance(response_body["limit"], int)

        for user in response_body["users"]:
            logger.debug(f"Validating user ID: {user.get('id')}")

            assert isinstance(user["id"], int)
            assert isinstance(user["email"], str)
            assert isinstance(user["firstName"], str)
            assert isinstance(user["lastName"], str)
            assert isinstance(user["maidenName"], str)
            assert isinstance(user["age"], int)
            assert isinstance(user["gender"], str)
            assert isinstance(user["phone"], str)
            assert isinstance(user["username"], str)

            company = user["company"]
            assert "name" in company
            assert "address" in company

        assert len(response_body["users"]) <= response_body["total"]
        assert response.status == 200, "Unexpected status code"

        logger.info("Get all users validation successful")
        return response_body

    @staticmethod
    async def validate_add_user(response):
        logger.info("Validating add user response")

        response_body = await response.json()
        logger.debug(f"Add user response: {response_body}")

        with open("schema/add_user_schema.json") as f:
            schema = json.load(f)

        validate(instance=response_body, schema=schema)

        assert response.status == 201, "Unexpected status code"

        logger.info("Add user validation successful")
        return response_body

    @staticmethod
    async def validate_update_user(response, user_id):
        logger.info(f"Validating update user response for user_id: {user_id}")

        response_body = await response.json()
        logger.debug(f"Update user response: {response_body}")

        if response_body.get("message") == f"User with id '{user_id}' not found":
            logger.error(f"User not found: {user_id}")
            raise ValueError(f"Validation Error: Invalid user id : {user_id}")

        assert response.status == 200, "Unexpected status code"

        assert response_body['id'] == int(user_id)
        assert response_body['firstName'] == update_user_payload().get('firstName')
        assert response_body['lastName'] == update_user_payload().get('lastName')

        logger.info(f"User {user_id} updated successfully")
        return response_body
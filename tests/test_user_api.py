import pytest
from helpers.api_client import APIUtils

class TestAPIHealthCheck:


    @pytest.mark.asyncio
    @pytest.mark.healthcheck
    async def test_get_current_user(self, api_context):
        api_utils = APIUtils()
        await api_utils.get_current_user(api_context)

    @pytest.mark.asyncio
    @pytest.mark.smoke
    @pytest.mark.healthcheck
    async def test_get_all_users(self, api_context):
        api_utils = APIUtils()
        await api_utils.get_all_users(api_context)

    @pytest.mark.asyncio
    @pytest.mark.healthcheck
    async def test_search_users(self, api_context):
        api_utils = APIUtils()
        await api_utils.search_users(api_context)

    @pytest.mark.asyncio
    @pytest.mark.smoke
    @pytest.mark.healthcheck
    async def test_add_user(self, api_context):
        api_utils = APIUtils()
        await api_utils.add_user(api_context)

    @pytest.mark.asyncio
    @pytest.mark.healthcheck
    async def test_update_user(self, api_context):
        api_utils = APIUtils()
        await api_utils.update_user(api_context, user_id=1)

import os
import shutil

import pytest
from playwright.async_api import async_playwright
from config.settings import get_config_data


@pytest.fixture(scope="function")
async def api_context():
    """
    Creates reusable APIRequestContext for entire test session.
    """
    base_url = get_config_data('stg_base_url', 'base_url')

    async with async_playwright() as playwright:
        request = await playwright.request.new_context(
            base_url=base_url
        )
        yield request
        await request.dispose()

# def pytest_addoption(parser):
#     parser.addoption(
#         "--env",
#         action="store",
#         default="stg",
#         help="Environment to run tests against: stg/dev/prod"
#     )

def pytest_sessionstart(session):
    """
    Cleans previous Allure results before starting test execution
    """
    results_dir = "reports/allure-results"

    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)

    os.makedirs(results_dir, exist_ok=True)
import pytest

from api.client import APIClient
from config import BASE_URL, REQUEST_TIMEOUT, RETRY_COUNT


@pytest.fixture(scope="session")
def api_client():
    return APIClient(
        base_url=BASE_URL,
        timeout=REQUEST_TIMEOUT,
        retries=RETRY_COUNT,
    )


@pytest.fixture
def post_payload():
    return {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }

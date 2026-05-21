import pytest

from assertions.checks import (
    assert_field_equals,
    assert_has_schema,
    assert_list_has_schema,
    assert_status_code,
)
from models.schema import USER_SCHEMA


@pytest.mark.smoke
@pytest.mark.full
def test_get_users(api_client):
    response = api_client.get_users()
    assert_status_code(response, 200)

    users = response.json()
    assert_list_has_schema(users, USER_SCHEMA)


@pytest.mark.smoke
@pytest.mark.full
def test_get_user_by_id(api_client):
    user_id = 1
    response = api_client.get_user(user_id)
    assert_status_code(response, 200)

    user = response.json()
    assert_has_schema(user, USER_SCHEMA)
    assert_field_equals(user, "id", user_id)


@pytest.mark.full
def test_get_missing_user(api_client):
    response = api_client.get_user(9999)
    assert_status_code(response, 404)

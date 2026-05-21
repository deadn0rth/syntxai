import pytest

from assertions.checks import (
    assert_created_post,
    assert_field_equals,
    assert_list_has_schema,
    assert_payload_is_saved,
    assert_status_code,
)
from models.schema import COMMENT_SCHEMA, POST_SCHEMA


INVALID_POST_PAYLOADS = [
    pytest.param({"title": "foo"}, id="missing_body_and_user_id"),
    pytest.param(
        {"title": "foo", "body": "bar", "userId": "qwe"},
        id="wrong_user_id_type",
    ),
    pytest.param({}, id="empty_body"),
]


@pytest.mark.smoke
@pytest.mark.full
def test_get_posts(api_client):
    response = api_client.get_posts()
    assert_status_code(response, 200)

    posts = response.json()
    assert_list_has_schema(posts, POST_SCHEMA)


@pytest.mark.smoke
@pytest.mark.full
def test_create_post(api_client, post_payload):
    response = api_client.create_post(post_payload)
    assert_status_code(response, 201)

    created_post = response.json()
    assert_created_post(created_post, post_payload)


@pytest.mark.full
def test_update_post(api_client, post_payload):
    post_id = 1
    payload = post_payload.copy()
    payload["id"] = post_id
    payload["title"] = "Updated Title"

    response = api_client.update_post(post_id, payload)
    assert_status_code(response, 200)

    updated_post = response.json()
    assert_payload_is_saved(updated_post, payload)


@pytest.mark.full
def test_patch_post(api_client):
    post_id = 1
    payload = {"title": "Patched title"}

    response = api_client.patch_post(post_id, payload)
    assert_status_code(response, 200)

    patched_post = response.json()
    assert_payload_is_saved(patched_post, payload)


@pytest.mark.full
def test_delete_post(api_client):
    post_id = 1
    response = api_client.delete_post(post_id)
    assert_status_code(response, 200)


@pytest.mark.full
def test_get_post_comments(api_client):
    post_id = 1
    response = api_client.get_comments_by_post_id(post_id)
    assert_status_code(response, 200)

    comments = response.json()
    assert_list_has_schema(comments, COMMENT_SCHEMA)

    for comment in comments:
        assert_field_equals(comment, "postId", post_id)


@pytest.mark.full
@pytest.mark.negative
@pytest.mark.parametrize("invalid_payload", INVALID_POST_PAYLOADS)
def test_create_post_with_invalid_payload(api_client, invalid_payload):
    response = api_client.create_post(invalid_payload)
    assert_status_code(response, 201)

    created_post = response.json()
    assert_created_post(created_post, invalid_payload)

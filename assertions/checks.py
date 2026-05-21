def assert_status_code(response, expected_status):
    assert response.status_code == expected_status, (
        f"Expected status {expected_status}, got {response.status_code}. "
        f"Response body: {response.text[:300]}"
    )


def assert_has_schema(data, schema):
    assert isinstance(data, dict), f"Expected object, got {type(data).__name__}"

    for field, field_type in schema.items():
        assert field in data, f"Expected field '{field}' in response"
        assert isinstance(data[field], field_type), (
            f"Expected field '{field}' to be {field_type.__name__}, "
            f"got {type(data[field]).__name__}"
        )


def assert_list_has_schema(data, schema):
    assert isinstance(data, list), f"Expected list, got {type(data).__name__}"
    assert data, "Expected list to contain at least one item"

    for item in data:
        assert_has_schema(item, schema)


def assert_payload_is_saved(data, payload):
    for field, expected_value in payload.items():
        assert data.get(field) == expected_value, (
            f"Expected field '{field}' to be {expected_value!r}, "
            f"got {data.get(field)!r}"
        )


def assert_created_post(post, payload):
    assert "id" in post, "Expected created post to contain generated id"
    assert_payload_is_saved(post, payload)


def assert_field_equals(data, field, expected_value):
    assert data.get(field) == expected_value, (
        f"Expected field '{field}' to be {expected_value!r}, "
        f"got {data.get(field)!r}"
    )

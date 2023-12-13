from http import HTTPStatus
from API_tests.api_collections.users_api import UsersApi
from utilities.allure_logger import log_response


def test_get_all_users():
    resp = UsersApi().get_all_users()
    log_response(resp)
    assert resp.status_code == HTTPStatus.OK
    data = resp.json()
    assert isinstance(data, list)


def test_post_new_user(get_fake_user_payload):
    payload = get_fake_user_payload
    resp = UsersApi().post_new_user(user_data=payload)
    log_response(resp)
    assert resp.status_code == HTTPStatus.CREATED
    data = resp.json()
    assert data['name'] == payload['name']


def test_update_user(get_fake_user_payload):
    # Assuming there is an existing user with ID 1
    user_id = 1
    payload = get_fake_user_payload()
    resp = UsersApi().update_user(user_id, user_data=payload)
    log_response(resp)
    assert resp.status_code == HTTPStatus.OK
    data = resp.json()
    assert data['name'] == payload['name']


def test_delete_user():
    # Assuming there is an existing user with ID 1
    user_id = 1
    resp = UsersApi().delete_user(user_id)
    log_response(resp)
    assert resp.status_code == HTTPStatus.NO_CONTENT


def test_patch_user(get_fake_user_payload):
    # Assuming there is an existing user with ID 1
    user_id = 1
    payload = get_fake_user_payload()
    resp = UsersApi().patch_user(user_id, partial_user_data=payload)
    log_response(resp)
    assert resp.status_code == HTTPStatus.OK
    data = resp.json()
    assert data['name'] == payload['name']


def test_get_nonexistent_user():
    user_id = 999999  # Replace with a nonexistent user ID
    resp = UsersApi().get_all_users(user_id)
    log_response(resp)
    assert resp.status_code == HTTPStatus.NOT_FOUND


def test_post_user_missing_required_field():
    payload = {}  # Missing required fields
    resp = UsersApi().post_new_user(user_data=payload)
    log_response(resp)
    assert resp.status_code == HTTPStatus.BAD_REQUEST


def test_update_nonexistent_user(get_fake_user_payload):
    user_id = 999999  # Replace with a nonexistent user ID
    payload = get_fake_user_payload()
    resp = UsersApi().update_user(user_id, user_data=payload)
    log_response(resp)
    assert resp.status_code == HTTPStatus.NOT_FOUND


def test_delete_nonexistent_user():
    user_id = 999999  # Replace with a nonexistent user ID
    resp = UsersApi().delete_user(user_id)
    log_response(resp)
    assert resp.status_code == HTTPStatus.NOT_FOUND


def test_patch_user_invalid_id(get_fake_user_payload):
    user_id = "invalid user ID"  # Replace with an invalid user ID
    payload = get_fake_user_payload()
    resp = UsersApi().patch_user(user_id, partial_user_data=payload)
    log_response(resp)
    assert resp.status_code == HTTPStatus.BAD_REQUEST


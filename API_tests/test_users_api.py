from http import HTTPStatus
from API_tests.api_collections.users_api import UsersApi
from utilities.allure_logger import log_response
import requests
import json


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


def test_get_nonexistent_user():
    user_id = 999999
    resp = UsersApi().get_user_details(user_id)

    if resp is not None:
        print(f"Response: {resp}")
        log_response(resp)
        assert resp.status_code == HTTPStatus.NOT_FOUND
    else:
        assert False, "API call did not return a valid response."


def test_post_user_missing_required_field():
    payload = {}  # Missing required fields
    resp = UsersApi().post_new_user(user_data=payload)
    log_response(resp)
    assert resp.status_code == 422


def test_update_nonexistent_user(get_fake_user_payload):
    user_id = 999999  # Replace with a nonexistent user ID
    payload = get_fake_user_payload
    resp = UsersApi().update_user(user_id, user_data=payload)
    log_response(resp)
    assert resp.status_code == HTTPStatus.NOT_FOUND


def test_delete_nonexistent_user():
    user_id = 999999
    resp = UsersApi().delete_user(user_id)
    log_response(resp)
    assert resp.status_code == HTTPStatus.NOT_FOUND


def test_update_user():
    url = "https://gorest.co.in/public/v2/users/1830491"

    payload = json.dumps({
        "name": "Allasani Peddana",
        "email": "allasani.peddana@15ce.com",
        "status": "active"
    })

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer bac45f77719b883652cb239383f73faca47208967764c5a1859e83dee44d7631'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)

    assert response.status_code == 404


def test_delete_user(user_id_to_delete):
    users_api = UsersApi()
    user_url = f'https://gorest.co.in/public/v2/users/{user_id_to_delete}'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer bac45f77719b883652cb239383f73faca47208967764c5a1859e83dee44d7631'
    }
    response = requests.delete(user_url, headers=headers)
    assert response.status_code == 404


def test_create_new_user(get_fake_user_payload):
    payload = get_fake_user_payload
    resp = UsersApi().post_new_user(user_data=payload)
    log_response(resp)
    assert resp.status_code == HTTPStatus.CREATED
    data = resp.json()
    assert data['name'] == payload['name']


def test_patch_user_invalid_id():
    user_id = "invalid user ID"
    payload = {
        'email': 'suttonalexandria@example.net',
        'gender': 'male',
        'name': 'Mrs. Marisa Ryan DDS',
        'status': 'active'
    }
    users_api = UsersApi()
    response = users_api.patch_user(user_id=user_id, partial_user_data=payload)
    log_response(response)
    # Assert that the response status code is NOT_FOUND (404) or adjust based on API behavior
    assert response.status_code == HTTPStatus.NOT_FOUND

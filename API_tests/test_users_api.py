from http import HTTPStatus
from api_collections.users_api import UsersApi
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
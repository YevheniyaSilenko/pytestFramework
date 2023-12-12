import json
from API_tests.api_collections._base_api import BaseApi
from utilities.deco import auto_step


@auto_step
class UsersApi(BaseApi):
    def __init__(self, base_url='https://gorest.co.in/public/v2'):
        super().__init__(base_url)
        self.__url = '/users'
        self.__headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer bac45f77719b883652cb239383f73faca47208967764c5a1859e83dee44d7631'
        }

    def get_all_users(self):
        return self._get(url=self.__url, headers=self.__headers)

    def post_new_user(self, user_data: dict):
        return self._post(self.__url, data=json.dumps(user_data), headers=self.__headers)

    def update_user(self, user_id, user_data: dict):
        user_url = f'{self.__url}/{user_id}'
        return self._put(url=user_url, data=json.dumps(user_data), headers=self.__headers)

    def delete_user(self, user_id):
        user_url = f'{self.__url}/{user_id}'
        return self._delete(url=user_url, headers=self.__headers)

    def patch_user(self, user_id, partial_user_data: dict):
        user_url = f'{self.__url}/{user_id}'
        return self._patch(url=user_url, data=json.dumps(partial_user_data), headers=self.__headers)
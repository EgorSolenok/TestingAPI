import allure

from json import dumps
from clients.jsonplaceholder.base_client import BaseClient
from config import BASE_URL
from tests.helpers.request_data import InvalidData
from tests.helpers.request_data import ValidData
from utils.request import APIRequest


class PostClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = f'{BASE_URL}/posts'
        self.request = APIRequest()

    @allure.step("read_all_posts")
    def read_all_posts(self):
        return self.request.get(self.base_url), 'GET'

    @allure.step("read_all_posts_invalid_endpoint")
    def read_all_posts_invalid_endpoint(self):
        return self.request.get(f'{BASE_URL}/post'), 'GET'

    @allure.step("read_all_comments_by_post_id")
    def read_all_comments_by_post_id(self, post_id):
        comments_url = f'{self.base_url}/{post_id}/comments'
        return self.request.get(comments_url), 'GET'

    @allure.step("read_one_post_by_post_id")
    def read_one_post_by_post_id(self, post_id):
        post_url = f'{self.base_url}/{post_id}'
        return self.request.get(post_url), 'GET'

    @allure.step("delete_post_by_id")
    def delete_post_by_id(self, post_id):
        post_url = f'{self.base_url}/{post_id}'
        return self.request.delete(post_url), 'DELETE'

    @allure.step("delete_post_invalid_url")
    def delete_post_invalid_url(self, post_id=""):
        post_url = f'{self.base_url}/{post_id}'
        print(post_url)
        return self.request.delete(post_url), 'DELETE'

    @allure.step("create_new_post_invalid_data")
    def create_new_post_invalid_data(self, data=None):
        response, method, title, body, user_id = self.__create_post_with_invalid_data(data)
        return response, method, title, body, user_id

    def __create_post_with_invalid_data(self, data=None):
        if data is None:
            payload, title, body, user_id = InvalidData.get_invalid_data()
        else:
            payload = dumps(data)
            title, body, user_id = data['title'], data['body'], data['user_id']
        invalid_url = self.base_url + 's'
        response = self.request.post(invalid_url, payload, self.headers)
        method = 'POST'
        return response, method, title, body, user_id

    @allure.step("create_new_post")
    def create_new_post(self, data=None):
        response, method, title, body, user_id = self.__create_post_with_unique_data(data)
        return response, method, title, body, user_id

    def __create_post_with_unique_data(self, data=None):
        if data is None:
            payload, title, body, user_id = ValidData.get_random_payload()
        else:
            payload = dumps(data)
            title, body, user_id = data['title'], data['body'], data['user_id']

        response = self.request.post(self.base_url, payload, self.headers)
        method = 'POST'
        return response, method, title, body, user_id

    @allure.step("patch_post")
    def patch_post(self, post_id, data=None):
        post_url = f'{self.base_url}/{post_id}'
        response, method, title, body, user_id = self.__patch_post_with_unique_data(post_url, data)
        return response, method, title, body, user_id

    def __patch_post_with_unique_data(self, post_url, data=None):
        if data is None:
            payload, title, body, user_id = ValidData.get_random_payload()
        else:
            payload = dumps(data)
            title, body, user_id = data['title'], data['body'], data['user_id']
        response = self.request.patch(post_url, payload, self.headers)
        method = 'PATCH'
        return response, method, title, body, user_id

    @allure.step("put_body_in_post")
    def put_body_in_post(self, post_id, data=None):
        post_url = f'{self.base_url}/{post_id}'
        response, method, body = self.__put_unique_body_in_post(post_url, data)
        return response, method, body

    def __put_unique_body_in_post(self, post_url, data=None):
        if data is None:
            payload, body = ValidData.get_random_body()
        else:
            payload = dumps(data)
            body = data['body']

        response = self.request.put(post_url, payload, self.headers)
        method = 'PUT'
        return response, method, body

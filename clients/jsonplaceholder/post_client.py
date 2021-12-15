from json import dumps
from uuid import uuid4

from clients.jsonplaceholder.base_client import BaseClient
from config import BASE_URL
from utils.request import APIRequest
from utils.generated_data import GeneratedData


class PostClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = f'{BASE_URL}' + '/posts'
        self.request = APIRequest()

    def read_all_posts(self):
        return self.request.get(self.base_url), 'GET'

    def read_all_comments_by_post_id(self, post_id):
        comments_url = f'{self.base_url}/{post_id}/comments'
        return self.request.get(comments_url), 'GET'

    def read_one_comment_by_comment_id(self, comment_id):
        comment_url = f'{self.base_url}/{comment_id}'
        return self.request.get(comment_url), 'GET'

    def delete_post_by_id(self, post_id):
        post_url = f'{self.base_url}/{post_id}'
        return self.request.delete(post_url), 'DELETE'

    def create_post(self, data=None):
        response, method, title, body, user_id = self.__create_post_with_unique_data(data)
        return response, method, title, body, user_id

    def __create_post_with_unique_data(self, data=None):
        if data is None:
            title = GeneratedData.get_new_title()
            body = GeneratedData.get_new_body()
            user_id = GeneratedData.get_new_user_id()
            payload = dumps({
                'title': title,
                'body': body,
                'userId': user_id,
            })
        else:
            payload = dumps(data)
            title = data['title']
            body = data['body']
            user_id = data['user_id']

        response = self.request.post(self.base_url, payload, self.headers)
        method = 'POST'
        return response, method, title, body, user_id

    def patch_post(self, post_id, data=None):
        post_url = f'{self.base_url}/{post_id}'
        response, method, title, body, user_id = self.__patch_post_with_unique_data(post_url, data)
        return response, method, title, body, user_id

    def __patch_post_with_unique_data(self, post_url, data=None):
        if data is None:
            title = GeneratedData.get_new_title()
            body = GeneratedData.get_new_body()
            user_id = GeneratedData.get_new_user_id()
            payload = dumps({
                'title': title,
                'body': body,
                'userId': user_id,
            })
        else:
            payload = dumps(data)
            title = data['title']
            body = data['body']
            user_id = data['user_id']

        response = self.request.patch(post_url, payload, self.headers)
        method = 'PATCH'
        return response, method, title, body, user_id

    def put_body_in_post(self, post_id, data=None):
        post_url = f'{self.base_url}/{post_id}'
        response, method, body = self.__put_unique_body_in_post(post_url, data)
        return response, method, body


    def __put_unique_body_in_post(self, post_url, data=None):
        if data is None:
            body = GeneratedData.get_new_body()
            payload = dumps({
                'body': body,
            })
        else:
            payload = dumps(data)
            body = data['body']

        response = self.request.put(post_url, payload, self.headers)
        method = 'PUT'
        return response, method, body

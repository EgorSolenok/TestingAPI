from utils.generated_data import GeneratedData
from json import dumps, dump


class InvalidData:
    @staticmethod
    def get_invalid_data(): # Didn't manage correct. API-service accepts all structure and values of JSON
        title = GeneratedData.get_new_title()
        body = GeneratedData.get_new_body()
        user_id = GeneratedData.get_new_user_id()
        payload = dumps({
            'title': title,
            'body': body,
            'userId': user_id
        })
        return payload, title, body, user_id


class ValidData:
    @staticmethod
    def get_random_payload():
        title = GeneratedData.get_new_title()
        body = GeneratedData.get_new_body()
        user_id = GeneratedData.get_new_user_id()
        payload = dumps({
            'title': title,
            'body': body,
            'userId': user_id,
        })
        return payload, title, body, user_id

    @staticmethod
    def get_random_body():
        body = GeneratedData.get_new_body()
        payload = dumps({
            'body': body
        })
        return payload, body

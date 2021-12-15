from faker import Faker
from random import randint

class GeneratedData(object):
    GENERATED_TITLE = ''
    GENERATED_BODY = ''
    GENERATED_ID = 0

    @staticmethod
    def get_new_title():
        new_title = Faker().administrative_unit()
        GeneratedData.GENERATED_TITLE = new_title
        return new_title

    @staticmethod
    def get_new_body():
        new_body = Faker().address()
        GeneratedData.GENERATED_BODY = new_body
        return new_body

    @staticmethod
    def get_new_user_id():
        new_user_id = randint(10, 20)
        GeneratedData.GENERATED_ID = new_user_id
        return new_user_id





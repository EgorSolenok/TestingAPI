import requests
from assertpy import assert_that

from utils.project_logger import LogConfig

LogConfig.set_logger_config()


def assert_response_status_code_is_correct(response, method):
    if method == 'POST':
        assert_that(response.status_code).is_equal_to(requests.codes.created)
    if method == 'GET':
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
    if method == 'DELETE':
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
    if method == 'PATCH':
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
    if method == 'PUT':
        assert_that(response.status_code).is_equal_to(requests.codes.ok)


def assert_new_post_have_correct_title(response, given_title):
    assert_that([response.as_dict]).extracting('title').contains(given_title)


def assert_new_post_have_correct_body(response, given_body):
    assert_that([response.as_dict]).extracting('body').contains(given_body)


def assert_new_post_have_correct_user_id(response, given_user_id):
    assert_that([response.as_dict]).extracting('userId').contains(given_user_id)


def assert_body_of_items_is_not_empty(response):
    assert_that(response.as_dict).extracting('body').is_not_empty()


def assert_body_is_empty(response):
    assert_that(response.as_dict).is_empty()


def assert_body_of_single_item_is_not_empty(response):
    assert_that([response.as_dict]).extracting('body').is_not_empty()


def assert_header_have_correct_value(response, name_header, value):
    assert_that(response.headers[name_header]).contains(value)


def assert_post_id_have_correct_value(response, value):
    assert_that(response.as_dict).extracting('postId').contains(value)


def assert_comment_id_have_correct_value(response, value):
    assert_that([response.as_dict]).extracting('id').contains(value)

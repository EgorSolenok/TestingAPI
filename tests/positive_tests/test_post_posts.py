import json

import pytest
from assertpy import soft_assertions
from cerberus import Validator

from clients.jsonplaceholder.post_client import PostClient
from tests.assertions.posts_assertions import *
from tests.helpers.validation_schemes import PostsScheme

client = PostClient()


def test_status_code():
    response, method, _, _, _ = client.create_post()
    assert_response_status_code_is_correct(response, method)


def test_body_is_not_empty():
    response, _, _, _, _ = client.create_post()
    assert_body_of_single_item_is_not_empty(response)


def test_correct_header():
    response, _, _, _, _ = client.create_post()
    assert_header_have_correct_value(response, 'Server', 'cloudflare')


def test_correct_title():
    response, _, title, _, _ = client.create_post()
    assert_new_post_have_correct_title(response, title)


def test_correct_body():
    response, _, _, body, _ = client.create_post()
    assert_new_post_have_correct_body(response, body)


def test_correct_user_id():
    response, _, _, _, user_id = client.create_post()
    assert_new_post_have_correct_user_id(response, user_id)


def test_correct_scheme():
    response, _, _, _, user_id = client.create_post()
    post = json.loads(response.text)
    validator = Validator(PostsScheme.SCHEME, require_all=True)
    is_valid = validator.validate(post)
    assert_that(is_valid, description=validator.errors).is_true()
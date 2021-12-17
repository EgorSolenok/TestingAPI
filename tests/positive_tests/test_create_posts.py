import json

import pytest
from assertpy import soft_assertions
from cerberus import Validator

from clients.jsonplaceholder.post_client import PostClient
from tests.assertions.posts_assertions import *
from tests.helpers.validation_schemes import PostsScheme

@pytest.fixture(scope='module')
def create_post(request):
    client = PostClient()
    response, method, title, body, user_id = client.create_new_post()
    yield dict(response=response, method=method, title=title, body=body, user_id=user_id)

def test_status_code(create_post):
    assert_response_status_code_is_correct(create_post['response'],create_post['method'])


def test_body_is_not_empty(create_post):
    assert_body_of_single_item_is_not_empty(create_post['response'])


def test_correct_header(create_post):
    assert_header_have_correct_value(create_post['response'], 'Server', 'cloudflare')


def test_correct_title(create_post):
    assert_new_post_have_correct_title(create_post['response'], create_post['title'])


def test_correct_body(create_post):
    assert_new_post_have_correct_body(create_post['response'], create_post['body'])


def test_correct_user_id(create_post):
    assert_new_post_have_correct_user_id(create_post['response'], create_post['user_id'])


def test_correct_scheme(create_post):
    post = json.loads(create_post['response'].text)
    validator = Validator(PostsScheme.SCHEME, require_all=True)
    is_valid = validator.validate(post)
    assert_that(is_valid, description=validator.errors).is_true()
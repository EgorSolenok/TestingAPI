import json

import pytest
from assertpy import soft_assertions
from cerberus import Validator

from clients.jsonplaceholder.post_client import PostClient
from tests.assertions.posts_assertions import *
from tests.helpers.validation_schemes import PostsScheme

@pytest.fixture(scope='module')
def all_posts():
    client = PostClient()
    response, method = client.read_all_posts_invalid_endpoint()
    yield dict(response=response, method=method)

@pytest.mark.xfail
def test_status_code(all_posts):
    assert_response_status_code_is_correct(all_posts['response'], all_posts['method'])


@pytest.mark.xfail
def test_body_is_not_empty(all_posts):
    assert_body_of_items_is_not_empty(all_posts['response'])


@pytest.mark.xfail
def test_correct_header(all_posts):
     assert_header_have_correct_value(all_posts['response'], 'Server', 'AWS')

@pytest.mark.xfail
def test_correct_scheme(all_posts):
    posts = json.loads(all_posts['response'].text)
    validator = Validator(PostsScheme.SCHEME, require_all=True)
    is_valid = validator.validate(posts)
    assert_that(is_valid, description=validator.errors).is_true()


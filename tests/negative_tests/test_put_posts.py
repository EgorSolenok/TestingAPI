import json

import pytest
from cerberus import Validator

from clients.jsonplaceholder.post_client import PostClient
from tests.assertions.posts_assertions import *
from tests.helpers.validation_schemes import PostsScheme


@pytest.fixture(scope='module', params=[-10, -1, 0, 101, 102])
def put_body_post(request):
    client = PostClient()
    post_id = request.param
    response, method, body = client.put_body_in_post(post_id)
    yield dict(response=response, method=method, body=body)


@pytest.mark.xfail
def test_status_code(put_body_post):
    assert_response_status_code_is_correct(put_body_post['response'], put_body_post['method'])


@pytest.mark.xfail
def test_body_is_not_empty(put_body_post):
    assert_body_of_single_item_is_not_empty(put_body_post['response'])


@pytest.mark.xfail
def test_correct_header(put_body_post):
    assert_header_have_correct_value(put_body_post['response'], 'Server', 'AWS')


@pytest.mark.xfail
def test_correct_body(put_body_post):
    assert_new_post_have_correct_body(put_body_post['response'], put_body_post['body'])


@pytest.mark.xfail
def test_correct_scheme(put_body_post):
    post = json.loads(put_body_post['response'].text)
    validator = Validator(PostsScheme.PUT_SCHEME, require_all=True)
    is_valid = validator.validate(post)
    assert_that(is_valid, description=validator.errors).is_true()

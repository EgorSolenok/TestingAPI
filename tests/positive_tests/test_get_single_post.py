import json

import pytest
from assertpy import soft_assertions
from cerberus import Validator

from clients.jsonplaceholder.post_client import PostClient
from tests.assertions.posts_assertions import *
from tests.helpers.validation_schemes import PostsScheme


@pytest.fixture(scope='module', params=[post_id for post_id in range(1, 11)])
def single_post(request):
    client = PostClient()
    post_id = request.param
    response, method = client.read_one_post_by_post_id(post_id)
    yield dict(response=response, method=method, post_id=post_id)


def test_single_post_status_code(single_post):
    assert_response_status_code_is_correct(single_post['response'], single_post['method'])


def test_single_post_body_is_not_empty(single_post):
    assert_body_of_single_item_is_not_empty(single_post['response'])


def test_single_post_correct_header(single_post):
    assert_header_have_correct_value(single_post['response'], 'Server', 'cloudflare')


def test_single_post_correct_post_id(single_post):
    assert_comment_id_have_correct_value(single_post['response'], single_post['post_id'])

def test_single_post_correct_scheme(single_post):
    comment = json.loads(single_post['response'].text)
    validator = Validator(PostsScheme.SCHEME, require_all=True)
    is_valid = validator.validate(comment)
    assert_that(is_valid, description=validator.errors).is_true()

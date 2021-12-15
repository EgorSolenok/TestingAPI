import json

import pytest
from assertpy import soft_assertions
from cerberus import Validator

from clients.jsonplaceholder.post_client import PostClient
from tests.assertions.posts_assertions import *
from tests.helpers.validation_schemes import PostsScheme

client = PostClient()

def test_status_code():
    response, method = client.read_all_posts()
    assert_response_status_code_is_correct(response, method)


def test_body_is_not_empty():
    response, _ = client.read_all_posts()
    assert_body_of_items_is_not_empty(response)


def test_correct_header():
    response, _ = client.read_all_posts()
    assert_header_have_correct_value(response, 'Server', 'cloudflare')

def test_correct_scheme():
    response, _ = client.read_all_posts()
    posts = json.loads(response.text)
    validator = Validator(PostsScheme.SCHEME, require_all=True)
    with soft_assertions():
        for post in posts:
            is_valid = validator.validate(post)
            assert_that(is_valid, description=validator.errors).is_true()


@pytest.mark.parametrize('post_id', [_ for _ in range(1, 11)])
def test_single_post_status_code(post_id):
    response, method = client.read_one_post_by_post_id(post_id)
    assert_response_status_code_is_correct(response, method)


@pytest.mark.parametrize('post_id', [_ for _ in range(1, 11)])
def test_single_post_body_is_not_empty(post_id):
    response, method = client.read_one_post_by_post_id(post_id)
    assert_body_of_single_item_is_not_empty(response)


@pytest.mark.parametrize('post_id', [_ for _ in range(1, 11)])
def test_single_post_correct_header(post_id):
    response, method = client.read_one_post_by_post_id(post_id)
    assert_header_have_correct_value(response, 'Server', 'cloudflare')


@pytest.mark.parametrize('post_id', [_ for _ in range(1, 11)])
def test_single_post_correct_post_id(post_id):
    response, method = client.read_one_post_by_post_id(post_id)
    assert_comment_id_have_correct_value(response, post_id)

@pytest.mark.parametrize('post_id', [_ for _ in range(1, 11)])
def test_single_post_correct_scheme(post_id):
    response, _ = client.read_one_post_by_post_id(post_id)
    comment = json.loads(response.text)
    validator = Validator(PostsScheme.SCHEME, require_all=True)
    is_valid = validator.validate(comment)
    assert_that(is_valid, description=validator.errors).is_true()

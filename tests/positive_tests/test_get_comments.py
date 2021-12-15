import pytest
import json

from assertpy import assert_that, soft_assertions
from cerberus import Validator

from clients.jsonplaceholder.post_client import PostClient
from tests.assertions.posts_assertions import *
from tests.helpers.validation_schemes import CommentsScheme

client = PostClient()


@pytest.mark.parametrize('post_id', [_ for _ in range(1, 11)])
def test_comments_status_code(post_id):
    response, method = client.read_all_comments_by_post_id(post_id)
    assert_response_status_code_is_correct(response, method)


@pytest.mark.parametrize('post_id', [_ for _ in range(1, 11)])
def test_comments_body_is_not_empty(post_id):
    response, method = client.read_all_comments_by_post_id(post_id)
    assert_body_of_items_is_not_empty(response)


@pytest.mark.parametrize('post_id', [_ for _ in range(1, 11)])
def test_comments_correct_header(post_id):
    response, method = client.read_all_comments_by_post_id(post_id)
    assert_header_have_correct_value(response, 'Server', 'cloudflare')


@pytest.mark.parametrize('post_id', [_ for _ in range(1, 5)])
def test_comments_correct_post_id(post_id):
    response, method = client.read_all_comments_by_post_id(post_id)
    assert_post_id_have_correct_value(response, post_id)


@pytest.mark.parametrize('post_id', [_ for _ in range(1, 5)])
def test_comments_correct_scheme(post_id):
    response, _ = client.read_all_comments_by_post_id(post_id)
    comments = json.loads(response.text)
    validator = Validator(CommentsScheme.SCHEME, require_all=True)
    with soft_assertions():
        for comment in comments:
            is_valid = validator.validate(comment)
            assert_that(is_valid, description=validator.errors).is_true()



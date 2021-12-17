import json

import pytest
from cerberus import Validator

from clients.jsonplaceholder.post_client import PostClient
from tests.assertions.posts_assertions import *
from tests.helpers.validation_schemes import CommentsScheme


@pytest.fixture(scope='module', params=["/"])
def all_comments(request):
    client = PostClient()
    post_id = request.param
    response, method = client.read_all_comments_by_post_id(post_id)
    yield dict(response=response, method=method, post_id=post_id)


@pytest.mark.xfail
def test_comments_status_code(all_comments):
    print(all_comments['response'])
    assert_response_status_code_is_correct(all_comments['response'], all_comments['method'])


@pytest.mark.xfail
def test_comments_body_is_not_empty(all_comments):
    assert_body_of_items_is_not_empty(all_comments['response'])


@pytest.mark.xfail
def test_comments_correct_header(all_comments):
    assert_header_have_correct_value(all_comments['response'], 'Server', 'AWS')


@pytest.mark.xfail
def test_comments_correct_post_id(all_comments):
    assert_post_id_have_correct_value(all_comments['response'], all_comments['post_id'])


@pytest.mark.xfail
def test_comments_correct_scheme(all_comments):
    comments = json.loads(all_comments['response'].text)
    validator = Validator(CommentsScheme.SCHEME, require_all=True)
    is_valid = validator.validate(comments)
    assert_that(is_valid, description=validator.errors).is_true()

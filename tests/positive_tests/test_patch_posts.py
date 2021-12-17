import json
import pytest
from cerberus import Validator

from clients.jsonplaceholder.post_client import PostClient
from tests.assertions.posts_assertions import *
from tests.helpers.validation_schemes import PostsScheme

@pytest.fixture(scope='module', params=[10])
def patch_post(request):
    client = PostClient()
    post_id = request.param
    response, method, title, body, user_id = client.patch_post(post_id)
    yield dict(response=response, method=method, title=title, body=body, user_id=user_id)


def test_correct_status_code(patch_post):
    assert_response_status_code_is_correct(patch_post['response'],patch_post['method'])

def test_body_is_not_empty(patch_post):
    assert_body_of_single_item_is_not_empty(patch_post['response'])

def test_correct_header(patch_post):
    assert_header_have_correct_value(patch_post['response'], 'Server', 'cloudflare')

def test_correct_title(patch_post):
    assert_new_post_have_correct_title(patch_post['response'], patch_post['title'])

def test_correct_body(patch_post):
    assert_new_post_have_correct_body(patch_post['response'], patch_post['body'])

def test_correct_user_id(patch_post):
    assert_new_post_have_correct_user_id(patch_post['response'], patch_post['user_id'])

def test_correct_scheme(patch_post):
    post = json.loads(patch_post['response'].text)
    validator = Validator(PostsScheme.PATCH_SCHEME, require_all=True)
    is_valid = validator.validate(post)
    assert_that(is_valid, description=validator.errors).is_true()
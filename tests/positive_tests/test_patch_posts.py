import json

from cerberus import Validator

from clients.jsonplaceholder.post_client import PostClient
from tests.assertions.posts_assertions import *
from tests.helpers.validation_schemes import PostsScheme

client = PostClient()

def test_correct_status_code(post_id=10):
    response, method, title, body, user_id = client.patch_post(post_id)
    assert_response_status_code_is_correct(response, method)

def test_body_is_not_empty(post_id=10):
    response, _, _, _, _ = client.patch_post(post_id)
    assert_body_of_single_item_is_not_empty(response)

def test_correct_header(post_id=10):
    response, _, _, _, _ = client.patch_post(post_id)
    assert_header_have_correct_value(response, 'Server', 'cloudflare')

def test_correct_title(post_id=10):
    response, method, title, body, user_id = client.patch_post(post_id)
    assert_new_post_have_correct_title(response, title)

def test_correct_body(post_id=10):
    response, _, _, body, _ = client.patch_post(post_id)
    assert_new_post_have_correct_body(response, body)

def test_correct_user_id(post_id=10):
    response, _, _, _, user_id = client.patch_post(post_id)
    assert_new_post_have_correct_user_id(response, user_id)

def test_correct_scheme(post_id=10):
    response, _, _, _, _ = client.patch_post(post_id)
    post = json.loads(response.text)
    validator = Validator(PostsScheme.PATCH_SCHEME, require_all=True)
    is_valid = validator.validate(post)
    assert_that(is_valid, description=validator.errors).is_true()
import pytest
import json
from assertpy import soft_assertions
from cerberus import Validator
from tests.helpers.validation_schemes import PostsScheme
from utils.print_helpers import pretty_print
from clients.jsonplaceholder.post_client import PostClient
from tests.assertions.posts_assertions import *
client = PostClient()

def test_status_code(post_id=5):
    response, method, body = client.put_body_in_post(post_id)
    assert_response_status_code_is_correct(response, method)


def test_body_is_not_empty(post_id=5):
    response, method, body = client.put_body_in_post(post_id)
    assert_body_of_single_item_is_not_empty(response)


def test_correct_header(post_id=5):
    response, method, body = client.put_body_in_post(post_id)
    assert_header_have_correct_value(response, 'Server', 'cloudflare')


def test_correct_body(post_id=5):
    response, method, body = client.put_body_in_post(post_id)
    assert_new_post_have_correct_body(response, body)

def test_correct_scheme(post_id=5):
    response, _, _ = client.put_body_in_post(post_id)
    post = json.loads(response.text)
    validator = Validator(PostsScheme.PUT_SCHEME, require_all=True)
    is_valid = validator.validate(post)
    assert_that(is_valid, description=validator.errors).is_true()


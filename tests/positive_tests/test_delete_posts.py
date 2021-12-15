import pytest

from utils.print_helpers import pretty_print
from clients.jsonplaceholder.post_client import PostClient
from tests.assertions.posts_assertions import *

client = PostClient()

def test_status_code(post_id=10):
    response, method = client.delete_post_by_id(post_id)
    assert_response_status_code_is_correct(response, method)

def test_body_is_empty(post_id=10):
    response, _ = client.delete_post_by_id(post_id)
    assert_body_is_empty(response)

def test_correct_header(post_id=10):
    response, method = client.delete_post_by_id(post_id)
    assert_header_have_correct_value(response, 'Server', 'cloudflare')

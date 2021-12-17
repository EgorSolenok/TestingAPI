import pytest

from utils.print_helpers import pretty_print
from clients.jsonplaceholder.post_client import PostClient
from tests.assertions.posts_assertions import *




@pytest.fixture(scope='module', params=[10])
def delete_post(request):
    client = PostClient()
    post_id = request.param
    response, method = client.delete_post_by_id(post_id)
    yield dict(response=response, method=method, post_id=post_id)



def test_status_code(delete_post):
    assert_response_status_code_is_correct(delete_post['response'], delete_post['method'])

def test_body_is_empty(delete_post):
    assert_body_is_empty(delete_post['response'])

def test_correct_header(delete_post):
    assert_header_have_correct_value(delete_post['response'], 'Server', 'cloudflare')

import pytest

from utils.print_helpers import pretty_print
from clients.jsonplaceholder.post_client import PostClient
from tests.assertions.posts_assertions import *

client = PostClient()


# @pytest.mark.parametrize('comment_id', [_ for _ in range(1, 10)])
# def test_read_one_comment_by_comment_id(comment_id):
#     response, method = client.read_one_comment_by_comment_id(comment_id)
#     assert_response_status_code_is_correct(response, method)
#     assert_body_of_single_item_is_not_empty(response)
#     assert_header_have_correct_value(response, 'Server', 'cloudflare')
#     assert_comment_id_have_correct_value(response, comment_id)
#     print(type(response.as_dict))
#     pretty_print(response.headers)
#     pretty_print(response.as_dict)
#     pretty_print(response.status_code)
#
# def test_read_all_posts():
#     response, method = client.read_all_posts()
#     assert_response_status_code_is_correct(response, method)
#     assert_body_of_items_is_not_empty(response)
#     assert_header_have_correct_value(response, 'Server', 'cloudflare')
#     pretty_print(response.headers)
#     pretty_print(response.status_code)
#     pretty_print(response.as_dict)

# @pytest.mark.parametrize('post_id', [_ for _ in range(1, 5)])
# def test_read_all_comments_by_post_id(post_id):
#     response, method = client.read_all_comments_by_post_id(post_id)
#     assert_response_status_code_is_correct(response, method)
#     assert_body_of_items_is_not_empty(response)
#     assert_header_have_correct_value(response, 'Server', 'cloudflare')
#     assert_post_id_have_correct_value(response, post_id)
#     pretty_print(response.headers)
#     print(type(response.as_dict)
#     pretty_print(response.status_code)
#     pretty_print(response.as_dict)

# def test_new_post_can_be_added():
#     response, method, title, body, user_id = client.create_post()
#     assert_response_status_code_is_correct(response, method)
#     assert_body_of_single_item_is_not_empty(response)
#     assert_header_have_correct_value(response, 'Server', 'cloudflare')
#     assert_new_post_have_correct_title(response, title)
#     assert_new_post_have_correct_body(response, body)
#     assert_new_post_have_correct_user_id(response, user_id)
#     print(response.as_dict)
#     print(response.status_code)
#     print(response.headers)

def test_read_all_posts_check_status_code_equal_200():
    response, method = client.read_all_posts()
    assert_response_status_code_is_correct(response, method)


def test_read_all_posts_check_body_is_not_empty():
    response, _ = client.read_all_posts()
    assert_body_of_items_is_not_empty(response)


def test_correct_header():
    response, _ = client.read_all_posts()
    assert_header_have_correct_value(response, 'Server', 'cloudflare')


@pytest.mark.parametrize('post_id', [_ for _ in range(1, 11)])
def test_read_all_comments_by_post_id_check_status_code_equal_200(post_id):
    response, method = client.read_all_comments_by_post_id(post_id)
    assert_response_status_code_is_correct(response, method)


@pytest.mark.parametrize('post_id', [_ for _ in range(1, 11)])
def test_read_all_comments_by_post_id_check_body_is_not_empty(post_id):
    response, method = client.read_all_comments_by_post_id(post_id)
    assert_body_of_items_is_not_empty(response)


@pytest.mark.parametrize('post_id', [_ for _ in range(1, 11)])
def test_read_all_comments_by_post_id_check_header_have_correct_value(post_id):
    response, method = client.read_all_comments_by_post_id(post_id)
    assert_header_have_correct_value(response, 'Server', 'cloudflare')


@pytest.mark.parametrize('post_id', [_ for _ in range(1, 5)])
def test_read_all_comments_by_post_id_check_actual_post_id_equal_expected_id(post_id):
    response, method = client.read_all_comments_by_post_id(post_id)
    assert_post_id_have_correct_value(response, post_id)


@pytest.mark.parametrize('comment_id', [_ for _ in range(1, 10)])
def test_read_one_comment_by_comment_id_check_status_code_equal_200(comment_id):
    response, method = client.read_one_comment_by_comment_id(comment_id)
    assert_response_status_code_is_correct(response, method)


@pytest.mark.parametrize('comment_id', [_ for _ in range(1, 10)])
def test_read_one_comment_by_comment_id_check_body_is_not_empty(comment_id):
    response, method = client.read_one_comment_by_comment_id(comment_id)
    assert_body_of_single_item_is_not_empty(response)


@pytest.mark.parametrize('comment_id', [_ for _ in range(1, 10)])
def test_read_one_comment_by_comment_id_check_header_have_correct_value(comment_id):
    response, method = client.read_one_comment_by_comment_id(comment_id)
    assert_header_have_correct_value(response, 'Server', 'cloudflare')


@pytest.mark.parametrize('comment_id', [_ for _ in range(1, 10)])
def test_read_one_comment_by_comment_id_check_comment_id_equal_expected(comment_id):
    response, method = client.read_one_comment_by_comment_id(comment_id)
    assert_comment_id_have_correct_value(response, comment_id)


def test_new_post_can_be_added_check_status_code_equal_200():
    response, method, _, _, _ = client.create_post()
    assert_response_status_code_is_correct(response, method)


def test_new_post_can_be_added_check_body_is_not_empty():
    response, _, _, _, _ = client.create_post()
    assert_body_of_single_item_is_not_empty(response)


def test_new_post_can_be_added_header_have_correct_value():
    response, _, _, _, _ = client.create_post()
    assert_header_have_correct_value(response, 'Server', 'cloudflare')


def test_new_post_can_be_added_check_actual_title_equal_expected():
    response, _, title, _, _ = client.create_post()
    assert_new_post_have_correct_title(response, title)


def test_new_post_can_be_added_check_actual_body_equal_expected():
    response, _, _, body, _ = client.create_post()
    assert_new_post_have_correct_body(response, body)


def test_new_post_can_be_added_check_actual_user_id_equal_expected():
    response, _, _, _, user_id = client.create_post()
    assert_new_post_have_correct_user_id(response, user_id)

def test_post_can_be_deleted_check_status_code_is_correct(post_id=10):
    response, method = client.delete_post_by_id(post_id)
    assert_response_status_code_is_correct(response, method)

def test_post_can_be_deleted_check_body_is_empty(post_id=10):
    response, _ = client.delete_post_by_id(post_id)
    assert_body_is_empty(response)

def test_post_can_be_deleted_(post_id=10):
    response, method = client.delete_post_by_id(post_id)

def test_post_can_be_deleted(post_id=10):
    response, method = client.delete_post_by_id(post_id)
    assert_response_status_code_is_correct(response, method)
    assert_body_is_empty(response)
    assert_header_have_correct_value(response, 'Server', 'cloudflare')


def test_post_can_be_updated(post_id=10):
    response, method, title, body, user_id = client.patch_post(post_id, data=None)
    assert_response_status_code_is_correct(response, method)
    assert_body_of_single_item_is_not_empty(response)
    assert_header_have_correct_value(response, 'Server', 'cloudflare')
    assert_new_post_have_correct_title(response, title)
    assert_new_post_have_correct_body(response, body)
    assert_new_post_have_correct_user_id(response, user_id)

    # pretty_print(response.headers)
    # print(type(response.as_dict))
    # pretty_print(response.status_code)


def test_body_can_be_updated_in_post(post_id=5):
    response, method, body = client.put_body_in_post(post_id, data=None)
    assert_response_status_code_is_correct(response, method)
    assert_body_of_single_item_is_not_empty(response)
    assert_header_have_correct_value(response, 'Server', 'cloudflare')
    assert_new_post_have_correct_body(response, body)

    pretty_print(response.headers)
    pretty_print(response.as_dict)
    pretty_print(response.status_code)

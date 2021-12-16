import pytest
import allure
import os
import pytest

from utils.file_reader import read_file


@pytest.fixture
def create_data():
    payload = read_file('create_person.json')
    title = payload['title']
    body = payload['body']
    user_id = payload['userId']
    yield payload


def pytest_addoption(parser):
    parser.addoption('--user',
                     action='store',
                     default='None',
                     help="Set a username"
                     )
    parser.addoption('--password',
                     action='store',
                     default='None',
                     help="Set a password"
                     )


@pytest.fixture()
def user(request):
    user = request.config.getoption("user")
    return user


@pytest.fixture()
def password(request):
    password = request.config.getoption("password")
    return password


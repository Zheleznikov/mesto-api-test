import pytest

from client import signin


@pytest.fixture(scope="session", autouse=True)
def token():
    """
    Пример фиксуры с получением токена
    """
    return signin().json()['token']


@pytest.fixture(scope="session", autouse=True)
def token_and_id_base():
    """
    Пример фиксуры с присвоением значения внутри
    """
    rs = signin().json()
    token = rs['token']
    user_id = rs['user']['_id']
    return token, user_id
    # return rs['token'], rs['user']['_id']


@pytest.fixture(scope="session", autouse=True)
def token_and_id():
    """
    Пример фиксуры с получением токена и айди
    """
    rs = signin().json()
    return rs['token'], rs['user']['_id']



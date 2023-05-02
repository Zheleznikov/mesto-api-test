import pytest

from client import signin


@pytest.fixture(scope="session", autouse=True)
def token():
    return signin().json()['token']
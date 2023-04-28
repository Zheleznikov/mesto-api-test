import requests
from requests import post

from config import HOST, SIGNIN, CARDS
from data import USER_EMAIL, USER_PASSWORD, CARD_LINK, CARD_NAME


def signin():
    return post(
        url=HOST + SIGNIN,
        json={
            'email': USER_EMAIL,
            'password': USER_PASSWORD
        }
    )


def add_card(token):
    return requests.post(
        url=HOST + CARDS,
        headers={
            'Authorization': 'Bearer ' + token
        },
        json={
            'link': CARD_LINK,
            'name': CARD_NAME
        }
    )
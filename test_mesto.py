from client import signin, add_card


def test_add_card():
    signin_rs = signin()
    token = signin_rs.json()['token']

    add_card_rs = add_card(token)
    card_id = add_card_rs.json()['data']['_id']


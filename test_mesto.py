from client import signin, add_card


def test_add_card(token):
    print('\n token in test 1:\n')
    print(token)

    add_card_rs = add_card(token)
    card_id = add_card_rs.json()['data']['_id']


def test_add_card2(token):
    print('start test2')
    print('\n token in test 2:\n')
    print(token)

    signin_rs = signin()
    token = signin_rs.json()['token']

    add_card_rs = add_card(token)
    card_id = add_card_rs.json()['data']['_id']


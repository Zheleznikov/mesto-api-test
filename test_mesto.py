from client import signin, add_card


def test_add_card(token_and_id):
    """
    Пример теста с использованием фикстуры для получения токена и айди
    """
    token, user_id = token_and_id
    print(token)
    print(user_id)



def test_add_card2(token):
    print('start test2')
    print('\n token in test 2:\n')
    print(token)

    signin_rs = signin()
    token = signin_rs.json()['token']

    add_card_rs = add_card(token)
    card_id = add_card_rs.json()['data']['_id']


# def get_token_and_id():
#     rs = signin().json()
#     token = rs['token']
#     user_id = rs['user']['_id']
#     return token, user_id


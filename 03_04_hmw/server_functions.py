from utils import *

presence_request = {'action': 'probe', 'time': timestr}

response_100 = {'response': 100, 'time': timestr, 'alert': 'Welcome to our server'}

response_400 = {'response': 400, 'time': timestr, 'error': 'Bad request/JSON object'}


def handling_client_msg(client_msg, addr):
    if client_msg['action'] == 'presence':
        if client_msg['user']['account_name']:
            client_data = {'client': {'address': addr, 'account_name': client_msg['user']['account_name']},
                           'message': {'text': client_msg['user']['status'], 'type': client_msg['type'],
                                       'time': client_msg['time']}}
            return response_100
        else:
            return response_400
    else:
        return response_400

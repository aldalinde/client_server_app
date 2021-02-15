from utils import *

presence_request = {'action': 'probe', 'time': timestr}

response_200 = {'response': 200, 'time': timestr, 'alert': 'Welcome to our server_pack'}

response_400 = {'response': 400, 'time': timestr, 'error': 'Bad request/JSON object'}


def handling_client_msg(client_msg, addr):
    if client_msg['action'] == 'presence':
        if client_msg['user']['account_name']:
            client_data = {'client_pack': {'address': addr, 'account_name': client_msg['user']['account_name']},
                           'message': {'text': client_msg['user']['status'], 'type': client_msg['type'],
                                       'time': client_msg['time']}}
            return response_200
        else:
            return response_400
    else:
        return response_400

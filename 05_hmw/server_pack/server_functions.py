from server_utils import *
import logging

presence_request = {'action': 'probe', 'time': timestr}

response_200 = {'response': 200, 'time': timestr, 'alert': 'Welcome to our server_pack'}

response_400 = {'response': 400, 'time': timestr, 'error': 'Bad request/JSON object'}

logg = logging.getLogger('app_serv')


def handling_client_msg(client_msg, addr):
    if client_msg['action'] == 'presence':
        if client_msg['user']['account_name']:
            client_data = {'client_pack': {'address': addr, 'account_name': client_msg['user']['account_name']},
                           'message': {'text': client_msg['user']['status'], 'type': client_msg['type'],
                                       'time': client_msg['time']}}
            logg.info('correct presence message by client')
            return response_200
        else:
            logg.error('no account name given by client, code 400')
            return response_400
    else:
        logg.error('bad JSON object from client, code 400')
        return response_400

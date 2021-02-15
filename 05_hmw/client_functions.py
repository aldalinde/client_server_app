from utils import *
import logging


logger = logging.getLogger('app_cl')

presence_msg = {"action": "presence", "time": timestr, "type": "status",
                "user": {"account_name": "Somebody", "status": "Hello there!"}}


# parsing for message type and acting correspondingly

def parsing_server_msg(s, server_message):
    # sending presence message each time client_pack receives probe action
    if 'action' in server_message.keys():
        if server_message['action'] == 'probe':
            server_response = {'action': 'probe', 'time': server_message['time'],
                               'contents': 'request for presence message', 'type': 'action'}
            # logging INFO
            logger.info('Server action probe. Presence msg request.')
            send_msg(s, presence_msg)
            return server_response, 'action'
        else:
            server_response = {'action': server_message['action'], 'time': server_message['time'],
                               'contents': server_message, 'type': 'action'}
            # logging WARNING
            logger.warning('Server action unknown. See server_response.json')
            return server_response, server_message['action']

    # collecting server_pack responses
    elif 'response' in server_message.keys():
        if server_message['alert']:
            server_response = {'response': server_message['response'], 'time': server_message['time'],
                               'contents': server_message['alert'], 'type': 'alert'}
            # logging INFO

        elif server_message['error']:
            server_response = {'response': server_message['response'], 'time': server_message['time'],
                               'contents': server_message['error'], 'type': 'error'}
            # logging ERROR
        else:
            server_response = {'response': 'unknown', 'time': timestr,
                               'contents': [server_message], 'type': 'unknown'}
            # logging INFO
        return server_response, 'response'

    # collecting and printing unknown messages from server_pack
    else:
        server_response = {'response': 'unknown', 'time': timestr,
                           'contents': [server_message], 'type': 'unknown'}
        # logging ERROR
        return server_response, 'response'




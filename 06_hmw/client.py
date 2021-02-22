# Функции клиента: сформировать presence-сообщение; отправить сообщение серверу; получить ответ сервера;
# разобрать сообщение сервера; параметры командной строки скрипта client_pack.py <addr> [<port>]:
# addr — ip-адрес сервера; port — tcp-порт на сервере, по умолчанию 7777.

from socket import *
from sys import argv
from utils import *
import json
from client_pack.client_log import *
from decorator import log_func_call

log_ger = logging.getLogger('app_cl')

presence_msg = {"action": "presence", "time": timestr, "type": "status",
                "user": {"account_name": "Ho-Ho", "status": "Hello there!"}}

addr, port = get_addr_port(argv, log_ger, './client_pack/configs_client.yaml')


# parsing for message type and acting correspondingly
@log_func_call
def parsing_server_msg(s, server_message):
    # sending presence message each time client_pack receives probe action
    if 'action' in server_message.keys():
        if server_message['action'] == 'probe':
            server_response = {'action': 'probe', 'time': server_message['time'],
                               'contents': 'request for presence message', 'type': 'action'}
            # logging INFO
            log_ger.info('Server action probe. Presence msg request.')
            send_msg(s, presence_msg)
            return server_response, 'action'
        else:
            server_response = {'action': server_message['action'], 'time': server_message['time'],
                               'contents': server_message, 'type': 'action'}
            # logging WARNING
            log_ger.warning('Server action unknown. See server_response.json')
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


def main():

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, int(port)))

    server_responses = []

    # creating json file for future messages from server_pack
    json_file = './client_pack/server_response.json'
    json_file_root_value = 'server_messages'
    with open(json_file, 'w') as json_responses:
        json.dump({json_file_root_value: []}, json_responses)

    while True:
        # receiving messages from server_pack
        msg_in = s.recv(10000)
    # actions if there is incoming message from server_pack
        if msg_in:
            server_message = get_msg(msg_in)

            server_response, msg_type = parsing_server_msg(s, server_message)

            server_responses.append(server_response)
            print(server_response)

            # possibility to collect responses in json file
            msg_to_json(json_file, json_file_root_value, server_response)


if __name__ == '__main__':
    main()

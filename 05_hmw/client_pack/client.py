# Функции клиента: сформировать presence-сообщение; отправить сообщение серверу; получить ответ сервера;
# разобрать сообщение сервера; параметры командной строки скрипта client_pack.py <addr> [<port>]: addr — ip-адрес сервера;
# port — tcp-порт на сервере, по умолчанию 7777.

from client_functions import *
from client_utils import *
from socket import *
from sys import argv
import json


addr, port = get_addr_port(argv, 'configs_client.yaml')

s = socket(AF_INET, SOCK_STREAM)
s.connect((addr, int(port)))

server_responses = []

# creating json file for future messages from server_pack
json_file = 'server_response.json'
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





# Функции клиента: сформировать presence-сообщение; отправить сообщение серверу; получить ответ сервера;
# разобрать сообщение сервера; параметры командной строки скрипта client.py <addr> [<port>]: addr — ip-адрес сервера;
# port — tcp-порт на сервере, по умолчанию 7777.


from utils import *
from socket import *
from sys import argv


# assuming client's parameters are correct and in right order
if len(argv) == 5:
    port = argv[2]
    addr = argv[4]
elif len(argv) == 3:
    if argv[1] == '-p':
        port = argv[2]
        addr = parse_configs('configs_client.yaml')[0]
    elif argv[1] == '-a':
        addr = argv[2]
        port = parse_configs('configs_client.yaml')[1]
else:
    port = parse_configs('configs_client.yaml')[1]
    addr = parse_configs('configs_client.yaml')[0]


s = socket(AF_INET, SOCK_STREAM)
s.connect((addr, int(port)))


presence_msg = {"action": "presence", "time": timestr, "type": "status",
                "user": {"account_name": "Somebody", "status": "Hello there!"}}


server_responses = []
# sending presence message to server
while True:
    msg_in = s.recv(10000)
# actions if there is incoming message from server
    if msg_in:
        server_message = get_msg(msg_in)

# checking which kind of message came and acting correspondingly
        # sending presence message each time client receives probe action
        if 'action' in server_message.keys():
            if server_message['action'] == 'probe':
                # print(server_message)
                send_msg(s, presence_msg)
        # collecting and printing server responses
        elif 'response' in server_message.keys():
            if server_message['alert']:
                server_response = {'response': server_message['response'], 'time': server_message['time'],
                                   'contents': server_message['alert'], 'type': 'alert'}
            elif server_message['error']:
                server_response = {'response': server_message['response'], 'time': server_message['time'],
                                   'contents': server_message['error'], 'type': 'error'}
            else:
                server_response = {'response': 'unknown', 'time': timestr,
                                   'contents': [server_message], 'type': 'unknown'}
            print(server_response)
            server_responses.append(server_response)

        # collecting and printing unknown messages from server
        else:
            server_response = {'response': 'unknown', 'time': timestr,
                               'contents': [server_message], 'type': 'unknown'}

            print(server_response)
            server_responses.append(server_response)

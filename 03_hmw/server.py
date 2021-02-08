# Функции сервера: принимает сообщение клиента; формирует ответ клиенту; отправляет ответ клиенту;
# имеет параметры командной строки: -p <port> — TCP-порт для работы (по умолчанию использует 7777);
# -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).


from utils import *
from socket import *

from sys import argv

# assuming terminal input parameters are correct and in right order
if len(argv) == 5:
    port = argv[2]
    addr = argv[4]
elif len(argv) == 3:
    if argv[1] == '-p':
        port = argv[2]
        addr = parse_configs('configs_server.yaml')[0]
    elif argv[1] == '-a':
        addr = argv[2]
        port = parse_configs('configs_server.yaml')[1]
    else:
        addr = parse_configs('configs_server.yaml')[0]
        port = parse_configs('configs_server.yaml')[1]
else:
    addr = parse_configs('configs_server.yaml')[0]
    port = parse_configs('configs_server.yaml')[1]


s = socket(AF_INET, SOCK_STREAM)
s.bind(('', int(port)))
s.listen(3)


while True:
    client, addr = s.accept()
    print(" от %s" % str(addr))

    presence_request = {'action': 'probe', 'time': timestr}
    send_msg(client, presence_request)

    msg_in = client.recv(10000)
    client_msg = get_msg(msg_in)
    print(client_msg)

    if client_msg['action'] == 'presence':
        if client_msg['user']['account_name']:
            client_data = {'client': {'address': addr, 'account_name': client_msg['user']['account_name']},
                           'message': {'text': client_msg['user']['status'], 'type': client_msg['type'],
                                       'time': client_msg['time']}}
            response = {'response': 100, 'time': timestr,
                        'alert': 'Welcome to our server'}
        else:
            response = {'response': 400, 'time': timestr, 'error': 'Bad request/JSON object'}


    else:
        response = {'response': 400, 'time': timestr, 'error': 'Bad request/JSON object'}

    send_msg(client, response)

    client.close()



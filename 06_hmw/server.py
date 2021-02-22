# Функции сервера: принимает сообщение клиента; формирует ответ клиенту; отправляет ответ клиенту;
# имеет параметры командной строки: -p <port> — TCP-порт для работы (по умолчанию использует 7777);
# -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).

from socket import *
from sys import argv
from utils import *
import time
from server_pack.server_log import *
from decorator import log_func_call


timestr = time.ctime(time.time()) + "\n"
presence_request = {'action': 'probe', 'time': timestr}

response_200 = {'response': 200, 'time': timestr, 'alert': 'Welcome to our server_pack'}

response_400 = {'response': 400, 'time': timestr, 'error': 'Bad request/JSON object'}

logg = logging.getLogger('app_serv')


@log_func_call
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


# creating json file for future messages from clients
'''
json_file = 'client_msg.json'
json_file_root_value = 'client_messages'
json_responses = open(json_file, 'w')
json.dump({json_file_root_value: []}, json_responses)
json_responses.close()
'''
serv_addr, port = get_addr_port(argv, logg, './server_pack/configs_server.yaml')


def main():

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((serv_addr, int(port)))
    s.listen(3)

    while True:
        client, addr = s.accept()

        send_msg(client, presence_request)

        msg_in = client.recv(10000)

        if msg_in:
            client_msg = get_msg(msg_in)
            response = handling_client_msg(client_msg, addr)
            print(response)
            send_msg(client, response)

        client.close()


if __name__ == '__main__':
    main()

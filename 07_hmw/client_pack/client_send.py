# 2. Реализовать функции отправки/приема данных на стороне клиента. Чтобы упростить разработку на данном этапе,
# пусть клиентское приложение будет либо только принимать, либо только отправлять сообщения в общий чат.
# Эти функции надо реализовать в рамках отдельных скриптов.

from sys import argv
from socket import socket, AF_INET, SOCK_STREAM
from client_utils import *


ADDRESS = get_addr_port(argv, 'configs_client.yaml')


def echo_client():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(ADDRESS)
        while True:
            msg = input('Write your message: , "exit" - to exit messenger')
            if msg == 'exit':
                break
            sock.send(msg.encode('utf-8'))
            data = sock.recv(1024).decode('utf-8')
            print('Ответ:', data)


if __name__ == '__main__':
    echo_client()

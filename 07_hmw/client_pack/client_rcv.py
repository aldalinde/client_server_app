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
            data = sock.recv(1024).decode('utf-8')
            print('Сообщение:', data)


if __name__ == '__main__':
    echo_client()

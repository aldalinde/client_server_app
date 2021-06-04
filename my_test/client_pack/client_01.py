# 1. На клиентской стороне реализовать прием и отправку сообщений с помощью потоков в P2P-формате
# (обмен сообщениями между двумя пользователями).

from sys import argv
from socket import socket, AF_INET, SOCK_STREAM
from client_utils import *
from threading import Thread


ADDRESS = get_addr_port(argv, 'configs_client.yaml')

with open('cl_01.txt', 'w') as f:
    f.write('Messages from chat with client_02' + '\n')


def echo_client():
    # function to get input message from client
    def get_message(s):
        while True:
            msg_new = input('')
            if msg_new:
                send_msg(s, msg_new)

    def receive_msg(s):
        while True:
            data = s.recv(1024).decode('utf-8')
            if data:
                with open('cl_01.txt', 'a') as fa:
                    fa.writelines(data + timestr + '\n')
                print(data)

    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(ADDRESS)
        while True:
            # opening thread for writing a new message with timeout 20 sec
            new_msg_thread = Thread(target=get_message, args=(sock,))
            rcv_msg_thread = Thread(target=receive_msg, args=(sock,))

            new_msg_thread.start()
            rcv_msg_thread.start()
            # closing thread every 20 seconds to receive new messages
            new_msg_thread.join()
            rcv_msg_thread.join()



if __name__ == '__main__':
    echo_client()

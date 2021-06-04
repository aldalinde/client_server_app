import threading
from socket import socket, AF_INET, SOCK_STREAM

address = ('localhost', 7777)


def client_send_message():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(address)
        while True:
            msg = input('')
            if msg:
                sock.send(msg.encode('utf-8'))


def client_get_message():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(address)
        while True:
            data = sock.recv(1024).decode('utf-8')
            if data:
                print(f'\nmessage: {data}')


if __name__ == '__main__':
    csm = threading.Thread(target=client_send_message)
    cgm = threading.Thread(target=client_get_message)
    csm.daemon = True
    cgm.daemon = True
    csm.start()
    cgm.start()
    csm.join()
    cgm.join()

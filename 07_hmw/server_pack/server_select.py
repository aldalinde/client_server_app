# 1. Реализовать обработку нескольких клиентов на сервере, используя функцию select.
# Клиенты должны общаться в «общем чате»: каждое сообщение участника отправляется всем, подключенным к серверу.

from server_utils import *
import select
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv
import json


def read_requests(r_clients, all_clients):
    responses = {} # Словарь ответов сервера вида {сокет: запрос}
    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)
    return responses


def write_responses(requests, w_clients, all_clients):
    for sock in w_clients:
        if sock in requests:
            resp = requests[sock].encode('utf-8')
            for cl in w_clients:
                try:
                    cl.send(resp.upper())
                except:
                    print('Клиент {} {} отключился'.format(cl.fileno(), cl.getpeername()))
                    cl.close()
                    all_clients.remove(cl)


def mainloop():
    address = get_addr_port(argv, 'configs_server.yaml')
    clients = []
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(1)
    with open('msgs.json', 'w') as f_n:
        json.dump({'messages': []}, f_n, indent=4)

    while True:
        try:
            conn, addr = s.accept()
            print(conn)
        except OSError:
            pass
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            clients.append(conn)
        finally:
            wait = 10
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)

            except:
                pass  # Ничего не делать, если какой-то клиент отключился
            requests = read_requests(r, clients)  # Сохраним запросы клиентов
            if requests:
                write_responses(requests, w, clients)  # Выполним отправку ответов клиентам


print('Эхо-сервер запущен!')
mainloop()

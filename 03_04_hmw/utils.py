# 1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
# клиент отправляет запрос серверу;
# сервер отвечает соответствующим кодом результата. Клиент и сервер должны быть реализованы в виде отдельных скриптов,
# содержащих соответствующие функции.
import yaml
import json
import time


# assuming terminal input parameters are correct and in right order
def get_addr_port(argv, config_file):
    if len(argv) == 5:
        port = argv[4]
        addr = argv[2]
    elif len(argv) == 3:
        if argv[1] == '-p':
            port = argv[2]
            addr = parse_configs(config_file)[0]
        elif argv[1] == '-a':
            addr = argv[2]
            port = parse_configs(config_file)[1]
    else:
        port = parse_configs(config_file)[1]
        addr = parse_configs(config_file)[0]

    return addr, port


# parsing config files to get address and port
def parse_configs(file_name):
    with open(file_name, encoding='utf-8') as y:
        y_content = yaml.load(y, Loader=yaml.Loader)
    return y_content['addr'], y_content['port']



def get_msg(msg_in):
    json_in = json.loads(msg_in)
    return json_in


def send_msg(destination_host, msg):
    g = json.dumps(msg)
    destination_host.send(g.encode('utf-8'))


timestr = time.ctime(time.time()) + "\n"




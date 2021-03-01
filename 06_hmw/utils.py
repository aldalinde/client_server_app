# 1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
# клиент отправляет запрос серверу;
# сервер отвечает соответствующим кодом результата. Клиент и сервер должны быть реализованы в виде отдельных скриптов,
# содержащих соответствующие функции.
import yaml
import json
import time
from decorator import log_func_call


# assuming terminal input parameters are correct and in right order
@log_func_call
def get_addr_port(argv, logg, config_file):

    if '-p' in argv:
        try:
            if int(argv[argv.index('-p')+1]):

                if not 1024 <= int(argv[argv.index('-p')+1]) <= 65535:
                    raise ValueError
                else:
                    port = argv[argv.index('-p')+1]

            else:
                raise ValueError
        except ValueError:
            print('PORT type must be int with value from 1024 to 65535, default values taken')
            port = parse_configs(config_file)[1]
            # logging WARNING
            logg.warning('PORT type must be int with value from 1024 to 65535, default values taken')
    else:
        port = parse_configs(config_file)[1]
        # logging INFO
        logg.info('default PORT value implemented')

    if '-a' in argv:
        addr = argv[argv.index('-a')+1]
    else:
        addr = parse_configs(config_file)[0]
        # logging INFO
        logg.info('default ADDR value implemented')

    return addr, port



# parsing config files to get address and port
def parse_configs(file_name):
    with open(file_name, encoding='utf-8') as y:
        y_content = yaml.load(y, Loader=yaml.Loader)
    return y_content['addr'], y_content['port']


@log_func_call
def get_msg(msg_in):
    json_in = json.loads(msg_in)
    return json_in


def send_msg(destination_host, msg):
    g = json.dumps(msg)
    destination_host.send(g.encode('utf-8'))


# function collecting messages to json
def msg_to_json(filename, root_value, message):
    with open(filename) as f:
        data = json.load(f)
        temp = data[root_value]
        temp.append(message)
    with open(filename, 'w') as new_f:
        json.dump(data, new_f, indent=4)


timestr = time.ctime(time.time()) + "\n"



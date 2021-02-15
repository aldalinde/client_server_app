# 3. Реализовать применение созданных логгеров для решения двух задач:
# Журналирование обработки исключений try/except.
# Вместо функции print() использовать журналирование и обеспечить вывод служебных сообщений в лог-файл;
# Журналирование функций, исполняемых на серверной и клиентской сторонах при работе мессенджера.
import yaml
import json
import time


# parsing config files to get address and port
def parse_configs(file_name):
    with open(file_name, encoding='utf-8') as y:
        y_content = yaml.load(y, Loader=yaml.Loader)
    return y_content['addr'], y_content['port']


# assuming terminal input parameters are correct and in right order
def get_addr_port(argv, config_file):

    if '-p' in argv:
        try:
            if type(argv[argv.index('-p')+1]) == int:
                if not 1024 >= argv[argv.index('-p')+1] >= 65535:
                    raise ValueError
                else:
                    port = argv[argv.index('-p')+1]

            else:
                raise ValueError
        except ValueError:
            print('PORT type must be int with value from 1024 to 65535, default values taken')
            port = parse_configs(config_file)[1]
            # logging WARNING
    else:
        port = parse_configs(config_file)[1]
        # logging INFO

    if '-a' in argv:
        addr = argv[argv.index('-a')+1]
    else:
        addr = parse_configs(config_file)[0]
        # logging INFO

    return addr, port


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




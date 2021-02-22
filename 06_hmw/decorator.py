from server_pack.server_log import *
from client_pack.client_log import *


def log_func_call(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        # if fuction module is client - using client log configuration and path, else - server's
        if func.__module__ == 'client':
            loger = logging.getLogger('app_cl')
        else:
            loger = logging.getLogger('app_serv')
        func_name = func.__name__
        func_module = func.__module__
        print(f'Функция {func_name} вызвана из функции {func_module}')
        loger.info(f'Функция {func_name} вызвана из функции/модуля {func_module}')
        return ret

    return wrapper

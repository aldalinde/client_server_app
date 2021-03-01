from server_pack.server_log import *
from client_pack.client_log import *
import inspect

def log_func_call(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        # if module is client.py - client logs are used; if utils or server - server's
        if str(inspect.getmodule(func))[-6] == 't':
            loger = logging.getLogger('app_cl')
        elif str(inspect.getmodule(func))[-6] == 'r':
            loger = logging.getLogger('app_serv')
        else:
            loger = logging.getLogger('app_serv')
        func_name = func.__name__
        func_module = func.__module__
        print(f'Функция {func_name} вызвана из функции/модуля {func_module}')
        loger.info(f'Функция {func_name} вызвана из функции/модуля {func_module}')
        return ret

    return wrapper

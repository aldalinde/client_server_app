# В каждом модуле выполнить настройку соответствующего логгера по следующему алгоритму:
# Создание именованного логгера;
# Сообщения лога должны иметь следующий формат: "<дата-время> <уровеньважности> <имямодуля> <сообщение>";
# Журналирование должно производиться в лог-файл;
# На стороне сервера необходимо настроить ежедневную ротацию лог-файлов.

import logging.handlers
# from server_utils import *
import logging


logger = logging.getLogger('app_serv')
#  %(asctime)s -10s
log_msg_format = '%(asctime)s %(levelname)-10s %(module)-20s %(message)s'


# 
formatter = logging.Formatter(log_msg_format)

# we'll do rotating log files by max.volume instead of daily rotation for more evident work
file_handler = logging.handlers.RotatingFileHandler('./server_logs/app_serv.log', maxBytes=500, backupCount=2)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

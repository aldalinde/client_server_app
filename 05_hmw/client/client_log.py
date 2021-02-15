# В каждом модуле выполнить настройку соответствующего логгера по следующему алгоритму:
# Создание именованного логгера;
# Сообщения лога должны иметь следующий формат: "<дата-время> <уровеньважности> <имямодуля> <сообщение>";
# Журналирование должно производиться в лог-файл;
from ..utils import *
import logging

logger = logging.getLogger('app_cl')
#  %(asctime)s
log_msg_format = '%(created)f %(levelname)s %(module)s %(message)s'

formatter = logging.Formatter(log_msg_format, timestr)
file_handler = logging.FileHandler('app_cl.log')
file_handler.setLevel(logging.INFO)


logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


# В каждом модуле выполнить настройку соответствующего логгера по следующему алгоритму:
# Создание именованного логгера;
# Сообщения лога должны иметь следующий формат: "<дата-время> <уровеньважности> <имямодуля> <сообщение>";
# Журналирование должно производиться в лог-файл;

import logging

logger = logging.getLogger('app_cl')
#  %(created)f
log_msg_format = '%(asctime)s %(levelname)s %(module)s %(message)s'


# , timestr
formatter = logging.Formatter(log_msg_format)
file_handler = logging.FileHandler('app_cl.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.setLevel(logging.INFO)



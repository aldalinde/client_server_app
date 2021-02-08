# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
# в строковый тип на кириллице.

import chardet
import subprocess

args_list = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for args in args_list:
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line)
        print(line.decode('utf-8'))

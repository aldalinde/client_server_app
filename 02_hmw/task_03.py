# 3. Задание на закрепление знаний по модулю yaml. Написать скрипт,
# автоматизирующий сохранение данных в файле YAML-формата.
# Для этого:
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
# второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
# отсутствующим в кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла
# с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import yaml


test_dict = {'test_list': ['one', 'two', 'three'],
             'test_int': 99,
             'test_d': {'int10€': 10,
                        'int11€': 11}}

with open('file.yaml', 'w', encoding='utf-8') as fn:
    yaml.dump(test_dict, fn, default_flow_style=False, sort_keys=False, allow_unicode=True)

with open('file.yaml', encoding='utf-8') as y:
    y_content = yaml.load(y, Loader=yaml.Loader)
print(y_content)

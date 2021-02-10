# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных
# из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
# Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
# данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения
# параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка
# — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список
# для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных
# в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import re
import csv


def get_data(file_source_list, pattern_list):
    found_patterns_list = []
    for file_source in file_source_list:
        patterns_by_file = []
        for pattern in pattern_list:
            for line in open(file_source, 'rt', encoding='utf-8'):
                if re.findall(pattern, line):
                    patterns_by_file.append(line)
        found_patterns_list.append(patterns_by_file)

    ready_values = []
    for one_file in found_patterns_list:
        list_per_file = []
        for pat in one_file:
            list_per_file.append(''.join(re.findall(r'(\S+\s?\S+)+', re.split(':', pat)[1])))
        ready_values.append(list_per_file)

    # implementing task: "Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка
    # — например, os_prod_list, os_name_list, os_code_list, os_type_list."
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    for item in ready_values:
        os_prod_list.append(item[0])
        os_name_list.append(item[1])
        os_code_list.append(item[2])
        os_type_list.append(item[3])
    os_list = os_prod_list + os_name_list + os_code_list + os_type_list

# return list of future columns; found in files values, ready for csv conversion; found values collected by columns
    return pattern_list, ready_values, os_list


# writing column names and found values to csv file
def write_to_csv(file_source_list, pattern_list, file_destination_name):
    data_columns, data_values, val_grouped_by_column = get_data(file_source_list, pattern_list)
    with open(file_destination_name, 'w', newline='', encoding='utf-8') as fn:
        my_data = [data_columns] + data_values
        fn_write = csv.writer(fn)
        fn_write.writerows(my_data)

# reading data from file
def test_scv(scv_file):
    with open(scv_file, encoding='utf-8') as fn:
        fn_reader = csv.reader(fn)
        fn_header = next(fn_reader)
        return fn_header, list(fn_reader)


my_source_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
my_pattern_list = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
file_destination = 'test_01.csv'



write_to_csv(my_source_list, my_pattern_list, file_destination)

headers, values = test_scv(file_destination)

print(headers)
print(values)


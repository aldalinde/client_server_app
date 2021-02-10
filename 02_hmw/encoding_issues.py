import chardet

from task_1_for_utf8 import *


def encoding_issues(f_source_list):
    for file in f_source_list:
        with open(file, 'rb') as f:
            data = f.read()
            charset = chardet.detect(data)
            print(charset)
        a = data.decode(charset['encoding']).encode('utf-8')

        b = a.decode('utf-8')

        with open(file, 'w', encoding='utf-8', newline='') as fil:
            fil.write(b)
    return fil

source_list = ['inf_1.txt', 'inf_2.txt', 'inf_3.txt']

test_source_list = encoding_issues(source_list)

write_to_csv(my_source_list, my_pattern_list, 'test_02.csv')


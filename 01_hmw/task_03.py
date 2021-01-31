# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

words_list_03 = (b'attribute', b'функция', b'класс', b'type')

for elem in words_list_03:
    print(f'data: {elem}, data type: {type(elem)}, data length: {len(elem)}')
    print()


# SyntaxError: bytes can only contain ASCII literal characters.
# ASCII doesn't contain cyrillic letters => words «класс», «функция» are unsuitable

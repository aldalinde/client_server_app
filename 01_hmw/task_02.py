# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

byte_list_01 = (b'class', b'function', b'method')

for elem in byte_list_01:
    print(f'data: {elem}, data type: {type(elem)}, data length: {len(elem)}')
    print()

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор».


import chardet

f = open('test_file.txt', 'w')
my_str = ['сетевое программирование', 'сокет', 'декоратор']

for line in my_str:
    f.write(line + '\n')

f.close()

# file contents
with open('test_file.txt') as f:
    print(f'File contents:' + '\n'
          f'{f.read()}')

# Проверить кодировку файла по умолчанию.
with open('test_file.txt', 'rb') as f:
    data = f.read()
    charset = chardet.detect(data)
    print(f'File encoding: {charset["encoding"]}' + '\n')


print(f'Data decoded from win codec and encoded by utf-8: {data.decode(charset["encoding"]).encode("utf-8")}' + '\n')

a = data.decode(charset["encoding"]).encode("utf-8")
b = a.decode("utf-8")
print(b)
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

print(f'Script: ' + '\n'
      f'with open("test_file.txt", encoding="utf-8") as f:' + '\n' +
      f'print(f.read())' + '\n' +
      f'gives an error:' + '\n' +
      f'UnicodeDecodeError: "utf-8" codec cant decode byte 0xf1 in position 0: invalid continuation byte' + '\n')

# checking byte contents of the original file to see the part which can't be decoded by utf-8
print(f'Byte contents of the original file: {data}' + '\n')

print(f'Visible "\xf1" in 0 position')

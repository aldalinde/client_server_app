# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

word_list_04 = ['разработка', 'администрирование', 'protocol', 'standard']
enc_list = []
dec_list = []
for word in word_list_04:
    enc_list.append(word.encode())
    dec_list.append(enc_list[word_list_04.index(word)].decode('utf-8'))

print(enc_list)
print(dec_list)
print(dec_list == word_list_04)

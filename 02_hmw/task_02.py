# 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
# цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря
# в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json


def write_order_to_json(item, quantity, price, buyer, date):
    obj_order = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    with open('orders.json') as fn:
        data = json.load(fn)
        temp = data['orders']
        if obj_order in temp:
            pass
        else:
            temp.append(obj_order)
    with open('orders.json', 'w') as fop:
        json.dump(data, fop, indent=4)



order_1 = write_order_to_json('paper white A4 100sh pack', 10, 5.89, 'JSC WAPTEE', '05/19/2020')
order_2 = write_order_to_json('panel 05/69', 18, 27.99, 'JSC WAPTEE', '05/19/2020')
order_3 = write_order_to_json('white paper A4 100sh pack', 6, 5.89, 'GP Carter', '05/19/2020')
order_4 = write_order_to_json('IndependenceDay card 30/71', 29, 1.09, 'GP Carter', '05/19/2020')
order_5 = write_order_to_json('polish transparent 1.2 gal 63/02', 1, 5.89, 'LLC BingDay', '05/19/2020')

with open('orders.json', ) as fn:
    test_obj = json.load(fn)

for key, value in test_obj.items():
    print(key)

    for item in value:
        print(item)

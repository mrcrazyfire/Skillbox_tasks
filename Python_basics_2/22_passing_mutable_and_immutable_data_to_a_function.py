"""Передача изменяемых и неизменяемых данных в функцию"""

import random, copy

#Задача 1. Ошибка
def change_dict(dct):
    dct = copy.deepcopy(dct)
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)


nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}
common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}

change_dict(common_dict)
print(common_dict)


#Задача 2. Непонятно!
data_input = {1 : 2, 2 : 3}

print("Тип данных: {}".format(type(data_input)))
if isinstance(data_input, (list, dict, set, bytearray)):
    print("Изменяемый (mutable)")
else:
    print("Неизменяемый (immutable)")
print("id объекта: {}".format(id(data_input)))


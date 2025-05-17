"""Представление вещественных чисел в программе"""


"""
Задача 1. Возможности компьютера
"""

def min_num():
    number = 1
    count = 0
    save_number = number
    while number:
        save_number = number
        number /= 2
        count += 1

    print(save_number, count)


"""
Задача 2. Тестирование
"""

def test():
    while True:
        # Если мы хотим проверить мантиссу - то нам нужно работать с числом как со строкой, поэтому float к input добавлять пока не будем
        delta = input("Введите число в эксп. форме ")
        # проверка, что мантисса равна числу от 1 до 9
        # сперва получим отдельно часть строки до символа 'e'
        mantissa = ''
        for cipher in delta:
            if cipher == 'e':
                break
            mantissa += cipher
        # получив мантиссу - мы можем проверить, что она удовлетворяет условию (равна числу от 1 до 9)
        # так же мы сразу можем добавить проверку порядка - если порядок отрицательный, то введенное число будет меньше 1, это мы и проверим:
        if 1 <= float(mantissa) <= 9 and float(delta) < 1:
            print('Число введено верно!')
            delta = float(delta)
            break
        else:
            print(
                "Число введено с ошибкой, мантисса всегда должна быть равна числу от 1 до 9, а порядок должен быть меньше нуля")

    start_number = 1
    count = 0
    while start_number <= 2:
        start_number += delta
        count += 1

    print("Кол-во прибавлений: ", count)


"""
Задача 3. Урок информатики
"""

def floating_point_format(n):
    counter = 0
    while n > 10:
        counter += 1
        n /= 10

    text = "Формат плавающей точки: x = " + str(n) + " * 10 ** " + str(counter)
    return text


number = float(input("Введите число: "))
result = floating_point_format(number)
print(result)
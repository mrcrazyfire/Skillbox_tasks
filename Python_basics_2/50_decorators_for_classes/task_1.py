"""Задача 1. Createtime
Реализуйте декоратор класса, который выдаёт дату и время создания,
а также список всех методов объекта класса каждый раз, когда объект класса создаётся в основном коде."""

from datetime import datetime
import time


def create_time(cls):
    def wrapper(*args, **kwargs):
        print(datetime.now())
        for method in dir(cls):
            if not method.startswith("__"):
                print(method)
        return cls(*args, **kwargs)
    return wrapper





@create_time
class MyClass:
    def __init__(self, number):
        self.number = number



    def numbers_sum(self):
        return sum(num for num in range(1, self.number + 1))

    def numbers_milt(self):
        res = 1
        for num in range(1, self.number + 1):
            res *= num
        return res




my_class = MyClass(500)

my_class.numbers_sum()
my_class.numbers_milt()


my_class_2 = MyClass(1000)
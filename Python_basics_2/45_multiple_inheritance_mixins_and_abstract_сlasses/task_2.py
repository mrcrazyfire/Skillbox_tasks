"""
Задача 2. Фигуры
При моделировании компьютерных объектов используются два типа фигур: прямоугольники и квадраты.
Каждая из них имеет координаты XY, длину и ширину.
Также каждая фигура может менять координаты (двигаться) и менять размер.

Реализуйте такие классы.
Учтите, что с точки зрения интерфейса прямоугольник и квадрат — это разные фигуры и работают они по-разному.
В частности, по разному работает метод изменения размера фигуры, так как у квадрата все стороны равны.

Подсказка: чтобы избежать ошибки TypeError при наследовании класса с абстрактным методом,
наследующий класс обязательно должен переопределить этот метод.
"""

from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def resize(self, *args):
        pass

class Rectangle(Figure):
    def __init__(self, x, y, length, width):
        super().__init__(x, y)
        self.length = length
        self.width = width

    def resize(self, new_length, new_width):
        self.length = new_length
        self.width = new_width

    def __str__(self):
        return f"Прямоугольник ({self.x},{self.y}) {self.length}x{self.width}"

class Square(Figure):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def resize(self, new_side):
        self.side = new_side

    def __str__(self):
        return f"Квадрат ({self.x},{self.y}) {self.side}x{self.side}"

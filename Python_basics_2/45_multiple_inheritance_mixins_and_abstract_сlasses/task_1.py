"""
Задача 1. Транспорт
У нас есть парк транспорта. У каждого транспорта есть цвет и скорость,
и каждый умеет двигаться и подавать сигнал. В парке транспорта стоят:

Автомобили. Они могут ездить только по земле.
Лодки. Ездят только по воде.
Амфибии. Могут перемещаться и по земле, и по воде.
Напишите код, который реализует соответствующие классы и методы.
Класс «Транспорт» должен быть абстрактным и содержать абстрактные методы.

Также добавьте класс-примесь, в котором реализован функционал проигрывания музыки. «Замешайте» этот класс в «Амфибию»
"""

from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def signal(self):
        pass


class MusicPlayer:
    def music_on(self):
        print("Включается музыка")

    def music_off(self):
        print("Музыка выключается")


class Car(Transport):
    def move(self):
        print(f"{self.name} начинает ехать")

    def signal(self):
        print(f"{self.name} сигналит")


class Boat(Transport):
    def move(self):
        print(f"{self.name} начинает плыть")

    def signal(self):
        print(f"{self.name} сигналит")

class Amphibian(MusicPlayer, Transport):
    def __init__(self, name, color, road=True):
        super().__init__(name, color)
        self.road = road

    def move(self):
        if self.road:
            print(f"{self.name} начинает ехать")
        else:
            print(f"{self.name} начинает плыть")

    def signal(self):
        print(f"{self.name} сигналит")
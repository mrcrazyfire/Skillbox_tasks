from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0

    @property
    def name(self):
        return self.name()

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def color(self):
        return self.color()

    @color.setter
    def color(self, color):
        self.color = color

    @property
    def speed(self):
        return self.speed

    @speed.setter
    def speed(self, speed):
        self.speed = speed

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
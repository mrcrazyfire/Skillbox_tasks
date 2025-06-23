import random


class MyIterator:
    def __init__(self, count):
        self.__counter = 0
        self.__total = 0
        self.__count = count

    def __iter__(self):
        self.__counter = 0
        self.__total = 0
        return self

    def __next__(self):
        if self.__counter < self.__count:
            self.__counter += 1
            self.__total += random.random()
            return round(self.__total, 2)
        else:
            raise StopIteration


my_iterator = MyIterator(5)

for i in my_iterator:
    print(i)

me_iterator = MyIterator(6)

print("\nНовое кол-во элементов: 6")
for i in me_iterator:
    print(i)

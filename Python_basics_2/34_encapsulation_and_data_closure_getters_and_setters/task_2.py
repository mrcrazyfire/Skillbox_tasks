class Human:
    __count = 0

    def __init__(self, name: str, age: int):
        type(self).__count += 1
        self.name = name
        self.age = age

    @classmethod
    def get_count(cls):
        return cls.__count

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and value.isalpha():
            self.__name = value
        else:
            raise ValueError("Name must be a string containing only letters.")

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int):
        if isinstance(value, int) and 0 <= value < 100:
            self.__age = value
        else:
            raise ValueError("Age must be a positive integer from 0 to 99.")

    def __str__(self):
        return f"{self.name} ({self.age})"

human = Human("John", 18)
print(human)
print(human.name)
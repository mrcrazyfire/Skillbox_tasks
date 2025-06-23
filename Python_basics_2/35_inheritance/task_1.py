class Car:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"Модель автомобиля: {self.model}"

    def run(self):
        print("Автомобиль начинает ехать.")


class Truck(Car):
    def __init__(self, model):
        super().__init__(model)
        self.trunk_capacity = 0

    def load_truck(self, value):
        print("Загружаем багажник.")
        self.trunk_capacity += value
        print(f"Текущая загруженность багажника: {self.trunk_capacity}")

    def unload_truck(self, value):
        if self.trunk_capacity != 0:
            print("Разгружаем багажник.")
            self.trunk_capacity -= value
        else:
            print("Багажник пустой!")


class PassengerCar(Car):
    def __init__(self, model, navigator):
        super().__init__(model)
        self.navigator = navigator

    @staticmethod
    def on_navigator():
        print("Навигатор включен.")

    @staticmethod
    def off_navigator():
        print("Навигатор выключен.")



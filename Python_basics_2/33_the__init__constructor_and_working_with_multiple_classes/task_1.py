class Car:
    def __init__(self, color, price, max_speed = 200, speed = 0):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.speed = speed

    def info(self):
        print(f"Color: {self.color}"
              f"\nPrice: {self.price}"
              f"\nMax Speed: {self.max_speed}"
              f"\nCurrent Speed: {self.speed}")

    def current_speed(self, speed):
        self.speed = speed

car = Car("red", 100)

car.info()

car.current_speed(120)

car.info()


import random

class Toyota:
    color = "red"
    price = 1_000_000
    max_speed = 200
    current_speed = 0


car_1 = Toyota()
car_2 = Toyota()
car_3 = Toyota()

car_1.current_speed = random.randint(0, 200)
car_2.current_speed = random.randint(0, 200)
car_3.current_speed = random.randint(0, 200)


print(car_1.current_speed)
print(car_2.current_speed)
print(car_3.current_speed)

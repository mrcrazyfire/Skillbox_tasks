def infinite_counter():
    number = 0
    while True:
        yield number
        number += 1


for i in infinite_counter():
    print(i)
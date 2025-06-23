def number_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            for number in line.strip().split():
                yield float(number)

total = sum(number_generator('numbers.txt'))
print("Сумма чисел в файле:", total)

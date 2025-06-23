class MyException(Exception):
    pass



with open("numbers.txt", 'r') as numbers:
        for line in numbers:
            parts = line.strip().split()
            num1 = float(parts[0])
            num2 = float(parts[1])
            if num1 < num2:
                raise MyException("Моя ошибка!")
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")

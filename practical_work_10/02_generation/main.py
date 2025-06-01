N = int(input("Введите длину списка: "))

nums = [1 if num % 2 == 0 else num % 5 for num in range(0, N)]

print(nums)
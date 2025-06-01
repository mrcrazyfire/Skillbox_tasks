text = input("Введите текст: ")
vowels = "аеёиоуыэюя"

letters = [char for char in text if char in vowels]

print(f"Список гласных букв: {letters}")
print(f"Длинна списка {len(letters)}")

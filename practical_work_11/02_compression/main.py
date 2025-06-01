text = "aaAAbbсaaaA"
encoded = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        encoded += text[i - 1] + str(count)
        count = 1

encoded += text[-1] + str(count)  # Добавляем последний символ

print(encoded)
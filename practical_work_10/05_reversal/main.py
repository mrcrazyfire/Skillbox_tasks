text = input("Введите строку: ")

first_h = text.index("h")
last_h = text.rindex("h")

reversed_text = text[first_h + 1: last_h][::-1]

print("Развёрнутая последовательность между первым и последним h:", reversed_text)

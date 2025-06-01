def encrypt(text, shift):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    encrypted_text = ""

    for char in text:
        if char in alphabet:
            index = (alphabet.index(char) + shift) % len(alphabet)
            encrypted_text += alphabet[index]
        else:
            encrypted_text += char

    return encrypted_text


message = input("Введите сообщение: ")
K = int(input("Введите сдвиг: "))

encrypted_message = encrypt(message, K)

print(encrypted_message)

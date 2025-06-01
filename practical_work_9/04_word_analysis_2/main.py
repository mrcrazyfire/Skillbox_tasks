def is_palindrome(text):
    for index in range(0, len(word)):
        if text[index] != text[len(word) - index - 1]:
            return False
    return True


word = input("Введите слово: ")

if is_palindrome(word):
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")

"""
Задача 2. Логирование
Возможно, вы замечали, что некоторые программы не просто выдают ошибку и закрываются,
но и записывают эту ошибку в файл. Таким образом проще сформировать отчёт об ошибках,
а значит, программисту будет проще их исправить. Это называется логированием ошибок.

Дан файл words.txt, в котором построчно записаны слова. Необходимо определить количество слов,
из которых можно получить палиндром (привет предыдущим модулям). Если в строке встречается число,
то программа выдаёт ошибку ValueError и записывает эту ошибку в файл errors.log
"""
def is_palindrome(text):
    text = text.lower().replace(' ', '')  # убираем пробелы и приводим к нижнему регистру
    return text == text[::-1]


def count_palindromes(input_filename):
    count_words = 0

    with open(input_filename, 'r') as input_file:
        for line in input_file:
            try:
                word = line.strip()
                if word.isdigit():
                    raise ValueError("Обнаружено число.")
                if is_palindrome(word):
                    count_words += 1
            except ValueError:
                with open("errors.log", 'w', encoding="utf-8") as error_log:
                    error_log.write("Обнаружено число " + word + '\n')
                raise

    return count_words

palindromes = count_palindromes("words.txt")


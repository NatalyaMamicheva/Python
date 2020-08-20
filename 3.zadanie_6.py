import re
# Вывод одного слова
def int_func(words):
    up_words = [word for word in words if word.isupper()]
    len_words = len(set(words.split()))
    lat = re.search(r"[а-я]", words)
    if up_words:
        print("Ошибка! Можно вводить слова только с маленькой буквы!")
    elif lat:
        print("Ошибка! Вводим слово, используя только латинские буквы!")
    elif len_words > 1:
        print("Ошибка! Можно ввести только одно слово!")
    else:
        print(words.title())

int_func(input("Через пробел введите слово, используя маленькие латинские буквы: "))

# Вывод нескольких слов в строку
def int_func(letters):
    up_letters = [letter for letter in letters if letter.isupper()]
    lat = re.search(r"[а-я]", letters)
    if up_letters:
        print("Ошибка! Можно вводить слова только с маленькой буквы!")
    elif lat:
        print("Ошибка! Вводим слова, используя только латинские буквы!")
    else:
        print(letters.title())

int_func(input("Через пробел введите слова, используя маленькие латинские буквы: "))


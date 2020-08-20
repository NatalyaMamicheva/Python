# Вывод одного словв
def int_func(words):
    up_words = [word for word in words if word.isupper()]
    len_words = len(set(words.split()))
    if up_words:
        print("Ошибка! Можно вводить слова только с маленькой буквы!")
    elif len_words > 1:
        print("Ошибка! Можно ввести только одно слово!")
    else:
        print(words.title())

int_func(input("Через пробел введите слово, которое начинается с маленькой буквы: "))

# Вывод нескольких слов в строку
def int_func(letters):
    up_letters = [letter for letter in letters if letter.isupper()]
    if up_letters:
        print("Ошибка! Можно вводить слова только с маленькой буквы!")
    else:
        print(letters.title())

int_func(input("Через пробел введите слова, которые начинаются с маленькой буквы: "))

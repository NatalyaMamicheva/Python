def information(**kwargs):
    return " ".join(kwargs.values())

print(information(name=input("Введите свое имя: "), surname=input("Введите свою фамилию: "),
                  year=input("Введите свой год рождения: "), city=input("Введите свой город проживания: "),
                  email=input("Введите свою почту: "), telephone=input("Введите свой номер телефона: ",)))
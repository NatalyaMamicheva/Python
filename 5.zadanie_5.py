def summa():
    try:
        with open("number.txt", 'w+', encoding="utf-8") as f_obj:
            number = input("Введите числа через пробел:\n")
            f_obj.writelines(number)
            sum_num = sum(map(int, number.split()))
            print(f"Сумма введенных Вами чисел = {sum_num}")
    except IOError:
        print("Ошибка в файле!")
    except ValueError:
        print("Введите числа через пробел!")
summa()

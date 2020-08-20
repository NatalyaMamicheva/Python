def division_num(num1, num2):
    try:
        result = int(num1) / int(num2)
        print(f"Результат деления первого числа на второе = {result:.3f}")

    except ValueError:
        print("Некоррекктное значение! Введите число!")

    except ZeroDivisionError:
        print("Ошибка! На ноль делить нельзя!")

division_num(input("Введите первое число: "), input("Введите второе число: "))
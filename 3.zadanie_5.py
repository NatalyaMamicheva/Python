def summa_num():
    sum_sum_2 = 0
    result = True
    while result == True:
        numbers = input('Введите только числа с пробелами и в конце нажмите Enter или нажмите q для выхода: ')
        try:
            sum_sum = sum((float(number) for number in numbers.split()))
            print(f"Сумма этих чисел равна {sum_sum}")
            sum_sum_2 = sum_sum_2 + sum_sum
            print(f"Сумма всех чисел равна {sum_sum_2}")
        except:
            for number in range(len(numbers)):
                if numbers[number] == 'q' or numbers[number] == 'Q':
                    print(f"До свидания!")
                    result = False
                    break
                else:
                    print("Некорректно введены данные! Здесь присутствует что-то кроме чисел или же чисел нет совсем!")
                    break

            print(f"Сумма всех чисел равна {sum_sum_2}")


summa_num()
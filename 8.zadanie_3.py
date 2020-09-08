class MyException(Exception):
    sps = []
    result = True
    while result == True:
            numbers = input('Введите только числа с пробелами и в конце нажмите Enter. Или нажмите q для выхода и вывода на экран введенного списка чисел: ')
            try:
                num = (int(number) for number in numbers.split())
                for i in num:
                    sps.append(i)
            except Exception as e:
                for number in range(len(numbers)):
                    if numbers[number] == 'q' or numbers[number] == 'Q':
                        print(f"До свидания!")
                        result = False
                        break
                    else:
                        print("Некорректно введены данные! Здесь присутствует что-то кроме чисел или же чисел нет совсем!")
                        break
M = MyException()
print(f"Список чисел: {M.sps}")
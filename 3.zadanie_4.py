#Вариант 1
def my_func(x, y):
    if x < 0 or y > 0:
        return "Ошибка! Внимательно читайте условие!"
    else:
        result = x ** y
        return result

print(my_func(float(input("Введите действительное положительное число x: ")), int(input("Введите второе целое отрицательное число y: "))))

#Вариант 2
def my_func2(x, y):
    while True:
        if x < 0 or y > 0:
            print("Ошибка! Внимательно читайте условие!")
            break
        elif y == 0:
            print(1)
            break
        else:
            print(x * (x ** (y - 1)))
            break

my_func2(float(input("Введите действительное положительное число x: ")), int(input("Введите второе целое отрицательное число y: ")))
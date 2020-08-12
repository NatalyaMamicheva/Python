name = input("Введите свое имя: ")
print(f"Здравствуйте, {name}. Вы можете воспользоваться этим калькулятором!")

while True:
    number_1 = float(input("Введите первое число: "))
    number_2 = float(input("Введите второе число: "))

    calculator = input("Выберите действие:  - + * /   q-выход из калькулятора:  ")

    if calculator == "q":
        print(f"{name}, спасибо, что воспользовались этим калькулятором! До встречи!")
        break

    elif calculator == "+":
        print(f" {number_1} + {number_2} = {number_1 + number_2}")

    elif calculator == "-":
        print(f" {number_1} - {number_2} = {number_1 - number_2}")

    elif calculator == "*":
        print(f" {number_1} * {number_2} = {number_1 * number_2}")

    elif calculator == "/":
        print(f" {number_1} / {number_2} = {number_1 / number_2}")

    else:
        print("Неизвестная операция")

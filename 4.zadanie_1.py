from sys import argv
def script():
    script_name, first_param, second_param, third_param = argv

    try:
        first_param = int(first_param)
        second_param = int(second_param)
        third_param = int(third_param)
        result = (first_param * second_param) + third_param
        print("Имя скрипта: ", script_name)
        print("Выработка в часах: ", first_param)
        print("Ставка в час: ", second_param)
        print("Премия: ", third_param)
        print(f'Заработная плата сотрудника: {result}')

    except ValueError:
        print("Вы вводите не числа!")

script()
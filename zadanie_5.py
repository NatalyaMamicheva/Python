revenue = int(input("Введите количество выручки фирмы: "))
cost = int(input("Введите количество издержек фирмы: "))

profit = revenue - cost

if revenue > cost:
    print("Фирма работает без убытков")

    efficiency = profit / revenue
    print(f"Рентабельность выручки составляет {efficiency}%")

    staff = int(input("Введите численность сотрудников фирмы: "))
    profit_staff = int(profit / staff)
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет {profit_staff} рублей")

else:
    print("Фирма работает без прибыли")
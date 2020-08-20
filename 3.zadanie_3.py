def my_func(x, y, z):
    three = [x, y, z]
    three.remove(min(three))
    result = sum(three)
    print(f"Сумма максимальных чисел = {result}")

my_func(9, 2, 15)
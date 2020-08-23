from functools import reduce
#Вариант 1

def my_func(prev_el, el):
    return prev_el * el

print(reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0]))

#Вариант 2

def my_func(prev_el, el):
    return prev_el * el

print(reduce(my_func, range(100, 1001, 2)))


#Вариант 1
from itertools import count
from math import factorial

def fact(n):
    for el in count(1):
        yield factorial(el)

print(fact(5))

n = 0
for i in fact(n):
    if n < 5:
        print(i)
        n += 1
    else:
        break

#Вариант 2
fac_l = 5
print(f"Факториал {fac_l} = {factorial(fac_l)}")
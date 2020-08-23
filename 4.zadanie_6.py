#Вариант 1
"""
count = list(range(7, 11))
cycle = "ABC"

for x in count:
    print(x)
for x in cycle:
    print(x)

"""

#Вариант 2
"""

from itertools import cycle

count = list(range(7, 11))
progr_lang = ("A", "B", "C", "\n".join(map(str, count)))
iter = cycle(progr_lang)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter)) 

"""

#Вариант 3
from itertools import count

for el in count(7):
    if el > 10:
        break
    else:
        print(el)

from itertools import cycle

c = 0
for el in cycle("ABC"):
    if c > 4:
        break
    print(el)
    c += 1
elements = [element for element in input('Введите элементы списка через пробел и в конце нажмите Enter: ').split()]
print(elements)
i = 0
for element in range(int(len(elements) / 2)):
    elements[i], elements[i + 1] = elements[i + 1], elements[i]
    i += 2

print(elements)
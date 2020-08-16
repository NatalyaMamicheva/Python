string = [el for el in input('Введите строку из нескольких слов, разделённых пробелами. В конце нажмите Enter: ').split()]

for i, el in enumerate(string, 1):
        print(i, el[0:10])
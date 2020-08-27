#Задание 1

with open("data.txt", 'w+', encoding="utf-8") as f_obj:
    information = input("Введите данные: " )
    new_information = information + "\n"

    while information:
        if information == None:
            break
        else:
            f_obj.writelines(new_information)
            information = input("Введите данные: ")
            new_information = information + "\n"

#Задание 2
    f_obj.seek(0)
    lines = f_obj.readlines()
    print(f"Количество строк в файле: {len(lines)}")

    for i, line in enumerate(lines):
        word = len(line.split())
        print(f"Количество слов {i + 1}-ой строки: {word}")
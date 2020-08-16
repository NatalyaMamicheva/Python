hello = input("Здравствуйте! Вы хотите приобрести товар? Да/Нет: ")
while True:
    if hello == "Нет":
        print("До скорых встреч!")
        break
    elif hello == "Да":
        product = int(input("Введите количество товара, которое Вы хотите приобрести: "))
        number = 1
        result = []
        review_1 = []
        review_2 = []
        review_3 = []
        review_4 = []
        review = {}
        while number <= product:
            my_buy = dict({'название': input("Введите название товара: "), 'цена': int(input("Введите цену товара: ")),
                           'количество': int(input('Введите количество товара: ')), 'ед': input("Введите единицу измерения")})
            result.append((number, my_buy))

            review_1.append(my_buy.get("название"))
            review_2.append(my_buy.get("цена"))
            review_3.append(my_buy.get("количество"))
            review_4.append(my_buy.get("ед"))

            review = dict(
                {'название': review_1, 'цена': review_2, 'количество': review_3,
                 'ед': review_4})

            number += 1

        print(result)
        print(review)

        open_2 = input("Хотите приобрести что-то еще? Да/Нет: ")
        if open_2 == "Да":
            number += 1
        elif open_2 == "Нет":
            print("До скорых встреч!")
            break
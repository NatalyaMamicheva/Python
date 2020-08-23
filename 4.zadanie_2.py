numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"Исходный список: {numbers}")

numbers_2 = [number for num, number in zip(numbers, numbers[1:]) if number > num]
print(f"Новый список: {numbers_2}")



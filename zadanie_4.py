number = int(input("Введите целое положительное число: "))
max_number = 0
while number > 0:
    digit = number % 10
    number = number // 10
    if max_number <= digit:
        max_number = digit
print(max_number)
time = int(input("Введите время в секундах: "))

hours = int(time / 3600)
minutes = int((time / 60) % 60)
seconds = int(time % 60)

print(f"{hours:02}:{minutes:02}:{seconds:02}")

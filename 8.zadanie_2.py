class MyException(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def null(self):
        try:
            print(self.a / self.b)

        except Exception as e:
            if self.b == 0:
                print("Ошибка! На 0 делить нельзя!")

        finally:
            print("Конец")

M = MyException(int(input("Введите делимое: ")), int(input("Введите делитель: ")))
M.null()
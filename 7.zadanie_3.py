class Cell:
    def __init__(self, cell):
        self.cell = int(cell)

    def __str__(self):
        return f"{self.cell}"

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if (self.cell - other.cell) < 0:
            return "Ошибка! Отрицательное число!"
        elif (self.cell - other.cell) > 0:
            return Cell(self.cell - other.cell)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        if other.cell == 0:
            return "Ошибка! На 0 делить нельзя!"
        else:
            return Cell(self.cell // other.cell)

    def make_order(self, rows):
        row = ""
        for i in range(self.cell // rows):
            row = row + f'{"*" * rows} \n'
        row = row + f'{"*" * (self.cell % rows)}'
        return row


c1 = Cell(12)
c2 = Cell(13)
print(f"Сумма ячеек двух клеток = {c1 + c2}")
print(f"Разность количества ячеек двух клеток = {c1 - c2}")
print(f"Произведение количества ячеек этих двух клеток = {c1 * c2}")
print(f"Целочисленное деление количества ячеек этих двух клеток = {c1 // c2}")
print(c1.make_order(5))
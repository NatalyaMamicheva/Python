class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки...{self.title}")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки...{self.title}")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки...{self.title}")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки...{self.title}")

pen = Pen("Ручка")
pen.draw()
pencil = Pencil("Карандаш")
pencil.draw()
handle = Handle("Маркер")
handle.draw()
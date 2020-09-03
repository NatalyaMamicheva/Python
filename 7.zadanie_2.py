from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, size, height):
        self.size = size
        self.height = height

    def overcoat(self):
        return (self.size / 6.5) + 0.5

    def suit(self):
        return (self.height * 2) + 0.3

    @property
    def all(self):
        return str(f"{round(((self.size / 6.5) + 0.5) + ((self.height * 2) + 0.3))}")

    @abstractmethod
    def color(self):
        pass


class Coat(Clothes):

    def color(self):
        super().color()
        print("Используем ткань белого цвета")

    def __init__(self, size, height):
        super().__init__(size, height)
        self.overcoat = round((self.size / 6.5) + 0.5)
        print(f"Площадь расхода ткани на пальто = {self.overcoat} м")


class Costume(Clothes):

    def color(self):
        super().color()
        print("Используем ткань белого цвета")

    def __init__(self, size, height):
        super().__init__(size, height)
        self.suit = round((self.height * 2) + 0.3)
        print(f"Площадь расхода ткани на костюм = {self.suit} м")

ca = Coat(2, 3)
ca.color()
cs = Costume(2, 3)
cs.color()
print(f"Общая площадь расхода белой ткани на одежду = {ca.all} м")
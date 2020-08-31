class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} поехал"

    def stop(self):
        return f"{self.name} остановился"

    def turn_right(self):
        return f"{self.name} повернул направо"

    def turn_left(self):
        return f"{self.name} повернул налево"

    def show_speed(self):
        return f"Скорость {self.name} {self.speed} км/ч"

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Сбавьте скорость! Скорость {self.name} {self.speed} км/ч"
        else:
            return f"Скорость {self.name} {self.speed} км/ч"

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 150:
            return f"Сбавьте скорость! Cкорость {self.name} {self.speed} км/ч"
        else:
            return f"Скорость {self.name} {self.speed} км/ч"

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Сбавьте скорость! Скорость {self.name} {self.speed} км/ч"
        else:
            return f"Скорость {self.name} {self.speed} км/ч"

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Сбавьте скорость! Скорость {self.name} {self.speed} км/ч"
        else:
            return f"Скорость {self.name} {self.speed} км/ч"

    def police(self):
        if self.is_police:
            return f"{self.name} полицейская машина!"
        else:
            return f"{self.name} не полицейская машина!"

Jaguar = SportCar(140, "Серый", "Jaguar", False)
Mazda = TownCar(70, "Серый металлик", "Mazda", False)
Toyota = WorkCar(55, "Белый", "Toyota", False)
Ford = PoliceCar(90, "Синий", "Ford", True)
print(f"{Toyota.stop()}, далее {Toyota.turn_right()}. {Toyota.show_speed()}")
print(f"{Jaguar.turn_right()}, {Mazda.go()}")
print(f"{Mazda.turn_left()}, {Mazda.show_speed()}")
print(f"{Jaguar.name}, {Jaguar.color}, {Jaguar.show_speed()}")
print(f"{Jaguar.name} полицейская машина? {Jaguar.is_police}")
print(f"{Ford.name} полицейская машина? {Ford.is_police}. {Ford.show_speed()}")
class Complex_Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f"Сумма(z1 + z2): ")
        return f"z = {self.a + other.a} + {self.b + other.b}i"

    def __mul__(self, other):
        print(f"Произведение(z1 * z2): ")
        return f"z = {self.a * other.a - (self.b * other.b)} + {self.a * other.b + (self.b * other.a)}i"

    def __str__(self):
        return f"z = {self.a} + ({self.b}i)"


z1 = Complex_Number(3, 1)
z2 = Complex_Number(2, 3)
print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)
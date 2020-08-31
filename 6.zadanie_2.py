class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        m_asph = 25
        w_asph = 5
        massa = int((self._length * self._width * m_asph * w_asph) / 1000)
        print(f"Масса асфальта, необходимого для покрытия всего дорожного полотна: {self._length}м * {self._width}м * {m_asph}кг * {w_asph}см = {massa}т")

r = Road(5000, 20)
r.mass()
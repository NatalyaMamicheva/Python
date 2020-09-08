import sys
class Warehouse_equipment:
    def reception(self):
        count = []
        name = []
        tehn = {'Модель устройства': name,
                   'Количество': count}
        try:
            while True:
                rec = {'Модель устройства': int(input("Введите номер устройства, которое хотите выбрать: 1(Принтер), 2(Сканер), 3(Ксерокс): ")),
                       'Количество': int(input('Введите количество устройств: '))}
                if rec['Модель устройства'] == 1:
                    name.append("".join("Принтер"))
                    count.append(rec['Количество'])
                    return tehn
                elif rec['Модель устройства'] == 2:
                    name.append("Сканер")
                    count.append(rec['Количество'])
                    return tehn
                elif rec['Модель устройства'] == 3:
                    name.append("Ксерокс")
                    count.append(rec['Количество'])
                    return tehn
                else:
                    return "Ошибка! Выберите устройство только под номер 1, 2 или 3!"
        except:
            print("Ошибка ввода данных! Завершение программы...")
            sys.exit()


class Office_equipment(Warehouse_equipment):
    def __init__(self, name):
        self.name = name

    def of(self):
        return Warehouse_equipment.reception(self)


class Printer(Office_equipment):
    def __init__(self, name):
        super().__init__(name)

    def pr(self):
        return "Фирма принтера: LG"


class Scanner(Office_equipment):
    def __init__(self, name):
        super().__init__(name)

    def sc(self):
        return "Фирма сканера: HP"


class Copier(Office_equipment):
    def __init__(self, name):
        super().__init__(name)

    def cop(self):
        return "Фирма ксерокса: Samsung"


o = Office_equipment("Фирма устройства")
print(o.of())
p = Printer("LG")
print(p.pr())
s = Scanner("HP")
print(s.sc())
c = Copier("Samsung")
print(c.cop())
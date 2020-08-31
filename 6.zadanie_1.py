import time
class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый", "Желтый"]

    def running(self):
        while True:
            i = 0
            while i < 4:
                if i == 0:
                    time.sleep(2)
                    print("\033[31m {}" .format(TrafficLight.__color[0]))
                elif i == 1:
                    time.sleep(7)
                    print("\033[33m {}" .format(TrafficLight.__color[1]))
                elif i == 2:
                    time.sleep(2)
                    print("\033[32m {}" .format(TrafficLight.__color[2]))
                elif i == 3:
                    time.sleep(7)
                    print("\033[33m {}" .format(TrafficLight.__color[3]))
                i += 1
TL = TrafficLight()
TL.running()
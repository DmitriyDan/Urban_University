from threading import Thread
from time import sleep
class Knight(Thread):
    def __init__(self, name, power):
        super(Knight, self).__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        vrag = 100
        dni = 0
        while vrag > 0:
            sleep(1)
            dni += 1
            vrag = vrag - self.power
            if vrag > 0:
                sleep(1)
                print(f'{self.name}, сражается {dni} день(дня)..., осталось {vrag} воинов.')
            else:
                print(f'{self.name}, сражается {dni} день(дня)..., осталось 0 воинов.')
                break
        print(f'{self.name} одержал победу спустя {dni} дней(дня)!')

first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')
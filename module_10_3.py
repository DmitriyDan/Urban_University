import time
import random
import threading

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sluchaynoe_chislo = random.randint(50, 500)
            self.balance += sluchaynoe_chislo
            print(f'Пополнение: {sluchaynoe_chislo}. Баланс: {self.balance}') # вывод строки
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            sluchaynoe_chislo = random.randint(50, 500)
            print(f'Запрос на {sluchaynoe_chislo}')
            if sluchaynoe_chislo <= self.balance:
                self.balance -= sluchaynoe_chislo
                print(f'Снятие: {sluchaynoe_chislo}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')




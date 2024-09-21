import threading
import time
from random import randint


class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            rand_digit = randint(50, 500)
            self.balance += rand_digit
            if (self.balance >= 500 and self.lock.locked()):
                self.lock.release()
            print(f'Пополнение: {rand_digit}. Баланс: {self.balance}')
        time.sleep(0.001)

    def take(self):
        for _ in range(100):
            rand_digit_take = randint(50, 500)
            print(f'Запрос на {rand_digit_take}')
            if rand_digit_take <= self.balance:
                self.balance -= rand_digit_take
                print(f'Снятие: {rand_digit_take}. Баланс {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()



bk = Bank(0)

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
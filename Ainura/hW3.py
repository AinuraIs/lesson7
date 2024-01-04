from calclass Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        additional_money = float(input("Введите сумму для добавления на счет: "))
        self._balance += additional_money
        print(f"Текущий баланс после добавления: {self._balance}")

    def _kill(self):
        self._balance = 0
        print("Баланс обнулен")

    def _jackpot(self):
        self._balance *= 10
        print("Джекпот! Баланс увеличен в 10 раз")

    def _merge_balance(self, other_account):
        self._balance += other_account._balance
        other_account._balance = 0
        print(f"Баланс объединен. Текущий баланс: {self._balance}")

account1 = Bank("Beka's Account", 100)
account2 = Bank("Ainura's Account", 100)

account1.moneyX()
account1._jackpot()
account1._merge_balance(account2)

print(f"{account1._name}'s balance: {account1._balance}")
print(f"{account2._name}'s balance: {account2._balance}")

culator import Calculator

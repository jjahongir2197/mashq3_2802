class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"+{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"-{amount}")
            return True
        return False

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, name, balance):
        self.accounts.append(Account(name, balance))

    def find(self, name):
        return next((a for a in self.accounts if a.name == name), None)

    def transfer(self, sender, receiver, amount):
        s = self.find(sender)
        r = self.find(receiver)

        if s and r and s.withdraw(amount):
            r.deposit(amount)
            print("Pul o‘tkazildi")
        else:
            print("Xatolik")

def run():
    bank = Bank()
    bank.add_account("Ali", 1000000)
    bank.add_account("Vali", 500000)

    while True:
        print("\n1. O‘tkazma\n2. Hisoblar\n3. Chiqish")
        c = input("Tanlang: ")

        if c == "1":
            bank.transfer(input("Kimdan: "), input("Kimga: "), int(input("Summa: ")))
        elif c == "2":
            for a in bank.accounts:
                print(a.name, a.balance, a.history)
        else:
            break

run()

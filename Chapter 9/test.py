class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"Balance: ${self.balance}")


account = BankAccount("Talha")

account.deposit(500)
account.withdraw(100)

account.show_balance()
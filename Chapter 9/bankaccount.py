class Bank_account:
    def __init__(self,account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self,amount):
         self.balance = self.balance + amount

    def withdraw(self, amount):

        self.balance = self.balance - amount

    def show_balance(self):
        print(f"Hello {self.account_holder}!")
        print(f"Your balance is {self.balance}")

user1 = Bank_account("Talha")
user1.deposit(500)
user1.withdraw(5000)
user1.show_balance()


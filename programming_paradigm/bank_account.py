class BankAccount:
    def __init__(self,account_balance=0):
        self.account_balance=account_balance

    def deposit(self,amount):
        self.account_balance+=amount

    def withdraw(amount):
        if self.account_balance < amount:
            return False
        else:

            return True

    def display_balance():
        print(f"Current Balance: ${self.account_balance}")

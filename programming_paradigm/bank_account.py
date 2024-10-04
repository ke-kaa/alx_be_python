class BankAccount:
    def __init__(self, balance=0) -> None:
        self.account_balance = balance
    
    def deposit(self, amount):
        self.account_balance += amount
    
    def withdraw(self, amount):
        if self.account_balance < amount:
            return False
        self.account_balance -= amount
        return True
    
    def display_balance(self):
        return f'Current Balance: ${self.account_balance}'
    
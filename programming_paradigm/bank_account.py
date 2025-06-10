class BankAccount:
    def __init__(self, initial_amount=0):
        self.account_balance = initial_amount

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        current_balance = self.account_balance
        print(f"Your balance is: {current_balance}")
    


        
class BankAccount:
    def __init__(self, initial_amount=0):
        self.account_balance = initial_amount

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        elif amount > self.account_balance:
            return False
        return False
    
    def display_balance(self): 
        print(f"Current Balance: ${self.account_balance:.2f}")
    


        
# import hashlib, os, csv

# BANK_CSV = "BANK.csv"

# def hash_password(pw: str) -> str:
#     return hashlib.sha256(pw.encode()).hexdigest()
# from cashback import Cashback
class Account:
    def __init__(self, account_id, balance=0.0):
        self.account_id = int(account_id)
        self.balance = float(balance)
        self.overdraft_count = 0
        self.active = True
        self.overdraft_limit = -100

    def deposit(self, amount: float, cashback_rate=0.095):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        cashback_amount = round(amount * cashback_rate, 2)
        self.balance += cashback_amount

    def withdraw(self, amount: float):
        if not self.active:
            raise ValueError("Account is deactivated due to overdrafts")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
      
        self.balance -= amount


        if self.balance < 0:
            self.overdraft_count += 1
            print(f"⚠️ Overdraft! Count = {self.overdraft_count}")

      
        if self.overdraft_count >= 2:
            self.active = False
            raise ValueError(" Account deactivated due to 2 overdrafts")

        if self.balance < self.overdraft_limit:
            raise ValueError(" Cannot withdraw beyond -SR100 overdraft limit")
        
        return self.balance
        
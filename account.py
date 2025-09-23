import csv, os, hashlib

BANK_CSV = "bank.csv"

def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

class Account:
    def __init__(self, account_id, balance=0.0):
        self.account_id = int(account_id)
        self.balance = float(balance)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if self.balance - amount < 0:
            raise ValueError("Insufficient funds")
        self.balance -= amount

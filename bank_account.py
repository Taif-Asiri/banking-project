import csv, os, hashlib

BANK_CSV = "bank.csv"

def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

class Account:
    def __init__(self, account_id, balance=0.0):
        self.account_id = int(account_id)
        self.balance = float(balance)
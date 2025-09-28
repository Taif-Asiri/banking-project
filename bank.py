import csv
import os 
import hashlib
import re
from datetime import datetime
from customer import Customer
from account import Account

BANK_CSV = "BANK.csv"
TRANSACTIONS_CSV = "transactions.csv"
def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

def validate_password(pw: str) -> bool:
    if len(pw) < 8:
        return False
    if not re.search(r"[A-Z]", pw):
        return False
    if not re.search(r"[a-z]", pw):
        return False
    if not re.search(r"\d", pw):
        return False
    return True

class Bank:
    def __init__(self, filename):
        self.filename = filename
        self.customers = {}
        self.load_customers()

    def load_customers(self):
        if not os.path.exists(self.filename):
                return    
        with open(self.filename, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                checking = float(row.get('balance_checking') or 0)
                savings = float(row.get('balance_savings') or 0)
                cust = Customer(
                    account_id=row['account_id'],
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    password=row['password'],
                    balance_checking=float(row['balance_checking']),
                    balance_savings=float(row['balance_savings']),
                )
                self.customers[int(row['account_id'])] = cust
                
    def save_customers(self):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['account_id','first_name','last_name','password','balance_checking','balance_savings'])
            for cid in sorted(self.customers.keys()):
                c = self.customers[cid]
                writer.writerow([c.account_id, c.first_name, c.last_name, c.password, c.checking.balance, c.savings.balance]) 
                
    def log_transaction(self, from_acc, to_acc, trans_type, amount):
        write_header = not os.path.exists(TRANSACTIONS_CSV) 
        with open(TRANSACTIONS_CSV, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if write_header:
               writer.writerow(["date_time", "from_account", "to_account", "type", "amount"]) 
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([now, from_acc, to_acc, trans_type, amount])            
                
    def login(self, account_id, password):
        account_id = int(account_id)
        cust = self.customers.get(account_id)
        if cust and cust.password == hash_password(password):
            return cust
        return None  
                              
    def get_next_account_id(self):
        if not os.path.exists(BANK_CSV):
            return 10001
        with open(self.filename, mode="r") as f:
            reader = csv.reader(f)
            next(reader)  
            ids = [int(row[0]) for row in reader]
        return max(ids) + 1 if ids else 10001


    def create_new_account(self):
        while True:
            first_name = input("Enter first name: ")
            if not first_name.isalpha():
                print("Name must contain only letters.")
            else:
                break
        while True:
            last_name = input("Enter last name: ").strip()
            if not last_name.isalpha():
                print("Name must contain only letters.")
            else:
                break 
        while True:       
            password = input("Enter password: ").strip()
            if not validate_password(password):
                print(" Password must be at least 8 characters and include uppercase, lowercase, and a number.")
                continue
            break
        
        while True:
            try:
                balance_checking = float(input("Enter initial checking balance: "))
                break
            except ValueError:
                print("Balance must be a valid number. Please try again.")
        
        
        while True:
            try:
                balance_savings = float(input("Enter initial savings balance: "))
                break
            except ValueError:
                print(" Balance must be a valid number. Please try again.")      
        new_id = self.get_next_account_id()
        hashed_pw = hash_password(password)

        with open(BANK_CSV, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([new_id, first_name, last_name, hashed_pw, balance_checking, balance_savings])
        self.load_customers()
        print(f" Account created successfully! Your account ID is {new_id}")
           
    
    def transfer(self, from_customer, from_type, to_customer, to_type, amount):
        
        if from_type == "checking":
            from_acct = from_customer.checking
        else:
            from_acct = from_customer.savings

        if to_type == "checking":
            to_acct = to_customer.checking
        else:
            to_acct = to_customer.savings

        if from_acct.balance - amount < from_acct.overdraft_limit:
            raise ValueError(f"Cannot transfer: would exceed overdraft limit of {from_acct.overdraft_limit}")
       
        from_acct.withdraw(amount)

        to_acct.deposit(amount)

        
        print(f" Transferred {amount} from {from_customer.first_name}'s {from_type} "
                f"to {to_customer.first_name}'s {to_type}")


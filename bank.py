import csv, hashlib , os
from customer import Customer
from account import hash_password, BANK_CSV
def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

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
                cust = Customer(
                    account_id=row['account_id'],
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    password=row['password'],
                    balance_checking=float(row['balance_checking']),
                    balance_savings=float(row['balance_savings'])
                )
                self.customers[int(row['account_id'])] = cust

    def login(self, account_id, password):
        account_id = int(account_id)
        cust = self.customers.get(account_id)
        if cust and cust.password == password:
            return cust
        return None


    def create_new_account(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        password = input("Enter password: ")
        balance_checking = float(input("Enter initial checking balance: "))
        balance_savings = float(input("Enter initial savings balance: "))


    balance_checking = float(input("Enter initial checking balance: "))
    balance_savings = float(input("Enter initial savings balance: "))

    new_id = self.get_next_account_id()


    def get_next_account_id(self):
        if not os.path.exists(BANK_CSV):
            return 10001
    with open(BANK_CSV, mode="r") as f:
        reader = csv.reader(f)
        next(reader)  
        ids = [int(row[0]) for row in reader]
    return max(ids) + 1 if ids else 10001

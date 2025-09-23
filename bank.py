import csv, hashlib
from customer import Customer

def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

class Bank:
    def __init__(self, filename):
        self.filename = filename
        self.customers = {}
        self.load_customers()

    def load_customers(self):
        try:
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
        except FileNotFoundError:
            print(f"CSV file {self.filename} not found.")

    def login(self, account_id, password):
        account_id = int(account_id)
        cust = self.customers.get(account_id)
        if cust and cust.password == password:
            return cust
        return None

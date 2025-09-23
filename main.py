
from bank import Bank

def main():
    bank = Bank("bank.csv")
    print("=== Welcome to ACME Bank ===")
    account_id = input("Enter your account ID: ")
    password = input("Enter your password: ")
    
if __name__ == "__main__":
    main()
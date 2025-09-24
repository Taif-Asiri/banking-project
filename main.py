from bank import Bank

def main():
    bank = Bank()
    print("=== Welcome to ACME Bank ===")

    while True:
        print("\nOptions:")
        print("1 - Login")
        print("2 - Create New Account")
        print("0 - Exit")
        choice = input("Choose an option: ")

        if choice == "0":
            break
        elif choice == "2":
            bank.create_new_account()
        elif choice == "1":
            account_id = input("Enter your account ID: ")
            password = input("Enter your password: ")
            customer = bank.login(account_id, password)
            if not customer:
                print("Login failed. Check your ID or password.")
                continue

            print(f"Welcome {customer.first_name} {customer.last_name}!")
    while True:
                print("\nYour balances:")
                print(f"Checking: {customer.checking.balance}")
                print(f"Savings: {customer.savings.balance}")

if __name__ == "__main__":
    main()
    
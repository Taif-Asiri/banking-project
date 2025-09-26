from bank import Bank

def main():
    bank = Bank("BANK.CSV")
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
            
            print("\nOptions:")
            print("1 - Deposit")
            print("2 - Withdraw")
            print("3 - Transfer")
            print("0 - Logout")
            action = input("Choose an option: ").strip()

            if action == "0":
                print("Logging out...")
                break
            
            elif action in ["1", "2", "3"]:
                acct_type = input("Choose account (checking/savings): ").lower()
                if acct_type not in ("checking", "savings"):
                   print("Invalid account type.")
                   continue  
                
                try:
                    amount = float(input("Enter amount: "))
                except ValueError:
                    print("Invalid amount.")
                    continue   
                   
                try:
                    if action == "1":
                        if acct_type == "checking":
                            customer.checking.deposit(amount)
                        else:
                                customer.savings.deposit(amount)
                                
                    elif action == "2":
                        if acct_type == "checking":
                                customer.checking.withdraw(amount)
                        else:
                                customer.savings.withdraw(amount)
                                
                    elif action == "3":
                        to_id = input("Enter recipient account ID: ").strip()
                        from_type = input("Transfer from (checking/savings)? ").lower()
                        to_type = input("Transfer to (checking/savings)? ").lower()
                        amount = float(input("Enter amount to transfer: "))

                    try:
                        to_customer = bank.customers.get(int(to_id))
                        if not to_customer:
                            print("❌ Recipient not found.")
                            continue
                        bank.transfer(customer, from_type, to_customer, to_type, amount)
                    except ValueError as e:
                        print("Error:", e)
                        
                    except ValueError as e:
                        print("Error:", e)
            else:
                 print("Invalid option.")    
    else:
            print("Invalid option, please try again.")                 
if __name__ == "__main__":
    main()
    
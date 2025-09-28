from bank import Bank

def main():
    bank = Bank("BANK.csv")
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
                print("3 - Transfer between your accounts")
                print("4 - Transfer to another account")
                print("0 - Logout")
                action = input("Choose an option: ").strip()

                if action == "0":
                    print("Logging out...")
                    break
            
                elif action == "1":
                    acct_type = input("Deposit into (checking/savings)? ").lower()
                    amount = float(input("Enter amount: "))
                    try:
                        if acct_type == "checking":
                            customer.checking.deposit(amount)
                        else:
                            customer.savings.deposit(amount)
                        bank.log_transaction(customer.account_id, customer.account_id, "deposit", amount)
                        bank.save_customers()    

                        print("✅ Deposit successful.")
                    except ValueError as e:
                        print("Error:", e)                     
                elif action == "2": 
                    acct_type = input("Withdraw from (checking/savings)? ").lower()
                    amount = float(input("Enter amount: "))
                    try:
                        if acct_type == "checking":
                            customer.checking.withdraw(amount)
                        else:
                            customer.savings.withdraw(amount)
                        bank.log_transaction(customer.account_id, customer.account_id, "withdraw", amount)
                        bank.save_customers()
                        print("Withdraw successful")     
                    except ValueError as e:
                        print("Error:", e)   
                                         
                elif action == "3":
                    from_type = input("Transfer from (checking/savings)? ").lower()
                    to_type = "savings" if from_type == "checking" else "checking"
                    amount = float(input("Enter amount to transfer: "))
                
                    try:
                        bank.transfer(customer, from_type, customer, to_type, amount)
                        bank.log_transaction(customer.account_id, customer.account_id, "transfer", amount)
                        bank.save_customers()
                    except ValueError as e:
                        print("Error", e)
                elif action == "4":
                    to_id = input("Enter recipient account ID: ").strip()
                    from_type = input("Transfer from checking/savings? ").lower()
                    amount = float(input("Enter amount: "))  
                    
                    to_customer = bank.customers.get(int(to_id))
                    if not to_customer:
                        print("Recipient not found.")
                        continue
                    to_type = "checking"
                    
                    try:    
                        bank.transfer(customer, from_type, to_customer, to_type, amount)
                        bank.log_transaction(customer.account_id, to_customer.account_id, "transfer", amount)
                        bank.save_customers()
                    except ValueError as e:
                        print("Error:", e)
                              
        else:
            print("Invalid option.")    
                
if __name__ == "__main__":
    main()
    
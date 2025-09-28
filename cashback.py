# as a bank, I want to reward customers with cashback when they deposit into savings, so I can reward loyal users during National Day.
class Cashback:
    def __init__(self, rate=0.095):
        self.rate = rate
        self.transactions = []

    def apply_cashback(self, customer, amount, description="National Day cashback"):

        cashback_amount = round(amount * self.rate, 2)
        customer.checking.deposit(cashback_amount)
    
        from datetime import datetime
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append({
            "account_id": customer.account_id,
            "description": description,
            "amount_spent": amount,
            "cashback": cashback_amount,
            "date_time": now
        })
        
        print(f"💚 Congratulations! You have received a {self.rate*100}% cashback on the occasion of the 95th National Day💚!")
        print(f" {cashback_amount} has been added to your account. Your new balance is:{customer.checking.balance}")
 
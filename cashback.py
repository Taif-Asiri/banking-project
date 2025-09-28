class Cashback:
    def __init__(self, rate=0.095):
        self.rate = rate
        self.transactions = []

    def apply_cashback(self, customer, amount, description="National Day cashback"):

        cashback_amount = round(amount * self.rate, 2)
        customer.checking.deposit(cashback_amount)

 
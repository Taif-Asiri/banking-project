# user story
# as a customer, i want to have personal info (first name, last name, password) and 2 accounts (checking and savings)
from account import Account

class Customer:
    def __init__(self, account_id, first_name, last_name, password,
                balance_checking=0.0, balance_savings=0.0):
        self.account_id = int(account_id)
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.checking = Account(account_id, balance_checking)
        self.savings = Account(account_id, balance_savings)


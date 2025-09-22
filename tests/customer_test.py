import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):

    def test_customer_init_and_accounts(self):
        cust = Customer(
            account_id=10001,
            first_name="Suresh",
            last_name="Sigera",
            password="juagw362",
            balance_checking=1000.0,
            balance_savings=10000.0
        )
import unittest
import os
from bank import Bank
from account import hash_password, BANK_CSV

class TestBank(unittest.TestCase):

    def setUp(self):
   
        with open(self.TEST_CSV, "w", newline="") as f:
            f.write("account_id,first_name,last_name,password,balance_checking,balance_savings\n")
            f.write(f"10001,Suresh,Sigera,{hash_password('juagw362')},1000,10000\n")
    def test_load_and_login(self):
        bank = Bank(BANK_CSV)
        cust = bank.login(10001, "juagw362")
        self.assertIsNotNone(cust)
        self.assertEqual(cust.first_name.lower(), "suresh")

    def test_login_fail_wrong_password(self):
        bank = Bank(BANK_CSV)
        cust = bank.login(10001, "wrongpassword")
        self.assertIsNone(cust)

    def test_create_new_account(self):
        inputs = iter(["Alice", "Wonderland", "mypassword", "500", "1000"])
        self.bank.input = lambda _: next(inputs)
        
        original_input = __builtins__.input
        __builtins__.input = lambda _: next(inputs)
        try:
            self.bank.create_new_account()
        finally:
            __builtins__.input = original_input

        new_id = max(self.bank.customers.keys())
        self.assertIn(new_id, self.bank.customers)
        new_cust = self.bank.customers[new_id]
        self.assertEqual(new_cust.first_name, "Alice")
        self.assertEqual(new_cust.checking.balance, 500.0)
        self.assertEqual(new_cust.savings.balance, 1000.0)

if __name__ == "__main__":
    unittest.main()
# python -m unittest tests/bank_test.py
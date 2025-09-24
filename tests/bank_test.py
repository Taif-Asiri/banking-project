import unittest
import os
from bank import Bank
from account import hash_password, BANK_CSV

class TestBank(unittest.TestCase):
    TEST_CSV = "test_BANK.CSV"
    def setUp(self):
   
        with open(self.TEST_CSV, "w", newline="") as f:
            f.write("account_id,first_name,last_name,password,balance_checking,balance_savings\n")
            f.write(f"10001,Suresh,Sigera,{hash_password('juagw362')},1000,10000\n")
        self.bank = Bank(self.TEST_CSV)
    def test_load_and_login(self):
        cust = self.bank.login(10001, "juagw362")
        self.assertIsNotNone(cust)
        self.assertEqual(cust.first_name.lower(), "suresh")

    def test_login_fail_wrong_password(self):
        cust = self.bank.login(10001, "wrongpassword")
        self.assertIsNone(cust)

    def test_create_new_account(self):
        inputs = iter(["Alice", "Wonderland", "mypassword", "500", "1000"])
        self.bank.input = lambda _: next(inputs)

if __name__ == "__main__":
    unittest.main()
# python -m unittest tests/bank_test.py
import unittest
from account import Account, hash_password 

class TestAccount(unittest.TestCase):

    def test_account_init(self):
        acc = Account(10001, 1000.0)
        self.assertEqual(acc.account_id, 10001)
        self.assertEqual(acc.balance, 1000.0)
        

        # python -m unittest tests/account_test.py
        
    def test_deposit(self):
        acc = Account(10002, 100.0)
        acc.deposit(50)
        self.assertEqual(acc.balance, 150.0)
        
    def test_withdraw(self):
        acc = Account(10003, 200.0)
        acc.withdraw(100)
        self.assertEqual(acc.balance, 100.0)
        
if __name__ == "__main__":
    unittest.main()
        

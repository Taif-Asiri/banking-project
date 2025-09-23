import unittest
from bank import Bank

class TestBank(unittest.TestCase):
    def test_load_and_login(self):
        bank = Bank("bank.csv")
        cust = bank.login(10001, "juagw362")
        self.assertIsNotNone(cust)
        self.assertEqual(cust.first_name.lower(), "suresh")

if __name__ == "__main__":
    unittest.main()
# python -m unittest tests/bank_test.py
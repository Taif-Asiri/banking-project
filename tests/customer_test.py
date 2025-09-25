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
            balance_savings=10000.0,
        )
        self.assertEqual(cust.account_id, 10001)
        self.assertEqual(cust.first_name, "Suresh")
        self.assertEqual(cust.last_name, "Sigera")
        self.assertEqual(cust.password, "juagw362")
        self.assertEqual(cust.checking.balance, 1000.0)
        self.assertEqual(cust.savings.balance, 10000.0)   
        
    def test_customer_account_operations(self):
        cust = Customer(10002, "James", "Taylor", "pwd", balance_checking=200, balance_savings=500)
       
        cust.checking.deposit(50)
        self.assertEqual(cust.checking.balance, 250)
      
        cust.savings.withdraw(100)
        self.assertEqual(cust.savings.balance, 400)

if __name__ == "__main__":
    unittest.main() 
    #  python -m unittest tests/customer_test.py
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # python -m unittest tests/customer_test.py    
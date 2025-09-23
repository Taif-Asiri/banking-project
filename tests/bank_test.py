import unittest
import tempfile
import os
import csv
from bank import Bank

SAMPLE_ROWS = [
    {'account_id':'10001','first_name':'suresh','last_name':'sigera','password':'juagw362','balance_checking':'1000','balance_savings':'10000'},
    {'account_id':'10002','first_name':'james','last_name':'taylor','password':'idh36%@#FGd','balance_checking':'10000','balance_savings':'10000'},
]
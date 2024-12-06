"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: Olusola Ropo
Date: 03/10/2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_chequing_account.py
"""

import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount


class TestChequingAccount(unittest.TestCase):

    def setUp(self):
        """Set up some default values for ChequingAccount to use in the tests."""
        self.account_number = 123456
        self.client_number = 7891011
        self.balance = 1000.0
        self.date_created = date.today()
        self.valid_overdraft_limit = -100.0
        self.valid_overdraft_rate = 0.05

    def test_chequing_account_initialization(self):
        """Test the initialization of a ChequingAccount object."""
        account = ChequingAccount(self.account_number, self.client_number, self.balance,
                                  self.date_created, self.valid_overdraft_limit, self.valid_overdraft_rate)

        # Check that the attributes are set correctly
        self.assertEqual(account.account_number, self.account_number)
        self.assertEqual(account.client_number, self.client_number)
        self.assertEqual(account.balance, self.balance)
        self.assertEqual(account._ChequingAccount__overdraft_limit,
                         self.valid_overdraft_limit)
        self.assertEqual(account._ChequingAccount__overdraft_rate,
                         self.valid_overdraft_rate)

    def test_invalid_overdraft_limit(self):
        """Test that an invalid overdraft limit is set to the default value."""
        account = ChequingAccount(self.account_number, self.client_number, self.balance,
                                  self.date_created, "invalid_limit", self.valid_overdraft_rate)
        self.assertEqual(account._ChequingAccount__overdraft_limit, -100.0)

    def test_invalid_overdraft_rate(self):
        """Test that an invalid overdraft rate is set to the default value."""
        account = ChequingAccount(self.account_number, self.client_number, self.balance,
                                  self.date_created, self.valid_overdraft_limit, "invalid_rate")
        self.assertEqual(account._ChequingAccount__overdraft_rate, 0.05)

    def test_get_service_charges_within_limit(self):
        """Test service charges when balance is above overdraft limit."""
        account = ChequingAccount(self.account_number, self.client_number, 50.0,
                                  self.date_created, self.valid_overdraft_limit, self.valid_overdraft_rate)
        expected_service_charge = 0.50  # BASE_SERVICE_CHARGE
        actual_service_charge = account.get_service_charges()
        self.assertEqual(expected_service_charge,
                         round(actual_service_charge, 2))

    def test_get_service_charges_below_limit(self):
        """Test service charges when balance is below overdraft limit."""
        account = ChequingAccount(self.account_number, self.client_number, -600.0,
                                  self.date_created, self.valid_overdraft_limit, self.valid_overdraft_rate)
        # Expected service charge based on formula
        expected_service_charge = 0.50 + \
            (-100 - (-600)) * 0.05  # 0.50 + (500 * 0.05) = 25.50
        actual_service_charge = account.get_service_charges()
        self.assertEqual(expected_service_charge,
                         round(actual_service_charge, 2))

    def test_str_method(self):
        """Test the string representation of the ChequingAccount."""
        account = ChequingAccount(self.account_number, self.client_number, self.balance,
                                  self.date_created, self.valid_overdraft_limit, self.valid_overdraft_rate)
        expected_str = (f"Account Number: {self.account_number} Balance: ${self.balance:,.2f}\n"
                        f"Overdraft Limit: ${self.valid_overdraft_limit:,.2f} "
                        f"Overdraft Rate: {self.valid_overdraft_rate * 100:.2f}% Account Type: Chequing")
        self.assertEqual(str(account), expected_str)


if __name__ == "__main__":
    unittest.main()

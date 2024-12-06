"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: Olusola Ropo
Date: 03/10/2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_investment_account.py
"""

import unittest
from datetime import date
from bank_account.investment_account import InvestmentAccount


class TestInvestmentAccount(unittest.TestCase):

    def setUp(self):
        """Set up some default values for InvestmentAccount to use in the tests."""
        self.account_number = 123456
        self.client_number = 7891011
        self.balance = 1000.0
        self.date_created_less_than_10_years = date.today()
        self.date_created_more_than_10_years = date(2010, 1, 1)
        self.management_fee = 2.00

    def test_investment_account_initialization(self):
        """Test initialization of an InvestmentAccount."""
        account = InvestmentAccount(self.account_number, self.client_number,
                                    self.balance, self.date_created_less_than_10_years, self.management_fee)

        # Ensure attributes are set correctly
        self.assertEqual(account.account_number, self.account_number)
        self.assertEqual(account.client_number, self.client_number)
        self.assertEqual(account.balance, self.balance)
        self.assertEqual(
            account._InvestmentAccount__management_fee, self.management_fee)

    def test_invalid_management_fee(self):
        """Test that an invalid management fee is set to the default value."""
        account = InvestmentAccount(self.account_number, self.client_number,
                                    self.balance, self.date_created_less_than_10_years, "invalid_fee")
        self.assertEqual(account._InvestmentAccount__management_fee, 2.55)

    def test_str_method_less_than_10_years(self):
        """Test the string representation for an account less than 10 years old."""
        account = InvestmentAccount(self.account_number, self.client_number,
                                    self.balance, self.date_created_less_than_10_years, self.management_fee)
        expected_str = (f"Account Number: {self.account_number} Balance: ${self.balance:,.2f}\n"
                        f"Date Created: {self.date_created_less_than_10_years} Management Fee: ${self.management_fee:,.2f} Account Type: Investment")
        self.assertEqual(str(account), expected_str)

    def test_str_method_more_than_10_years(self):
        """Test the string representation for an account more than 10 years old."""
        account = InvestmentAccount(self.account_number, self.client_number,
                                    self.balance, self.date_created_more_than_10_years, self.management_fee)
        expected_str = (f"Account Number: {self.account_number} Balance: ${self.balance:,.2f}\n"
                        f"Date Created: {self.date_created_more_than_10_years} Management Fee: Waived Account Type: Investment")
        self.assertEqual(str(account), expected_str)

    def test_get_service_charges_less_than_10_years(self):
        """Test service charges for an account less than 10 years old."""
        account = InvestmentAccount(self.account_number, self.client_number,
                                    self.balance, self.date_created_less_than_10_years, self.management_fee)
        # BASE_SERVICE_CHARGE + management_fee
        expected_service_charge = 0.50 + self.management_fee
        self.assertEqual(expected_service_charge, round(
            account.get_service_charges(), 2))

    def test_get_service_charges_more_than_10_years(self):
        """Test service charges for an account more than 10 years old."""
        account = InvestmentAccount(self.account_number, self.client_number,
                                    self.balance, self.date_created_more_than_10_years, self.management_fee)
        # BASE_SERVICE_CHARGE, since the management fee is waived
        expected_service_charge = 0.50
        self.assertEqual(expected_service_charge, round(
            account.get_service_charges(), 2))


if __name__ == "__main__":
    unittest.main()

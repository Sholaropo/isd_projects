import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):

    def setUp(self):
        """Set up some default values for SavingsAccount to use in the tests."""
        self.account_number = 9483914
        self.client_number = 987654
        self.balance_above_minimum = 100.00
        self.balance_below_minimum = 49.99
        self.date_created = date(2023, 1, 1)
        self.minimum_balance = 50.00
        self.invalid_minimum_balance = "invalid_min_balance"

    def test_savings_account_initialization(self):
        """Test initialization of a SavingsAccount."""
        account = SavingsAccount(self.account_number, self.client_number, self.balance_above_minimum, self.date_created, self.minimum_balance)
        
        # Ensure attributes are set correctly
        self.assertEqual(account.account_number, self.account_number)
        self.assertEqual(account.client_number, self.client_number)
        self.assertEqual(account.balance, self.balance_above_minimum)
        self.assertEqual(account._SavingsAccount__minimum_balance, self.minimum_balance)

    def test_invalid_minimum_balance(self):
        """Test that an invalid minimum balance is set to the default value."""
        account = SavingsAccount(self.account_number, self.client_number, self.balance_above_minimum, self.date_created, self.invalid_minimum_balance)
        self.assertEqual(account._SavingsAccount__minimum_balance, 50.00)

    def test_str_method(self):
        """Test the string representation of a SavingsAccount."""
        account = SavingsAccount(self.account_number, self.client_number, self.balance_above_minimum, self.date_created, self.minimum_balance)
        expected_str = (f"Account Number: {self.account_number} Balance: ${self.balance_above_minimum:,.2f}\n"
                        f"Minimum Balance: ${self.minimum_balance:,.2f} Account Type: Savings")
        self.assertEqual(str(account), expected_str)

    def test_get_service_charges_above_minimum_balance(self):
        """Test service charges when balance is above minimum."""
        account = SavingsAccount(self.account_number, self.client_number, self.balance_above_minimum, self.date_created, self.minimum_balance)
        expected_service_charge = 0.50  # BASE_SERVICE_CHARGE
        self.assertEqual(round(account.get_service_charges(), 2), expected_service_charge)

    def test_get_service_charges_below_minimum_balance(self):
        """Test service charges when balance is below minimum."""
        account = SavingsAccount(self.account_number, self.client_number, self.balance_below_minimum, self.date_created, self.minimum_balance)
        expected_service_charge = 0.50 * 2.00  # BASE_SERVICE_CHARGE * SERVICE_CHARGE_PREMIUM
        self.assertEqual(round(account.get_service_charges(), 2), expected_service_charge)

if __name__ == "__main__":
    unittest.main()

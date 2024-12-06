import unittest
from bank_account.bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Initialize a BankAccount object for testing
        self.account = BankAccount(123456, 1001, 500.00)

    def test_deposit_valid(self):
        self.account.deposit(100)
        expected_balance = 600.00
        self.assertEqual(expected_balance, round(self.account.balance, 2))

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError) as cm:
            self.account.deposit(-50)
        self.assertEqual(str(cm.exception),
                         "Deposit amount: $-50.00 must be positive.")

    def test_deposit_non_numeric(self):
        with self.assertRaises(ValueError) as cm:
            self.account.deposit("abc")
        self.assertEqual(str(cm.exception), "Deposit amount must be numeric.")

    def test_withdraw_valid(self):
        self.account.withdraw(100)
        expected_balance = 400.00
        self.assertEqual(expected_balance, round(self.account.balance, 2))

    def test_withdraw_exceeds_balance(self):
        with self.assertRaises(ValueError) as cm:
            self.account.withdraw(600)
        self.assertEqual(str(
            cm.exception), "Withdrawal amount: $600.00 must not exceed the account balance: $500.00")

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError) as cm:
            self.account.withdraw(-50)
        self.assertEqual(str(cm.exception),
                         "Withdrawal amount: $-50.00 must be positive.")

    def test_withdraw_non_numeric(self):
        with self.assertRaises(ValueError) as cm:
            self.account.withdraw("abc")
        self.assertEqual(str(cm.exception), "Withdraw amount must be numeric.")


if __name__ == '__main__':
    unittest.main()

import os
import sys
import csv
import copy
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMessageBox
from ui_superclasses.details_window import DetailsWindow
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from bank_account.bank_account import Client
from bank_account.bank_account import BankAccount



class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    # Signal to notify of balance updates
    balance_updated = Signal()

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the AccountDetailsWindow.
        
        Args:
            account: The BankAccount object to be displayed and managed.
        """
        super().__init__()
        self.account = copy.deepcopy(account)  # Create a copy to avoid direct modifications

        # Set up the UI with account details
        self.setup_ui()

    def setup_ui(self) -> None:
        """
        Sets up the UI elements for displaying account details.
        """
        # Set initial account details in the UI
        self.account_number_label.setText(str(self.account.account_number))
        self.balance_label.setText(f"${self.account.balance:,.2f}")
        self.account_type_label.setText(self.account.__class__.__name__)
        self.date_created_label.setText(self.account.date_created.strftime("%Y-%m-%d"))

        # Connect buttons to their corresponding methods
        self.deposit_button.clicked.connect(self.on_deposit)
        self.withdraw_button.clicked.connect(self.on_withdraw)

    def on_deposit(self) -> None:
        """
        Handles deposit transactions.
        """
        amount_text = self.deposit_input.text()
        try:
            amount = float(amount_text)
            if amount <= 0:
                raise ValueError("Amount must be positive.")

            # Perform the deposit
            self.account.balance += amount
            self.update_balance_label()
            self.balance_updated.emit()  # Emit signal to notify of updates
            QMessageBox.information(self, "Success", f"Deposited ${amount:,.2f}.")
        except ValueError as e:
            QMessageBox.warning(self, "Invalid Input", str(e))

    def on_withdraw(self) -> None:
        """
        Handles withdrawal transactions.
        """
        amount_text = self.withdraw_input.text()
        try:
            amount = float(amount_text)
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            if amount > self.account.balance:
                raise ValueError("Insufficient balance.")

            # Perform the withdrawal
            self.account.balance -= amount
            self.update_balance_label()
            self.balance_updated.emit()  # Emit signal to notify of updates
            QMessageBox.information(self, "Success", f"Withdrew ${amount:,.2f}.")
        except ValueError as e:
            QMessageBox.warning(self, "Invalid Input", str(e))

    def update_balance_label(self) -> None:
        """
        Updates the balance label with the current account balance.
        """
        self.balance_label.setText(f"${self.account.balance:,.2f}")

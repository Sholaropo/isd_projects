import copy
from typing import Tuple, Dict
import logging
from datetime import datetime
import csv
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtWidgets import QMainWindow, QPushButton, QComboBox, QLineEdit, QLabel, QTableWidget, QTableWidgetItem
from ui_superclasses.details_window import DetailsWindow
from ui_superclasses.lookup_window import LookupWindow
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from bank_account import SavingsAccount, ChequingAccount, InvestmentAccount
from bank_account.bank_account import Client
from bank_account.bank_account import BankAccount

# *************************************************************
# LOGGING AND FILE PATH SETUP
root_dir = os.path.dirname(os.path.dirname(__file__))
log_dir = os.path.join(root_dir, 'logs')
os.makedirs(log_dir, exist_ok=True)
log_file_path = os.path.join(log_dir, 'manage_data.log')
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')

data_dir = os.path.join(root_dir, 'data')
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
# *************************************************************


class ChequingAccount(BankAccount):
    def __init__(self, account_number, client_number, balance, date_created, overdraft_limit, overdraft_rate):
        super().__init__(account_number, client_number, balance, date_created)
        self.account_type = 'ChequingAccount'
        self.overdraft_limit = overdraft_limit
        self.overdraft_rate = overdraft_rate

def parse_date(date_string: str) -> datetime:
    """Parses date strings with multiple possible formats."""
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    raise ValueError(f"Date {date_string} does not match known formats.")

def load_data() -> Tuple[Dict[int, Client], Dict[int, list]]:
    """Loads client and account data from CSV files."""
    client_listing = {}
    accounts = {}

    # Load client data
    with open(clients_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                client_number = int(row['client_number'])
                client = Client(
                    client_number, row['first_name'], row['last_name'], row['email_address']
                )
                client_listing[client_number] = client
            except ValueError as e:
                logging.error(f"Error processing client row {row}: {e}")

    # Load account data
    with open(accounts_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                account_number = int(row['account_number'])
                client_number = int(row['client_number'])
                balance = float(row['balance'])
                date_created = parse_date(row['date_created'])
                account_type = row['account_type']  # Extract account type

                account = None

                if account_type == "SavingsAccount":
                    account = SavingsAccount(account_number, client_number, balance, date_created,
                                             float(row.get('minimum_balance', '0.0')), 10.0)
                elif account_type == "ChequingAccount":
                    account = ChequingAccount(account_number, client_number, balance, date_created,
                                              float(row.get('overdraft_limit', '0.0')),
                                              float(row.get('overdraft_rate', '0.0'))) 
                elif account_type == "InvestmentAccount":
                    account = InvestmentAccount(account_number, client_number, balance, date_created,
                                                float(row.get('management_fee', '0.0')))
                if account:
                    # Group accounts by client_number
                    if client_number not in accounts:
                        accounts[client_number] = []
                    accounts[client_number].append(account)

            except ValueError as e:
                logging.error(f"Error processing account row {row}: {e}")

    return client_listing, accounts


class ClientLookupWindow(LookupWindow):
    """Manages client lookup and account filtering."""

    def __init__(self):
        super().__init__()
        self.client_listing, self.accounts = load_data()

        # Filter-related widget connections and initial state
        self.filter_button.clicked.connect(self.on_filter_clicked)
        self.filter_combo_box.setEnabled(False)
        self.filter_edit.setEnabled(False)
        self.filter_button.setEnabled(False)

        # Connect lookup and account table interactions
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.account_table.cellClicked.connect(self.on_select_account)

    def on_filter_clicked(self):
        """Handles filter application and toggling."""
        if self.filter_button.text() == "Apply Filter":
            filter_index = self.filter_combo_box.currentIndex()
            filter_text = self.filter_edit.text().strip().lower()

            if not filter_text:
                QMessageBox.warning(self, "Invalid Filter",
                                    "Filter text cannot be empty.")
                return

            for row in range(self.account_table.rowCount()):
                item = self.account_table.item(row, filter_index)
                if item and filter_text in item.text().lower():
                    self.account_table.setRowHidden(row, False)
                else:
                    self.account_table.setRowHidden(row, True)

            self.toggle_filter(filter_on=True)
        else:
            self.toggle_filter(filter_on=False)
    def toggle_filter(self, filter_on: bool):
        """Toggles the filtering widgets and state."""
        if filter_on:
            # Filtering is active
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            # Reset to show all data
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.clear()
            self.filter_combo_box.setCurrentIndex(0)
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)
            self.filter_label.setText("Data is Not Currently Filtered")
            
    def on_lookup_client(self):
        """Handles client lookup and toggles filter state."""
        client_number_text = self.client_number_edit.text().strip()
        try:
            client_number = int(client_number_text)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input",
                                "Client Number must be numeric.")
            self.reset_display()
            return

        if client_number not in self.client_listing:
            QMessageBox.warning(self, "Client Not Found",
                                f"Client {client_number} does not exist.")
            self.reset_display()
            return

        # Check if the client has accounts
        if client_number not in self.accounts:
            QMessageBox.warning(self, "No Accounts Found",
                                f"No accounts found for client {client_number}.")
            self.reset_display()
            return

        client = self.client_listing[client_number]
        self.client_info_label.setText(
            f"{client.first_name} {client.last_name}")
        self.populate_account_table(client_number)

        # Enable filter functionality when client has accounts
        self.filter_combo_box.setEnabled(True)
        self.filter_edit.setEnabled(True)
        self.filter_button.setEnabled(True)

        # Ensure the filtering state is reset when a new client is looked up
        self.toggle_filter(filter_on=False)


    def populate_account_table(self, client_number):
        """Populates the account table with the selected client's accounts."""
        self.account_table.setRowCount(0)  # Clear the table

        # Check if the client has accounts
        if client_number not in self.accounts:
            QMessageBox.warning(
                self, "No Accounts", f"No accounts found for client {client_number}."
            )
            return

        # Populate the table with account details
        for account in self.accounts[client_number]:
            row_position = self.account_table.rowCount()
            self.account_table.insertRow(row_position)

            # Add account details to the respective columns
            self.account_table.setItem(
                row_position, 0, QTableWidgetItem(str(account.account_number)))  # Account Number
            self.account_table.setItem(
                row_position, 1, QTableWidgetItem(f"${account.balance:,.2f}"))  # Account Type (from class name)
            self.account_table.setItem(
                row_position, 2, QTableWidgetItem(account.date_created.strftime('%Y-%m-%d')))  # Balance
            self.account_table.setItem(
                row_position, 3, QTableWidgetItem(account.__class__.__name__))  # Date Created

    def reset_display(self):
        """Resets the display when no client is found."""
        self.client_info_label.setText("")
        self.account_table.setRowCount(0)
        self.filter_label.setText("")
        self.filter_combo_box.setEnabled(False)
        self.filter_edit.setEnabled(False)
        self.filter_button.setEnabled(False)

    @Slot(int, int)
    def on_select_account(self, row: int, column: int):
        """Handles account selection from the table."""
        account_number_item = self.account_table.item(row, 0)
        if account_number_item:
            account_number = int(account_number_item.text())
            # You can handle additional logic for account selection
            print(f"Account Selected: {account_number}")

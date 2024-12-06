from datetime import date
# Base Strategy Class
from service_charge_strategy import ServiceChargeStrategy
from overdraft_strategy import OverdraftStrategy

class BankAccount:
    def __init__(self, account_number: int, client_number: int, balance: float, service_charge_strategy: ServiceChargeStrategy, date_created: date = None):
        # Validate account_number
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number

        # Validate client_number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        # Validate balance
        try:
            self.__balance = float(balance)
        except (TypeError, ValueError):
            self.__balance = 0.0

        # Assign service charge strategy
        self._service_charge_strategy = service_charge_strategy

        # Validate or assign date_created
        if date_created is None or not isinstance(date_created, date):
            self.__date_created = date.today()
        else:
            self.__date_created = date_created

    # Property for account_number
    @property
    def account_number(self):
        return self.__account_number

    # Property for client_number
    @property
    def client_number(self):
        return self.__client_number

    # Property for balance (with setter added)
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value: float):
        try:
            self.__balance = float(value)
        except (TypeError, ValueError):
            raise ValueError("Balance must be a numeric value.")

    # Property for date_created
    @property
    def date_created(self):
        return self.__date_created

    # Update balance method
    def update_balance(self, amount: float):
        try:
            amount = float(amount)
            self.__balance += amount
        except ValueError:
            pass  # Invalid amount, balance is not updated

    # Deposit method
    def deposit(self, amount: float):
        if not isinstance(amount, (int, float)):
            raise ValueError("Deposit amount must be numeric.")
        if amount <= 0:
            raise ValueError(f"Deposit amount: {amount} must be positive.")

        self.update_balance(amount)

    # Withdraw method
    def withdraw(self, amount: float):
        if not isinstance(amount, (int, float)):
            raise ValueError("Withdraw amount must be numeric.")
        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount: {amount} must not exceed the account balance: {self.__balance}.")
        if amount < 0:
            raise ValueError(f"Withdrawal amount: {amount} must be positive.")

        self.update_balance(-amount)

    # String representation
    def __str__(self):
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f} Date: {self.__date_created}"

    # Get service charges method
    def get_service_charges(self) -> float:
        # Delegate service charge calculation to the strategy
        return self._service_charge_strategy.calculate_service_charges(self)


# Create an instance of OverdraftStrategy
overdraft_strategy = OverdraftStrategy(300,900)  # Replace with actual arguments

# Create a BankAccount instance with OverdraftStrategy
account = BankAccount(3203265355, 3444444, 1000.00,
                      overdraft_strategy, date(2024, 10, 19))

# Withdraw a valid, positive amount
try:
    account.withdraw(200.00)  # Positive amount
    print(f"After withdrawal: {account.balance}")  # This will work fine
except ValueError as e:
    print(e)

# Attempt to withdraw 0.0 (which will raise the error)
try:
    account.withdraw(0.0)  # This will raise a ValueError
except ValueError as e:
    print(e)  # This will print "Withdrawal amount: 0.0 must be positive."

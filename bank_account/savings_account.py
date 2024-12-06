
# Import the strategy class
from abc import ABC, abstractmethod
from datetime import date
from bank_account import BankAccount
# Strategy Base Class


class ServiceChargeStrategy(ABC):
    @abstractmethod
    def calculate_service_charges(self, account) -> float:
        pass

# Default strategy (base service charge)


# Minimum Balance Strategy for Savings Account


class MinimumBalanceStrategy(ServiceChargeStrategy):
    def __init__(self, minimum_balance: float, premium_rate: float):
        self.__minimum_balance = minimum_balance
        self.__premium_rate = premium_rate

    def calculate_service_charges(self, account) -> float:
        # Apply premium service charge if balance is below the minimum balance
        if account.balance < self.__minimum_balance:
            return account.BASE_SERVICE_CHARGE * self.__premium_rate
        else:
            return account.BASE_SERVICE_CHARGE

class SavingsAccount(BankAccount):
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, minimum_balance: float, premium_rate: float):
        # Call the parent class (BankAccount) constructor to initialize common attributes
        super().__init__(account_number, client_number, balance, date_created)

        # Validate the minimum balance, default to 50 if invalid
        try:
            self.__minimum_balance = float(minimum_balance)
        except ValueError:
            self.__minimum_balance = 50.00

        # Initialize MinimumBalanceStrategy with minimum balance and premium rate
        self.__minimum_balance_strategy = MinimumBalanceStrategy(
            self.__minimum_balance, premium_rate)

    def __str__(self):
        # Superclass string representation with added SavingsAccount details
        account_info = super().__str__()
        return f"{account_info}\nMinimum Balance: ${self.__minimum_balance:,.2f} Account Type: Savings"

    # Override service charges calculation for SavingsAccount
    def get_service_charges(self) -> float:
        # Use MinimumBalanceStrategy to calculate the service charges
        return self.__minimum_balance_strategy.calculate_service_charges(self)


# Example usage
savings_account = SavingsAccount(
    12345678, 87654321, 500.00, date(2024, 5, 1), 1000.00, 2.00)

# Print account details and service charges
print(savings_account)
print(f"Service Charges: {savings_account.get_service_charges()}")

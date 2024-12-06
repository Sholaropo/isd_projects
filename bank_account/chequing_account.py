from datetime import date
from bank_account import BankAccount
from abc import ABC, abstractmethod

# Strategy Interface


class ServiceChargeStrategy(ABC):
    @abstractmethod
    def calculate_service_charges(self, account) -> float:
        pass

# Overdraft Strategy for Chequing Account


class OverdraftStrategy(ServiceChargeStrategy):
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account) -> float:
        if account.balance >= self.__overdraft_limit:
            return account.BASE_SERVICE_CHARGE
        else:
            overdraft_penalty = (self.__overdraft_limit -
                                 account.balance) * self.__overdraft_rate
            return round(account.BASE_SERVICE_CHARGE + overdraft_penalty, 2)



class ChequingAccount(BankAccount):

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, overdraft_limit: float, overdraft_rate: float):
        # Call the parent constructor
        super().__init__(account_number, client_number, balance, date_created)

        # Assign an instance of OverdraftStrategy with appropriate arguments
        self.__overdraft_strategy = OverdraftStrategy(
            overdraft_limit, overdraft_rate)

    # Override __str__ method to include overdraft information
    def __str__(self):
        base_str = super().__str__()  # Use the superclass __str__ method for common fields
        return (f"{base_str}\n"
                f"Overdraft Limit: ${self.__overdraft_strategy._OverdraftStrategy__overdraft_limit:,.2f} "
                f"Overdraft Rate: {self.__overdraft_strategy._OverdraftStrategy__overdraft_rate * 100:.2f}% Account Type: Chequing")

    # Override service charges calculation for ChequingAccount
    def get_service_charges(self) -> float:
        # Use OverdraftStrategy to calculate the service charges
        return self.__overdraft_strategy.calculate_service_charges(self)


# Use a proper date object here
newmy = ChequingAccount(2652727, 444444, 30000.00,
                        date(2024, 10, 19), 567.00, 0.04)

# Print account details and service charges
print(newmy)
print(f"Service Charges: {newmy.get_service_charges()}")

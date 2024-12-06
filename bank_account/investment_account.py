from datetime import date
from bank_account import BankAccount
from abc import ABC, abstractmethod


class ManagementFeeStrategy(BankAccount):
    def __init__(self, management_fee: float, ten_years_ago: date, date_created: date):
        self.__management_fee = management_fee
        self.__ten_years_ago = ten_years_ago
        self.__date_created = date_created

    def calculate_service_charges(self) -> float:
        if self.__date_created <= self.__ten_years_ago:
            return 0.0  # Fee is waived if the account is older than 10 years
        return self.__management_fee

class InvestmentAccount(BankAccount):
    # Class-level constant
    TEN_YEARS_AGO = date.today().replace(year=date.today().year - 10)

    def __init__(self, account_number, client_number, balance, date_created, management_fee):
        # Call the parent class (BankAccount) constructor to initialize common attributes
        super().__init__(account_number, client_number, balance, date_created)

        # Assign an instance of ManagementFeeStrategy with appropriate arguments
        self.__management_fee_strategy = ManagementFeeStrategy(
            management_fee, self.TEN_YEARS_AGO, date(2024, 10, 19))

    # Override __str__ method to include management fee information
    def __str__(self):
        management_fee_str = "Waived" if self.date_created <= self.TEN_YEARS_AGO else f"${self.__management_fee_strategy._ManagementFeeStrategy__management_fee:.2f}"
        return f"{super().__str__()} Management Fee: {management_fee_str}"

    # Override service charges calculation for InvestmentAccount
    def get_service_charges(self) -> float:
        # Use ManagementFeeStrategy to calculate the service charges
        return self.__management_fee_strategy.calculate_service_charges()


# Example of usage
new_account = InvestmentAccount(
    12345678, 87654321, 5000.00, date(2015, 5, 22), 100.00)

# Print account details and service charges
print(new_account)
# print(f"Service Charges: {new_account.get_service_charges()}")

from datetime import date
from bank_account import BankAccount


class ManagementFeeStrategy(BankAccount):
    def __init__(self, management_fee: float, ten_years_ago: date, date_created: date):
        self.__management_fee = management_fee
        self.__ten_years_ago = ten_years_ago
        self.__date_created = date_created

    def calculate_service_charges(self) -> float:
        if self.__date_created <= self.__ten_years_ago:
            return 0.0  # Fee is waived if the account is older than 10 years
        return self.__management_fee

from abc import ABC, abstractmethod

# Strategy Interface

class ServiceChargeStrategy(ABC):
    @abstractmethod
    def calculate_service_charges(self, account) -> float:
        pass

# Minimum Balance Strategy for Savings Account


class MinimumBalanceStrategy(ServiceChargeStrategy):
    def __init__(self, minimum_balance: float, premium_rate: float):
        self.__minimum_balance = minimum_balance
        self.__premium_rate = premium_rate

    def calculate_service_charges(self, account) -> float:
        # Apply premium service charge if balance is below the minimum balance
        if account < self.__minimum_balance:
            return account.BASE_SERVICE_CHARGE * self.__premium_rate
        else:
            return account.BASE_SERVICE_CHARGE
        
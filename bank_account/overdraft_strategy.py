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

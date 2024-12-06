from service_charge_strategy import ServiceChargeStrategy


class OverdraftStrategy(ServiceChargeStrategy):
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        self.overdraft_limit = overdraft_limit
        self.overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account) -> float:
        if account.balance < 0:
            return self.BASE_SERVICE_CHARGE + abs(account.balance) * self.overdraft_rate
        return self.BASE_SERVICE_CHARGE

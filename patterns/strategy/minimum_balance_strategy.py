from service_charge_strategy import ServiceChargeStrategy


class MinimumBalanceStrategy(ServiceChargeStrategy):
    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, minimum_balance):
        self._minimum_balance = minimum_balance

    def calculate_service_charges(self, account):
        if account.balance < self._minimum_balance:
            return self.BASE_SERVICE_CHARGE + self.SERVICE_CHARGE_PREMIUM
        return self.BASE_SERVICE_CHARGE
    

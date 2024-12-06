from datetime import date, timedelta
from service_charge_strategy import ServiceChargeStrategy


class ManagementFeeStrategy(ServiceChargeStrategy):
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, date_created, management_fee):
        self._date_created = date_created
        self._management_fee = management_fee

    def calculate_service_charges(self, account):
        if self._date_created < self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE + self._management_fee
        return self.BASE_SERVICE_CHARGE

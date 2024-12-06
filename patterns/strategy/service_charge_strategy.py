from abc import ABC, abstractmethod


class ServiceChargeStrategy(ABC):
    BASE_SERVICE_CHARGE: float = 0.50

    @abstractmethod
    def calculate_service_charges(self, account) -> float:
        """Abstract method to calculate service charges, to be overridden by subclasses."""
        pass

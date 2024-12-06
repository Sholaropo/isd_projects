from datetime import date
from abc import ABC, abstractmethod


class Client:
    def __init__(self, client_number, first_name, last_name, email):
        self.client_number = client_number
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def update(self, message):
        print(f"Notification for {self.first_name} {self.last_name}: {message}")


# Strategy Base Class
class ServiceChargeStrategy(ABC):
    @abstractmethod
    def calculate_service_charges(self, account) -> float:
        pass


class BaseServiceChargeStrategy(ServiceChargeStrategy):
    BASE_SERVICE_CHARGE = 0.50

    def calculate_service_charges(self, account) -> float:
        return self.BASE_SERVICE_CHARGE


# BankAccount Class
class BankAccount(ABC):
    BASE_SERVICE_CHARGE: float = 0.50

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date = None, service_charge_strategy: ServiceChargeStrategy = None):

        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number

        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        try:
            self.__balance = float(balance)
        except (TypeError, ValueError):
            self.__balance = 0.0

        if date_created is None or not isinstance(date_created, date):
            self.__date_created = date.today()
        else:
            self.__date_created = date_created

        if service_charge_strategy is None:
            self.service_charge_strategy = BaseServiceChargeStrategy()
        else:
            self.service_charge_strategy = service_charge_strategy

        self.observers = []  # List to hold observers (clients)

    @property
    def account_number(self):
        return self.__account_number

    @property
    def client_number(self):
        return self.__client_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value: float):
        try:
            self.__balance = float(value)
        except (TypeError, ValueError):
            raise ValueError("Balance must be a numeric value.")

    @property
    def date_created(self):
        return self.__date_created

    def attach(self, observer: Client):
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer: Client):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, message: str):
        for observer in self.observers:
            observer.update(message)

    def update_balance(self, amount: float):
        try:
            amount = float(amount)
            self.__balance += amount
            self.notify_observers(f"Balance updated by {amount}. New balance: {self.__balance}")
        except ValueError:
            pass

    def deposit(self, amount: float):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount: float):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount: {amount} exceeds the balance: {self.__balance}")

        self.update_balance(-amount)

    def __str__(self):
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f} Date: {self.__date_created}"

    def get_service_charges(self) -> float:
        return self.service_charge_strategy.calculate_service_charges(self)


# Create clients
client1 = Client(1, "John", "Doe", "johndoe@example.com")
client2 = Client(2, "Jane", "Doe", "janedoe@example.com")

# Create a BankAccount instance
account = BankAccount(3203265355, 3444444, 1000.00, date(2024, 10, 19))

# Attach clients to account
account.attach(client1)
account.attach(client2)

# Perform transactions
try:
    account.deposit(500.00)
    account.withdraw(300.00)
except ValueError as e:
    print(e)

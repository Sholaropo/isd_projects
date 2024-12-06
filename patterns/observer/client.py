from utility.file_utils import simulate_send_email
from datetime import datetime

class Observer:
    def update(self, message: str):
        raise NotImplementedError("Subclasses must override this method.")

class Client(Observer):
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        self.__client_number = client_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email_address = email_address

    def update(self, message: str):
        subject = f"ALERT: Unusual Activity: {datetime.now()}"
        email_message = f"Notification for {self.__client_number}: {self.__first_name} {self.__last_name}: {message}"
        simulate_send_email(self.__email_address, subject, email_message)

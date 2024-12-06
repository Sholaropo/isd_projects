"""
Description: A client program written to verify correctness of 
the BankAccount and Transaction classes.
Author: ACE Faculty
Edited by: Olusola Ropo
Date: 12/11/2024
"""
from bank_account.bank_account import BankAccount
from patterns.observer.client import Client


def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Transaction classes.
    """
    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.
    try:
        client = Client(client_number=67890, first_name="Sola", last_name="Ropo",
                        email_address="solaropo@gmail.com")
        print(f"Client created: {client}")
    except Exception as e:
        print(f"Error creating client: {e}")

    # 2. Declare a BankAccount object with an initial value of None.
    bank_account = None

    # 3. Using the bank_account object declared in step 2, code a statement
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the
    # BankAccount's client_number.
    # Use a floating point value for the balance.
    try:
        bank_account = BankAccount(
            account_number=12345, client_number=client.client_number, balance=1000.0)
        print(f"BankAccount created: {bank_account}")
    except Exception as e:
        print(f"Error creating bank account: {e}")

    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the
    # BankAccount's client_number.
    # Use an INVALID value (non-float) for the balance.
    try:
        invalid_bank_account = BankAccount(
            account_number=54321, client_number=client.client_number, balance="invalid_balance")
    except Exception as e:
        print(f"Error creating bank account with invalid balance: {e}")

    # 5. Code a statement which prints the Client instance created in step 1.
    # Code a statement which prints the BankAccount instance created in step 3.
    print(f"Client Details: {client}")
    print(f"BankAccount Details: {bank_account}")

    # 6. Attempt to deposit a non-numeric value into the BankAccount created in step 3.
    try:
        bank_account.deposit("invalid_deposit")
    except Exception as e:
        print(f"Error depositing non-numeric value: {e}")

    # 7. Attempt to deposit a negative value into the BankAccount created in step 3.
    try:
        bank_account.deposit(-500.0)
    except Exception as e:
        print(f"Error depositing negative value: {e}")

    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount created in step 3.
    try:
        bank_account.withdraw(200.0)
        print(f"Withdrawal successful. New balance: {bank_account.balance}")
    except Exception as e:
        print(f"Error withdrawing valid amount: {e}")

    # 9. Attempt to withdraw a non-numeric value from the BankAccount created in step 3.
    try:
        bank_account.withdraw("invalid_withdraw")
    except Exception as e:
        print(f"Error withdrawing non-numeric value: {e}")

    # 10. Attempt to withdraw a negative value from the BankAccount created in step 3.
    try:
        bank_account.withdraw(-100.0)
    except Exception as e:
        print(f"Error withdrawing negative value: {e}")

    # 11. Attempt to withdraw a value from the BankAccount created in step 3 which
    # exceeds the current balance of the account.
    try:
        bank_account.withdraw(2000.0)
    except Exception as e:
        print(f"Error withdrawing amount exceeding balance: {e}")

    # 12. Code a statement which prints the BankAccount instance created in step 3.
    print(f"Final BankAccount Details: {bank_account}")


if __name__ == "__main__":
    main()

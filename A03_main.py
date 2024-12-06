"""
Description: A client program written to verify implementation 
of the Observer Pattern.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""

# 1. Import all BankAccount types using the bank_account package
# from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.bank_account import Client

# 2. Create a Client object with data of your choice.
client1 = Client(1, "John", "Doe", "johndoe@example.com")

# 3a. Create a ChequingAccount object with data of your choice.
chequing_account = ChequingAccount(2652727, 444444, 30000.00, client1.client_id, 567.00, 0.04)

# 3b. Create a SavingsAccount object with data of your choice.
savings_account = SavingsAccount(
    client1.client_id, 87654321, 500.00, '2024, 5, 1', 1000.00, 2.00)

# 4a. Attach the Client object to the ChequingAccount object.
chequing_account.attach(client1)


# 4b. Attach the Client object to the SavingsAccount object.
savings_account.attach(client1)

# 5a. Create a second Client object with data of your choice.
client2 = Client(2, "Jane", "Smith", "janesmith@example.com")

# 5b. Create a SavingsAccount object with data of your choice.
savings_account2 = SavingsAccount(
    client1.client_id, 5647848, 500.00, '2024, 5, 1', 2000.00, 2.00)
savings_account2.attach(client2)

# 6. Perform transactions
# Transactions for ChequingAccount
try:
    chequing_account.deposit(200.0)  # This should notify client1
    chequing_account.withdraw(100.0)  # This should notify client1
    # This should raise an exception (insufficient funds)
    chequing_account.withdraw(700.0)
except ValueError as e:
    print(e)

# Transactions for SavingsAccount
try:
    savings_account.deposit(300.0)  # This should notify client1
    savings_account.withdraw(500.0)  # This should notify client1
    # This should raise an exception (insufficient funds)
    savings_account.withdraw(900.0)
except ValueError as e:
    print(e)

# Transactions for SavingsAccount2
try:
    savings_account2.deposit(200.0)  # This should notify client2
    savings_account2.withdraw(200.0)  # This should notify client2
    # This should raise an exception (insufficient funds)
    savings_account2.withdraw(800.0)
except ValueError as e:
    print(e)

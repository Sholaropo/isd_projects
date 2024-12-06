"""
Description: A client program written to verify the correctness of 
the BankAccount subclasses.
Author: ACE Faculty
Edited by: Olusola Ropo
Date: 12/11/2024
"""

# 1. Import all BankAccount types using the bank_account package
#    Import date from datetime
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount
from datetime import date

# 2. Create an instance of a ChequingAccount with values of your
# choice including a balance which is below the overdraft limit.
chequing_account = ChequingAccount(
    account_number=123456,
    client_number=98765,
    balance=50.0,  # Below the overdraft limit
    date_created=date(2023, 1, 1),
    overdraft_limit=100.0,
    overdraft_rate=5.0
)

# 3. Print the ChequingAccount created in step 2.
print(chequing_account)
# 3b. Print the service charges amount if calculated based on the
# current state of the ChequingAccount created in step 2.
print("Service Charges:", chequing_account.get_service_charges())

# 4a. Use ChequingAccount instance created in step 2 to deposit
# enough money into the chequing account to avoid overdraft fees.
chequing_account.deposit(100.0)  # Deposit to avoid overdraft fees
# 4b. Print the ChequingAccount
print(chequing_account)
# 4c. Print the service charges amount if calculated based on the
# current state of the ChequingAccount created in step 2.
print("Service Charges after deposit:", chequing_account.get_service_charges())

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your
# choice including a balance which is above the minimum balance.
savings_account = SavingsAccount(
    account_number=234567,
    client_number=87654,
    balance=500.0,  # Above minimum balance
    date_created=date(2022, 5, 15),
    minimum_balance=100.0,
    premium_rate=20.0
)

# 6. Print the SavingsAccount created in step 5.
print(savings_account)
# 6b. Print the service charges amount if calculated based on the
# current state of the SavingsAccount created in step 5.
print("Service Charges:", savings_account.get_service_charges())

# 7a. Use this SavingsAccount instance created in step 5 to withdraw
# enough money from the savings account to cause the balance to fall
# below the minimum balance.
savings_account.withdraw(450.0)  # Withdraw to drop below minimum balance
# 7b. Print the SavingsAccount.
print(savings_account)
# 7c. Print the service charges amount if calculated based on the
# current state of the SavingsAccount created in step 5.
print("Service Charges after withdrawal:",
      savings_account.get_service_charges())

print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your
# choice including a date created within the last 10 years.
investment_account_recent = InvestmentAccount(
    account_number=345678,
    client_number=76543,
    balance=2000.0,
    date_created=date(2018, 8, 20),
    management_fee=0.02
)

# 9a. Print the InvestmentAccount created in step 8.
print(investment_account_recent)
# 9b. Print the service charges amount if calculated based on the
# current state of the InvestmentAccount created in step 8.
print("Service Charges:", investment_account_recent.get_service_charges())

# 10. Create an instance of an InvestmentAccount with values of your
# choice including a date created prior to 10 years ago.
investment_account_old = InvestmentAccount(
    account_number=456789,
    client_number=65432,
    balance=1500.0,
    date_created=date(2000, 6, 15),
    management_fee=0.015
)

# 11a. Print the InvestmentAccount created in step 10.
print(investment_account_old)
# 11b. Print the service charges amount if calculated based on the
# current state of the InvestmentAccount created in step 10.
print("Service Charges:", investment_account_old.get_service_charges())

print("===================================================")
# 12. Update the balance of each account created in steps 2, 5, 8, and 10
# by using the withdraw method of the superclass and withdrawing
# the service charges determined by each instance invoking the
# polymorphic get_service_charges method.

# Withdraw service charges from each account's balance
chequing_account.withdraw(chequing_account.get_service_charges())
savings_account.withdraw(savings_account.get_service_charges())
investment_account_recent.withdraw(
    investment_account_recent.get_service_charges())
investment_account_old.withdraw(investment_account_old.get_service_charges())

# 13. Print each of the bank account objects created in steps 2, 5, 8, and 10.
print(chequing_account)
print(savings_account)
print(investment_account_recent)
print(investment_account_old)

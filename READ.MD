## Assignment


# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each 
assignment will build on the work done in the previous assignment(s).  Ultimately, 
an entire system will be created to manage bank transactions for clients who 
have one or more bank accounts.

## Author
Olushola Ropo

Assignment 1: [Indicate the name and description of the current assignment]

## Encapsulation
[use this section to explain how Encapsulation was achieved in the BankAccount and Transaction classes.]


Assignment 2: This assignment will extend the BankAccount class created in your previous assignment. The BankAccount class will be used as a superclass from which more specific subclasses will be derived. Each subclass will inherit attributes and methods from the superclass, and will incorporate functionality specific to the subclass. Polymorphism will be realized by having each subclass provide their own unique implementation to a superclass method. Unit testing in this assignment will be limited to verifying the expected polymorphic behaviour.

## Polymorphism

Polymorphism in the `BankAccount` subclasses (`ChequingAccount`, `SavingsAccount`, and `InvestmentAccount`) is achieved by overriding and extending the methods from the base `BankAccount` class. Each subclass provides specific implementations for the `get_service_charges()` and `__str__()` methods, tailored to the rules of each account type. This allows instances of different account types to respond to the same method calls (e.g., `get_service_charges()`) but perform their own unique behaviors depending on the type of account.


## Event-Driven Programming Paradigm
In this banking application, the Event-Driven Programming Paradigm is employed to manage user interactions and system responses based on events (such as clicks, text input, or selections). This paradigm enables the system to react to user actions asynchronously, ensuring a responsive and dynamic user interface.

Some of the events include: Button Clicks events, ComboBox Selection, Table Cell Clicks, filter event and so on.


## Filtering
The filtering functionality allows users to refine their search for account details by applying various conditions such as account type, balance range, and date created. This feature makes it easier to manage and view specific account information from a larger dataset.


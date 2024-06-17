# 💰 Bank Account Management System 💳

Welcome to the **Bank Account Management System**! This Python application provides a simple command-line interface for managing bank accounts. Create accounts, deposit and withdraw money, transfer funds, check balances, change the bank name, and even clone accounts—all with ease! 🚀

## 🌟 Features

- **🆕 Create Account**: Easily create new bank accounts with an initial balance.
- **💸 Deposit Money**: Deposit money in INR or USD (with automatic conversion to INR).
- **🏧 Withdraw Money**: Withdraw money from your account, ensuring sufficient funds.
- **🔄 Transfer Money**: Transfer funds between accounts seamlessly.
- **💹 Check Balance**: Check the current balance of any account.
- **🏦 Change Bank Name**: Update the bank name for all accounts.
- **🔍 Clone Account**: Create a clone of an existing account with a new account number.

## 🚀 Getting Started
- **💿The main data structure that is being used is: `dictionary`**

### 📋 Prerequisites

- Python 3.x 🐍

### 📜 Menu Options

1. **🆕 Create Account**: Enter the account number and initial balance to create a new account.
2. **💸 Deposit Money**: Enter the account number, amount, and currency (default is INR) to deposit money.
3. **🏧 Withdraw Money**: Enter the account number and amount to withdraw money.
4. **🔄 Transfer Money**: Enter the source and target account numbers and the amount to transfer funds.
5. **💹 Check Balance**: Enter the account number to check the current balance.
6. **🏦 Change Bank Name**: Enter the new bank name to update it for all accounts.
7. **🔍 Clone Account**: Enter the account number to clone and the new account number for the clone.
8. **🚪 Exit**: Exit the application.

## 🧩 Code Overview

### 🏛️ Class Definition

- **BankAccount**: Represents a bank account with attributes like account number and balance. It includes methods for depositing, withdrawing, transferring funds, checking balance, and more.

### 🔧 Methods

- **Constructor (`__init__`)**: Initializes a new instance of `BankAccount`.
- **Destructor (`__del__`)**: Prints a message when an account is deleted.
- **Deposit**: Adds money to the account balance.
- **Withdraw**: Deducts money from the account balance.
- **Transfer**: Transfers money to another account.
- **Get Balance**: Returns the current balance.
- **Change Bank Name**: Updates the bank name for all accounts.
- **Is Valid Account Number**: Checks if an account number is valid.
- **String Representation (`__str__`)**: Returns a string representation of the account.
- **Clone**: Creates a clone of the account.

### 🏗️ Main Function

- **main()**: Manages user interaction with the bank account system through a menu-driven interface.

## 📧 Contact

For any inquiries or feedback, please contact [arreyanhamid@icloud.com](mailto:arreyanhamid@icloud.com).

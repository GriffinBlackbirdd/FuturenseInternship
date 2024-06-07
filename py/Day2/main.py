class BankAccount:
    bank_name = "Futurense Global Bank"

    # Here I am using the constructor, which is also a special method in python.
    def __init__(self, account_number=0, balance=0.0):
        self.__account_number = account_number #The double underscore before the variable names makes it hidden or private.
        self.__balance = balance

    # Here I am using the destructor, which is the exact ooosite of the constructor.
    def __del__(self):
        print(f"Account {self.__account_number} will be deleted")

    # This is the normal method
    # This deposit method checks if the account number exists in the dictionary that we are using, if True then it deposits the amount in the BankAccount object.
    def deposit(self, amount, currency="INR"):  # Here I am using a default parameter that is INR for method overloading.
        if currency == "INR":
            self.__balance += amount
        elif currency == "USD":
            self.__balance += amount * 83.00 # Here I am using the current exchange rate of 1 USD to INR.

    # Normal
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    # Normal
    def transfer(self, target_account, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            target_account.__balance += amount

    # Normal
    def get_balance(self):
        return self.__balance

    # Using the class method here which is initialised by using the @classmethod DECORATOR.
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    # Using the static method here which is initialised by using the @staticmethod DECORATOR.
    @staticmethod
    def is_valid_account_number(account_number):
        return isinstance(account_number, int) and account_number > 0

    # Special Method
    def __str__(self):
        return f"Account({self.__account_number}, Balance: {self.__balance})"

    # Using the special method __new__ to create a new instance of the class.
    def __new__(cls, *args, **kwargs):
        instance = super(BankAccount, cls).__new__(cls)
        return instance

    # Using the return statement to return a new instance of the class.
    def clone(self):
        return BankAccount(self.__account_number, self.__balance)

    # Data hiding method
    def __hidden_method(self):
        print("This is a hidden method")
def main():
    accounts = {} # This is the Data Structure
    while True:
        print("\n--- Bank Account Management System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Check Balance")
        print("6. Change Bank Name")
        print("7. Clone Account")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = int(input("Enter account number: "))
            balance = float(input("Enter initial balance: "))
            accounts[account_number] = BankAccount(account_number, balance)
            print(f"Account {account_number} created successfully.")

        elif choice == '2':
            account_number = int(input("Enter account number: "))
            if account_number in accounts:
                amount = float(input("Enter amount to deposit: "))
                currency = input("Enter currency (default is INR): ") or "USD"
                accounts[account_number].deposit(amount, currency)
                print(f"Deposited {amount}INR only {currency} to account {account_number}.")
            else:
                print("Account not found.")

        elif choice == '3':
            account_number = int(input("Enter account number: "))
            if account_number in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[account_number].withdraw(amount)
                print(f"Withdrew {amount}INR only from account {account_number}.")
            else:
                print("Account not found.")

        elif choice == '4':
            source_account_number = int(input("Enter source account number: "))
            target_account_number = int(input("Enter target account number: "))
            if source_account_number in accounts and target_account_number in accounts:
                amount = float(input("Enter amount to transfer: "))
                accounts[source_account_number].transfer(accounts[target_account_number], amount)
                print(f"Transferred {amount}INR only from account {source_account_number} to account {target_account_number}.")
            else:
                print("One or both accounts not found.")

        elif choice == '5':
            account_number = int(input("Enter account number: "))
            if account_number in accounts:
                balance = accounts[account_number].get_balance()
                print(f"Balance for account {account_number} is {balance}INR only.")
            else:
                print("Account not found.")

        elif choice == '6':
            new_name = input("Enter new bank name: ")
            BankAccount.change_bank_name(new_name)
            print(f"Bank name changed to {new_name}.")

        elif choice == '7':
            account_number = int(input("Enter account number to clone: "))
            if account_number in accounts:
                new_account = accounts[account_number].clone()
                new_account_number = int(input("Enter new account number for the clone: "))
                new_account._BankAccount__account_number = new_account_number
                accounts[new_account_number] = new_account
                print(f"Account {account_number} cloned to new account {new_account_number}.")
            else:
                print("Account not found.")

        elif choice == '8':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
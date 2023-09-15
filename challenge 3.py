
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Withdrawal amount exceeds account balance or is invalid."

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}"

# Example usage:
if __name__ == "__main__":
    # Create a BankAccount instance
    my_account = BankAccount("1234567890", "John Doe", 1000.0)

    # Test deposit and withdrawal
    print(my_account.display_balance())  # Display initial balance
    print(my_account.deposit(500.0))     # Deposit $500
    print(my_account.withdraw(200.0))    # Withdraw $200
    print(my_account.display_balance())  # Display updated balance
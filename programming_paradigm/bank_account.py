class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional initial balance (default = 0)."""
        self.__account_balance = initial_balance   # private attribute for encapsulation

    def deposit(self, amount):
        """Add amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw amount if sufficient funds exist."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
    """Print the current balance in a user-friendly format with 2 decimals."""
    print(f"Current Balance: ${self.__account_balance:.2f}")
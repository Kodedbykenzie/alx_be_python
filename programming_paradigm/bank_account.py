class BankAccount:
    """A simple Bank Account class."""

    def __init__(self, initial_balance=0):
        """Initialize account balance with an optional initial amount (default 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a given amount into the account."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw a given amount if funds are sufficient."""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.account_balance}")

# Create a BankAccount class with the attributes interest rate and balance
class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = .01
        self.balance = 0

# Add a deposit method to the BankAccount class

    def deposit(self, amount):
        self.balance += amount
        return self
# Add a withdraw method to the BankAccount class

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 5
            print('Insufficient funds: Charging a $5 fee')
        return self

# Add a display_account_info method to the BankAccount class

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

# Add a yield_interest method to the BankAccount class

    def yield_interest(self):
        if self.balance >= 0:
            self.balance = 1 + 1*self.int_rate
        return self


# Create 2 accounts
Luci_account = BankAccount()
Shirley_account = BankAccount()

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
Luci_account.deposit(66).deposit(599).deposit(31).withdraw(
    30).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
Shirley_account.deposit(66).deposit(599).withdraw(10).withdraw(
    400).withdraw(30).yield_interest().display_account_info()
# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)


@classmethod
def all_balances(cls):
    sum = 0
    for account in cls.all_accounts:
        sum += account.balance
    return sum
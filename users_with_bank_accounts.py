# Assignment: Users with Bank Accounts
class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

# Add a deposit method to the BankAccount class

    def make_deposit(self, amount):
        self.balance += amount
        return self
# Add a withdraw method to the BankAccount class

    def make_withdrawl(self, amount):
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
            self.balance = self.balance + self.balance*self.int_rate
        return self


# Update the User class __init__ method
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

# Update the User class make_deposit method
    def deposit(self, amount):
        self.account.make_deposit(amount)
        print(self.account.balance)
        return self

# Update the User class make_withdrawal method
    def withdrawl(self, amount):
        self.account.make_withdrawl(amount)
        print(self.account.balance)
        return self

    def transfer(self, amount, user_two):
        self.account.make_withdrawl(amount)
        user_two.account.make_deposit(amount)
        print(self.name,self.account.balance)
        print(user_two.name,user_two.account.balance)
        return self

# Update the User class display_user_balance method
    def display_user_balance(self):
        print(self.account.display_account_info())
        return self

luci = User("Lucifurr","lucifurr@numnums.com")
shirley = User("Shirley","shirley@youcan'tbeserious.com")
luci.deposit(100).withdrawl(10).transfer(200, shirley).display_user_balance()
shirley.deposit(100).withdrawl(10).transfer(200, shirley).display_user_balance()

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
#change account option
#add second account option

# Create a BankAccount class with the attributes interest rate and balance
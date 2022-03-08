# Assignment: Users with Bank Accounts
class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

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
            self.balance = self.balance + self.balance*self.int_rate
        return self


# Update the User class __init__ method
class User:
    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

# Update the User class make_deposit method
    def deposit(self):
        self.account.deposit(100)
        print(self.account.balance)

# Update the User class make_withdrawal method
    def withdrawal(self):
        self.account.withdrawal(100)
        print(self.account.balance)

# Update the User class display_user_balance method
    def display_user_balance(self):
        print(self.account.balance)
# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
#change account option
#add second account option

# Create a BankAccount class with the attributes interest rate and balance
class User:
    @classmethod
    def add_bank_account(self, int_rate, balance)
            
            return self

#     def deposit(self,which_account):
#         self.account.deposit(100)
#         print(self.account.balance)
#         return cls

#     def withdrawal(self):
#         self.account.withdrawal(100)
#         print(self.account.balance)

    # def display_user_balance(self):
    #     print(self.account.balance)

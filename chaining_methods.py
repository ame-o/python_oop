# In the last assignment, your code might have looked something like this:

class User:
    def __init__(self , name, account_balance):
        self.name = name
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance+= amount
        return self
# Add a make_withdrawal method to the User class

    def make_withdrawal(self, amount):
        self.account_balance-=amount
        return self

    def display_balance(self):
        print(f"{self.name}, your balance shows as ${self.account_balance}.")
        return self

    def transfer_money(self, amount, user2):
        self.account_balance-=amount
        user2.account_balance+=amount
        print(f"{self.name}, your balance shows as ${self.account_balance}.")
        print(f"{user2.name}, your balance shows as ${user2.account_balance}.")
        return self



    
# Create 3 instances of the User class
america = User("America", 1200)
asia = User("Asia",200)
memory = User("Memory",200)


# class User:
#     def make_deposit(self, amount):
#         # your code goes here...
#         return self
# copy
# The practice of having OOP return its own instance is pretty common and is done in other programming languages, though the variable name in some languages is not self, but instead this.

america.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(499).display_balance().transfer_money(500,memory)

asia.make_deposit(100).make_deposit(500).make_withdrawal(100).make_withdrawal(300).display_balance()

memory.make_deposit(900).make_withdrawal(100).make_withdrawal(300).make_withdrawal(300).display_balance()





# Update your previous assignment so that each instance's methods are chained
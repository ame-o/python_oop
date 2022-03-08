# Assignment: User
# Objectives:
# Practice creating a class and making instances from it
# Practice accessing the methods and attributes of different instances

# Create a file with the User class, including the __init__ and make_deposit methods
class User:
    def __init__(self , name, account_balance):
        self.name = name
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance+=amount
# Add a make_withdrawal method to the User class

    def make_withdrawal(self, amount):
        self.account_balance-=amount
    def transfer_money(self, amount, user2):
        self.account_balance-=amount
        user2.account_balance+=amount
        print(self.name,self.account_balance)
        print(user2.name,user2.account_balance)

# Add a display_user_balance method to the User class

    def display_balance(self):
        print(self.name,self.account_balance)
    
# Create 3 instances of the User class
america = User("America",1200)
asia = User("Asia",200)
memory = User("Memory",200)


# Have the first user make 3 deposits and 1 withdrawal and then display their balance
america.make_deposit(100)
america.make_deposit(100)
america.make_deposit(100)
america.make_withdrawal(499)
america.display_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
asia.make_deposit(100)
asia.make_deposit(500)
asia.make_withdrawal(100)
asia.make_withdrawal(300)
asia.display_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
memory.make_deposit(900)
memory.make_withdrawal(100)
memory.make_withdrawal(300)
memory.make_withdrawal(300)
memory.display_balance()

#BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
america.transfer_money(500,memory)


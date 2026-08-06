class BankAccount():

    def __init__(self,holder, balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f'Deposit Completed')


    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance-=amount
            print(f'Withdrawl Completed')

        else:
            print("Insuffecient Balance")
            print(f'Withdrawl Failed')


    def show_balance(self):
        print(f'Your Balance is {self.balance}')


h1=BankAccount("Devanshu",100000)

print(h1.holder)

# h1.deposit(100)

h1.withdraw(1000)

h1.show_balance()


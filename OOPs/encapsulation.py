# Revision of encapsulation in Python

# Bank Deposit and Withdrawal System

# Parent Class
class Bank:
    # Constructor
    def __init__(self, Account: str, balance:int) -> None:
        self.Account = Account
        self.__balance = balance

    # Method for getting the balance
    def get_balance(self) -> int:
        return self.__balance

    # Method for depositing money
    def deposit(self, amount: int) -> None:
        self.__balance += amount

    def withdraw(self, amount:int) -> None:
        if amount > self.__balance:
            print("Not Enough Balance in your Account")
            return
        self.__balance -= amount    

    def display(self) -> None:
        print(f"Name of the Account Holder is {self.Account} and the balance: {self.__balance}\n")

# Object Creation
Anand = Bank("Anand Vishwakarma", 1000)
Anand.display()            

Anand.__balance = 1000000000
# Anand.deposit(500)
# Anand.display()  

print(Anand.get_balance())

# Anand.withdraw(200)
# Anand.display() 
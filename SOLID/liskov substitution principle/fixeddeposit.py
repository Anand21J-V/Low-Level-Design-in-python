from bankaccount import BankAccount

class FixedDeposit(BankAccount):
    def __init__(self, balance: float) -> None:
        super().__init__(balance)

    def deposit(self, amount: float) -> None:
        self.balance += amount
        print(f"Depositing {self.balance} into the fixed deposit")     
from withdrawble_account import WithdrawbleAccount

class SavingsAccount(WithdrawbleAccount):
    def __init__(self, balance: float) -> None:
        super().__init__(balance)

    def deposit(self, amount: float) -> None:
        print(f"Depositing {self.balance + amount} into the savings account")

    def withdraw(self, amount: float) -> None:
        print(f"Withdrawing {amount} from savings account") 


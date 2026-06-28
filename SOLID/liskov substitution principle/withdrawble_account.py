from abc import ABC, abstractmethod

from bankaccount import BankAccount

class WithdrawbleAccount(BankAccount):
    def __init__(self, balance: float) -> None:
        super().__init__(balance)

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass    
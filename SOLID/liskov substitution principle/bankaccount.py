from abc import ABC, abstractmethod

class BankAccount:
    def __init__(self, balance: float) -> None:
        self.balance = balance

    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

        
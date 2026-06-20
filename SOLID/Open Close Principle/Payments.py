# Open Close Principle
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class UPI(Payment):
    def pay(self, amount: float) -> None:
        print(f"Transaction of {amount} completed using UPI")

class CreditCard(Payment):
    def pay(self, amount: float) -> None:
        print(f"Transaction of {amount} completed using CreditCard")

# ADDING NEW PAYMENT METHOD - OPEN FOR EXTENSION
class DebitCard(Payment):
    def pay(self, amount: float) -> None:
        print(f"Transaction of {amount} completed using DebitCard")

class PaymentProcessor:
    def process_payment(self, payment: Payment, amount: float) -> None:
        payment.pay(amount)

UPI = UPI()
credit = CreditCard()
debit = DebitCard()
Process_payment = PaymentProcessor()
Process_payment.process_payment(UPI, 5000)
Process_payment.process_payment(credit, 5000)
Process_payment.process_payment(debit, 5000)
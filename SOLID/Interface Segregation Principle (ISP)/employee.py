from workable import Workable
from eatable import Eatable

class Employee(Workable, Eatable):
    def eat(self) -> None:
        print("Employee is Eating")

    def work(self) -> None:
        print("Employee is Working")
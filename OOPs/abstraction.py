# Revision of abstraction in Python

from abc import ABC, abstractmethod

# Parent Class
class Shape(ABC):

    # Abstract Method for area
    @abstractmethod
    def area(self) -> float:
        pass

    # Abstract Method for perimeter
    @abstractmethod
    def perimeter(self) -> float:
        pass

# Child Class
class rectangle(Shape):
    def __init__(self, length: float, breadth: float) -> None:
        self.length = length
        self.breadth = breadth

    def area(self) -> float:
        print("RECTANGLE CLASS")
        print(f"The area of the rectangle is {self.length * self.breadth}")    

    def perimeter(self) -> float:
        print(f"The perimeter of the rectangle is {2 * (self.length + self.breadth)}\n")

# Child Class
class Square(Shape):
    def __init__(self, length: float) -> None:
        self.length = length

    def area(self):
        print("SQUARE CLASS")
        print(f"The area of the square is {self.length * self.length}")    

    def perimeter(self) -> float:
        print(f"The perimeter of the square is {4 * self.length}")

# Object Creation
rect = rectangle(10, 20)
rect.area()
rect.perimeter()

square = Square(10)
square.area()   
square.perimeter()
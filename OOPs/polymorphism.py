# Revision of polymorphism in Python

# Class Creation
class Animal:
    # Constructor
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # Method Creation under Animal Class
    def move(self) -> None:
        print("Animal is moving")

# Child Class using Animal Class as Parent Class
class Dog(Animal):
    # Method Creation under Dog Class (Method is overridden from Animal Class) -> This is known as Polymorphism
    def move(self) -> None:
        print("Dog is Moving")

# Object Creation
dog = Dog("Maxxy", 5)
dog.move()

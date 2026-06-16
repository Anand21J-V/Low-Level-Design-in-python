# Revision of inheritance in Python

# Parent Class
class Animal:
    # Constructor
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # Method
    def eat(self) -> None:
        print(f"{self.name} is eating")
 
    # Method
    def move(self) -> None:
        print(f"{self.name} is moving")

# Child Class
class dog(Animal):
    # Constructor
    def __init__(self, name: str, age: int, breed: str) -> None:
        # Calling the constructor of the parent class
        super().__init__(name, age)
        self.breed = breed

    # Display Method
    def display(self) -> None:
        print(f"{self.name} is a dog and is {self.age} years old and the breed is {self.breed}")

# Object Creation
max = dog("Maxxy", 5, "Labrador")   
max.display()
# print(max)           
# Revision of classes and objects and OOPs concepts

# Class Creation
class Animal:
    def __init__(self, name: str, age: int) -> None:  # Initializer method (Will get called when object is created)
        self.name = name
        self.age = age

    # Method for displaying the attributes of the object
    def display(self) -> None:
        print(f"Name of the Animal is {self.name} and the age is {self.age}")    

# Object Creation
dog = Animal("Maxxy", 5)
print(dog)
dog.display()
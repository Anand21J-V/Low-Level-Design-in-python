# Single Responsibility Principle

# Single Responsibility Principle states that a class should have only one responsibility and should be responsible for only one thing.
# If a class has more than one responsibility, it should be split into multiple classes.
# The Single Responsibility Principle is a fundamental principle of object-oriented programming that promotes code organization, maintainability, and readability.
# It is one of the SOLID principles, which stands for Single Responsibility Principle, Open/Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, and Dependency Inversion Principle.
# The Single Responsibility Principle is a key concept in creating clean, maintainable, and scalable code.
# It helps in creating classes that are focused on a single responsibility, making them easier to understand, test, and modify.
# By adhering to the Single Responsibility Principle, developers can create more modular and reusable code, which is essential for building robust and maintainable software systems.

from user import User
from userRepository import userRepository

anand = User("Anand", 20, "anand@gmail.com")
anand.get_student_info()

anand_db = userRepository()
anand_db.save_to_database(anand)
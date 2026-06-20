class User:
    def __init__(self, name: str, age:int, email: str) -> None:
        self.name = name
        self.age = age
        self.email = email

    def get_student_info(self):
        print(f"Name of the Student is {self.name} and age is {self.age} and email is {self.email}")
        
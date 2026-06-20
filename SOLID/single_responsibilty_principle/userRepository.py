from user import User

class userRepository:
    def save_to_database(self, user: "User") -> None:
        print(f"Saving the {user.name} to the database")

class User:
    """User Profile"""
    def __init__(self,first_name,last_name,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    def describe_user(self):
        """Return a neatly formatted user information."""
        description = print(f"{self.first_name} {self.last_name}:{self.age}:{self.gender}")

    def greet_user(self):
        """Print a greeting"""
        greeting = print(f"Hello {self.first_name} {self.last_name}!\n"
                    f"your age is {self.age}!\n"
                    f"and you are {self.gender}.")

talha = User("Talha","Ahmed","28","male")
talha.describe_user()
talha.greet_user()
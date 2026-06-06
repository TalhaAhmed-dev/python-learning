class User:
    """User Profile"""
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """Return a neatly formatted user information."""
        description = f"{self.first_name} {self.last_name}"
        return description

    def greet_user(self):
        """Print a greeting"""
        greeting =f"Hello {self.first_name} {self.last_name}!"
        return greeting

    def attempts(self):
        """print login attempts"""
        print(f"You have {self.login_attempts} login attempts.")

    def increment_login_attempt(self):
        """Increment the login attempts."""
        self.login_attempts += 1


    def reset_login_method(self):
        """Reset the login attempts to 0."""
        self.login_attempts = 0
class Admin(User):
    """Admin Profile"""
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = [
            "can add post",
            "can delete post",
        "can ban user"]

    def show_privilges(self):
        print("An administrator can:")
        for privilege in self.privileges:
            print(privilege)
Admin1 = Admin(first_name="Talha ",last_name="Ahmed")
print(Admin1.describe_user())
Admin1.show_privilges()





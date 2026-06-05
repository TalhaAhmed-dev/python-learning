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

user1 = User("Talha","Ahmed")
user1.attempts()
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.attempts()
user1.reset_login_method()
user1.attempts()


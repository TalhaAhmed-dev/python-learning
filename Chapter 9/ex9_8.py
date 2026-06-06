class User:
    """User Profile"""
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
class Privileges:
    """Class to represent a admin's privileges."""
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"]

    def show_privileges(self):
        print("An administrator can:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
        def __init__(self, first_name, last_name):
            super().__init__(first_name, last_name)

            self.privileges = Privileges()

if __name__ == "__main__":
    admin1 = Admin("Talha","Ahmed")
    admin1.privileges.show_privileges()
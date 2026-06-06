class Restaurant:
    def __init__(self,name,type):
        self.name = name.upper()
        self.type = type
    def describe_restaurant(self):
        print(f"Name of restaurant is {self.name} and type is {self.type}")

    def open_restaurant(self):
        print(f"The {self.name.upper()} is open now.")

my_restaurant = Restaurant("momo palace","momo's and Dumplings")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print(f"Name of restaurant : {my_restaurant.name}\nType of restaurant : {my_restaurant.type}\n{my_restaurant.name} is open now.")
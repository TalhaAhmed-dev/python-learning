class Restaurant:
    def __init__(self,name,type):
        self.name = name.title()
        self.type = type
    def describe_restaurant(self):
        print(f"Name of restaurant is {self.name} and type is {self.type}")

    def open_restaurant(self):
        print(f"The {self.name} is open now.")

talha = Restaurant("Momo palace","Momo's.")
fatima = Restaurant("Fafu fries","Fries.")
taha = Restaurant("K Pops","Korean.")

talha.describe_restaurant()
fatima.describe_restaurant()
taha.describe_restaurant()
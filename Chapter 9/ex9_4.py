class Restaurant:
    def __init__(self,name,type):
        self.name = name.upper()
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Name of restaurant is {self.name} and type is {self.type}")


    def served_customer(self):

        print(f"{self.number_served} people are served now.")

    def updated_customer(self,new_number):
        self.number_served = new_number

        print(f"{self.number_served} people are served now.")

    def increment_number_served(self,total_served):
        self.number_served += total_served
        print(f"{self.number_served} people are served now.")

talha = Restaurant("Talha ahmed","Restaurant")
talha.describe_restaurant()
talha.served_customer()

talha.updated_customer(3)
talha.increment_number_served(5)




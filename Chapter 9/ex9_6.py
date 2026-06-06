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

class Ice_Cream_stand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type)
        self.flavours = []

    def ice_cream_flavours(self):
        while True:
            customer_flavour = input("Enter your desired flavours\n(Enter q to quit): ")

            if customer_flavour !="q":
                self.flavours.append(customer_flavour)
            elif customer_flavour == "q":
                break
        print(f"Your requested flavours are : ")
        for flavour in self.flavours:
            print(flavour.title())

if __name__ == "__main__":
    customer1 = Ice_Cream_stand("fatima","icecream")
    customer1.ice_cream_flavours()
    print(customer1.flavours)

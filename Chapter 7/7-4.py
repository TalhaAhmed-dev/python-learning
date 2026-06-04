
active = True
while active:
    pizza_topping = input("pizza topping: ")
    if pizza_topping.lower() != "quit":
        print("Thanks for adding", pizza_topping)

    if pizza_topping.lower() == "quit":
        active = False

print("Goodbye!")



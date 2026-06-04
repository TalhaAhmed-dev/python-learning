"""Write a program that:
    #Asks user for numbers
    #Stops if user enters 0
    #Prints the number otherwise"""
active = True

while active:
    guess = input("Enter a number: ")
    if int(guess)==0:
        active = False
    else:
        print(f"Guess number is {guess} (enter 0 to stop) ")




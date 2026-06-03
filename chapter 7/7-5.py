age=""
active = True
while active:
    age = input("Enter your age: ")
    age = int(age)
    if age <3:
        print("Ticket is free")
    if age >=3 and age <=12:
        print("Ticket is $10")
    else:
        print("Ticket is $15")


def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def power(a,b):
    return a**b
def square(a):
    return a^2
def cube(a):
    return a**3

while True:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    moderator = input("Enter moderator: ")
    if moderator == "+":
        print(add(a,b))
    elif moderator == "-":
        print(subtract(a,b))
    elif moderator == "*":
        print(multiply(a,b))
    elif moderator == "/":
        print(divide(a,b))
    elif moderator == "**" or moderator == "^":
        print(power(a,b))
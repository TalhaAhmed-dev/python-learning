number = input("Enter number: ")
number  =  float(number)

if number % 10 == 0:
    print(f"{number} is divisible by 10")

if number % 10 != 0:
    print(f"{number} is not divisible by 10")
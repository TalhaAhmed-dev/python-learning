users = ["admin", "talha", "guest", "ali", "sara", "john"]

for user in users:

    if user=="admin":
        print(f"Hello admin you are nice")

    elif user=="guest":
        print("Limited access granted")

    else:
        print(f"welcome {user}")
#2
animals=["dog","cat","mouse","pig","rabbit"]

for animal in animals:
    print(f"A {animal} would make a great pet.")

print("All these animals are amazing!")
#3
shopping_cart=[]
if shopping_cart:
    for items in shopping_cart:
        print(items)
else:
    print("No items available")
#4
print("Odd numbers are \n")

for number in range (1,11,2):
    print(number)

print("even numbers are")
for numbers in range (0,11,2):
    print(numbers)
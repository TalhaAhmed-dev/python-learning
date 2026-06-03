#4-10
sweets=["cake","ice cream","candy","biscuits"]
print("the first three items in sweets are: ")
print(sweets[:3])
print("the middle two items in sweets are: ")
print(sweets[1:2])
print("the last three items in sweets are: ")
print(sweets[-3:])
#4-11
pizza= ["dominos","papa john","cheezious"]
friends_pizza=pizza[:]
pizza.append("Pizza hut")
friends_pizza.append("fredrigo")
print("My favourite pizzas are: ")
for p in pizza:
    print(p.title())
print("\nMy friend's favourite pizzas are: ")
for piz in pizza:
    print(piz.title())
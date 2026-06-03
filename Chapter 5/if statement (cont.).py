products = ["laptop", "mouse", "keyboard", "monitor"]
cart_item = "laptop"
if cart_item in products:
    print("Item available")
else:
    print("Out of stock")
#question
allowed_users = ["admin", "talha", "ahmed"]
username = input("Enter username \n")
if username not in allowed_users:
    print("Access Denied")
elif username == "admin":
    print("Full access")
else:
    print("Access granted")
#question
prices = [220, 150, 305, 180, 90]

for price in prices:
    if price>200:
        print(f"Sell signal: {price}")
    if price<100:
        print(f"Buy signal {price}")
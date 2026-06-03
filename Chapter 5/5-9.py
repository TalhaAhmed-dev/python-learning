username=[]

if username:
    for name in username:
        if name =="talha":
            print("Hello admin")
        elif name in username:
            print(f"Hello {name}")
else:
    print("list is empty")
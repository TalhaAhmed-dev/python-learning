#4-13
menu=("sushi","pizza","macaroni","biryani","fried chicken")
print("We offer only below listed menu: ")
for item in menu:
    print(item)
    #for printing an item from tuple
print(menu[0].title())
#amending tuple will give error
#menu[0]="yoyo"
#print(menu)
menu=("sushi","pizza","macaroni","biryani","fried chicken")
print("We offer only below listed menu: ")
for item in menu:
    print(item)
menu=("sushi","pizza","macaroni","biryani","fried chicken")
print("\nOur changed menu is listed below: ")
for item in menu:
    print(item)


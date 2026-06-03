river = ["ravi", "sutlaj","sindh","chenab","indus"]
#acessing element
print(river[4])
#using individual value
print("My fav river is "+ river[4].title()+".")
#modifying element in a list
river[0]= "sawat"
print(river)
#adding an element to list
river.append("ravi")
print(river)
#inserting an element
river.insert(3,"kalam")
print(river)
#removing an element from list(del)
del river[3]
print(river)
#removing an element from list(pop)
fav_river= river.pop(5)
print(river)
print(f"My fav river is {fav_river}")
#removing an element from list(by value)
river.remove("sindh")
print(river)
#sorting list permanently
river.sort()
print(river)
river.sort(reverse=True)
print(river)
#sorting list temporarily
print(sorted(river))
print(sorted(river,reverse=True))
river.reverse()
print(river)
#length of list
print(len(river))
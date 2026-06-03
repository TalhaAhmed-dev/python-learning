#making a list
friends = ["nono","tutu","bunty","capice","bunny","kyoto"]
print(friends)
#accessing an element from list by putting index
print(friends[-2])
#capitalizing of using a method on list
print(friends[0].title())
print(friends[4].upper())
#using individual value(anything that is separated by comma) from list
print(f"My best friend was " + friends[0].title() + ", \nbut then "
      + friends[0].title() + " changed and now my best friend is " + friends[-2].title() + " now.")
#modifying element in a list
friends[0]= "choocho"
print(friends)
#adding element to the list(appending)
friends.append("juica")
print(friends)
#inserting the element into list
friends.insert(0,"juica")
print(friends)
#removing an element from list
#1st method : deletion
del friends[0]
print(friends)
#2nd method : popping a number
popped_element = friends.pop(-1)
print(friends)
print(popped_element)
# more in next .py file
print(f"Dear {guest_list[0].title()}!you and {guest_list[1].title()}! you're still invited.")
del guest_list[0]
del guest_list[1]
print(guest_list)
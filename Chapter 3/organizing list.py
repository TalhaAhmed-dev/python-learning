#sorting list permanently
list= ["bmw", "audi","corolla","honda"]
list.sort()
print(list)
#sorting reverse list permanently
list.sort(reverse=True)
print(list)
#sorting list temporarily
print(list)
print(sorted(list))
print(sorted(list,reverse=True))
print(list)
list.reverse()
print(list)
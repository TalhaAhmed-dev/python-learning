#4-3
for n in range(1,21):
    print(n)
#4-4(first method)
numbers=[]
for no in range(1000000):
    numbers.append(no)
print(numbers)
print(sum(numbers))
print(max(numbers))
print(min(numbers))
#2nd method
number=[n for n in range(1,1000000)]
print(number)
print(sum(number))
print(max(number))
print(min(number))
#4-6
odd_numbers=[ odd for odd in range(1,20,2)]
print(odd_numbers)
#4-7
table=[number*3 for number in range(1,11)]
print(table)
#4-8(method 1 and 2)
#1
cubes=[]
for h in range(1,11):
    cubes.append(h**3)
    print(cubes)
#4-9, method 2
cube=[p**3 for p in range(1,11)]
print(cube)

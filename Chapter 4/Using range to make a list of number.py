#list of number
numbers=list(range(1,8))
print(numbers)
#Seperation by 2nd comma gives step step size e.g.
number=list(range(2,21,2))
print(number)
#for exponents
squares=[]
for number in range(1,11):
    square=number**2
    squares.append(square) #or squares.append(number**2)
    print(squares) # pertinent to nore here that print outside the for function only prints the last called value
print(squares)



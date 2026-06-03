list= []

for number in range(1,10):
    list.append(number)

for no in list:
    if no==1:
        print("1st")

    elif no==2:
        print("2nd")

    elif no==3:
        print("3rd")

    else:
        print(f"{no}th")
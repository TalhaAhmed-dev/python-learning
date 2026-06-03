current_users = ["Ali", "Talha", "Ahmed"]
new_users = ["talha", "Hamza", "ALI"]
for user in current_users:
    if user in new_users:
        print("Not available")
    else:
        print("Available")
#6
ages = [2, 15, 25, 70]
for age in ages:

    if age <4:
        print("Baby")

    elif age>=4 and age<=12:
        print("Child")

    elif age>=13 and age<=19:
        print("Teenager")

    elif age>=20 and age<=64:
        print("Adult")
    else:
        print("Elder")

#7
names = ["ali", "ahmed", "ali", "talha", "ali"]

print(f"Ali appears {names.count("ali")} times.")
#8
a = 10
b = 20
c = 10
print(a==b)
print(a==c)
print(a!=b)
print(a>b)
#10
fruit = "Aple"
if fruit.lower()=="apple":
    print("match found")
else:
    print("no match")
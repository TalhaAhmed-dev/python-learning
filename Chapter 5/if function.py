#Question
age=15
country="USA"
if age<13:
    print("Child")
elif age>=13 and age <=19 and country=="Pakistan":
    print("Pakistani teenager.")
elif age>=13 and age <=19 and country!="Pakistan":
    print("Foreign teenager.")
else:
    print("Adult")
#Question
marks=95

if marks<40:
    print("Fail")

elif marks>=40 and marks<=59:
    print("Pass")

elif marks>=60 and marks<=79:
    print("Good")

else:
    print("Excellent")
#Question
username="admino"
password=12345

if username!="admin":
    print("Wrong username")

elif username=="admin" and password!=1234:
    print("Wrong password")

else:
    print("Login successful")
#question
age=18
has_id=False
if age<18:\
    print("Not allowed")

if age>=18 and has_id==False:
    print("Bring your ID")

if age>=18 and has_id==True:
    print("Entry allowed")
#question
age=20
country="Pakistn"
student=False

if age<13:
    print("Too young")

elif age >=13 and age<=19 and student==True:
    print("Teen student")

elif age >=13 and age<=19 and student==False:
    print("Teen Non-student")

elif age >=20 and country!="Pakistan":
    print("International student")

else:
    print("Local adult")


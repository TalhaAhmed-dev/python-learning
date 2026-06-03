favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
names=["fatima","talha","jen","sarah","taha"]
for name in names:
    if name in favorite_languages.keys():
        print(f"Thank you {name.title()} for taking the pool")
    else:
        print(f"Please consider taking our pool Mr. {name.title()} ")

#6-6 Chatgpt exercise
members = {
    "ahmed": "active",
    "bilal": "active",
    "hamza": "active",
    "usman": "active"
}
check_in = ["ahmed", "talha", "usman", "zain", "bilal"]
for name in check_in:
    if name in members.keys():
        print(f"Welcome back {name.title()}.")
    else:
        print(f"{name.title()}, please register at the front desk.")

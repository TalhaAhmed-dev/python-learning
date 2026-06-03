responses = {}
active = True

while active:
    name = input("Enter your name: ")
    response = input("Enter your response: ")

    responses[name] = response

    repeat = input("Would you like to repeat another to respond? y/n: ")
    if repeat.lower() == "no" or repeat.lower() == "n":
        active = False

for name,response in responses.items():
    print(f"{name} would like to visit {response}")
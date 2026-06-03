numbers = 1
while numbers <=5:
    print(numbers)
    numbers += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt = prompt + "\nEnter 'quit' to end the program. "
message= " "
while message != "quit".lower():
    message = input(prompt)

    if message!= "quit".lower():
        print(message)

p
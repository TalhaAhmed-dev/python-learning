"""Make a login system:

Correct username = "talha"
Correct password = "1234"
Stop if login is correct
Stop after 3 wrong attempts"""
correct_username = "talha"
correct_password = "1234"
active = True
guesses = 3

while active:
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if username.lower() == correct_username.lower() and password == correct_password:
        print(f"Welcome, {username}!")
        break

    else:
        guesses -= 1
        print(f"Sorry, {username} is incorrect.")
        print("guesses left: ", guesses)
        if guesses == 0 :
            print(f"Login failed")
            active = False

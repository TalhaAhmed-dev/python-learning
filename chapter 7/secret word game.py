secret_word = "DODO"
guessed_word= ""
tries = 3
active = True
while active:
    guessed_word = input("Guess a word: ")
    if secret_word.lower() == guessed_word.lower():
        print("You guessed the word")
        break

    else:
            tries -= 1
            print("Try again")
            print("tries left: ", tries)

            if tries == 0:
                print("You failed. The correct word is ", secret_word)
                active = False




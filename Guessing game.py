tries = 3
guess_number = 2

while tries > 0:
    user_guess = int(input("Enter number: "))

    if user_guess == guess_number:
        print("Congratulations! You guessed correctly.")
        break
    else:
        tries -= 1
        print("Wrong guess, try again.")

if tries == 0:
    print("Game over!")

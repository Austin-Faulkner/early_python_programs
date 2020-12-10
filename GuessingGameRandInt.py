#  File: GuessingGame.py
#  Description: The Guessing Game will choose a "secret number", a number in [1, 9999]
#               (namely, a positive number less than 10000), and the user has 10 tries
#               to guess the number.
#  Student's Name: Austin Keith Faulkner
#  Student's UT EID: akf354
#  Course Name: CS 303E
#  Unique Number: 50075
#  Professor: Dr. William Bulko
#
#  Date Created: January 1, 2020
#  Date Last Modified:  (12:30pm)

import random

def main():

    randomInteger = random.randint(1,10000)

    # Invite the player to joing the guessing game:
    print("Welcome to the guessing game.  You have ten tries to guess my number.")

    # Ask for the first quesss:
    guessedNumber = int(input("Please enter your guess: "))

    # Set guesses to one.
    guesses = 1

    # User-input validation for the first try:
    while guessedNumber <= 0 or guessedNumber >= 10000:
        print("Your guess must be between 0001 and 9999.")
        guessedNumber = int(input("Please enter a valid guess: "))


    # When the user guesses correctly on the first try:
    if guessedNumber == randomInteger and guesses == 1:
        print("That's correct!")
        print("Congratulations! You guessed it on the first try!")


    # When the user guesses correctly within two to ten tries:
    while guesses <= 10:

        # User-input validation
        while guessedNumber <= 0 or guessedNumber >= 10000:
            print("Your guess must be between 0001 and 9999.")
            guessedNumber = int(input("Please enter a valid guess: "))

        # If the guessed number is greater than the "secret number", request the
        # player to enter another guess.
        if guessedNumber > randomInteger:
            print("Your guess is too high.")
            print("Guesses so far: " + str(guesses))
            guesses += 1

            # If the number of guesses is over 10, indicate the game is over.
            if guesses > 10:
                print("Game over: you ran out of guesses.")
                break

            guessedNumber = int(input("Please enter your guess: "))

        # Otherwise, if the guessed number is lower than the "secret number",
        # request the player to enter another guess.
        elif guessedNumber < randomInteger:
            print("Your guess is too low.")
            print("Guesses so far: " + str(guesses))
            guesses += 1

            # If the number of guesses is over 10, indicate the game is over.
            if guesses > 10:
                print("Game over: you ran out of guesses.")
                print("The secret number is: " + str(randomInteger))
                break

            guessedNumber = int(input("Please enter your guess: "))

        # Otherwise, if the guessed number is correct, send congratulations and
        # indicate which guess number the player quessed correctly on.
        elif guessedNumber == randomInteger and guesses != 1:
            print("That's correct!")
            print("Congratulations! You guessed it in " + str(guesses) + " guesses.")
            break

main()

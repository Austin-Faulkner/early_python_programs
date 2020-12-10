#  File: Deal.py
#  Description: Simulates Monty Hall's, "Let's Make a Deal", show. Evaluates the
#               probabilities of winning if you switch from the guessed door and
#               probabilities of winning if you do not switch from the guessed door.
#  Student's Name: Austin Keith Faulkner
#  Student's UT EID: akf354
#  Course Name: CS 303E 
#  Unique Number: 50075
#
#  Date Created: October 16, 2019
#  Date Last Modified: October 22, 2019  (8:25 pm)

import random

def roll(n):

    roll = random.randint(1, n + 1)

    gameRoll = roll % 3 + 1

    return gameRoll


def runOneTrial(games, i):

    view = 0
    
    newGuess = 0

    prize = roll(games) 
    
    guess = roll(games) 

    # View is contingent on prize and guess; it's always the different, third door. Also,
    # a new guess, newGuess, is only a winner if the guess, guess, is not already the prize.
    # In any case, each needs to be a different value from the other, since we're either choosing
    # our guess or our new guess, and not the open door.
    
    if guess != prize:
        if ((guess + prize) % 5) == 0:
            view = 1
        elif ((guess + prize) % 4) == 0:
            view = 2
        elif ((guess + prize) % 3) == 0:
            view = 3
    elif guess == prize:
        if guess == 1:
           view = random.randint(2,3)
        elif guess == 3:
           view = random.randint(1,2)
        elif guess == 2 and view != 1:
           view = 3
        elif guess == 2 and view != 3:
           view = 1

    if guess == 1 and view == 2:
        newGuess = 3
    elif guess == 1 and view == 3:
        newGuess = 2
    elif guess == 2 and view == 1:
        newGuess = 3
    elif guess == 2 and view == 3:
        newGuess = 1
    elif guess == 3 and view == 1:
        newGuess = 2
    elif guess == 3 and view == 2:
        newGuess = 1

    win = "win"
    lose = "lose"

    if newGuess == prize:
        return win, prize, guess, view, newGuess 
    else:
        return lose, prize, guess, view, newGuess


def main():

    games = int(input("How many trials do you want to run? ")) 

    wins = ''
    count = 0

    print()
    
    print("Prize" + format("Guess", ">7s") + format("View", ">6s") + format("New", ">5s") + format("Guess", ">6s")) 

    for i in range(1, games + 1):
        aWin, prizeDoor, guessDoor, viewDoor, newGuessDoor = runOneTrial(games, i)
        print(format(prizeDoor,">3d") + format(guessDoor,">7d") + format(viewDoor,">7d") + format(newGuessDoor,">9d"))
        if newGuessDoor == prizeDoor:
            wins += aWin
            if wins != '':
                count += 1
                     
    probWinSwitch = count / games
    probLoseSwitch = 1 - probWinSwitch
        
    print()

    print("The probability of winning if you switch = " + format(probWinSwitch, "1.1f"))
    print("The probability of winning if you do not switch = " + format(probLoseSwitch, "1.1f"))

main()
    

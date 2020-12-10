#  File: Handicap.py
#  Description: This program takes user input for a person's scores for each of three
#               bowling games. It then calculates the average and uses the average to
#               to calculate the the person's handicap for the next bowling game(s)
#               with beginners.
#  Student's Name: Austin Keith Faulkner
#  Student's UT EID: akf354
#  Course Name: CS 303E 
#  Unique Number: 50075
#  Professor: Dr. William Bulko
#
#  Date Created: September 9th, 2019
#  Date Last Modified: N/A

def main():

    # To print two lines above the program output
    print("")
    print("")

    # To store user input for the scores of each of three bowling matches
    gameOneScore = int(input("Enter Game 1: "))
    gameTwoScore = int(input("Enter Game 2: "))
    gameThreeScore = int(input("Enter Game 3: "))

    # The average of the three scores the bowler plays
    average = (gameOneScore + gameTwoScore + gameThreeScore) // 3

    # To calculate the handicap for the next game with beginner player(s)
    # Here we use 0.80 for 80%.
    handicap = int((200 - average) * 0.80)

    # To separate the int input from the output of the bowler's average and handicap
    print("")

    # To print the bowler's average and handicap, respectively
    print("The bowler's average is:", average)
    print("The bowler's handicap is:", handicap)

    # To print two lines below the program output
    print("")
    print("")

main()

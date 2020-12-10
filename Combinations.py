#  File: Combinations.py
#  Description: This program prints a table listing the number of
#               possible hands for n C r cards.
#  Student's Name: Austin Keith Faulkner    
#  Student's UT EID: akf354
#  Course Name: CS 303E 
#  Unique Number: 50075
#
#  Date Created: October 11, 2019
#  Date Last Modified: October 14, 2019


# To compute factorials
def factorial(num):

    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    return factorial


# To compute combinations
def combinations(n,r):

    comb = factorial(n) / (factorial(r) * factorial(n - r))

    return comb


# To print a table of combinatoric combinations for each r hands of cards,
# where a deck has 52 cards
def main():

    cardsInADeck = 52

    print()
    
    print("Cards" + format("Combinations", ">17s"))
    print("=" * 22)

    for i in range(0, cardsInADeck + 1):
        print(format(i, "3d") + format(int(combinations(cardsInADeck, i)), "19d"))
    
    print()

main()

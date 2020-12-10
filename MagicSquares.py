#  File: MagicSquares.py
#  Description: A magic square is an n by n grid of numbers in
#               which the entries in each row, column, and two
#               main diagonals each add up to the same number.
#               We print Magic Squares of size 1, 3, 5, . . . , 11, 13.
#  Student's Name: Austin Keith Faulkner
#  Student's UT EID: akf354
#  Course Name: CS 303E 
#  Unique Number: 50075
#
#  Date Created: November 12, 2019
#  Date Last Modified: November 15, 2019 (2:27 pm)

class MagicSquare():

    def __init__(self, side):

        self.sideLength = side

        # Making a blank n by n grid - an n X n list
        grid = [[0 for i in range(side)] for i in range(side)]

        # To track indices movements
        index = 0 
        half = side // 2

        # Setting the first position to the middle of the top row and assigning it 1
        grid[0][half] = 1   

        # Set i = 1 and let it range up to side^2
        for i in range(1, side**2):

            # If int is a multiple of side length
            if i % side == 0:
                if  index == side - 1:
                    grid[0][half] = i + 1
                else:
                    grid[index + 1][half] = i + 1
                    index += 1

            # Otherwise, if int is not a multiple
            else:
                if index == 0 and half == side - 1:
                    grid[side - 1][0] = i + 1
                elif half == side - 1:
                    grid[index - 1][0] = i + 1
                    index -= 1
                    half = 0
                elif index == 0:
                    grid[side - 1][half + 1] = i + 1
                    index = side - 1
                    half += 1
                else:
                    grid[index - 1][half + 1] = i + 1
                    index -= 1
                    half += 1

        self.grid = grid

              
    def display(self):

        magicList = self.grid

        for i in range(self.sideLength):
            for j in range(self.sideLength):
                print(format(magicList[i][j], ">5d"), end = "")
            print()


def main():

    maxNeededForFirst7MagicSquares = 8
    
    for i in range(1, maxNeededForFirst7MagicSquares):
        side = 2*i - 1
        
        # Create a MagicSquare object so as to use the display method iteratively
        mySquare = MagicSquare(side)
        
        print("Magic Square of size", side)
        print()
        mySquare.display()
        print()

main()



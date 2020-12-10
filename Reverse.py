#  File: Reverse.py
#  Description: This program takes integer user input and then prints the reverse of the integers entered.
#  Student's Name: Austin Keith Faulkner
#  Student's UT EID: akf354
#  Course Name: CS 303E 
#  Unique Number: 50075
#  Professor: Dr. William Bulko
#
#  Date Created: September 13th, 2019
#  Date Last Modified: September 16th, 2019

def main():

    # To get integer user input
    fullNumber = int(input("Enter an integer: "))
    

    # This is the algorithm for calculating the modulus of each of the remaining numbers in (integer) user input. For example,
    # if user input is 1234, then we have (NOTE: the int() makes its arguments integers as seen below in the examples):
    firstNumber = fullNumber % 10                                                                              # e.g.: 1234 % 10 = 4
    secondNumber = int((fullNumber - firstNumber) / 10) % 10                                                   # e.g.: ((1234 - 4) / 10) % 10 = 123 % 10 = 3
    thirdNumber = int((fullNumber - (secondNumber * 10 + firstNumber * 1)) / 100) % 10                         # e.g.: ((1234 - 34) / 100) % 10 = 12  % 10 = 2
    fourthNumber = int((fullNumber - (thirdNumber * 100 + secondNumber * 10 + firstNumber *1 )) / 1000) % 10   # e.g.: ((1234 - 234) / 1000) % 10 = 1 % 10 = 1


    # To capture the numbers calculated in reverse
    fullReversedNumber = firstNumber * 1000 + secondNumber * 100 + thirdNumber * 10 + fourthNumber * 1

    # To convert to a string.
    reverse = str(fullReversedNumber)

    # To print the resulting reversed number given from user input
    print("The reversed number is " + reverse + ".")
    
main()

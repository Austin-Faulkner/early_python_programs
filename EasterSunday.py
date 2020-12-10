#  File: EasterSunday.py
#  Description: The user is requested to input a year. Using Gauss's
#               algorithm -- basic arithmetic operations in Python --
#               the date of Easter Sunday is computed for the user-specified
#               year.
#  Student's Name: Austin Keith Faulkner
#  Student's UT EID: akf354
#  Course Name: CS 303E
#  Unique Number: 50075
#  Professor: Dr. William Bulko
#
#  Date Created: September 5th, 2019
#  Date Last Modified: September 5th, 2019

def main():

    # To provide two lines of spacing above the printed statements
    print("")
    print("")

    # To receive a year from user input
    y = int(input("Enter year: "))

    # Carl Friedrich Gauss's Easter Sunday algorithm
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32

    # To print the statement of the solution just below user input
    print("In", y, "Easter Sunday is on month", n, "and day", p)

    # To provide two lines of spacing below the printed statements
    print("")
    print("")

main()

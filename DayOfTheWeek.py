#  File: DayOfTheWeek.py
#  Description: Calculates and displays the day of the week for any year and month
#               entered between 1900 and 2100 inclusive, using Rev. Zeller's Congruence
#               Algorithm.
#  Student's Name: Austin Keith Faulkner
#  Student's UT EID: akf354
#  Course Name: CS 303E
#  Unique Number: 50075
#  Professor: Dr. William Bulko
#
#  Date Created: September 23, 2019
#  Date Last Modified: September 26, 2019

def main():

    # To receive user-input:
    year = int(input("Please enter the year (an integer): "))
    month = str(input("Please enter the month (a string): "))
    day = int(input("Please enter the day (an integer): "))

    b = day
    
    firstNumber = year % 10
    secondNumber = int((year - firstNumber) / 10) % 10


    # The digits in the ten's place and one's place in the year given by user-input.
    # Namely, these are the last two digits of the year entered (read left -> right).
    c = secondNumber * 10 + firstNumber * 1

    
    thirdNumber = int((year - (secondNumber * 10 + firstNumber * 1)) / 100) % 10
    fourthNumber = int((year - (thirdNumber * 100 + secondNumber * 10 + firstNumber *1 )) / 1000) % 10


    # The digits in the thousand's place and the hundred's place in the year given by user-input.
    # Namely, these are the first two digits of the year entered (read left -> right).
    d = fourthNumber * 10 + thirdNumber * 1


    # Zeller's Congruence Algorithm, Part 1:
    # In January and February - years 1900, 2000, and 2100 - we subtract one from the year; and do away
    # with the first two digits of the year for c; and mod c by 100 to get the last two digits of the
    # year previous to user-input. Then we decrement d by 1 so that d, as the first two digits of year,
    # matches (year - 1).
    
    # Zeller's Congruence Algorithm is designed to account for 'special' years - namely, leap years.
    # So, for January through December, we simply set a = i for i in [11, 12, 1, 2, . . ., 10], in that order,
    # where, for example, a = 11 is January; a = 12 is February; a = 1 is March; a = 2 is April; and so on.
    if (month == "January" and (year == 1900 or year == 2000 or year == 2100)):
        a = 11
        year -= 1
        c = (year - (d * 100)) % 100
        d -= 1
    elif (month == "January"):
        a = 11
        c -= 1
    elif (month == "February" and (year == 1900 or year == 2000 or year == 2100)):
        a = 12
        year -= 1
        c = (year - (d * 100)) % 100
        d -= 1
    elif (month == "February"):
        a = 12
        c -= 1
    elif (month == "March"):
        a = 1
    elif (month == "April"):
        a = 2
    elif (month == "May"):
        a = 3
    elif (month == "June"):
        a = 4
    elif (month == "July"):
        a = 5
    elif (month == "August"):
        a = 6
    elif (month == "September"):
        a = 7
    elif (month == "October"):
        a = 8
    elif (month == "November"):
        a = 9
    elif (month == "December"):
        a = 10


    # Zeller's Congruence Algorithm, Part 2:
    w = (13 * a - 1) // 5
    x = c // 4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r = z % 7
    r = (r + 7) % 7  # To handle negative values of r


    # To find the day of the week with the result, r, of the
    # Congruence Algorithm
    if (r == 0):
        print("The day of the week is Sunday.")
    elif (r == 1):
        print("The day of the week is Monday.")
    elif (r == 2):
        print("The day of the week is Tuesday.")
    elif (r == 3):
        print("The day of the week is Wednesday.")
    elif (r == 4):
        print("The day of the week is Thursday.")
    elif (r == 5):
        print("The day of the week is Friday.")
    else: 
        print("The day of the week is Saturday.")
        
main()

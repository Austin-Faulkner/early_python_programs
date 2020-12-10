#  File: NextDay.py
#  Description: This program prompts the user to enter a year (an int), a month
#               (a string), and a day (an int), and then computes and prints its
#               immediate successor.
#  Student's Name: Austin Keith Faulkner
#  Student's UT EID: akf354
#  Course Name: CS 303E 
#  Unique Number: 50075
#  Professor: Dr. William Bulko
#
#  Date Created: September 19, 2019
#  Date Last Modified:

def main():

    # To get user input for year, month, and day
    year = int(input("Please enter the year: "))
    month = str(input("Please enter the month: "))
    day = int(input("Please enter the day: "))


    # To set the boolean for when leap years are located in the annual calender
    isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


    # If it's a leap year and if the month is February the 29th, advance the
    # month to March and set day = 1; if it's a leap year and it's December the
    # the 31st, advance the month to January and set day = 1; otherwise,
    # merely increase the day.
    if isLeapYear:
        if month == "February" and day == 29:
            month = "March"
            day = 1
        elif month == "December" and day == 31:
            month = "January"
            day = 1
            year = year + 1
        else:
            day = day + 1
    # If the year is not a leap year, then, if the day is the last day of the month,
    # advance to the next month and set day = 1; otherwise, if it's not the last
    # day of the month, merely increase the day by 1.
    elif year != isLeapYear:
        if month == "January" and day == 31:
            month = "February"
            day = 1
        elif month == "February" and day == 28:
            month = "March"
            day = 1
        elif month == "March" and day == 31:
            month = "April"
            day = 1
        elif month == "April" and day == 30:
            month = "May"
            day = 1
        elif month == "May" and day == 31:
            month = "June"
            day = 1
        elif month == "June" and day == 30:
            month = "July"
            day = 1
        elif month == "July" and day == 31:
            month = "August"
            day = 1
        elif month == "August" and day == 31:
            month = "September"
            day = 1
        elif month == "September" and day == 30:
            month = "October"
            day = 1
        elif month == "October" and day == 31:
            month = "November"
            day = 1
        elif month == "November" and day == 30:
            month = "December"
            day = 1
        elif month == "December" and day == 31:
            month = "January"
            day = 1
            year = year + 1
        else:
            day = day + 1
            

    # Print the month, day, and year.
    print("The next day is " + month + " " + str(day) + ", " + str(year) + ".")

main()

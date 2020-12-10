#  File: Population.py
#  Description: This program studies "Benford's Law" by using
#               population statistics in the U.S.
#  Student's Name: Austin Keith Faulkner
#  Student's UT EID: akf354
#  Course Name: CS 303E 
#  Unique Number: 50075
#
#  Date Created: November 27, 2019
#  Date Last Modified: December 4, 2019


def main():

    infile = open("2009CensusData.txt", "r")
    garbage = infile.readline()

    sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8, sum9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    totalSum = 0

    print(format("Digit", "s") + format("Count", ">8s") + format("%", ">6s"))
    print("---------------------")

    line = infile.readline()
    
    while line != "":
        
        pop_stats_list = line.strip().split()
        pop_numbers = pop_stats_list[-1].strip()

        dictionary = {}
        
        key = pop_numbers[0]
        dictionary[key] = pop_numbers

        for key in dictionary:
            if key == '1':
                sum1 += 1
            elif key == '2':
                sum2 += 1
            elif key == '3':
                sum3 += 1
            elif key == '4':
                sum4 += 1
            elif key == '5':
                sum5 += 1
            elif key == '6':
                sum6 += 1
            elif key == '7':
                sum7 += 1
            elif key == '8':
                sum8 += 1
            elif key == '9':
                sum9 += 1

            totalSum = sum1 + sum2 + sum3 + sum4 + sum5 + sum6 + sum7 + sum8 + sum9

            relFreq1 = sum1 / totalSum * 100
            relFreq2 = sum2 / totalSum * 100
            relFreq3 = sum3 / totalSum * 100
            relFreq4 = sum4 / totalSum * 100
            relFreq5 = sum5 / totalSum * 100
            relFreq6 = sum6 / totalSum * 100
            relFreq7 = sum7 / totalSum * 100
            relFreq8 = sum8 / totalSum * 100
            relFreq9 = sum9 / totalSum * 100

        line = infile.readline()

    print(format(1, "d") + format(str(sum1), ">12s") + format(str(round(relFreq1, 1)), ">8s"))
    print(format(2, "d") + format(str(sum2), ">12s") + format(str(round(relFreq2, 1)), ">8s"))
    print(format(3, "d") + format(str(sum3), ">12s") + format(str(round(relFreq3, 1)), ">8s"))
    print(format(4, "d") + format(str(sum4), ">12s") + format(str(round(relFreq4, 1)), ">8s"))
    print(format(5, "d") + format(str(sum5), ">12s") + format(str(round(relFreq5, 1)), ">8s"))
    print(format(6, "d") + format(str(sum6), ">12s") + format(str(round(relFreq6, 1)), ">8s"))
    print(format(7, "d") + format(str(sum7), ">12s") + format(str(round(relFreq7, 1)), ">8s"))
    print(format(8, "d") + format(str(sum8), ">12s") + format(str(round(relFreq8, 1)), ">8s"))
    print(format(9, "d") + format(str(sum9), ">12s") + format(str(round(relFreq9, 1)), ">8s"))

    infile.close()

main()

    


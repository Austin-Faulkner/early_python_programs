#  File: Report.py
#  Description: Takes financial input and calculates total assets and total liabilities
#               and stockholders' equity. Then, with this information, a report/table is
#               printed for Lone Star Company for review.
#  Student's Name: Austin Keith Faulkner
#  Student's UT EID: akf354
#  Course Name: CS 303E 
#  Unique Number: 50075
#  Professor: Dr. William Bulko

#  Date Created: October 3, 2019
#  Date Last Modified: October 7, 2019 (7:53 pm)

def main():

    # input data
    companyName = "Lone Star Corporation"
    date = "October 1, 2019"
    cash = 7505.54
    acctsRec = 502.21
    supplies = 313.89
    land = 6456.23
    buildings = 81598.00
    machAndEquip = 8329.99
    patents = 2000.00
    acctsPay = 93569.23
    stock = 88100.00

    # To calculate total assets
    totalAssets = cash + acctsRec + supplies + land + buildings + machAndEquip + patents

    # To calculate total liability and stockholders' equity
    totalLiabilityAndStockholdersEquity = acctsPay + stock

    # To print the report for all input and calculated figues above
    print()
    print(companyName.upper().center(80))
    print("Balance Sheet".center(80))
    print(date.center(80))
    print()
    print(format("Liabilities and", ">58s"))
    print("Assets", end = " ")
    print(format("   Stockholders' Equity", ">59s"))
    print("--------------------------------------------------------------------------------")
    print("   Cash" + format(cash, ">33.2f") + format("Liabilities:", ">15s"))
    print("   Accounts Receivable" + format(acctsRec, "18.2f") + format("   Accounts Payable", ">22s") + format(acctsPay, ">18.2f"))
    print("   Supplies" + format(supplies, "29.2f"))
    print("   Land" + format(land, ">33.2f"))
    print("   Buildings" + format(buildings, ">28.2f") + format("   Stockholders' Equity:", ">27s"))
    print("   Machines and Equipment" + format(machAndEquip, ">15.2f") + format("      Capital Stock:", ">23s") + format(stock, ">17.2f"))
    print("   Patents" + format(patents, ">30.2f"))
    print()                            
    print("Total Assets", format(totalAssets, ">27.2f"), format("Total Liabilities and", ">23s"))
    print(format("   Stockholders' Equity", ">66s") + format(totalLiabilityAndStockholdersEquity, ">14.2f"))
    print()

main()

'''
FIle Name: ebaxter1_midterm.py
Made by: Erin Baxter
This program will calculate an amortization schedule for a loan
'''

print("Hello and welcome to the Loan Amortization Schedule Generator Midterm Edition!\n")

def main():
    loanAmount = input("Please enter loan amount as a number: ")
    yearAmount = input("Please enter loan duration in years: ")
    annualRate = input("Please enter annual interest rate: ")

    if testInput(loanAmount, yearAmount, annualRate):
        print("made it")
        #calcPayment()

def testInput(loan, years, rate):
    if " " in loan:
        print("Invaild input for loan amount! Please try again with no spaces!")
    elif " " in years:
        print("Invaild input for years amount! Please try again with no spaces!")
    elif " " in rate:
        print("Invaild input for annual rate! Please try again with no spaces!")
    elif loan == "" or years == "" or rate == "":
        print("No input found for one option. Please try again!")
    elif loan.isnumeric() == False:
        print("Loan ammount entered is not a number! Please try again")
    elif years.isnumeric() == False:
        print("Year ammount entered is not a number! Please try again")
    elif rate.isnumeric() == False:
        print("Annual rate entered is not a number! Please try again!")
    elif float(years):
        print("Input error! Years amount can not have a decimal! Please again")
    elif float(loan) and int(years) and float(rate):
        return True
    else:
        print("Invaild input. Please try again")
        
        

#def calcPayment():

#def displayInfo():
    


#call main
main()

print("\nProgram ending, have a nice day!")

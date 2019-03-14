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
        calcPayment(loanAmount, yearAmount, annualRate)


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
    elif "." in years:
        print("Input error! Years amount can not have a decimal! Please again")
    elif years.isnumeric() == False:
        print("Year ammount entered is not a number! Please try again")
    elif rate.isnumeric() == False:
        print("Annual rate entered is not a number! Please try again!")
    elif float(loan) and int(years) and float(rate):
        return True
    else:
        print("Invaild input. Please try again")

       
def calcPayment(loan, years, rate):
    monthlyRate = (float(rate) / 12) / 100
    months = float(years) * 12
    monthlyPay = (monthlyRate * float(loan)) / (1 - (1 + monthlyRate)**(-months))
    interest = monthlyRate * float(loan)
   
    balance = (float(loan) - (monthlyPay - interest))
    principal = monthlyPay - interest

    displayInfo(monthlyPay, months, principal, balance, interest, monthlyRate)
      

def displayInfo(pay, length, prin, newBalance, newInterest, monthRate):
    stringMonthly = "${:,.2f}".format(pay)
    stringTotal = "${:,.2f}".format(pay * length)
    spaces = "           "
    sizeTest = True
    sizeTest2 =  True

    print(f'''\nMonthly Payment: {stringMonthly}\nTotal Payment: {stringTotal}\n\nPayment#    Interest   Principal   Balance''')
    for x in range(1,int(length)+1):
        stringInterest = "${0:.2f}".format(newInterest)
        stringPrincipal = "${:,.2f}".format(prin)
        stringNewBalance = "${:,.2f}".format(newBalance)
        print(f'{x}{spaces}{stringInterest}     {stringPrincipal}    {stringNewBalance}')
        newInterest = monthRate * newBalance
        prin = pay - newInterest
        newBalance = (newBalance - (prin))
        if sizeTest == True:
            if x >= 9 and x < 100:
                spaces = "          "
                test = False
        if sizeTest2 == True:
            if x >= 99:
                spaces = "         "
                test2 = False


#call main
main()

print("\nProgram ending, have a nice day!")

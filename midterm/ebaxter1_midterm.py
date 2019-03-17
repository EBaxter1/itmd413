'''
FIle Name: ebaxter1_midterm.py
Made by: Erin Baxter
This program will calculate an amortization schedule for a loan
'''

print("Hello and welcome to the Loan Amortization Schedule Generator Midterm Edition!\n")

# function that gets user input and calls other methods 
def main():
    #get user input 
    loanAmount = input("Please enter loan amount as a number: ")
    yearAmount = input("Please enter loan duration in years: ")
    annualRate = input("Please enter annual interest rate: ")

    #send input to test and if return true get next method 
    if testInput(loanAmount, yearAmount, annualRate):
        calcPayment(loanAmount, yearAmount, annualRate)

#function that test input to be correct form 
def testInput(loan, years, rate):
    if " " in loan:
        print("Invaild input for loan amount! Please try again with no spaces!")
    elif " " in years:
        print("Invaild input for years amount! Please try again with no spaces!")
    elif " " in rate:
        print("Invaild input for annual rate! Please try again with no spaces!")
    elif loan == "" or years == "" or rate == "":
        print("No input found for one option. Please try again!")
    #make sure input are numbers 
    elif "." in years:
        print("Input error! Years amount can not have a decimal! Please again")
    elif years.isnumeric() == False:
        print("Year ammount entered is not a number! Please try again")
    elif float(loan) and int(years) and float(rate):
        return True
    elif loan.isnumeric() == False:
        print("Loan ammount entered is not a number! Please try again")
    elif rate.isnumeric() == False:
        print("Annual rate entered is not a number! Please try again!")
    else:
        print("Invaild input. Please try again")

#function that calcuates the loan payments 
def calcPayment(loan, years, rate):
    #set all inputs to float from string 
    monthlyRate = (float(rate) / 12) / 100
    months = float(years) * 12
    monthlyPay = (monthlyRate * float(loan)) / (1 - (1 + monthlyRate)**(-months))
    interest = monthlyRate * float(loan)
    balance = (float(loan) - (monthlyPay - interest))
    principal = monthlyPay - interest

    #send calc data to next function 
    displayInfo(monthlyPay, months, principal, balance, interest, monthlyRate)
      
#this function will take loan data and display it in correct format 
def displayInfo(pay, length, prin, newBalance, newInterest, monthRate):
    #set format for monthly pay and total 
    stringMonthly = "${:,.2f}".format(pay)
    stringTotal = "${:,.2f}".format(pay * length)
    #number of spaces between payment # and interest 
    spaces = "           "
    #variables to be used to check payment number and set's number of spaces 
    sizeTest = True
    sizeTest2 =  True

    #print out formated data 
    print(f'''\nMonthly Payment: {stringMonthly}\nTotal Payment: {stringTotal}\n\nPayment#    Interest   Principal   Balance''')
    #for loop to print each payment line 
    for x in range(1,int(length)+1):
        #format data 
        stringInterest = "${0:.2f}".format(newInterest)
        stringPrincipal = "${:,.2f}".format(prin)
        #make sure balance is postive 
        stringNewBalance = "${:,.2f}".format(abs(newBalance))
        #print data spaced nicely to match headers 
        print(f'{x}{spaces}{stringInterest}     {stringPrincipal}    {stringNewBalance}')
        #calculation for next payment 
        newInterest = monthRate * newBalance
        prin = pay - newInterest
        newBalance = (newBalance - (prin))
        #if statments to check if payment # is above something and will take away spaces as needed to make sure everything aligned nice 
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

#say good bye
print("\nProgram ending, have a nice day!")

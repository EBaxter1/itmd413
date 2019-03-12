'''
File Name: ebaxter1_hw7.py
Made by: Erin Baxter
This program will take a phone number that has letters and make it all numbers
'''

#import regualr expressions 
import re

print("Hello and welcome to the Number Converter 13,000!")

#this function will get the input from a user and then sends it to other methods 
def main():
    #variable to keep running
    noStop = "y"

    while noStop == "y" or noStop == "yes":
        #get input
        pNum = input("\nPlease enter a phone number with no spaces in the following format, XXX-XXX-XXXX: ")

        #test input and then convert it 
        if testNum(pNum):
            print("Converting phone number...")
            convertNum(pNum)

        #check and see if they wanna go again
        noStop = input("\nWould you like to put another number?(Enter y or yes for yes or anything else for no: ")
        noStop = noStop.lower()
        
# this function will test the input and then return true if everything is fine 
def testNum(num):
    #create test regular expressions
    testExpression = (r"^[\w\d]{3}-[\w\d]{3}-[\w\d]{4}$")
    normalExpression = (r"^[\d]{3}-[\d]{3}-[\d]{4}$")
    
    #test input
    if " " in num:
        print("Invaild input! Please try again with no spaces!")
    elif num == "":
        print("No input found. Please try again")
    elif "_" in num:
        print("Invaild input! Please try again with no underscores")
    elif re.match(normalExpression, num):
        print("That phone number doesn't need to be converted!")
    elif re.match(testExpression, num):
        return True
    else:
        print("Invaild input! Please try again with format XXX-XXX-XXXX and using only numbers or letters")

      
#this function will convert phone humber to all digits 
def convertNum(num):
    #regular expressions for letter maps 
    digit = r"[0-9]"
    digit2 = r"[abcABC]"
    digit3 = r"[defDEF]"
    digit4 = r"[ghiGHI]"
    digit5 = r"[jklJKL]"
    digit6 = r"[mnoMNO]"
    digit7 = r"[pqrsPQRS]"
    digit8 = r"[tuvTUV]"
    digit9 = r"[wxyzWXYZ]"

    #convert to number
    for element in num:
        #skips numbers
        if re.match(digit, element):
            continue
        #skips dashes 
        elif element == "-":
            continue
        #replaces letter with mapped number 
        elif re.match(digit2, element):
            num = num.replace(element, "2")
        elif re.match(digit3, element):
            num = num.replace(element, "3")
        elif re.match(digit4, element):
            num = num.replace(element, "4")
        elif re.match(digit5, element):
            num = num.replace(element, "5")
        elif re.match(digit6, element):
            num = num.replace(element, "6")
        elif re.match(digit7, element):
            num = num.replace(element, "7")
        elif re.match(digit8, element):
            num = num.replace(element, "8")
        elif re.match(digit9, element):
            num = num.replace(element, "9")
            
    #output converted number 
    print("The converted phone number is:", num)

#call main
main()

print("\nHave a nice day! Program now ending")

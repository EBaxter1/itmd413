'''
File Name: hw3
Made By: Erin baxter
This program will test to see if a card number is vaild or not
'''

print("Hello and welcome to the card tester program!\n")

# get number
try:
    cNumber = int(input("Please enter a credit card number to test: "))
    print("\n")
except ValueError:
    print("Invaild input, please try again with an integer between 13-16 digits. Program now ending")
    quit()

    
# return true if the card number is valid
def isValid(number):
    reversedNumber = number[::-1]
    # newNumber = int(reversedNumber)
    length = getSize(reversedNumber)
    
    numberList = list(reversedNumber)
   
    sumOfDoubleEvenPlace(numberList)
    
    nextSum = 0      
    for x in range(0, length, 2):
        num = int(numberList[x])
        nextSum+=num
    tSum = cSum + nextSum
    end = tSum % 10
    if (end == 0):
       print("Number is valid")
    else:
        print("Number is not valid")


# get the result from step 2
def sumOfDoubleEvenPlace(number):
    length = getSize(number)
    evenSum = 0
    
    for x in range(1, length, 2):
        getDigit(int(number[x]))
        
    return evenSum

# Return this number if it is a single digit, otherise, return the sum of the two digits
def getDigit(number):
    product = number * 2
    if (product < 10):
        digitSum+=product
    else:
        product = str(product)
        newList = list(product)
        newSum = int(newList[0]) + int(newList[1])
        digitSum+=newSum
    return digitSum

# return sum of odd place digits in number
#def sumOfOddPlace(number):


# return true if the digit d is a prefix for number
#def prefixMatched(number, d):


# return the number of digits in d
def getSize(d):
  # reversing card number given by using revered function and making int again
    length = len(d)
    length = int(length)
    return length

#return the first k number of digits from number. If the
# number of digits in number is less than k, return number
#def getPrefix(number, k):

# make card number input a string for testing 
makeString = str(cNumber)

if (len(makeString) >= 13 and len(makeString) <= 16):
    isValid(makeString)
else:
    print("Number is not between 13-16 digits so it not a card number. Please try again, program now closing")
    quit()

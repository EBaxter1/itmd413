'''
File Name: hw3
Made By: Erin baxter
This program will test to see if a card number is vaild or not
'''

print("Hello and welcome to the credit card tester program!\n")

# get number from user and make sure it is an int 
try:
    cNumber = int(input("Please enter a credit card number to test: "))
except ValueError:
    print("Invaild input, please try again with an integer between 13-16 digits. Program now ending")
    quit()


# this function gives user friendly result of if card is valid
def outputUser(number):
    if (isValid(number)):
        print("That credit card number is valid!")
    else:
        print("That credit card number is not valid!")
    print("\nThank you for using this program. See you next time!")


    
# return true if the card number is valid
def isValid(number):
    # convert number to string and the reverse it 
    number = str(number)
    reversedNumber = number[::-1]
    
    length = getSize(reversedNumber)

    #make the number into an array 
    numberList = list(reversedNumber)
    
    totalSum = sumOfDoubleEvenPlace(numberList) + sumOfOddPlace(numberList)

    #check if sum can be divided by 10
    result = totalSum % 10
    
    if (result == 0):
        return True
    else:
        return False 

# get the result from step 2
def sumOfDoubleEvenPlace(number):
    length = getSize(number)
    evenSum = 0

    #run through card number array and get every even number 
    for x in range(1, length, 2):
        num = getDigit(int(number[x]))
        evenSum+=num

    return evenSum

# Return this number if it is a single digit, otherise, return the sum of the two digits
def getDigit(number):
    numberProduct = number * 2
    
    if (numberProduct < 10):
        return numberProduct
    else:
        # make the product of the number a string and then caculate
        numberProduct = str(numberProduct)
        newList = list(numberProduct)
        newSum = int(newList[0]) + int(newList[1])
        return newSum

# return sum of odd place digits in number
def sumOfOddPlace(number):
    length = getSize(number)
    oddSum = 0

    #go through each number in array and make it an int
    for x in range(0, length, 2):
        num = int(number[x])
        oddSum+=num
 
    return oddSum

# return true if the digit d is a prefix for number
#def prefixMatched(number, d):


# return the number of digits in d
def getSize(d):
    length = len(d)
    length = int(length)
    return length

#return the first k number of digits from number. If the
# number of digits in number is less than k, return number
#def getPrefix(number, k):

# make card number input a string fortesting length 
cardLength = getSize(str(cNumber))

# check if real card length and then call first function 
if (cardLength >= 13 and cardLength <= 16):
    outputUser(cNumber)
else:
    print("Number is not between 13-16 digits so it not a card number. Please try again, program now closing")
    quit()

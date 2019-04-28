'''
File name: ebaxter_hw12.py
Made by: Erin Baxter
This program has a digits reverse function and a decimal to hex function
'''

print("Hello and welcome to the Recursion Fun Maker 26,000!")

def main():
    while 1 == 1:
        try:
            menuOption = int(input(f'''\nWhat would you like to do?\n1. Reverse a number\n2. Convert a decimal to a hex number\n3. End program\nEnter option: '''))
            if menuOption == 1:
                try:
                    number = int(input("\nPlease enter a number to reverse: "))
                    reverseDisplay(number)
                    continue
                except ValueError:
                    print("Error! Please enter a integer!")
                    continue
            elif menuOption == 2:
                try:
                    number = int(input("\nPlease enter a decimal number to convert: "))
                    decimalToHex(number)
                    continue
                except ValueError:
                    print("Error! Please enter a integer!")
                    continue   
            else:
                break
        except ValueError:
            break
                


def reverseDisplay(value):
    test = type(value)
    if test is int:
        value = list(str(value))
        print("The reverse of that number is: ", end="")
    if len(value) > 0:
        num = value.pop()
        print(int(num), end="")
        reverseDisplay(value)
    else:
        print()
  
    

def decimalToHex(value):
    decimalToHexHelper(value, "")
 
def decimalToHexHelper(value, valueString):
    hexList = ["A" , "B", "C", "D", "E", "F"]
    if value > 0:
        dec = value % 16
        if dec > 9:
            dec = hexList[dec - 10]
        else:
            dec = str(dec)
        valueString = dec + valueString 
        value = value / 16
        decimalToHexHelper(int(value), valueString)
    else:
        print("That number in hex is:", valueString)    
      


# call main 
main()

print("\nGoodbye!")

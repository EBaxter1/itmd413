'''
File name: ebaxter_hw12.py
Made by: Erin Baxter
This program has a digits reverse function and a decimal to hex function
'''

print("Hello and welcome to the Recursion Fun Maker 26,000!")

#main function that has menu to choice which function to call 
def main():
    while 1 == 1: # while loop that is always true so it will keep  running until breaks 
        try: # this try makes it so if any option vs 1,2,3 it will end loop
            # options
            menuOption = int(input(f'''\nWhat would you like to do?\n1. Reverse a number\n2. Convert a decimal to a hex number\n3. End program\nEnter option: '''))
            if menuOption == 1:
                try:
                    number = int(input("\nPlease enter a number to reverse: "))
                    # call function and pass input 
                    reverseDisplay(number)
                    continue # keep loop going
                except ValueError: # catch to make sure input in int 
                    print("Error! Please enter a integer!")
                    continue # keep loop going 
            elif menuOption == 2:
                try:
                    number = int(input("\nPlease enter a decimal number to convert: "))
                    decimalToHex(number) # call function and pass input 
                    continue
                except ValueError: # catch to make sure input is int
                    print("Error! Please enter a integer!")
                    continue # keep loop going
            else:
                break # end loop if user type 3
        except ValueError:
            break # end loop if user types anything but 1,2

                
# this function will take a int value and reverse it and display the reverse 
def reverseDisplay(value):
    # variable to see if int or list 
    test = type(value)
    if test is int: # this would be first pass into function
        # make value a list 
        value = list(str(value))
        # print here so it only displays once 
        print("The reverse of that number is: ", end="") # end makes it so there is no new line
    if len(value) > 0: # make sure list isn't zero 
        num = value.pop() # take last item of list 
        print(int(num), end="") # print it out with no newline
        reverseDisplay(value) # call function again to add other numbers
    else:
        print() # print a newline after everything

  
# this function calls a recursive helper function that performs the convertion of decimal to hex
def decimalToHex(value):
    # passes value and empty string so that there is no need for global variable 
    decimalToHexHelper(value, "")

# this funciton is a helper function that has an extra argument to hold the result so it can be reversed 
def decimalToHexHelper(value, valueString):
    # list that has letters for hex values that are letters 
    hexList = ["A" , "B", "C", "D", "E", "F"]
    if value > 0: # make sure value isn't done 
        dec = value % 16 # get reminder 
        if dec > 9: # set reminder to letter if about 9
            dec = hexList[dec - 10]# get letter based on which number it is 
        else:
            # make reminder a string
            dec = str(dec) 
        #add reminder to variable in right order 
        valueString = dec + valueString
        # get current answer
        value = value / 16
        # call helper function again 
        decimalToHexHelper(int(value), valueString)
    else:
        # output new hex string that is in right order 
        print("That number in hex is:", valueString)    
      

# call main 
main()

# say bye-bye
print("\nGoodbye!")
